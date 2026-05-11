# Sources and References

This document lists the official sources, standards and documentation consulted during the development of OpenSignals Protocol v0.1.

## Primary Sources

| Source | Link | Relevance to OpenSignals | Repository Sections Informed |
|--------|------|-------------------------|------------------------------|
| **AdCP (Ad Context Protocol)** | [adcontextprotocol.org](https://adcontextprotocol.org/) | Signal discovery and activation framework. OpenSignals extends AdCP by adding pre-activation trust verification. | README.md, integrations/adcp/, specs/opensignals-v0.1.md |
| **AdCP GitHub Repository** | [github.com/adcontextprotocol/adcp](https://github.com/adcontextprotocol/adcp) | Technical implementation of AdCP signal protocol, schemas and examples. | integrations/adcp/, schemas structure |
| **AdCP Documentation** | [docs.adcontextprotocol.org](https://docs.adcontextprotocol.org/) | Core concepts of signal discovery, activation, provenance and freshness. | specs/opensignals-v0.1.md, terminology.md |
| **IAB Tech Lab AAMP** | [iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/](https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/) | Industry framework for agentic advertising with three pillars: Foundations, Protocols, and Trust and Transparency. OpenSignals aligns with the Trust pillar. | README.md, integrations/aamp/, docs/governance-model.md |
| **IAB Tech Lab AdCOM** | [github.com/InteractiveAdvertisingBureau/AdCOM](https://github.com/InteractiveAdvertisingBureau/AdCOM) | Common object model for programmatic advertising. Referenced for taxonomy and enumeration patterns. | schemas/v0.1/open-signal-manifest.schema.json (signal_type enums) |
| **IAB Tech Lab OpenRTB** | [github.com/InteractiveAdvertisingBureau/openrtb2.x](https://github.com/InteractiveAdvertisingBureau/openrtb2.x) | Real-time bidding protocol. OpenSignals operates above the execution layer that OpenRTB defines. | README.md, specs/opensignals-v0.1.md |
| **Model Context Protocol (MCP)** | [modelcontextprotocol.io](https://modelcontextprotocol.io/) | Open protocol for LLM integration with external data sources and tools. Referenced as potential transport for OpenSignals. | README.md, specs/opensignals-v0.1.md |
| **MCP Specification** | [modelcontextprotocol.io/specification/2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25) | Technical specification for MCP protocol. | specs/opensignals-v0.1.md (MCP integration considerations) |
| **Agent2Agent (A2A) Protocol** | [a2a-protocol.org](https://a2a-protocol.org/) | Open protocol for agent communication. Referenced as potential inter-agent transport. | README.md, specs/opensignals-v0.1.md |
| **A2A Specification** | [a2a-protocol.org/latest/specification/](https://a2a-protocol.org/latest/specification/) | Technical specification for A2A protocol including Agent Cards and Task structures. | specs/opensignals-v0.1.md (A2A integration considerations) |
| **RFC 2119 (Key words for RFCs)** | [datatracker.ietf.org/doc/html/rfc2119](https://datatracker.ietf.org/doc/html/rfc2119) | Defines MUST, SHOULD, MAY terminology used in specifications. | specs/opensignals-v0.1.md, specs/conformance.md |
| **JSON Schema** | [json-schema.org](https://json-schema.org/) | Schema validation standard used throughout OpenSignals. | All files in schemas/v0.1/ |

## Secondary References

| Source | Relevance |
|--------|-----------|
| **IAB Tech Lab Standards Overview** | Context for programmatic advertising standards ecosystem |
| **RFC 9421 (HTTP Message Signatures)** | Authentication mechanism used by AdCP, referenced for security considerations |
| **VAST (Video Ad Serving Template)** | Video ad standard, part of IAB's broader standards family |
| **OpenDirect** | Direct programmatic buying specifications |

## Research Methodology

### What Was Reviewed

1. **AdCP Protocol**:
   - Core concepts of signal discovery via `get_signals`
   - Signal activation via `activate_signal`
   - Provenance and freshness mechanisms
   - Governance and audit capabilities
   - HTTP Message Signatures for authentication
   - Transport over MCP and A2A

2. **IAB Tech Lab AAMP**:
   - Three-pillar architecture (Foundations/ARTF, Protocols, Trust and Transparency)
   - Agent Registry for transparency and accountability
   - Extension approach for existing standards (OpenRTB, AdCOM, OpenDirect)
   - Industry governance model

3. **IAB Standards (OpenRTB, AdCOM, OpenDirect)**:
   - Object model patterns and taxonomy structures
   - Enumeration conventions
   - Real-time bidding execution layer

4. **MCP and A2A Protocols**:
   - Resource and tool exposure patterns (MCP)
   - Agent-to-agent communication patterns (A2A)
   - Task structures and capability advertisement

### What Was Not Directly Reviewed

The following were not reviewed in detail but may be relevant for future versions:

- ARTF (Agentic Runtime Framework) technical specifications
- IAB Tech Lab Agent Registry implementation details
- Specific DSP/SSP signal activation APIs
- Privacy framework specifications (GDPR, CCPA technical implementations)
- Brand safety vendor specifications

## Key Distinctions Made

Based on source review, OpenSignals Protocol was designed to:

1. **Complement AdCP**, not replace it:
   - AdCP handles signal discovery and activation
   - OpenSignals adds pre-activation trust verification

2. **Align with AAMP's Trust pillar**, not duplicate it:
   - AAMP provides industry governance framework
   - OpenSignals provides practical implementation layer for signal trust

3. **Operate above OpenRTB/OpenDirect**, not modify them:
   - OpenRTB/OpenDirect handle execution and auctions
   - OpenSignals helps agents decide which signals are trusted enough to use in those systems

4. **Conceptual integration with MCP/A2A**, not formal dependency:
   - OpenSignals tasks could be exposed as MCP tools or A2A skills
   - This is a design possibility, not a confirmed integration

## Accuracy and Limitations

### Confirmed Facts

- AdCP provides signal discovery and activation via `get_signals` and `activate_signal`
- AAMP has three pillars including Trust and Transparency
- IAB Tech Lab maintains OpenRTB, AdCOM and OpenDirect standards
- MCP and A2A are open protocols for agent communication
- AdCP uses HTTP Message Signatures for authentication

### Conceptual Mappings

The following are conceptual integrations, not confirmed implementations:

- AdCP extension examples in `integrations/adcp/` (labelled as conceptual)
- AAMP trust layer mapping in `integrations/aamp/` (labelled as conceptual)
- MCP and A2A integration possibilities (described as potential approaches)

### Unconfirmed Claims

OpenSignals Protocol does NOT claim:

- Official endorsement from AdCP, IAB Tech Lab, or any standards body
- Formal integration with any existing protocol
- Compatibility certification with any platform or vendor
- That any organization is using or planning to use OpenSignals

## Future Source Review

As OpenSignals Protocol evolves, the following sources should be reviewed:

- Formal AAMP protocol specifications when published
- AdCP signal schema updates
- IAB Tech Lab Agent Registry technical specifications
- Industry feedback on signal trust requirements
- Regulatory guidance on AI agent advertising (UK, EU, US)

## How to Update This Document

When adding new sources:

1. Verify the source is official and authoritative
2. Add to the appropriate table with full details
3. Update the "Repository Sections Informed" column
4. Document what was reviewed and what was inferred
5. Distinguish confirmed facts from conceptual mappings
6. Update relevant specification files to reference the new source

## Contact

For questions about source accuracy or to suggest additional sources, please open a GitHub issue with the `sources` label.

---

**Last Updated**: May 2026
**Protocol Version**: 0.1 (Draft RFC)
