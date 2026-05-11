#!/usr/bin/env python3
"""
OpenSignals Protocol MCP Server

A Model Context Protocol (MCP) server that exposes OpenSignals Protocol functionality
as tools and resources for AI agents to use in agentic advertising workflows.

This server enables AI agents to:
- Get signal manifests and trust metadata
- Verify signals for brand compliance
- Calculate trust scores
- Audit signal usage
- Check compliance requirements
"""

import asyncio
import json
import logging
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional
from uuid import uuid4

from mcp.server import Server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
)
import mcp.server.stdio

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("opensignals-mcp")

# Path to the OpenSignals Protocol repository
REPO_ROOT = Path(__file__).parent.parent
EXAMPLES_DIR = REPO_ROOT / "examples"
SCHEMAS_DIR = REPO_ROOT / "schemas" / "v0.1"
DOCS_DIR = REPO_ROOT / "docs"
SPECS_DIR = REPO_ROOT / "specs"

# Initialize MCP server
app = Server("opensignals-protocol")


# =============================================================================
# Helper Functions
# =============================================================================

def load_json_file(file_path: Path) -> Optional[Dict[str, Any]]:
    """Load and parse a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading {file_path}: {e}")
        return None


def load_text_file(file_path: Path) -> Optional[str]:
    """Load a text file."""
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        logger.error(f"Error loading {file_path}: {e}")
        return None


def get_available_signals() -> List[Dict[str, Any]]:
    """Get list of available signal manifests from examples directory."""
    signals = []
    if EXAMPLES_DIR.exists():
        for json_file in EXAMPLES_DIR.glob("*.json"):
            manifest = load_json_file(json_file)
            if manifest and manifest.get("protocol") == "opensignals":
                signals.append({
                    "signal_id": manifest.get("signal_id"),
                    "name": manifest.get("name"),
                    "signal_type": manifest.get("signal_type"),
                    "status": manifest.get("status"),
                    "overall_trust_score": manifest.get("quality", {}).get("overall_trust_score"),
                    "file_path": str(json_file)
                })
    return signals


def calculate_trust_score(manifest: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Calculate comprehensive trust score for a signal.

    Args:
        manifest: Signal manifest
        context: Optional context for scoring (brand, objective, etc.)

    Returns:
        Trust score breakdown with all dimensions
    """
    quality = manifest.get("quality", {})
    provenance = manifest.get("provenance", {})
    permissioning = manifest.get("permissioning", {})

    # Base scores from manifest
    scores = {
        "coverage": quality.get("coverage_score", 0.5),
        "freshness": quality.get("freshness_score", 0.5),
        "precision": quality.get("precision_score", 0.5),
        "stability": quality.get("stability_score", 0.5),
        "explainability": quality.get("explainability_score", 0.5),
        "compliance": quality.get("compliance_safety_score", 0.5),
        "overall": quality.get("overall_trust_score", 0.5)
    }

    # Calculate dimension details
    details = {
        "coverage": {
            "score": scores["coverage"],
            "geographic_markets": provenance.get("geographic_coverage", []),
            "reach_estimate": manifest.get("coverage", {}).get("estimated_reach", 0)
        },
        "freshness": {
            "score": scores["freshness"],
            "last_updated": provenance.get("last_updated", "unknown"),
            "update_frequency": provenance.get("update_frequency", "unknown")
        },
        "precision": {
            "score": scores["precision"],
            "methodology": provenance.get("collection_method", "unknown")
        },
        "stability": {
            "score": scores["stability"],
            "status": manifest.get("status", "unknown")
        },
        "explainability": {
            "score": scores["explainability"],
            "transparency": manifest.get("transparency", {}).get("explainability", "unknown")
        },
        "compliance": {
            "score": scores["compliance"],
            "frameworks": manifest.get("governance", {}).get("compliance_frameworks", [])
        }
    }

    # Determine trust band
    overall_score = scores["overall"]
    if overall_score >= 0.90:
        trust_band = "highly_trusted"
        autonomy_recommendation = "autonomous_with_limits"
    elif overall_score >= 0.75:
        trust_band = "trusted"
        autonomy_recommendation = "approve_with_human"
    elif overall_score >= 0.50:
        trust_band = "limited_trust"
        autonomy_recommendation = "recommend"
    elif overall_score >= 0.25:
        trust_band = "low_trust"
        autonomy_recommendation = "observe"
    else:
        trust_band = "unsafe"
        autonomy_recommendation = "blocked"

    return {
        "signal_id": manifest.get("signal_id"),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "version": "1.0",
        "scores": scores,
        "details": details,
        "trust_band": trust_band,
        "autonomy_recommendation": autonomy_recommendation,
        "calculation_method": "opensignals_v0.1_reference_implementation"
    }


