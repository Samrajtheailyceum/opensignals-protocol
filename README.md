# OpenSignals Protocol

OpenSignals Protocol is an open trust layer for advertising signals used by AI agents.

It does not replace AdCP, AAMP, OpenRTB, OpenDirect, AdCOM or existing advertising infrastructure. Instead, it adds a standard way to declare, verify, score, permission and audit the signals that agents use when planning, buying and optimising media.

**AdCP helps agents discover and activate signals.**

**OpenSignals helps agents know which signals to trust.**

## Why OpenSignals?

The advertising industry is building infrastructure for AI agents to discover inventory, buy media and optimise campaigns. That infrastructure is necessary, but not sufficient.

Before an advertising agent activates a signal, it needs to know:

- Is this signal **valid** for my brand, market and category?
- Is this signal **permissioned** for this use case?
- Is this signal **fresh** enough to rely on?
- Can this signal be **explained** and **audited**?
- Is this signal **safe** for regulated categories like alcohol, gambling or financial services?
- Does this signal require **human approval** before activation?

OpenSignals provides a standardised framework to answer these questions.

## Core Principle

**Every signal used by an advertising agent should be declared, permissioned, scored and auditable.**

## Relationship to Existing Standards

OpenSignals is designed to complement existing advertising standards and agentic protocols:

### AdCP (Ad Context Protocol)
AdCP provides signal discovery and activation through `get_signals` and `activate_signal` tasks. OpenSignals extends this by adding trust metadata that can be evaluated before activation.

**Relationship**: OpenSignals adds a trust verification layer that sits between AdCP's signal discovery and signal activation steps.

