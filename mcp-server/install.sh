#!/bin/bash
#
# OpenSignals Protocol MCP Server Installation Script
#
# This script installs the OpenSignals MCP server and optionally configures
# it for Claude Desktop or other MCP clients.
#

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}OpenSignals Protocol MCP Server Installer${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Check Python version
echo -e "${YELLOW}Checking Python version...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed${NC}"
    echo "Please install Python 3.8 or later"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo -e "${RED}Error: Python 3.8 or later is required (found $PYTHON_VERSION)${NC}"
    exit 1
fi

echo -e "${GREEN}Python $PYTHON_VERSION detected${NC}"
echo ""

# Create virtual environment
echo -e "${YELLOW}Creating virtual environment...${NC}"
cd "$SCRIPT_DIR"

if [ -d "venv" ]; then
    echo -e "${YELLOW}Virtual environment already exists. Removing...${NC}"
    rm -rf venv
fi

python3 -m venv venv
source venv/bin/activate

echo -e "${GREEN}Virtual environment created${NC}"
echo ""

# Install dependencies
echo -e "${YELLOW}Installing dependencies...${NC}"
pip install --upgrade pip
pip install -r requirements.txt

echo -e "${GREEN}Dependencies installed${NC}"
echo ""

# Create .env file if it doesn't exist
if [ ! -f "$SCRIPT_DIR/.env" ]; then
    echo -e "${YELLOW}Creating .env file from template...${NC}"
    cp "$SCRIPT_DIR/.env.example" "$SCRIPT_DIR/.env"
    echo -e "${GREEN}.env file created${NC}"
else
    echo -e "${BLUE}.env file already exists${NC}"
fi
echo ""

# Test the server
echo -e "${YELLOW}Testing server installation...${NC}"
if python3 -c "import mcp; print('MCP SDK imported successfully')" &> /dev/null; then
    echo -e "${GREEN}Server test passed${NC}"
else
    echo -e "${RED}Server test failed${NC}"
    exit 1
fi
echo ""

# Detect operating system for Claude Desktop configuration
OS_TYPE="unknown"
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS_TYPE="macos"
    CLAUDE_CONFIG_DIR="$HOME/Library/Application Support/Claude"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS_TYPE="linux"
    CLAUDE_CONFIG_DIR="$HOME/.config/claude"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    OS_TYPE="windows"
    CLAUDE_CONFIG_DIR="$APPDATA/Claude"
fi

# Ask if user wants to configure Claude Desktop
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Claude Desktop Configuration${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo "Would you like to configure this MCP server for Claude Desktop?"
echo -e "${YELLOW}This will add the server to your Claude Desktop configuration.${NC}"
echo ""
read -p "Configure for Claude Desktop? (y/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    if [ "$OS_TYPE" == "unknown" ]; then
        echo -e "${RED}Unable to detect operating system. Please configure manually.${NC}"
    else
        # Create Claude config directory if it doesn't exist
        mkdir -p "$CLAUDE_CONFIG_DIR"

        CONFIG_FILE="$CLAUDE_CONFIG_DIR/claude_desktop_config.json"

        # Backup existing config
        if [ -f "$CONFIG_FILE" ]; then
            echo -e "${YELLOW}Backing up existing configuration...${NC}"
            cp "$CONFIG_FILE" "$CONFIG_FILE.backup"
            echo -e "${GREEN}Backup created at $CONFIG_FILE.backup${NC}"
        fi

        # Get absolute path to server
        SERVER_PATH="$SCRIPT_DIR/server.py"
        VENV_PYTHON="$SCRIPT_DIR/venv/bin/python"

        # Create or update configuration
        if [ -f "$CONFIG_FILE" ]; then
            echo -e "${YELLOW}Updating existing Claude Desktop configuration...${NC}"
            # Use Python to merge configurations
            python3 << EOF
import json
import sys

config_file = "$CONFIG_FILE"
try:
    with open(config_file, 'r') as f:
        config = json.load(f)
except:
    config = {}

if 'mcpServers' not in config:
    config['mcpServers'] = {}

config['mcpServers']['opensignals-protocol'] = {
    "command": "$VENV_PYTHON",
    "args": ["$SERVER_PATH"],
    "env": {
        "OPENSIGNALS_LOG_LEVEL": "INFO"
    }
}

with open(config_file, 'w') as f:
    json.dump(config, f, indent=2)

print("Configuration updated successfully")
EOF
        else
            echo -e "${YELLOW}Creating new Claude Desktop configuration...${NC}"
            cat > "$CONFIG_FILE" << EOF
{
  "mcpServers": {
    "opensignals-protocol": {
      "command": "$VENV_PYTHON",
      "args": ["$SERVER_PATH"],
      "env": {
        "OPENSIGNALS_LOG_LEVEL": "INFO"
      }
    }
  }
}
EOF
        fi

        echo -e "${GREEN}Claude Desktop configuration updated${NC}"
        echo -e "${BLUE}Config file: $CONFIG_FILE${NC}"
        echo ""
        echo -e "${YELLOW}Please restart Claude Desktop to activate the MCP server.${NC}"
    fi
fi

echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}Installation Complete!${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo "The OpenSignals Protocol MCP server is now installed."
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Review and customize .env file if needed:"
echo "   $SCRIPT_DIR/.env"
echo ""
echo "2. If you configured Claude Desktop:"
echo "   - Restart Claude Desktop"
echo "   - The 'opensignals-protocol' server will be available"
echo "   - Try: 'List available OpenSignals tools'"
echo ""
echo "3. For manual integration with other MCP clients:"
echo "   - Server command: $SCRIPT_DIR/venv/bin/python"
echo "   - Server args: $SCRIPT_DIR/server.py"
echo ""
echo "4. Test the server:"
echo "   cd $SCRIPT_DIR"
echo "   source venv/bin/activate"
echo "   python server.py"
echo ""
echo -e "${BLUE}Documentation:${NC}"
echo "   README: $SCRIPT_DIR/README.md"
echo "   OpenSignals Spec: $REPO_ROOT/specs/opensignals-v0.1.md"
echo ""
echo -e "${GREEN}Happy agentic advertising!${NC}"
echo ""