def verify_signal_compliance(
    manifest: Dict[str, Any],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Verify if a signal is compliant for specific use case.

    Args:
        manifest: Signal manifest
        context: Verification context (brand, category, market, intended_use)

    Returns:
        Verification decision with reasoning
    """
    signal_id = manifest.get("signal_id")
    category = context.get("category", "general")
    market = context.get("market", "US")
    intended_use = context.get("intended_use", "targeting")

    governance = manifest.get("governance", {})
    permissioning = manifest.get("permissioning", {})
    quality = manifest.get("quality", {})

    # Check signal status
    if manifest.get("status") not in ["active", "experimental"]:
        return {
            "signal_id": signal_id,
            "decision": "rejected",
            "approval_required": False,
            "reasoning": f"Signal status is '{manifest.get('status')}' and cannot be activated.",
            "trust_score": 0.0,
            "conditions": []
        }

    # Check geographic restrictions
    geographic_restrictions = permissioning.get("usage_restrictions", {}).get("geographic_restrictions", [])
    if market in geographic_restrictions:
        return {
            "signal_id": signal_id,
            "decision": "rejected",
            "approval_required": False,
            "reasoning": f"Signal is restricted in market '{market}'.",
            "trust_score": 0.0,
            "conditions": []
        }

    # Check permitted uses
    permitted_uses = permissioning.get("permitted_uses", [])
    if permitted_uses and intended_use not in permitted_uses:
        return {
            "signal_id": signal_id,
            "decision": "rejected",
            "approval_required": False,
            "reasoning": f"Signal does not permit '{intended_use}' use case. Allowed uses: {', '.join(permitted_uses)}",
            "trust_score": 0.0,
            "conditions": []
        }

    # Calculate trust score
    trust_score_result = calculate_trust_score(manifest, context)
    overall_trust_score = trust_score_result["scores"]["overall"]
    trust_band = trust_score_result["trust_band"]

    # Determine if human approval is required
    human_approval_required = False
    conditions = []

    # Sensitive categories require human approval
    sensitive_categories = ["alcohol", "gambling", "pharma", "finance", "healthcare"]
    if category in sensitive_categories:
        human_approval_required = True
        conditions.append("human_approval_required")
        conditions.append(f"sensitive_category_{category}")

    # Low trust scores require human approval
    if overall_trust_score < 0.75:
        human_approval_required = True
        conditions.append("low_trust_score")

    # Check if signal requires audit
    if governance.get("audit_required", False):
        conditions.append("audit_required")

    # Determine decision
    if overall_trust_score >= 0.75 and not human_approval_required:
        decision = "approved"
        reasoning = f"Signal approved for {intended_use}. Trust score: {overall_trust_score:.2f} ({trust_band})."
    elif overall_trust_score >= 0.50:
        decision = "approved_with_conditions"
        reasoning = f"Signal approved with conditions for {intended_use}. "
        if human_approval_required:
            reasoning += f"Human approval required for {category} category. "
        reasoning += f"Trust score: {overall_trust_score:.2f} ({trust_band})."
    else:
        decision = "rejected"
        reasoning = f"Signal trust score too low for activation. Trust score: {overall_trust_score:.2f} ({trust_band}). Minimum required: 0.50."

    # Add compliance-specific conditions
    if category in sensitive_categories:
        conditions.append(f"no_individual_profiling_for_{category}")
        conditions.append("age_verification_required")

    policy_bindings = []
    if category == "alcohol":
        policy_bindings.append({
            "policy_id": "alcohol_age_restriction",
            "enforcement": "mandatory"
        })

    return {
        "signal_id": signal_id,
        "decision": decision,
        "approval_required": human_approval_required,
        "trust_score": overall_trust_score,
        "trust_band": trust_band,
        "conditions": conditions,
        "policy_bindings": policy_bindings,
        "reasoning": reasoning,
        "valid_until": (datetime.utcnow() + timedelta(days=1)).isoformat() + "Z",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


def create_audit_log(
    signal_id: str,
    event_type: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Create an audit log entry for signal usage.

    Args:
        signal_id: Signal identifier
        event_type: Type of event (signal_activated, signal_verified, etc.)
        context: Event context

    Returns:
        Audit log entry
    """
    audit_id = f"aud_{uuid4().hex[:12]}"
    timestamp = datetime.utcnow().isoformat() + "Z"

    return {
        "audit_id": audit_id,
        "event_type": event_type,
        "signal_id": signal_id,
        "timestamp": timestamp,
        "context": context,
        "status": "logged",
        "retention_until": (datetime.utcnow() + timedelta(days=90)).isoformat() + "Z"
    }


def check_category_compliance(category: str, market: str) -> Dict[str, Any]:
    """
    Check compliance requirements for a specific category and market.

    Args:
        category: Product category (alcohol, gambling, etc.)
        market: Market/country code

    Returns:
        Compliance requirements and restrictions
    """
    compliance_rules = {
        "alcohol": {
            "human_approval_required": True,
            "age_restrictions": True,
            "minimum_age": 25 if market in ["GB", "IE"] else 21,
            "prohibited_uses": ["individual_profiling", "behavioral_targeting"],
            "allowed_uses": ["contextual_targeting", "geographic_targeting"],
            "audit_required": True,
            "approval_workflow_required": True,
            "restricted_markets": ["SA", "AE"],
            "compliance_frameworks": ["local_alcohol_advertising_standards"],
            "documentation_required": True
        },
        "gambling": {
            "human_approval_required": True,
            "age_restrictions": True,
            "minimum_age": 21,
            "prohibited_uses": ["individual_profiling", "lookalike_modeling"],
            "allowed_uses": ["contextual_targeting"],
            "audit_required": True,
            "restricted_markets": ["US-UT", "AE", "SA"],
            "compliance_frameworks": ["gambling_commission_rules"],
            "self_exclusion_required": True
        },
        "pharma": {
            "human_approval_required": True,
            "age_restrictions": False,
            "prohibited_uses": ["individual_profiling", "health_data_targeting"],
            "allowed_uses": ["contextual_targeting", "geographic_targeting"],
            "audit_required": True,
            "restricted_markets": [],
            "compliance_frameworks": ["fda_guidelines", "ema_guidelines"],
            "prescription_restrictions": True
        },
        "finance": {
            "human_approval_required": True,
            "age_restrictions": True,
            "minimum_age": 18,
            "prohibited_uses": ["financial_vulnerability_targeting"],
            "allowed_uses": ["contextual_targeting", "demographic_targeting"],
            "audit_required": True,
            "compliance_frameworks": ["financial_advertising_standards"],
            "risk_warnings_required": True
        },
        "general": {
            "human_approval_required": False,
            "age_restrictions": False,
            "prohibited_uses": [],
            "allowed_uses": ["all"],
            "audit_required": False,
            "compliance_frameworks": ["general_advertising_standards"]
        }
    }

    rules = compliance_rules.get(category, compliance_rules["general"])

    # Check if market is restricted
    is_restricted = market in rules.get("restricted_markets", [])

    return {
        "category": category,
        "market": market,
        "is_restricted": is_restricted,
        "compliance_requirements": rules,
        "recommendation": "blocked" if is_restricted else "proceed_with_checks",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


# =============================================================================
# MCP Resources
# =============================================================================

@app.list_resources()
async def list_resources() -> List[Resource]:
    """List available OpenSignals resources."""
    resources = []

    # Signal manifest resources
    signals = get_available_signals()
    for signal in signals:
        resources.append(Resource(
            uri=f"opensignals://manifests/{signal['signal_id']}",
            name=f"Signal Manifest: {signal['name']}",
            mimeType="application/json",
            description=f"{signal['signal_type']} signal with trust score {signal['overall_trust_score']}"
        ))

    # Schema resources
    if SCHEMAS_DIR.exists():
        for schema_file in SCHEMAS_DIR.glob("*.json"):
            schema_name = schema_file.stem
            resources.append(Resource(
                uri=f"opensignals://schemas/{schema_name}",
                name=f"Schema: {schema_name}",
                mimeType="application/json",
                description=f"OpenSignals v0.1 schema for {schema_name}"
            ))

    # Documentation resources
    resources.append(Resource(
        uri="opensignals://docs/specification",
        name="OpenSignals Protocol Specification",
        mimeType="text/markdown",
        description="Complete OpenSignals Protocol v0.1 specification"
    ))

    resources.append(Resource(
        uri="opensignals://docs/trust-scoring",
        name="Trust Scoring Documentation",
        mimeType="text/markdown",
        description="Trust scoring methodology and dimensions"
    ))

    resources.append(Resource(
        uri="opensignals://docs/compliance",
        name="Compliance Rules",
        mimeType="text/markdown",
        description="Compliance requirements for regulated categories"
    ))

    return resources


@app.read_resource()
async def read_resource(uri: str) -> str:
    """Read an OpenSignals resource."""

    # Parse URI
    if not uri.startswith("opensignals://"):
        raise ValueError(f"Invalid URI scheme: {uri}")

    path = uri.replace("opensignals://", "")
    parts = path.split("/")

    if len(parts) < 2:
        raise ValueError(f"Invalid URI format: {uri}")

    resource_type = parts[0]
    resource_id = "/".join(parts[1:])

    # Handle different resource types
    if resource_type == "manifests":
        # Find signal manifest
        signal_id = resource_id
        signals = get_available_signals()
        signal = next((s for s in signals if s["signal_id"] == signal_id), None)

        if not signal:
            raise ValueError(f"Signal not found: {signal_id}")

        manifest = load_json_file(Path(signal["file_path"]))
        if not manifest:
            raise ValueError(f"Failed to load manifest: {signal_id}")

        return json.dumps(manifest, indent=2)

    elif resource_type == "schemas":
        # Load schema
        schema_file = SCHEMAS_DIR / f"{resource_id}.schema.json"
        if not schema_file.exists():
            schema_file = SCHEMAS_DIR / f"{resource_id}.json"

        if not schema_file.exists():
            raise ValueError(f"Schema not found: {resource_id}")

        schema = load_json_file(schema_file)
        if not schema:
            raise ValueError(f"Failed to load schema: {resource_id}")

        return json.dumps(schema, indent=2)

    elif resource_type == "docs":
        # Load documentation
        if resource_id == "specification":
            spec_file = SPECS_DIR / "opensignals-v0.1.md"
            content = load_text_file(spec_file)
            if content:
                return content
            raise ValueError("Specification not found")

        elif resource_id == "trust-scoring":
            # Generate trust scoring documentation
            return """# Trust Scoring Model

OpenSignals uses a multi-dimensional trust scoring model across 7 dimensions:

## Dimensions

1. **Provenance (20%)**: Data source transparency and chain of custody
2. **Permissioning (20%)**: Clear consent and usage rights
3. **Freshness (15%)**: How recently the signal was updated
4. **Quality (20%)**: Coverage, precision and stability
5. **Explainability (10%)**: How well the signal can be explained
6. **Outcome Relevance (10%)**: Historical performance
7. **Compliance Safety (5%)**: Adherence to regulations

## Trust Score Bands

- **0.90 to 1.00**: Highly trusted. Can be used autonomously (if policy allows)
- **0.75 to 0.89**: Trusted with conditions. Use with governance checks
- **0.50 to 0.74**: Limited trust. Require human review
- **0.25 to 0.49**: Low trust. Do not activate without explicit approval
- **0.00 to 0.24**: Unsafe or invalid. Block usage

## Calculation Method

Overall trust score is calculated as weighted average of dimension scores:
```
overall_score = (provenance * 0.20) + (permissioning * 0.20) +
                (freshness * 0.15) + (quality * 0.20) +
                (explainability * 0.10) + (outcome * 0.10) +
                (compliance * 0.05)
```
"""

        elif resource_id == "compliance":
            # Generate compliance documentation
            return """# Compliance Rules

## Regulated Categories

### Alcohol
- **Human Approval**: Required
- **Age Restrictions**: Yes (21-25 depending on market)
- **Prohibited Uses**: Individual profiling, behavioral targeting
- **Allowed Uses**: Contextual targeting, geographic targeting
- **Restricted Markets**: Saudi Arabia, UAE
- **Audit**: Required

### Gambling
- **Human Approval**: Required
- **Age Restrictions**: Yes (21+)
- **Prohibited Uses**: Individual profiling, lookalike modeling
- **Allowed Uses**: Contextual targeting only
- **Restricted Markets**: US-Utah, UAE, Saudi Arabia
- **Special Requirements**: Self-exclusion support

### Pharmaceuticals
- **Human Approval**: Required
- **Prohibited Uses**: Individual profiling, health data targeting
- **Allowed Uses**: Contextual targeting, geographic targeting
- **Compliance**: FDA/EMA guidelines
- **Special Requirements**: Prescription restriction notices

### Financial Services
- **Human Approval**: Required
- **Age Restrictions**: Yes (18+)
- **Prohibited Uses**: Financial vulnerability targeting
- **Allowed Uses**: Contextual, demographic targeting
- **Special Requirements**: Risk warnings required

## Privacy Compliance

All signals must comply with:
- GDPR (EU markets)
- CCPA/CPRA (California)
- Local data protection regulations

## Brand Safety

Signals must include brand safety controls:
- Content adjacency controls
- Fraud detection (TAG certified)
- Viewability standards (MRC accredited)
"""

        raise ValueError(f"Documentation not found: {resource_id}")

    raise ValueError(f"Unknown resource type: {resource_type}")


# =============================================================================
# MCP Tools
# =============================================================================

@app.list_tools()
async def list_tools() -> List[Tool]:
    """List available OpenSignals tools."""
    return [
        Tool(
            name="get_signal_manifest",
            description="""Get the complete OpenSignals manifest for a specific signal.

This tool retrieves the full signal manifest including:
- Signal metadata (name, type, status)
- Provenance information (data sources, collection method)
- Quality scores (coverage, freshness, precision, stability, explainability)
- Permissioning rules (consent requirements, usage restrictions)
- Governance controls (audit requirements, compliance frameworks)
- Technical specifications (API endpoints, authentication)

Use this tool when you need detailed information about a signal before verification or activation.

Example: Get manifest for attention measurement signal
Input: {"signal_id": "verified-attention-quality"}""",
            inputSchema={
                "type": "object",
                "properties": {
                    "signal_id": {
                        "type": "string",
                        "description": "Unique identifier of the signal (e.g., 'verified-attention-quality', 'outdoor-recreation-enthusiasts')"
                    }
                },
                "required": ["signal_id"]
            }
        ),

        Tool(
            name="verify_signal",
            description="""Verify if a signal is permitted and compliant for a specific use case.

This is the PRIMARY GOVERNANCE TOOL that AI agents should call before activating any signal.

The tool checks:
- Signal status (active/inactive/revoked)
- Geographic restrictions
- Permitted vs prohibited uses
- Category-specific compliance rules (alcohol, gambling, pharma, finance)
- Trust score thresholds
- Human approval requirements

Returns:
- Decision: approved, approved_with_conditions, or rejected
- Trust score and trust band
- Conditions (human approval, audit required, usage restrictions)
- Policy bindings (category-specific rules)
- Reasoning for the decision

Use this for EVERY signal before activation in agentic workflows.

Example: Verify alcohol signal for UK market
Input: {
  "signal_id": "outdoor-recreation-enthusiasts",
  "context": {
    "brand": "premium-spirits-co",
    "category": "alcohol",
    "market": "GB",
    "intended_use": "contextual_targeting"
  }
}""",
            inputSchema={
                "type": "object",
                "properties": {
                    "signal_id": {
                        "type": "string",
                        "description": "Signal identifier to verify"
                    },
                    "context": {
                        "type": "object",
                        "properties": {
                            "brand": {
                                "type": "string",
                                "description": "Brand identifier"
                            },
                            "category": {
                                "type": "string",
                                "description": "Product category: alcohol, gambling, pharma, finance, healthcare, general"
                            },
                            "market": {
                                "type": "string",
                                "description": "ISO 3166-1 alpha-2 country code (e.g., 'US', 'GB', 'FR')"
                            },
                            "intended_use": {
                                "type": "string",
                                "description": "Intended use case: targeting, measurement, attribution, contextual_placement, etc."
                            },
                            "campaign_id": {
                                "type": "string",
                                "description": "Campaign identifier (optional)"
                            }
                        },
                        "required": ["category", "market", "intended_use"]
                    }
                },
                "required": ["signal_id", "context"]
            }
        ),

        Tool(
            name="score_signal",
            description="""Calculate comprehensive trust score for a signal.

Returns detailed scoring across 7 dimensions:
1. Coverage: Breadth and reach across target population
2. Freshness: How recently the signal was updated
3. Precision: Accuracy and correctness of classifications
4. Stability: Consistency and reliability over time
5. Explainability: Transparency and interpretability
6. Compliance: Adherence to privacy regulations
7. Overall: Composite trust score

Also returns:
- Trust band (highly_trusted, trusted, limited_trust, low_trust, unsafe)
- Autonomy recommendation (autonomous, approve_with_human, recommend, observe, blocked)
- Dimension-specific details

Use this to evaluate signal quality before committing budget or when comparing multiple signals.

Example: Score a signal
Input: {"signal_id": "verified-attention-quality"}""",
            inputSchema={
                "type": "object",
                "properties": {
                    "signal_id": {
                        "type": "string",
                        "description": "Signal identifier to score"
                    },
                    "context": {
                        "type": "object",
                        "description": "Optional context for scoring (brand, objective, etc.)",
                        "properties": {
                            "brand": {"type": "string"},
                            "campaign_goal": {"type": "string"},
                            "target_audience": {"type": "string"}
                        }
                    }
                },
                "required": ["signal_id"]
            }
        ),

        Tool(
            name="audit_signal_usage",
            description="""Log signal usage for audit and compliance tracking.

Creates an audit trail entry recording:
- When the signal was used
- Who used it (agent, human approver)
- What it was used for (campaign, use case)
- How it was approved (autonomous, human approval)
- Policy bindings applied

This tool should be called AFTER signal activation to maintain compliance audit trails.

Returns:
- Audit ID for tracking
- Timestamp
- Retention period (default 90 days)

Required for regulated categories (alcohol, gambling, pharma, finance).

Example: Log signal activation
Input: {
  "signal_id": "outdoor-recreation-enthusiasts",
  "event_type": "signal_activated",
  "context": {
    "brand": "premium-spirits-co",
    "campaign_id": "spring-campaign-2026",
    "buyer_agent": "media-optimizer-v2",
    "human_approver": "jane.smith@brand.com",
    "category": "alcohol",
    "trust_score": 0.87
  }
}""",
            inputSchema={
                "type": "object",
                "properties": {
                    "signal_id": {
                        "type": "string",
                        "description": "Signal identifier"
                    },
                    "event_type": {
                        "type": "string",
                        "description": "Event type: signal_activated, signal_verified, signal_deactivated",
                        "enum": ["signal_activated", "signal_verified", "signal_deactivated", "signal_modified"]
                    },
                    "context": {
                        "type": "object",
                        "description": "Event context (brand, campaign, agent, approver, etc.)",
                        "properties": {
                            "brand": {"type": "string"},
                            "campaign_id": {"type": "string"},
                            "buyer_agent": {"type": "string"},
                            "human_approver": {"type": "string"},
                            "category": {"type": "string"},
                            "trust_score": {"type": "number"}
                        }
                    }
                },
                "required": ["signal_id", "event_type", "context"]
            }
        ),

        Tool(
            name="list_signals",
            description="""List all available signals with summary information.

Returns a list of signals from the examples directory, including:
- Signal ID and name
- Signal type (audience, contextual, attention, commerce, etc.)
- Status (active, inactive, experimental, deprecated)
- Overall trust score
- File path

Use this to discover available signals before requesting full manifests.

Example: List all signals
Input: {}

Optional filter by type:
Input: {"signal_type": "attention"}""",
            inputSchema={
                "type": "object",
                "properties": {
                    "signal_type": {
                        "type": "string",
                        "description": "Optional: Filter by signal type (audience, contextual, attention, commerce, etc.)"
                    },
                    "status": {
                        "type": "string",
                        "description": "Optional: Filter by status (active, inactive, experimental, deprecated)"
                    },
                    "min_trust_score": {
                        "type": "number",
                        "description": "Optional: Minimum trust score (0-1)"
                    }
                }
            }
        ),

        Tool(
            name="check_compliance",
            description="""Check compliance requirements for a specific category and market.

This tool provides category-specific compliance rules without requiring a specific signal.
Use it to understand requirements BEFORE searching for signals.

Returns:
- Whether the category is restricted in the market
- Human approval requirements
- Age restrictions
- Prohibited and allowed uses
- Required compliance frameworks
- Special requirements (documentation, risk warnings, etc.)

Essential for regulated categories: alcohol, gambling, pharma, finance.

Example: Check alcohol compliance in UK
Input: {
  "category": "alcohol",
  "market": "GB"
}""",
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "Product category: alcohol, gambling, pharma, finance, healthcare, general"
                    },
                    "market": {
                        "type": "string",
                        "description": "ISO 3166-1 alpha-2 country code (e.g., 'US', 'GB', 'FR', 'SA')"
                    }
                },
                "required": ["category", "market"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> List[TextContent]:
    """Handle tool calls."""

    try:
        if name == "get_signal_manifest":
            signal_id = arguments.get("signal_id")
            if not signal_id:
                return [TextContent(
                    type="text",
                    text=json.dumps({"error": "signal_id is required"}, indent=2)
                )]

            # Find signal
            signals = get_available_signals()
            signal = next((s for s in signals if s["signal_id"] == signal_id), None)

            if not signal:
                available_ids = [s["signal_id"] for s in signals]
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "error": f"Signal not found: {signal_id}",
                        "available_signals": available_ids
                    }, indent=2)
                )]

            # Load manifest
            manifest = load_json_file(Path(signal["file_path"]))
            if not manifest:
                return [TextContent(
                    type="text",
                    text=json.dumps({"error": f"Failed to load manifest for {signal_id}"}, indent=2)
                )]

            return [TextContent(
                type="text",
                text=json.dumps({
                    "task": "get_signal_manifest",
                    "signal_id": signal_id,
                    "manifest": manifest
                }, indent=2)
            )]

        elif name == "verify_signal":
            signal_id = arguments.get("signal_id")
            context = arguments.get("context", {})

            if not signal_id:
                return [TextContent(
                    type="text",
                    text=json.dumps({"error": "signal_id is required"}, indent=2)
                )]

            if not context.get("category") or not context.get("market") or not context.get("intended_use"):
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "error": "context must include category, market, and intended_use"
                    }, indent=2)
                )]

            # Find signal
            signals = get_available_signals()
            signal = next((s for s in signals if s["signal_id"] == signal_id), None)

            if not signal:
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "error": f"Signal not found: {signal_id}"
                    }, indent=2)
                )]

            # Load manifest
            manifest = load_json_file(Path(signal["file_path"]))
            if not manifest:
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "error": f"Failed to load manifest for {signal_id}"
                    }, indent=2)
                )]

            # Verify compliance
            verification = verify_signal_compliance(manifest, context)

            return [TextContent(
                type="text",
                text=json.dumps({
                    "task": "verify_signal",
                    **verification
                }, indent=2)
            )]

        elif name == "score_signal":
            signal_id = arguments.get("signal_id")
            context = arguments.get("context")

            if not signal_id:
                return [TextContent(
                    type="text",
                    text=json.dumps({"error": "signal_id is required"}, indent=2)
                )]

            # Find signal
            signals = get_available_signals()
            signal = next((s for s in signals if s["signal_id"] == signal_id), None)

            if not signal:
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "error": f"Signal not found: {signal_id}"
                    }, indent=2)
                )]

            # Load manifest
            manifest = load_json_file(Path(signal["file_path"]))
            if not manifest:
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "error": f"Failed to load manifest for {signal_id}"
                    }, indent=2)
                )]

            # Calculate trust score
            trust_score = calculate_trust_score(manifest, context)

            return [TextContent(
                type="text",
                text=json.dumps({
                    "task": "score_signal",
                    **trust_score
                }, indent=2)
            )]

        elif name == "audit_signal_usage":
            signal_id = arguments.get("signal_id")
            event_type = arguments.get("event_type")
            context = arguments.get("context", {})

            if not signal_id or not event_type:
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "error": "signal_id and event_type are required"
                    }, indent=2)
                )]

            # Create audit log
            audit_log = create_audit_log(signal_id, event_type, context)

            return [TextContent(
                type="text",
                text=json.dumps({
                    "task": "audit_signal_usage",
                    **audit_log
                }, indent=2)
            )]

        elif name == "list_signals":
            signal_type = arguments.get("signal_type")
            status = arguments.get("status")
            min_trust_score = arguments.get("min_trust_score")

            # Get all signals
            signals = get_available_signals()

            # Apply filters
            if signal_type:
                signals = [s for s in signals if s["signal_type"] == signal_type]

            if status:
                signals = [s for s in signals if s["status"] == status]

            if min_trust_score is not None:
                signals = [s for s in signals if s.get("overall_trust_score", 0) >= min_trust_score]

            return [TextContent(
                type="text",
                text=json.dumps({
                    "task": "list_signals",
                    "count": len(signals),
                    "signals": signals
                }, indent=2)
            )]

        elif name == "check_compliance":
            category = arguments.get("category")
            market = arguments.get("market")

            if not category or not market:
                return [TextContent(
                    type="text",
                    text=json.dumps({
                        "error": "category and market are required"
                    }, indent=2)
                )]

            # Check compliance
            compliance = check_category_compliance(category, market)

            return [TextContent(
                type="text",
                text=json.dumps({
                    "task": "check_compliance",
                    **compliance
                }, indent=2)
            )]

        else:
            return [TextContent(
                type="text",
                text=json.dumps({"error": f"Unknown tool: {name}"}, indent=2)
            )]

    except Exception as e:
        logger.error(f"Error in tool {name}: {e}", exc_info=True)
        return [TextContent(
            type="text",
            text=json.dumps({
                "error": str(e),
                "tool": name
            }, indent=2)
        )]


# =============================================================================
# Main Entry Point
# =============================================================================

async def main():
    """Run the MCP server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