- AdCP documentation: [adcontextprotocol.org](https://adcontextprotocol.org/)
- AdCP GitHub: [github.com/adcontextprotocol/adcp](https://github.com/adcontextprotocol/adcp)

### IAB Tech Lab AAMP (Agentic Advertising Management Protocols)
AAMP is the industry-wide framework for agentic advertising, built on three pillars: Foundations (ARTF), Protocols, and Trust and Transparency. OpenSignals specifically addresses the Trust and Transparency pillar by providing machine-readable signal trust metadata.

**Relationship**: OpenSignals complements AAMP's trust goals with a practical implementation framework for signal-level verification, permissioning and audit.

- AAMP overview: [iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/](https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/)

### OpenRTB, OpenDirect, AdCOM
These IAB Tech Lab standards define the execution layer for programmatic advertising. OpenSignals does not replace or modify these protocols. Instead, it provides a trust assessment layer that can be used before signals flow into OpenRTB auctions or OpenDirect transactions.

**Relationship**: OpenSignals operates above the execution layer, helping agents decide which signals are trusted enough to use in OpenRTB/OpenDirect workflows.

- IAB Tech Lab standards: [iabtechlab.com](https://iabtechlab.com/)
- AdCOM GitHub: [github.com/InteractiveAdvertisingBureau/AdCOM](https://github.com/InteractiveAdvertisingBureau/AdCOM)
- OpenRTB GitHub: [github.com/InteractiveAdvertisingBureau/openrtb2.x](https://github.com/InteractiveAdvertisingBureau/openrtb2.x)

### MCP (Model Context Protocol) and A2A (Agent2Agent)
OpenSignals can be exposed as an MCP resource or A2A skill, allowing agents to query signal trust before activation. This is a conceptual integration possibility, not a formal dependency.

- MCP specification: [modelcontextprotocol.io](https://modelcontextprotocol.io/)
- A2A specification: [a2a-protocol.org](https://a2a-protocol.org/)

## How It Works

```
┌─────────────────────────────────────────────────────────┐
│                    Brand Policy Layer                    │
│          (Brand safety, compliance, permissions)         │
└─────────────────────────────────────────────────────────┘
                            ▲
                            │
┌─────────────────────────────────────────────────────────┐
│                  OpenSignals Protocol                    │
│   (Trust scoring, verification, audit, permissioning)   │
└─────────────────────────────────────────────────────────┘
                            ▲
                            │
┌─────────────────────────────────────────────────────────┐
│               Signal Discovery Layer (AdCP)              │
│          (get_signals, activate_signal, catalogs)        │
└─────────────────────────────────────────────────────────┘
                            ▲
                            │
┌─────────────────────────────────────────────────────────┐
│              Execution Layer (AAMP ARTF)                 │
│         (OpenRTB, OpenDirect, DSP/SSP platforms)        │
└─────────────────────────────────────────────────────────┘
```

### Typical Workflow

1. **Brand Brief**: A brand wants to run a campaign for a regulated product (e.g., alcohol) in a specific market
2. **Signal Discovery**: Buyer agent discovers available signals via AdCP or compatible protocol
3. **Trust Verification**: Buyer agent requests OpenSignal Manifest for each signal
4. **Policy Check**: Governance agent verifies signal against brand policy, market restrictions and compliance requirements
5. **Trust Scoring**: Signal receives a trust score across multiple dimensions (provenance, freshness, quality, compliance)
6. **Human Approval**: For regulated categories or low-trust signals, human approval is required
7. **Signal Activation**: Once approved, signal is activated through AdCP or compatible workflow
8. **Audit Trail**: Signal usage is logged with full context (who, what, when, why, under what policy)
9. **Outcome Feedback**: Campaign results feed back into signal trust scores

## Core Protocol Tasks

OpenSignals defines seven core tasks:

| Task | Purpose |
|------|---------|
| `get_signal_manifest` | Retrieve the full OpenSignals manifest for a signal |
| `verify_signal` | Check if a signal is valid and permissioned for a specific use case |
| `score_signal` | Score a signal against a brand objective |
| `bind_signal_policy` | Attach brand policy rules to a signal before activation |
| `audit_signal_usage` | Record how a signal was used after activation |
| `revoke_signal` | Withdraw trust from a signal |
| `submit_signal_outcome_feedback` | Feed campaign results back into trust scoring |

See [specs/opensignals-v0.1.md](specs/opensignals-v0.1.md) for complete protocol specification.

## Quick Start

### 1. Request an OpenSignal Manifest

```bash
curl https://signals.example.com/.well-known/opensignals/outdoor-recreation-enthusiasts
```

Response:

```json
{
  "protocol": "opensignals",
  "version": "0.1",
  "signal_id": "outdoor-recreation-enthusiasts",
  "name": "Outdoor Recreation Enthusiasts",
  "signal_type": "audience",
  "status": "active",
  "owner": {
    "organization": "Example Data Co",
    "contact": "signals@example.com"
  },
  "provider": {
    "name": "Example Data Co",
    "url": "https://example.com"
  },
  "provenance": {
    "data_sources": ["first_party_behavioral", "survey"],
    "collection_method": "opt_in_panel",
    "last_updated": "2026-05-10T08:00:00Z"
  },
  "quality": {
    "overall_trust_score": 0.87,
    "coverage_score": 0.82,
    "freshness_score": 0.91,
    "precision_score": 0.85,
    "explainability_score": 0.89
  }
}
```

### 2. Verify Signal Before Activation

```bash
curl -X POST https://governance.brand.com/opensignals/verify \
  -H "Content-Type: application/json" \
  -d '{
    "signal_id": "outdoor-recreation-enthusiasts",
    "brand": "premium-spirits-co",
    "market": "GB",
    "category": "alcohol",
    "intended_use": "contextual_targeting"
  }'
```

Response:

```json
{
  "decision": "approved_with_conditions",
  "trust_score": 0.87,
  "conditions": [
    "human_approval_required",
    "audit_required",
    "no_individual_profiling"
  ],
  "policy_bindings": [
    "alcohol_age_restriction",
    "uk_advertising_standards"
  ],
  "decision_reasoning": "Signal approved for contextual use only. Individual-level targeting prohibited for alcohol category. Human review required before activation."
}
```

### 3. AdCP Integration Example

OpenSignals can extend AdCP responses with trust metadata:

```json
{
  "task": "get_signals",
  "signals": [
    {
      "signal_id": "outdoor-recreation-enthusiasts",
      "name": "Outdoor Recreation Enthusiasts",
      "coverage": 2400000,
      "cpm": 3.50,
      "open_signals": {
        "manifest_url": "https://signals.example.com/.well-known/opensignals/outdoor-recreation-enthusiasts",
        "overall_trust_score": 0.87,
        "verification_required": true,
        "audit_required": true,
        "policy_categories": ["general"],
        "last_verified": "2026-05-10T08:00:00Z"
      }
    }
  ]
}
```

See [integrations/adcp/](integrations/adcp/) for more examples.

## Repository Structure

```
opensignals-protocol/
├── README.md                   # This file
├── LICENSE                     # Apache 2.0 license
├── CONTRIBUTING.md             # Contribution guidelines
├── CODE_OF_CONDUCT.md          # Community standards
├── SOURCES.md                  # Official sources consulted
├── specs/
│   ├── opensignals-v0.1.md    # Protocol specification (RFC-style)
│   ├── terminology.md          # Definitions
│   └── conformance.md          # Conformance requirements
├── schemas/v0.1/               # JSON schemas
├── examples/                   # Example manifests
├── integrations/
│   ├── adcp/                   # AdCP integration examples
│   └── aamp/                   # AAMP conceptual mapping
├── reference-implementation/
│   └── python/                 # Python reference server
├── tests/                      # Validation tests
└── docs/                       # Additional documentation
```

## Trust Score Model

OpenSignals uses a multi-dimensional trust scoring model:

| Dimension | Description | Weight |
|-----------|-------------|--------|
| **Provenance** | Data source transparency and chain of custody | 20% |
| **Permissioning** | Clear consent and usage rights | 20% |
| **Freshness** | How recently the signal was updated | 15% |
| **Quality** | Coverage, precision and stability | 20% |
| **Explainability** | How well the signal can be explained | 10% |
| **Outcome Relevance** | Historical performance against similar objectives | 10% |
| **Compliance Safety** | Adherence to regulations and brand safety standards | 5% |

**Overall Trust Score Bands:**

- **0.90 to 1.00**: Highly trusted. Can be used autonomously (if policy allows)
- **0.75 to 0.89**: Trusted with conditions. Use with governance checks
- **0.50 to 0.74**: Limited trust. Require human review
- **0.25 to 0.49**: Low trust. Do not activate without explicit approval
- **0.00 to 0.24**: Unsafe or invalid. Block usage

## Examples

Four example manifests demonstrate different signal types and trust levels:

- **[Alcohol Contextual Signal](examples/alcohol-contextual-signal.json)**: Regulated category with strict governance
- **[Attention Signal](examples/attention-signal.json)**: High-quality measurement signal
- **[Retail Commerce Signal](examples/retail-commerce-signal.json)**: First-party commerce data
- **[Sustainability Signal](examples/sustainability-signal.json)**: Environmental impact signal

## Contributing

We welcome contributions from advertising practitioners, standards bodies, agencies, brands, platforms, data providers and AI agent developers.

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Key principles:**

- Maintain neutrality and avoid vendor-specific claims
- Distinguish confirmed integrations from conceptual mappings
- Cite official sources for compatibility claims
- Focus on practical signal trust challenges
- Keep specifications clear and implementable

## License

- **Code**: Apache License 2.0
- **Documentation and Specifications**: Intended to be shared under Creative Commons Attribution 4.0 International (CC BY 4.0)

See [LICENSE](LICENSE) for details.

## Status and Disclaimer

**Status**: Draft RFC v0.1 (May 2026)

OpenSignals Protocol is an independent open-source project. It is not endorsed by, affiliated with, or officially recognized by:

- AdCP or AgenticAdvertising.Org
- IAB Tech Lab or IAB
- Any standards body or industry organization

This protocol is a draft proposal intended to stimulate discussion and collaboration around signal trust in agentic advertising.

The goal is to create a practical, implementable standard that complements existing infrastructure by addressing a specific gap: how agents can assess signal trust before activation.

## Contact

- **Issues and Discussion**: [GitHub Issues](https://github.com/opensignals-protocol/opensignals-protocol/issues)
- **Specification Questions**: Open an issue with the `spec-question` label
- **Integration Examples**: Open an issue with the `integration-example` label

## Acknowledgments

This protocol was developed with reference to public documentation from:

- AdCP and the Ad Context Protocol community
- IAB Tech Lab's AAMP initiative
- Model Context Protocol specification
- Agent2Agent Protocol specification
- IAB Tech Lab's OpenRTB, OpenDirect and AdCOM standards

See [SOURCES.md](SOURCES.md) for complete references.
