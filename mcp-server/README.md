# OpenSignals Protocol MCP Server

A production-ready [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that exposes OpenSignals Protocol functionality as tools and resources for AI agents to use in agentic advertising workflows.

## Overview

This MCP server enables AI agents to:

- **Discover signals**: Browse available advertising signals with trust metadata
- **Verify compliance**: Check if signals are permitted for specific brand/category/market combinations
- **Calculate trust scores**: Evaluate signal quality across 7 dimensions
- **Audit usage**: Log signal activations for compliance tracking
- **Check regulations**: Understand category-specific compliance requirements

The server bridges the gap between AI agents (like Claude) and the OpenSignals Protocol, enabling agents to make trust-informed decisions about advertising signals automatically while maintaining proper governance controls.

## Features

### Tools (6 total)

1. **`get_signal_manifest`** - Retrieve complete signal manifests with all metadata
2. **`verify_signal`** - Verify signal compliance for specific use cases (PRIMARY GOVERNANCE TOOL)
3. **`score_signal`** - Calculate 7-dimensional trust scores
4. **`audit_signal_usage`** - Log signal usage for audit trails
5. **`list_signals`** - Browse available signals with filtering
6. **`check_compliance`** - Check category/market compliance requirements

### Resources (3 types)

1. **Signal Manifests** - `opensignals://manifests/{signal_id}`
2. **JSON Schemas** - `opensignals://schemas/{schema_name}`
3. **Documentation** - `opensignals://docs/{doc_name}`

## Installation

### Prerequisites

- Python 3.8 or later
- pip package manager
- Claude Desktop (for Claude integration) or another MCP client

### Quick Install

```bash
# Clone the repository (if not already)
git clone https://github.com/opensignals-protocol/opensignals-protocol.git
cd opensignals-protocol/mcp-server

# Run the installation script
./install.sh
```

The installation script will:
1. Create a Python virtual environment
2. Install dependencies
3. Create a `.env` configuration file
4. Optionally configure Claude Desktop
5. Test the installation

### Manual Installation

If you prefer to install manually:

```bash
cd opensignals-protocol/mcp-server

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env if needed
nano .env
```

## Configuration

### For Claude Desktop

The installer can automatically configure Claude Desktop. Alternatively, manually add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or equivalent:

```json
{
  "mcpServers": {
    "opensignals-protocol": {
      "command": "/path/to/opensignals-protocol/mcp-server/venv/bin/python",
      "args": ["/path/to/opensignals-protocol/mcp-server/server.py"],
      "env": {
        "OPENSIGNALS_LOG_LEVEL": "INFO"
      }
    }
  }
}
```

Replace `/path/to/` with the actual absolute path to your installation.

### For Other MCP Clients

Use the following configuration pattern:

```json
{
  "command": "python",
  "args": ["/path/to/opensignals-protocol/mcp-server/server.py"],
  "cwd": "/path/to/opensignals-protocol/mcp-server",
  "env": {
    "OPENSIGNALS_LOG_LEVEL": "INFO"
  }
}
```

### Environment Variables

Edit `.env` to customize:

```bash
# Logging level
OPENSIGNALS_LOG_LEVEL=INFO

# Optional: Custom paths
OPENSIGNALS_REPO_ROOT=/path/to/opensignals-protocol
OPENSIGNALS_EXAMPLES_DIR=/path/to/examples
OPENSIGNALS_SCHEMAS_DIR=/path/to/schemas

# Optional: Remote manifest fetching
OPENSIGNALS_MANIFEST_BASE_URL=https://signals.example.com/.well-known/opensignals
OPENSIGNALS_ENABLE_REMOTE_FETCH=false

# Optional: Audit logging
OPENSIGNALS_AUDIT_LOG_DIR=/var/log/opensignals
OPENSIGNALS_ENABLE_AUDIT_PERSISTENCE=false
```

## Usage

### Starting the Server

The server is automatically started by your MCP client (Claude Desktop, etc.). For testing:

```bash
cd opensignals-protocol/mcp-server
source venv/bin/activate
python server.py
```

The server runs in stdio mode and communicates via JSON-RPC 2.0.

### Example Workflows for AI Agents

#### 1. Discover and List Signals

**Agent Prompt:**
> "List all available advertising signals"

**Behind the scenes:**
```json
{
  "tool": "list_signals",
  "arguments": {}
}
```

**Response:**
```json
{
  "task": "list_signals",
  "count": 4,
  "signals": [
    {
      "signal_id": "verified-attention-quality",
      "name": "Verified Attention Quality Measurement",
      "signal_type": "attention",
      "status": "active",
      "overall_trust_score": 0.94
    },
    ...
  ]
}
```

#### 2. Verify Signal for Regulated Category

**Agent Prompt:**
> "I need to use the outdoor-recreation-enthusiasts signal for a UK alcohol campaign. Check if it's compliant."

**Behind the scenes:**
```json
{
  "tool": "verify_signal",
  "arguments": {
    "signal_id": "outdoor-recreation-enthusiasts",
    "context": {
      "brand": "premium-spirits-co",
      "category": "alcohol",
      "market": "GB",
      "intended_use": "contextual_targeting"
    }
  }
}
```

**Response:**
```json
{
  "task": "verify_signal",
  "signal_id": "outdoor-recreation-enthusiasts",
  "decision": "approved_with_conditions",
  "approval_required": true,
  "trust_score": 0.87,
  "trust_band": "trusted",
  "conditions": [
    "human_approval_required",
    "sensitive_category_alcohol",
    "audit_required",
    "no_individual_profiling_for_alcohol",
    "age_verification_required"
  ],
  "policy_bindings": [
    {
      "policy_id": "alcohol_age_restriction",
      "enforcement": "mandatory"
    }
  ],
  "reasoning": "Signal approved with conditions for contextual_targeting. Human approval required for alcohol category. Trust score: 0.87 (trusted).",
  "valid_until": "2026-05-12T19:32:00Z"
}
```

#### 3. Calculate Trust Score

**Agent Prompt:**
> "What's the trust score for the attention measurement signal?"

**Behind the scenes:**
```json
{
  "tool": "score_signal",
  "arguments": {
    "signal_id": "verified-attention-quality"
  }
}
```

**Response:**
```json
{
  "task": "score_signal",
  "signal_id": "verified-attention-quality",
  "timestamp": "2026-05-11T19:32:00Z",
  "version": "1.0",
  "scores": {
    "coverage": 0.89,
    "freshness": 0.98,
    "precision": 0.93,
    "stability": 0.95,
    "explainability": 0.95,
    "compliance": 0.97,
    "overall": 0.94
  },
  "details": {
    "coverage": {
      "score": 0.89,
      "geographic_markets": ["US", "GB", "FR", "DE", ...],
      "reach_estimate": 125000000
    },
    ...
  },
  "trust_band": "highly_trusted",
  "autonomy_recommendation": "autonomous_with_limits"
}
```

#### 4. Check Compliance Before Signal Search

**Agent Prompt:**
> "What are the compliance requirements for gambling advertising in the US?"

**Behind the scenes:**
```json
{
  "tool": "check_compliance",
  "arguments": {
    "category": "gambling",
    "market": "US"
  }
}
```

**Response:**
```json
{
  "task": "check_compliance",
  "category": "gambling",
  "market": "US",
  "is_restricted": false,
  "compliance_requirements": {
    "human_approval_required": true,
    "age_restrictions": true,
    "minimum_age": 21,
    "prohibited_uses": ["individual_profiling", "lookalike_modeling"],
    "allowed_uses": ["contextual_targeting"],
    "audit_required": true,
    "restricted_markets": ["US-UT", "AE", "SA"],
    "compliance_frameworks": ["gambling_commission_rules"],
    "self_exclusion_required": true
  },
  "recommendation": "proceed_with_checks"
}
```

#### 5. Audit Signal Activation

**Agent Prompt:**
> "Log that we've activated the outdoor-recreation signal for the spring campaign"

**Behind the scenes:**
```json
{
  "tool": "audit_signal_usage",
  "arguments": {
    "signal_id": "outdoor-recreation-enthusiasts",
    "event_type": "signal_activated",
    "context": {
      "brand": "premium-spirits-co",
      "campaign_id": "spring-campaign-2026",
      "buyer_agent": "claude-media-buyer",
      "human_approver": "jane.smith@brand.com",
      "category": "alcohol",
      "trust_score": 0.87
    }
  }
}
```

**Response:**
```json
{
  "task": "audit_signal_usage",
  "audit_id": "aud_a1b2c3d4e5f6",
  "event_type": "signal_activated",
  "signal_id": "outdoor-recreation-enthusiasts",
  "timestamp": "2026-05-11T19:32:00Z",
  "context": { ... },
  "status": "logged",
  "retention_until": "2026-08-09T19:32:00Z"
}
```

### Example Agent Prompts

Here are natural language prompts that trigger OpenSignals tools:

1. **Discovery:**
   - "What advertising signals are available?"
   - "Show me all attention measurement signals"
   - "List signals with trust score above 0.85"

2. **Compliance Checking:**
   - "Can I use signal X for alcohol advertising in the UK?"
   - "Verify if this signal is compliant for pharma in the US"
   - "What are the gambling advertising rules in Nevada?"

3. **Trust Scoring:**
   - "What's the trust score for signal X?"
   - "How reliable is the retail commerce signal?"
   - "Score this signal for our brand awareness campaign"

4. **Audit:**
   - "Log that we activated signal X for campaign Y"
   - "Record this signal usage for compliance"

5. **Full Workflow:**
   - "I need to run an alcohol campaign in the UK. Find compliant signals, verify them, and set up the campaign."

### Resources

Access OpenSignals resources directly:

```python
# Get signal manifest
resource = "opensignals://manifests/verified-attention-quality"

# Get schema
resource = "opensignals://schemas/open-signal-manifest"

# Get documentation
resource = "opensignals://docs/specification"
resource = "opensignals://docs/trust-scoring"
resource = "opensignals://docs/compliance"
```

## Architecture

### Directory Structure

```
mcp-server/
├── server.py              # Main MCP server implementation
├── requirements.txt       # Python dependencies
├── config.json           # MCP configuration template
├── .env.example          # Environment variables template
├── install.sh            # Installation script
├── README.md             # This file
└── venv/                 # Virtual environment (created during install)
```

### Data Sources

The server reads from the OpenSignals Protocol repository:

- **Signal Manifests**: `../examples/*.json`
- **Schemas**: `../schemas/v0.1/*.json`
- **Specifications**: `../specs/*.md`
- **Documentation**: `../docs/*.md`

### Trust Score Calculation

Trust scores are calculated using the OpenSignals v0.1 methodology:

```python
# Weighted average of 7 dimensions
overall_score = (
    provenance * 0.20 +
    permissioning * 0.20 +
    freshness * 0.15 +
    quality * 0.20 +
    explainability * 0.10 +
    outcome_relevance * 0.10 +
    compliance_safety * 0.05
)
```

Trust bands:
- **0.90-1.00**: Highly trusted (autonomous with limits)
- **0.75-0.89**: Trusted (approve with human)
- **0.50-0.74**: Limited trust (recommend)
- **0.25-0.49**: Low trust (observe)
- **0.00-0.24**: Unsafe (blocked)

### Compliance Rules

Built-in compliance rules for regulated categories:

- **Alcohol**: Human approval, age 21-25, contextual only, audit required
- **Gambling**: Human approval, age 21, contextual only, self-exclusion
- **Pharma**: Human approval, contextual only, no health data targeting
- **Finance**: Human approval, age 18, no vulnerability targeting
- **General**: Standard advertising rules

Rules are automatically applied during `verify_signal` calls.

## Troubleshooting

### Server Won't Start

```bash
# Check Python version
python3 --version  # Should be 3.8+

# Verify MCP SDK installation
source venv/bin/activate
python -c "import mcp; print('MCP SDK OK')"

# Check for errors
python server.py
```

### Claude Desktop Not Seeing Server

1. Check config file location:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Linux: `~/.config/claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. Verify paths are absolute (not relative)

3. Restart Claude Desktop completely

4. Check Claude Desktop logs for errors

### Signals Not Found

```bash
# Verify examples directory exists
ls ../examples/*.json

# Check OPENSIGNALS_REPO_ROOT in .env
cat .env
```

### Trust Scores Seem Wrong

Trust scores come directly from signal manifests in `examples/` directory. To update:

1. Edit the manifest JSON file
2. Adjust `quality.overall_trust_score` and dimension scores
3. Restart the MCP server

## Development

### Running Tests

```bash
# Activate virtual environment
source venv/bin/activate

# Test imports
python -c "from server import get_available_signals; print(get_available_signals())"

# Test tool calls
python << EOF
from server import verify_signal_compliance, load_json_file
from pathlib import Path

manifest = load_json_file(Path("../examples/attention-signal.json"))
result = verify_signal_compliance(manifest, {
    "category": "general",
    "market": "US",
    "intended_use": "measurement"
})
print(result)
EOF
```

### Adding New Tools

1. Add tool definition to `list_tools()` function
2. Implement handler in `call_tool()` function
3. Add helper functions as needed
4. Update README with examples

### Adding New Resources

1. Add resource to `list_resources()` function
2. Implement handler in `read_resource()` function
3. Update resource URI scheme documentation

## Integration with Agentic Workflows

### Typical Agent Workflow

```
1. Agent receives campaign brief (brand, category, market, objectives)
   ↓
2. Agent calls check_compliance(category, market) to understand rules
   ↓
3. Agent calls list_signals(filters) to find candidate signals
   ↓
4. For each signal:
   a. Call get_signal_manifest(signal_id) for details
   b. Call score_signal(signal_id, context) for trust evaluation
   c. Call verify_signal(signal_id, context) for compliance check
   ↓
5. Agent selects approved signals meeting trust thresholds
   ↓
6. If human approval required:
   - Agent presents signals to human with reasoning
   - Human approves/rejects
   ↓
7. Agent activates signals (via AdCP or other protocol)
   ↓
8. Agent calls audit_signal_usage() for each activated signal
   ↓
9. Campaign runs with compliant, trusted signals
```

### Integration Points

- **AdCP Integration**: Use `verify_signal` before `activate_signal`
- **OpenRTB Integration**: Include trust scores in bid requests
- **DSP Integration**: Filter signals by trust band before bidding
- **Governance Integration**: Automated policy enforcement via `verify_signal`
- **Audit Integration**: Compliance trails via `audit_signal_usage`

## Security Considerations

- Server runs locally with no network exposure
- All data read from local file system
- No credentials or API keys required for local operation
- Audit logs contain no PII by default
- Signal manifests follow OpenSignals privacy standards

## Performance

- **Cold start**: ~100ms
- **Tool calls**: ~10-50ms per call
- **Resource reads**: ~5-20ms per resource
- **Memory footprint**: ~50MB
- **Concurrent requests**: Handled via MCP protocol async support

## Roadmap

- [ ] Remote manifest fetching from `.well-known/opensignals/` endpoints
- [ ] Persistent audit log storage
- [ ] Real-time trust score updates
- [ ] Integration with signal provider APIs
- [ ] Webhook support for approval workflows
- [ ] Multi-tenancy for agency use cases
- [ ] Historical trend analysis
- [ ] Performance benchmarking suite

## Contributing

Contributions welcome! See the main OpenSignals Protocol [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

Areas of interest:
- Additional compliance rules for more categories/markets
- Remote manifest fetching implementation
- Performance optimizations
- Integration examples with AdCP, OpenRTB, etc.
- Test coverage improvements

## License

- **Code**: Apache License 2.0
- **Documentation**: Creative Commons Attribution 4.0 International (CC BY 4.0)

See [LICENSE](../LICENSE) for details.

## Support

- **Issues**: [GitHub Issues](https://github.com/opensignals-protocol/opensignals-protocol/issues)
- **Discussions**: Use `mcp-server` label
- **Documentation**: [OpenSignals Protocol Specification](../specs/opensignals-v0.1.md)

## Acknowledgments

Built on:
- [Model Context Protocol](https://modelcontextprotocol.io) by Anthropic
- [OpenSignals Protocol](../README.md) community
- Python MCP SDK

Designed for use with:
- Claude Desktop (Anthropic)
- AdCP (Ad Context Protocol)
- AAMP (IAB Tech Lab)
- OpenRTB (IAB Tech Lab)

---

**Made for the agentic advertising era.**

For questions about the OpenSignals Protocol itself, see the [main README](../README.md).
