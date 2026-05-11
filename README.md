# OpenSignals Protocol

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-0.1.0-brightgreen.svg)](CHANGELOG.md)
[![Status](https://img.shields.io/badge/Status-Draft%20RFC-yellow.svg)](specs/opensignals-v0.1.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

OpenSignals Protocol is an open standard for signal trust verification in programmatic advertising. It provides machine-readable manifests for data quality, provenance, permissioning, and compliance assessment.

**Purpose**: Enable programmatic buyers and AI agents to evaluate signal trust before activation.

**Scope**: Signal-level trust verification. Does not replace signal discovery (AdCP), agent governance (AAMP), or real-time bidding (OpenRTB).

---

## Table of Contents

- [Overview](#overview)
- [Protocol Tasks](#protocol-tasks)
- [Trust Scoring Model](#trust-scoring-model)
- [Integration](#integration)
- [Implementation](#implementation)
- [Specification](#specification)
- [Examples](#examples)
- [Contributing](#contributing)

---

## Overview

### Problem Statement

Programmatic advertising increasingly relies on third-party signals for targeting. Buyers need standardized methods to assess:

1. **Data Quality**: Coverage, precision, stability
2. **Provenance**: Source transparency and chain of custody
3. **Permissioning**: Consent scope and usage rights
4. **Freshness**: Update frequency and staleness
5. **Compliance**: Regulatory adherence (GDPR, CCPA, industry codes)
6. **Auditability**: Ability to trace signal usage

Currently, these assessments are:
- Manual and non-standardized
- Opaque to automated systems
- Difficult to audit
- Inconsistent across providers

### Solution

OpenSignals Protocol defines:

1. **Signal Manifests**: Machine-readable declarations of signal properties
2. **Trust Scoring**: Multi-dimensional quality assessment
3. **Verification Tasks**: Standard API for trust assessment
4. **Audit Trails**: Logging and accountability mechanisms
5. **Policy Binding**: Governance rule enforcement

### Relationship to Existing Standards

| Protocol | Purpose | OpenSignals Relationship |
|----------|---------|-------------------------|
| **AdCP** | Signal discovery and activation | OpenSignals extends AdCP responses with trust metadata |
| **IAB AAMP** | Agent governance framework | OpenSignals implements signal-level trust (AAMP pillar 3) |
| **OpenRTB** | Real-time bidding | OpenSignals provides pre-bid trust assessment |
| **OpenDirect** | Direct programmatic deals | OpenSignals verifies signal quality for deal terms |
| **AdCOM** | Common advertising object model | OpenSignals uses compatible taxonomies |

---

## Protocol Tasks

OpenSignals defines seven tasks:

### 1. `get_signal_manifest`
Retrieve the trust manifest for a signal.

**Request**:
```json
{
  "task": "get_signal_manifest",
  "signal_id": "outdoor-recreation-enthusiasts"
}
```

**Response**: Complete manifest (see [schemas/v0.1/open-signal-manifest.schema.json](schemas/v0.1/open-signal-manifest.schema.json))

### 2. `verify_signal`
Check if a signal meets brand policy requirements.

**Request**:
```json
{
  "task": "verify_signal",
  "signal_id": "outdoor-recreation-enthusiasts",
  "brand": "premium-spirits-co",
  "market": "GB",
  "category": "alcohol",
  "intended_use": "contextual_targeting"
}
```

**Response**:
```json
{
  "decision": "approved_with_conditions",
  "trust_score": 0.87,
  "conditions": ["human_approval_required", "audit_required"],
  "policy_bindings": ["alcohol_age_restriction", "uk_advertising_standards"],
  "reasoning": "Signal approved for contextual use. Individual-level targeting prohibited."
}
```

### 3. `score_signal`
Calculate trust score against specific objectives.

### 4. `bind_signal_policy`
Attach brand policy rules to a signal.

### 5. `audit_signal_usage`
Log signal activation for compliance.

### 6. `revoke_signal`
Mark a signal as untrusted.

### 7. `submit_signal_outcome_feedback`
Report campaign performance for score adjustment.

**Complete specification**: [specs/opensignals-v0.1.md](specs/opensignals-v0.1.md)

---

## Trust Scoring Model

OpenSignals uses a multi-dimensional scoring model:

### Dimensions (0.0 to 1.0)

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Provenance** | 20% | Data source transparency |
| **Permissioning** | 20% | Consent and usage rights |
| **Freshness** | 15% | Update recency |
| **Quality** | 20% | Coverage, precision, stability |
| **Explainability** | 10% | Clarity of methodology |
| **Outcome** | 10% | Historical performance |
| **Compliance** | 5% | Regulatory adherence |

**Overall Trust Score**: Weighted average of dimensions

### Score Bands

- **0.90-1.00**: High trust
- **0.75-0.89**: Moderate trust
- **0.50-0.74**: Limited trust
- **0.25-0.49**: Low trust
- **0.00-0.24**: Untrusted

**Score interpretation depends on brand risk tolerance**. Custom weighting is supported.

---

## Integration

### With AdCP

OpenSignals extends AdCP `get_signals` responses:

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
        "manifest_url": "https://provider.example/.well-known/opensignals/outdoor-recreation-enthusiasts",
        "overall_trust_score": 0.87,
        "verification_required": true,
        "last_verified": "2026-05-11T08:00:00Z"
      }
    }
  ]
}
```

**Integration point**: Optional `open_signals` field in signal objects.

### With AAMP

OpenSignals provides signal-level trust data for AAMP's Trust & Transparency pillar:

- **Agent Registry**: Signal providers publish OpenSignal Manifests
- **Bounded Autonomy**: Trust scores determine human-in-loop requirements
- **Audit Trails**: OpenSignals logging integrates with AAMP audit requirements

### With OpenRTB

Trust scores can be passed in bid request extensions:

```json
{
  "imp": [{
    "ext": {
      "opensignals": {
        "signals_used": ["outdoor-recreation-enthusiasts"],
        "trust_scores": [0.87],
        "verification_status": "approved_with_conditions"
      }
    }
  }]
}
```

**Use case**: DSPs can factor trust scores into bid pricing and decisioning.

---

## Implementation

### Reference Implementation (Python)

Production-ready FastAPI server:

```bash
cd reference-implementation/python
pip install -r requirements.txt
python server.py
```

**Endpoints**:
- `GET /health` - Health check
- `POST /validate-manifest` - Validate signal manifest
- `POST /verify-signal` - Verify signal compliance
- `POST /score-signal` - Calculate trust score
- `POST /audit-signal-usage` - Log activation

**API Documentation**: http://localhost:8000/docs

### MCP Server (AI Agent Integration)

Model Context Protocol server for Claude Desktop and other MCP clients:

```bash
cd mcp-server
./install.sh
```

**Tools exposed**:
- `get_signal_manifest`
- `verify_signal`
- `score_signal`
- `list_signals`
- `check_compliance`
- `audit_signal_usage`

### Client Libraries

**Python**:
```python
from opensignals import Client

client = Client()
result = client.verify_signal(
    signal_id="outdoor-recreation-enthusiasts",
    brand="premium-spirits-co",
    market="GB",
    category="alcohol"
)
```

**JavaScript/TypeScript**: Planned Q3 2026
**Go**: Planned Q4 2026

---

## Specification

### Core Documents

- **[Protocol Specification](specs/opensignals-v0.1.md)** - Complete technical specification
- **[Conformance Requirements](specs/conformance.md)** - Implementation requirements
- **[Terminology](specs/terminology.md)** - Definitions

### JSON Schemas

All schemas use JSON Schema Draft 2020-12:

- [open-signal-manifest.schema.json](schemas/v0.1/open-signal-manifest.schema.json)
- [trust-score.schema.json](schemas/v0.1/trust-score.schema.json)
- [verify-signal-request.schema.json](schemas/v0.1/verify-signal-request.schema.json)
- [verify-signal-response.schema.json](schemas/v0.1/verify-signal-response.schema.json)
- [audit-signal-usage-request.schema.json](schemas/v0.1/audit-signal-usage-request.schema.json)
- [audit-signal-usage-response.schema.json](schemas/v0.1/audit-signal-usage-response.schema.json)
- [policy-binding.schema.json](schemas/v0.1/policy-binding.schema.json)

### Authentication

OpenSignals supports:
- **HTTP Message Signatures** (RFC 9421) - Recommended
- **OAuth 2.0** - For platform integrations
- **API Keys** - For simple deployments
- **Chain-of-Thought Authentication** - Cryptographic reasoning verification (see [docs/CHAIN-OF-THOUGHT-AUTH.md](docs/CHAIN-OF-THOUGHT-AUTH.md))

---

## Examples

### Signal Manifests

Ten production-ready examples demonstrating different signal types and compliance requirements:

**Regulated Categories**:
- [alcohol-contextual-signal.json](examples/alcohol-contextual-signal.json) - Age-restricted, CAP Code compliant
- [pharmaceutical-signal.json](examples/pharmaceutical-signal.json) - HIPAA considerations
- [financial-services-signal.json](examples/financial-services-signal.json) - GLBA, SOX compliance
- [gambling-signal.json](examples/political-signal.json) - Election law compliance
- [children-safe-signal.json](examples/children-safe-signal.json) - COPPA compliant

**Standard Categories**:
- [attention-signal.json](examples/attention-signal.json) - Measurement signal
- [retail-commerce-signal.json](examples/retail-commerce-signal.json) - First-party commerce data
- [luxury-intent-signal.json](examples/luxury-intent-signal.json) - High-value audience
- [sustainability-signal.json](examples/sustainability-signal.json) - ESG-verified
- [carbon-neutral-signal.json](examples/carbon-neutral-signal.json) - Climate-conscious

**Documentation**:
- [SIGNAL-CATALOG.md](examples/SIGNAL-CATALOG.md) - Detailed explanations
- [EXAMPLES-BY-SCENARIO.md](examples/EXAMPLES-BY-SCENARIO.md) - Organized by use case

### Integration Examples

**AdCP**:
- [adcp-extension-example.json](integrations/adcp/adcp-extension-example.json)
- [get-signals-with-opensignals.json](integrations/adcp/get-signals-with-opensignals.json)
- [README.md](integrations/adcp/README.md)

**AAMP**:
- [aamp-trust-layer-mapping.md](integrations/aamp/aamp-trust-layer-mapping.md)
- [README.md](integrations/aamp/README.md)

---

## Testing

### Validation Tests

```bash
cd tests
pytest test_manifest_validation.py -v
```

**Test coverage**:
- Schema validation (all 7 schemas)
- Trust score calculation
- Compliance checking
- Example manifest validation

### Integration Tests

```bash
cd reference-implementation/python
python test_api.py
```

**Test scenarios**:
- Alcohol campaign verification
- Trust score threshold checking
- Policy binding enforcement
- Audit trail creation

---

## Documentation

### Architecture

- [architecture.md](docs/architecture.md) - System design
- [gap-analysis.md](docs/gap-analysis.md) - Market analysis

### Implementation Guides

- [adoption-guide.md](docs/adoption-guide.md) - Implementation roadmap
- [brand-side-use-case.md](docs/brand-side-use-case.md) - Real-world example
- [NATURAL-LANGUAGE-GUIDE.md](docs/NATURAL-LANGUAGE-GUIDE.md) - AI agent integration

### Governance

- [governance-model.md](docs/governance-model.md) - Protocol governance
- [ROADMAP.md](ROADMAP.md) - Development roadmap
- [SECURITY.md](SECURITY.md) - Security policy

### FAQ

See [docs/FAQ.md](docs/FAQ.md) for:
- Protocol scope and limitations
- Integration requirements
- Performance characteristics
- Privacy considerations
- Adoption strategy

---

## Contributing

OpenSignals Protocol is an open standard. Contributions welcome from:

- Signal providers
- Programmatic platforms (DSPs, SSPs)
- Brands and agencies
- Standards bodies
- Technology providers
- Researchers

**Contribution types**:
- Protocol enhancements
- Schema improvements
- Implementation code
- Integration examples
- Test cases
- Documentation

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Key principles**:
- Technical merit over marketing
- Interoperability over features
- Simplicity over complexity
- Standards over proprietary solutions

---

## Versioning

OpenSignals uses semantic versioning:

- **Major** (1.0): Breaking changes
- **Minor** (0.x): Backward-compatible additions
- **Patch** (0.x.y): Bug fixes and clarifications

**Current version**: 0.1.0 (Draft RFC)

**Status**: The v0.1 specification is feature-complete and ready for implementation. Breaking changes are possible before 1.0.

**Deprecation policy**: 12 months notice for breaking changes.

---

## License

- **Code and Schemas**: [Apache License 2.0](LICENSE)
- **Documentation**: [Creative Commons Attribution 4.0](LICENSE-DOCS)

**Why open source**: Maximize adoption, prevent vendor lock-in, enable community governance.

---

## Status and Disclaimer

**Status**: Draft RFC v0.1.0 (May 2026)

OpenSignals Protocol is an independent open-source project. It is not endorsed by:
- AdCP or AgenticAdvertising.Org
- IAB Tech Lab or IAB
- Any standards body or industry organization

**Goal**: Create a practical standard that complements existing infrastructure by addressing signal trust verification.

**Adoption**: Voluntary. Signal providers, platforms, and buyers choose whether to implement.

---

## References

### Standards

- **AdCP**: [adcontextprotocol.org](https://adcontextprotocol.org/) | [GitHub](https://github.com/adcontextprotocol/adcp)
- **IAB AAMP**: [iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/](https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/)
- **OpenRTB**: [GitHub](https://github.com/InteractiveAdvertisingBureau/openrtb2.x)
- **AdCOM**: [GitHub](https://github.com/InteractiveAdvertisingBureau/AdCOM)
- **Model Context Protocol**: [modelcontextprotocol.io](https://modelcontextprotocol.io/)
- **Agent2Agent**: [a2a-protocol.org](https://a2a-protocol.org/)

See [SOURCES.md](SOURCES.md) for complete references.

---

## Contact

**Repository**: https://github.com/Samrajtheailyceum/opensignals-protocol

**Issues**: [github.com/Samrajtheailyceum/opensignals-protocol/issues](https://github.com/Samrajtheailyceum/opensignals-protocol/issues)

**Discussions**: [github.com/Samrajtheailyceum/opensignals-protocol/discussions](https://github.com/Samrajtheailyceum/opensignals-protocol/discussions)

**Security**: See [SECURITY.md](SECURITY.md) for vulnerability reporting.

---

## Repository Structure

```
opensignals-protocol/
├── specs/                  # Protocol specification
│   ├── opensignals-v0.1.md
│   ├── terminology.md
│   └── conformance.md
├── schemas/v0.1/           # JSON schemas
├── examples/               # Sample signal manifests
├── integrations/           # Integration guides
│   ├── adcp/
│   └── aamp/
├── reference-implementation/
│   └── python/            # FastAPI server
├── mcp-server/            # AI agent integration
├── tests/                 # Test suite
└── docs/                  # Additional documentation
```

---

**OpenSignals Protocol** - Signal trust verification for programmatic advertising

Version 0.1.0 | May 2026 | Apache 2.0 License
