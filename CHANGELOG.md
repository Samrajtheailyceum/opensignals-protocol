# Changelog

All notable changes to the OpenSignals Protocol will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial draft protocol specification (v0.1)
- Core schema definitions for signal manifests, verification requests/responses, and audit trails
- Python reference implementation with FastAPI server
- AdCP integration examples showing `get_signals` extension
- AAMP trust layer mapping documentation
- Example signal manifests for alcohol, attention, retail commerce, and sustainability use cases
- Comprehensive documentation including architecture, governance model, and use cases
- Conformance requirements and terminology definitions
- Validation tests for manifest schemas

### Documentation
- README with protocol overview and quick start guide
- Contributing guidelines and code of conduct
- Sources and acknowledgments document
- Architecture documentation
- Brand-side use case examples
- Governance model specification

## [0.1.0] - 2026-05-11

### Initial Release

This is the first draft release of the OpenSignals Protocol, introducing a trust layer for advertising signals used by AI agents.

#### Core Features
- **Signal Manifests**: JSON Schema-based format for declaring signal trust metadata
- **Trust Scoring**: Multi-dimensional trust model across 7 dimensions (provenance, permissioning, freshness, quality, explainability, outcome relevance, compliance safety)
- **Verification API**: Endpoints for verifying signals against brand policies and use cases
- **Audit Trail**: Structured logging for signal usage and outcomes
- **Policy Binding**: Framework for attaching brand policy rules to signals

#### Protocol Tasks
- `get_signal_manifest`: Retrieve OpenSignals manifest for a signal
- `verify_signal`: Check if signal is valid and permissioned
- `score_signal`: Score signal against brand objective
- `bind_signal_policy`: Attach policy rules before activation
- `audit_signal_usage`: Record signal usage
- `revoke_signal`: Withdraw trust from signal
- `submit_signal_outcome_feedback`: Feed campaign results back

#### Integration Examples
- AdCP extension pattern showing trust metadata in `get_signals` responses
- AAMP trust layer conceptual mapping
- Example implementations for regulated categories (alcohol)

#### Reference Implementation
- Python/FastAPI server implementing core verification and scoring logic
- JSON Schema validation
- Basic trust score calculation
- API endpoints matching protocol specification

#### Known Limitations
- Draft specification, subject to change
- Reference implementation is illustrative, not production-ready
- No formal standardization body endorsement
- Limited real-world testing

### Notes
This release is intended to stimulate discussion and gather feedback from the advertising industry, standards bodies, and AI agent developers. The protocol addresses a specific gap in agentic advertising infrastructure: enabling agents to assess signal trust before activation.

---

## Version History

- **v0.1.0** (2026-05-11): Initial draft release with core protocol specification, schemas, reference implementation, and integration examples

[Unreleased]: https://github.com/Samrajtheailyceum/opensignals-protocol/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/Samrajtheailyceum/opensignals-protocol/releases/tag/v0.1.0
