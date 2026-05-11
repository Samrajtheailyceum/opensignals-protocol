# OpenSignals Protocol v0.1

**Status**: Draft RFC
**Version**: 0.1
**Date**: May 2026
**Authors**: OpenSignals Protocol Community
**License**: Apache 2.0 (code), CC BY 4.0 (documentation)

---

## Abstract

The OpenSignals Protocol defines a standardized framework for declaring, verifying, scoring, permissioning and auditing advertising signals used by autonomous AI agents. It provides a trust verification layer that operates above signal discovery protocols (such as AdCP) and below execution protocols (such as OpenRTB), enabling agents to assess signal trustworthiness before activation. The protocol specifies manifest structures, trust scoring models, permissioning frameworks, provenance tracking, audit mechanisms, and bounded autonomy controls to ensure advertising signals can be used safely and responsibly by autonomous systems.

## Status of This Document

This document is a draft specification intended to stimulate discussion and collaboration within the advertising technology community. It is not endorsed by any standards body. Implementers should treat this as an experimental proposal subject to change. Feedback is welcomed through the project's GitHub repository.

## Table of Contents

1. [Introduction](#1-introduction)
2. [Problem Statement](#2-problem-statement)
3. [Relationship to Existing Standards](#3-relationship-to-existing-standards)
4. [Goals and Non-Goals](#4-goals-and-non-goals)
5. [Design Principles](#5-design-principles)
6. [Core Entities](#6-core-entities)
7. [Signal Types](#7-signal-types)
8. [OpenSignal Manifest](#8-opensignal-manifest)
9. [Trust Score Model](#9-trust-score-model)
10. [Permissioning Model](#10-permissioning-model)
11. [Provenance Model](#11-provenance-model)
12. [Freshness Model](#12-freshness-model)
13. [Audit Model](#13-audit-model)
14. [Policy Binding Model](#14-policy-binding-model)
15. [Bounded Autonomy Model](#15-bounded-autonomy-model)
16. [Protocol Tasks](#16-protocol-tasks)
17. [Integration Models](#17-integration-models)
18. [Security Considerations](#18-security-considerations)
19. [Privacy Considerations](#19-privacy-considerations)
20. [Compliance and Brand Safety](#20-compliance-and-brand-safety)
21. [Conformance](#21-conformance)
22. [Governance Considerations](#22-governance-considerations)
23. [Future Roadmap](#23-future-roadmap)
24. [References](#24-references)

---

## 1. Introduction

The advertising industry is rapidly adopting AI agents for campaign planning, media buying, optimization and reporting. These agents require access to advertising signals—structured data describing audiences, contexts, inventory, attention metrics, commerce behaviors and other targeting attributes. While protocols exist for signal discovery (e.g., AdCP) and execution (e.g., OpenRTB), no standard exists for declaring and verifying signal trust before activation.

The OpenSignals Protocol addresses this gap by defining:

- A machine-readable **manifest format** for declaring signal properties, provenance, quality and permissions
- A **trust scoring model** across seven dimensions of signal reliability
- A **permissioning framework** for declaring valid use cases and consent scope
- A **provenance model** for tracking data lineage and chain of custody
- An **audit model** for recording signal usage and enabling post-activation review
- A **bounded autonomy model** for controlling when human approval is required
- Seven **core protocol tasks** that agents and platforms implement to verify, score, permission and audit signals

The protocol is designed to complement, not replace, existing advertising infrastructure. It operates as a trust verification layer between signal discovery and signal activation.

### 1.1 Key Words

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

---

## 2. Problem Statement

### 2.1 Why Agentic Advertising Needs Signal Trust

Autonomous advertising agents operate at speeds and scales that make manual signal verification impractical. An agent may discover thousands of signals, evaluate dozens of targeting combinations, and activate campaigns across multiple platforms—all within minutes. Without standardized trust metadata, agents cannot reliably answer:

1. **Validity**: Is this signal valid for my brand, category and market?
2. **Permission**: Is this signal permissioned for this specific use case?
3. **Freshness**: Is this signal recent enough to be reliable?
4. **Explainability**: Can this signal be explained to stakeholders and regulators?
5. **Safety**: Does this signal comply with brand safety and regulatory requirements?
6. **Autonomy**: Can this signal be activated autonomously, or is human approval required?

These questions are critical for regulated categories (alcohol, gambling, pharmaceuticals, financial services), privacy-sensitive applications (GDPR, CCPA, children's advertising), and brand safety contexts (premium publishers, sensitive content adjacency).

### 2.2 Current State and Limitations

Today's advertising ecosystem lacks standardized signal trust metadata:

- **Signal providers** describe signals informally through sales documentation, API docs or ad hoc metadata fields
- **Buyers and agents** assess trust through bilateral agreements, manual vendor reviews, or inconsistent scoring systems
- **Governance checks** are performed manually, using spreadsheets, custom scripts or platform-specific tooling
- **Audit trails** are fragmented across DSPs, DMPs, CDPs and measurement platforms
- **Provenance** is tracked inconsistently, making it difficult to verify data lineage
- **Permissioning** is implicit, with limited machine-readable consent scopes

This creates several problems:

1. **Inefficiency**: Agents cannot automatically assess signal trust, requiring manual reviews that slow activation
2. **Risk**: Signals may be activated without proper governance, creating compliance and brand safety exposure
3. **Opacity**: Stakeholders cannot easily audit which signals were used or why
4. **Fragmentation**: Each platform implements proprietary trust scoring, making cross-platform consistency impossible

### 2.3 What OpenSignals Provides

OpenSignals provides:

- A **standard manifest format** that signal providers publish alongside their signals
- A **trust scoring model** that buyers and agents use to assess signal reliability
- A **permissioning framework** that declares valid use cases and consent boundaries
- A **verification protocol** that governance agents use to approve or reject signals
- An **audit trail** that records signal usage with full context
- A **bounded autonomy model** that ensures appropriate human oversight

The protocol enables agents to make trust-informed decisions automatically while maintaining governance controls.

---

## 3. Relationship to Existing Standards

OpenSignals is designed to complement existing advertising standards and agentic protocols. It does not replace any existing specification.

### 3.1 AdCP (Ad Context Protocol)

**Relationship**: OpenSignals extends AdCP by adding trust verification between signal discovery and activation.

AdCP defines how agents discover and activate signals through `get_signals` and `activate_signal` tasks. OpenSignals adds a trust assessment layer:

```
AdCP: get_signals → [OpenSignals: verify_signal, score_signal] → AdCP: activate_signal
```

An AdCP-compatible signal provider MAY include OpenSignals metadata in `get_signals` responses. A buyer agent SHOULD verify signals using OpenSignals tasks before calling `activate_signal`.

**Specification**: [adcontextprotocol.org](https://adcontextprotocol.org/)
**Repository**: [github.com/adcontextprotocol/adcp](https://github.com/adcontextprotocol/adcp)

### 3.2 AAMP (Agentic Advertising Management Protocols)

**Relationship**: OpenSignals implements the Trust and Transparency pillar of AAMP.

AAMP defines three pillars for agentic advertising:

1. **Foundations (ARTF)**: Runtime framework and agent registry
2. **Protocols**: Extensions to OpenRTB, AdCOM and OpenDirect
3. **Trust and Transparency**: Mechanisms for verifying agent behavior and signal usage

OpenSignals provides a practical implementation layer for signal-level trust verification, complementing AAMP's broader trust framework.

**Specification**: [iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/](https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/)

### 3.3 OpenRTB, OpenDirect and AdCOM

**Relationship**: OpenSignals operates above the execution layer defined by these IAB Tech Lab standards.

OpenRTB and OpenDirect handle real-time bidding and programmatic direct transactions. AdCOM provides common object models. OpenSignals does not modify these protocols. Instead, it provides trust metadata that agents evaluate before submitting bid requests or direct orders.

**Workflow**:
```
OpenSignals: verify_signal → OpenRTB: bid request (with trusted signals)
```

A conforming implementation MAY include OpenSignals trust scores in OpenRTB extensions or deal metadata.

**Specifications**:
- AdCOM: [github.com/InteractiveAdvertisingBureau/AdCOM](https://github.com/InteractiveAdvertisingBureau/AdCOM)
- OpenRTB: [github.com/InteractiveAdvertisingBureau/openrtb2.x](https://github.com/InteractiveAdvertisingBureau/openrtb2.x)

### 3.4 MCP (Model Context Protocol)

**Relationship**: OpenSignals tasks MAY be exposed as MCP tools for agent consumption (conceptual integration).

MCP defines how AI systems integrate with external data sources and tools. OpenSignals tasks could be implemented as MCP tools, allowing agents to query signal trust through a standardized LLM integration protocol.

**Example conceptual mapping**:
```
MCP tool: opensignals_verify_signal
MCP resource: opensignals://manifests/{signal_id}
```

This integration is conceptual and not formally specified in this version.

**Specification**: [modelcontextprotocol.io/specification/2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25)

### 3.5 A2A (Agent2Agent Protocol)

**Relationship**: OpenSignals tasks MAY be exposed as A2A skills for inter-agent communication (conceptual integration).

A2A defines how agents communicate and delegate tasks. OpenSignals verification and scoring could be exposed as A2A skills that buyer agents invoke on governance agents.

**Example conceptual mapping**:
```
A2A skill: verify_signal_trust
A2A task: score_signal_for_brand_objective
```

This integration is conceptual and not formally specified in this version.

**Specification**: [a2a-protocol.org/latest/specification/](https://a2a-protocol.org/latest/specification/)

---

## 4. Goals and Non-Goals

### 4.1 Goals

The OpenSignals Protocol aims to:

1. **Standardize signal trust declaration** through a common manifest format
2. **Enable automated trust verification** by agents before signal activation
3. **Provide explainable trust scoring** across multiple dimensions of signal quality
4. **Support bounded autonomy** by defining when human approval is required
5. **Create portable audit trails** that work across platforms and vendors
6. **Complement existing standards** without requiring protocol modifications
7. **Support regulated categories** (alcohol, gambling, pharma, finance) with enhanced governance
8. **Maintain neutrality** across platforms, vendors and agent implementations

### 4.2 Non-Goals

The OpenSignals Protocol does NOT aim to:

1. **Replace AdCP or OpenRTB**: OpenSignals adds trust verification, not signal discovery or execution
2. **Define signal schemas**: Signal content structure is defined by AdCP, AdCOM or provider-specific formats
3. **Mandate specific trust thresholds**: Trust scoring is descriptive; enforcement is implementation-specific
4. **Certify signal providers**: Certification and accreditation are left to industry governance bodies
5. **Standardize pricing or commercial terms**: Signal costs and contracts are out of scope
6. **Define agent runtime behavior**: Agent decision-making logic is implementation-specific
7. **Create a registry or catalog**: Signal discovery is handled by AdCP and AAMP registries
8. **Replace brand safety tools**: OpenSignals integrates with, rather than replaces, existing brand safety systems

---

## 5. Design Principles

The protocol is designed according to the following principles:

### 5.1 Machine-Readable and Human-Explainable

All trust metadata MUST be machine-readable (JSON, JSON Schema) while remaining human-explainable. Trust scores MUST include reasoning fields that explain scoring decisions.

### 5.2 Composable and Extensible

The protocol MUST integrate with existing standards (AdCP, AAMP, OpenRTB) without requiring breaking changes. Manifest schemas MUST support extensibility through custom fields.

### 5.3 Progressive Disclosure

Simple use cases SHOULD require minimal metadata. Advanced use cases (regulated categories, complex governance) MAY require additional fields. Core fields are REQUIRED; extensions are OPTIONAL.

### 5.4 Trust but Verify

The protocol assumes signal providers act in good faith but provides verification mechanisms for governance agents to validate claims. Provenance chains MUST be verifiable through cryptographic signatures where appropriate.

### 5.5 Privacy by Design

Trust verification MUST NOT require sharing individual-level data. Aggregate quality metrics SHOULD be sufficient for most trust assessments. Permissioning models MUST support privacy-preserving use cases.

### 5.6 Bounded Autonomy

The protocol MUST support multiple autonomy levels, from full human control to fully autonomous activation. Decision modes MUST be explicit and auditable.

### 5.7 Fail-Safe Defaults

When trust cannot be verified, the protocol SHOULD default to requiring human approval. Unsafe or invalid signals MUST be blocked unless explicitly overridden by authorized personnel.

---

## 6. Core Entities

The OpenSignals Protocol defines six core entity types:

### 6.1 Signal Provider

An organization that creates, maintains and publishes advertising signals. Signal providers:

- MUST publish OpenSignal Manifests for each signal
- MUST maintain signal freshness and quality metrics
- MUST declare provenance, permissioning and usage constraints
- SHOULD implement verification endpoints for trust validation
- MAY provide outcome feedback mechanisms

**Examples**: Data providers, publishers, SSPs, measurement vendors, research firms.

### 6.2 Buyer Agent

An autonomous or semi-autonomous AI agent acting on behalf of an advertiser or agency. Buyer agents:

- MUST verify signals before activation
- SHOULD score signals against brand objectives
- MUST respect bounded autonomy constraints
- MUST log audit trails for signal usage
- MAY submit outcome feedback after campaigns complete

**Examples**: Campaign planning agents, media buying agents, optimization agents.

### 6.3 Governance Agent

An agent or system responsible for enforcing brand policy, compliance rules and approval workflows. Governance agents:

- MUST evaluate signals against brand policy
- MUST enforce regulatory and category restrictions
- SHOULD provide decision reasoning for auditability
- MAY delegate verification to specialized compliance tools
- MUST support human-in-the-loop approval for regulated categories

**Examples**: Brand safety platforms, compliance engines, approval workflow systems.

### 6.4 Audit Agent

An agent or system that records, analyzes and reports signal usage for accountability. Audit agents:

- MUST log signal activation events with full context
- SHOULD provide queryable audit trails
- MAY generate compliance reports for regulators
- SHOULD support outcome feedback integration

**Examples**: Audit trail platforms, compliance reporting tools, governance dashboards.

### 6.5 Execution Platform

A platform that executes media buying decisions made by agents. Execution platforms:

- MAY enforce signal trust thresholds before activation
- SHOULD integrate OpenSignals metadata into bid requests or insertion orders
- MAY provide outcome feedback to signal providers
- SHOULD support audit trail logging

**Examples**: DSPs, SSPs, ad servers, direct buying platforms.

### 6.6 Brand Policy Owner

The human stakeholder (advertiser, agency) who defines brand policy, approval requirements and trust thresholds. Brand policy owners:

- MUST define category restrictions and market-specific rules
- SHOULD specify bounded autonomy levels for different signal types
- MAY delegate policy enforcement to governance agents
- MUST review audit trails for regulated campaigns

---

## 7. Signal Types

OpenSignals defines 12 standard signal types. Signal providers MUST classify signals using one of these types or declare a custom type.

| Signal Type | Description | Common Use Cases |
|-------------|-------------|------------------|
| `audience` | Describes user attributes, behaviors or segments | Demographic targeting, interest-based targeting, lookalike modeling |
| `contextual` | Describes content, page or environment attributes | Contextual targeting, brand safety, adjacency controls |
| `geographic` | Describes location, region or geo-behavioral patterns | Local advertising, geo-fencing, regional campaigns |
| `temporal` | Describes time-based patterns or seasonality | Dayparting, event-based marketing, seasonal campaigns |
| `commerce` | Describes purchase behavior, intent or transaction data | Retargeting, conversion optimization, commerce media |
| `attention` | Describes viewability, engagement or attention metrics | Attention-based buying, viewability optimization |
| `creative` | Describes creative performance or A/B test results | Creative optimization, dynamic creative, format selection |
| `environmental` | Describes sustainability, carbon impact or ethical sourcing | Sustainable advertising, ESG reporting, brand values alignment |
| `compliance` | Describes regulatory adherence or certification status | Age verification, consent management, category restrictions |
| `outcome` | Describes performance, conversion or lift measurement | Attribution, incrementality testing, performance forecasting |
| `brand_safety` | Describes content classification or risk assessment | Brand safety targeting, exclusion lists, sensitive content avoidance |
| `custom` | Provider-defined signal type | Novel signal types not covered by standard taxonomy |

Signal providers using `custom` MUST provide detailed documentation in the manifest's `description` field.

---

## 8. OpenSignal Manifest

The OpenSignal Manifest is a JSON document that declares signal properties, trust metadata, provenance, permissioning and quality metrics. Each signal MUST have a corresponding manifest.

### 8.1 Manifest Structure

The manifest consists of the following sections:

1. **Metadata**: Protocol version, signal identity, naming and status
2. **Ownership**: Signal owner and provider contact information
3. **Classification**: Signal type, category and taxonomy
4. **Provenance**: Data sources, collection methods and lineage
5. **Quality**: Trust scores, coverage, precision and freshness
6. **Permissioning**: Valid use cases, consent scope and restrictions
7. **Audit**: Audit requirements, logging endpoints and retention policies
8. **Governance**: Bounded autonomy mode and approval requirements
9. **Integration**: Discovery URLs, activation endpoints and documentation

### 8.2 Core Manifest Fields

#### 8.2.1 Required Fields

The following fields MUST be present in every manifest:

| Field | Type | Description |
|-------|------|-------------|
| `protocol` | string | MUST be `"opensignals"` |
| `version` | string | Protocol version (MUST be `"0.1"` for this specification) |
| `signal_id` | string | Globally unique signal identifier (kebab-case recommended) |
| `name` | string | Human-readable signal name |
| `signal_type` | string | Signal classification (from Section 7 taxonomy) |
| `status` | string | Signal status: `active`, `deprecated`, `suspended`, `beta` |
| `owner` | object | Organization and contact information (see 8.2.2) |
| `provider` | object | Signal provider details (see 8.2.3) |
| `provenance` | object | Data lineage and collection methods (see Section 11) |
| `quality` | object | Trust scores and quality metrics (see Section 9) |
| `permissioning` | object | Valid use cases and consent scope (see Section 10) |
| `governance` | object | Bounded autonomy and approval requirements (see Section 15) |

#### 8.2.2 Owner Object

```json
{
  "owner": {
    "organization": "string (REQUIRED)",
    "contact": "string (REQUIRED, email or URL)",
    "country": "string (OPTIONAL, ISO 3166-1 alpha-2)",
    "registration": "string (OPTIONAL, business registration number)"
  }
}
```

#### 8.2.3 Provider Object

```json
{
  "provider": {
    "name": "string (REQUIRED)",
    "url": "string (REQUIRED, HTTPS URL)",
    "support_contact": "string (OPTIONAL)",
    "documentation_url": "string (OPTIONAL)"
  }
}
```

### 8.3 Example Minimal Manifest

```json
{
  "protocol": "opensignals",
  "version": "0.1",
  "signal_id": "outdoor-enthusiasts",
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
    "data_sources": ["first_party_behavioral"],
    "collection_method": "opt_in_panel",
    "last_updated": "2026-05-10T08:00:00Z"
  },
  "quality": {
    "overall_trust_score": 0.87,
    "provenance_score": 0.90,
    "permissioning_score": 0.85,
    "freshness_score": 0.91,
    "quality_score": 0.84,
    "explainability_score": 0.88,
    "outcome_score": 0.82,
    "compliance_score": 0.89
  },
  "permissioning": {
    "valid_use_cases": ["targeting", "measurement"],
    "consent_scope": "opt_in",
    "geographic_restrictions": [],
    "category_restrictions": []
  },
  "governance": {
    "decision_mode": "approve_with_human",
    "audit_required": true,
    "human_approval_required_for_categories": ["alcohol", "gambling", "pharma"]
  }
}
```

### 8.4 Manifest Discovery

Signal providers SHOULD publish manifests at well-known URLs:

```
https://{provider-domain}/.well-known/opensignals/{signal_id}
```

Agents MAY discover manifests through:
- AdCP signal responses (extended with OpenSignals metadata)
- Direct HTTP requests to well-known URLs
- MCP resources (if MCP integration is implemented)
- Provider-specific APIs or catalogs

### 8.5 Manifest Versioning

Manifests MUST include a `last_updated` timestamp. Providers SHOULD publish updated manifests when signal properties change. Agents SHOULD cache manifests for up to 24 hours unless `freshness_ttl` specifies otherwise.

---

## 9. Trust Score Model

The OpenSignals trust score model evaluates signals across seven dimensions. Each dimension contributes to an overall trust score on a 0.00 to 1.00 scale.

### 9.1 Trust Dimensions

#### 9.1.1 Provenance Score (20% weight)

Measures data source transparency and chain of custody.

**Scoring factors**:
- **Data source transparency** (0.0–0.3): Are data sources clearly declared?
- **Collection method clarity** (0.0–0.3): Is the collection methodology documented?
- **Chain of custody** (0.0–0.4): Can data lineage be traced from source to signal?

**Example scoring**:
- First-party data with documented collection: 0.85–1.00
- Third-party data with verified sources: 0.70–0.85
- Third-party data with undocumented sources: 0.30–0.50
- Data with unknown provenance: 0.00–0.30

#### 9.1.2 Permissioning Score (20% weight)

Measures consent transparency and usage rights clarity.

**Scoring factors**:
- **Consent scope** (0.0–0.5): Is consent explicitly granted for advertising use?
- **Usage restrictions** (0.0–0.3): Are usage constraints clearly documented?
- **Right to revoke** (0.0–0.2): Can users revoke consent?

**Example scoring**:
- Explicit opt-in with clear usage terms: 0.90–1.00
- Implicit consent with documented policies: 0.70–0.85
- Unclear or ambiguous consent: 0.30–0.50
- No documented consent: 0.00–0.30

#### 9.1.3 Freshness Score (15% weight)

Measures signal recency and update frequency.

**Scoring factors**:
- **Time since last update** (0.0–0.6): How recently was the signal refreshed?
- **Update frequency** (0.0–0.4): How often is the signal updated?

**Example scoring**:
- Updated within last 24 hours: 0.90–1.00
- Updated within last 7 days: 0.70–0.90
- Updated within last 30 days: 0.50–0.70
- Updated more than 30 days ago: 0.00–0.50

Time decay MAY be adjusted based on signal type (e.g., contextual signals decay faster than demographic signals).

#### 9.1.4 Quality Score (20% weight)

Measures signal coverage, precision and stability.

**Scoring factors**:
- **Coverage** (0.0–0.4): Does the signal reach the intended audience?
- **Precision** (0.0–0.4): Does the signal accurately represent declared attributes?
- **Stability** (0.0–0.2): Is signal composition consistent over time?

**Example scoring**:
- High coverage, validated precision, stable: 0.85–1.00
- Moderate coverage, estimated precision: 0.60–0.75
- Low coverage or unvalidated precision: 0.30–0.50
- Unknown or poor quality: 0.00–0.30

#### 9.1.5 Explainability Score (10% weight)

Measures how well the signal can be explained to stakeholders and regulators.

**Scoring factors**:
- **Documentation quality** (0.0–0.4): Is signal construction clearly documented?
- **Transparency** (0.0–0.3): Can signal composition be inspected?
- **Interpretability** (0.0–0.3): Can non-technical stakeholders understand the signal?

**Example scoring**:
- Full documentation with examples: 0.85–1.00
- Basic documentation available: 0.60–0.75
- Limited or technical-only documentation: 0.30–0.50
- No documentation: 0.00–0.30

#### 9.1.6 Outcome Relevance Score (10% weight)

Measures historical performance against similar brand objectives.

**Scoring factors**:
- **Past performance** (0.0–0.5): Has this signal driven outcomes in similar campaigns?
- **Validation** (0.0–0.3): Is performance measured by third-party verification?
- **Recency of outcomes** (0.0–0.2): How recent are performance measurements?

**Example scoring**:
- Validated performance in similar categories: 0.85–1.00
- Self-reported performance: 0.60–0.75
- Untested or theoretical: 0.30–0.50
- No outcome data: 0.00–0.30

Buyer agents MAY adjust outcome scores based on brand-specific performance data.

#### 9.1.7 Compliance Safety Score (5% weight)

Measures adherence to regulations and brand safety standards.

**Scoring factors**:
- **Regulatory compliance** (0.0–0.3): Does signal comply with GDPR, CCPA, category regulations?
- **Brand safety certification** (0.0–0.4): Is signal certified by brand safety vendors?
- **Risk assessment** (0.0–0.3): Has signal been assessed for content adjacency risks?

**Example scoring**:
- Certified compliant with no violations: 0.90–1.00
- Self-certified with documented policies: 0.70–0.85
- Unclear compliance status: 0.30–0.50
- Known compliance issues: 0.00–0.30

### 9.2 Overall Trust Score Calculation

The overall trust score is a weighted sum:

```
overall_trust_score =
  (provenance_score × 0.20) +
  (permissioning_score × 0.20) +
  (freshness_score × 0.15) +
  (quality_score × 0.20) +
  (explainability_score × 0.10) +
  (outcome_score × 0.10) +
  (compliance_score × 0.05)
```

Implementations MAY adjust weights based on brand priorities (e.g., regulated categories MAY increase compliance weight).

### 9.3 Score Bands and Decision Guidance

Overall trust scores map to five bands:

| Score Range | Band | Description | Decision Guidance |
|-------------|------|-------------|-------------------|
| 0.90–1.00 | Highly Trusted | Excellent quality, provenance and compliance | MAY activate autonomously (if policy allows) |
| 0.75–0.89 | Trusted | Good quality with minor gaps | SHOULD activate with governance checks |
| 0.50–0.74 | Limited Trust | Moderate quality or incomplete metadata | MUST require human review before activation |
| 0.25–0.49 | Low Trust | Poor quality or significant gaps | SHOULD NOT activate without explicit approval |
| 0.00–0.24 | Unsafe/Invalid | Unverified, non-compliant or invalid | MUST NOT activate |

These bands provide guidance; enforcement is implementation-specific.

### 9.4 Score Transparency

Trust scores MUST include reasoning:

```json
{
  "quality": {
    "overall_trust_score": 0.87,
    "provenance_score": 0.90,
    "provenance_reasoning": "First-party data with documented collection methodology",
    "permissioning_score": 0.85,
    "permissioning_reasoning": "Explicit opt-in consent with clear usage terms",
    "freshness_score": 0.91,
    "freshness_reasoning": "Updated within last 12 hours",
    "quality_score": 0.84,
    "quality_reasoning": "High coverage (82%) with validated precision",
    "explainability_score": 0.88,
    "explainability_reasoning": "Full documentation with use case examples",
    "outcome_score": 0.82,
    "outcome_reasoning": "Validated performance in similar CPG campaigns",
    "compliance_score": 0.89,
    "compliance_reasoning": "GDPR compliant with brand safety certification"
  }
}
```

---

## 10. Permissioning Model

The permissioning model declares valid use cases, consent scope and usage restrictions for each signal.

### 10.1 Permissioning Object Structure

```json
{
  "permissioning": {
    "valid_use_cases": ["string"],
    "consent_scope": "string",
    "consent_mechanism": "string (OPTIONAL)",
    "geographic_restrictions": ["string"],
    "category_restrictions": ["string"],
    "individual_profiling_allowed": "boolean",
    "sensitive_categories_allowed": "boolean",
    "data_retention_days": "integer (OPTIONAL)",
    "revocation_url": "string (OPTIONAL)"
  }
}
```

### 10.2 Valid Use Cases

Signal providers MUST declare which use cases are permitted:

| Use Case | Description |
|----------|-------------|
| `targeting` | Signal can be used for audience or contextual targeting |
| `frequency_capping` | Signal can be used for frequency management |
| `attribution` | Signal can be used for conversion attribution |
| `measurement` | Signal can be used for campaign measurement and reporting |
| `optimization` | Signal can be used for dynamic optimization (bidding, creative, placement) |
| `research` | Signal can be used for market research and insights (aggregate only) |
| `forecasting` | Signal can be used for reach and frequency forecasting |

Buyer agents MUST NOT use signals for use cases not declared as valid.

### 10.3 Consent Scope

| Consent Scope | Description |
|---------------|-------------|
| `explicit_opt_in` | Users explicitly consented to advertising use |
| `opt_in` | Users opted in through account creation or preference center |
| `legitimate_interest` | Usage based on legitimate interest (GDPR Article 6(1)(f)) |
| `contractual` | Usage based on contract performance |
| `consent_not_required` | Data does not require consent (e.g., fully anonymized contextual) |

### 10.4 Geographic and Category Restrictions

Signal providers MUST declare geographic and category restrictions:

```json
{
  "permissioning": {
    "geographic_restrictions": ["CN", "RU"],
    "category_restrictions": ["alcohol", "gambling", "political"]
  }
}
```

Buyer agents MUST NOT activate signals in restricted geographies or categories.

### 10.5 Individual Profiling and Sensitive Categories

```json
{
  "permissioning": {
    "individual_profiling_allowed": false,
    "sensitive_categories_allowed": false
  }
}
```

If `individual_profiling_allowed` is `false`, agents MUST use signal for aggregate or contextual targeting only.

If `sensitive_categories_allowed` is `false`, signal MUST NOT be used for sensitive categories (health, religion, politics, sexual orientation per GDPR Article 9).

---

## 11. Provenance Model

The provenance model tracks data lineage, collection methods and chain of custody.

### 11.1 Provenance Object Structure

```json
{
  "provenance": {
    "data_sources": ["string"],
    "collection_method": "string",
    "collection_date_range": {
      "start": "ISO 8601 date",
      "end": "ISO 8601 date (OPTIONAL)"
    },
    "last_updated": "ISO 8601 timestamp",
    "update_frequency": "string",
    "chain_of_custody": [
      {
        "entity": "string",
        "role": "string",
        "timestamp": "ISO 8601 timestamp"
      }
    ],
    "verification_method": "string (OPTIONAL)",
    "verification_url": "string (OPTIONAL)"
  }
}
```

### 11.2 Data Sources

Signal providers MUST declare data sources using standard taxonomy:

| Data Source | Description |
|-------------|-------------|
| `first_party_transactional` | Direct transaction data (purchases, subscriptions) |
| `first_party_behavioral` | Direct behavioral data (site visits, app usage) |
| `first_party_declared` | User-provided profile data |
| `second_party` | Data shared directly from partner first-party data |
| `third_party_aggregated` | Aggregated third-party data from multiple sources |
| `third_party_modeled` | Modeled or inferred data from third-party providers |
| `survey` | Survey or panel-based research |
| `public_data` | Publicly available data (census, government, open data) |
| `contextual_analysis` | Real-time content analysis (NLP, image recognition) |
| `measurement` | Measurement data (attention, viewability, brand lift) |

Providers using multiple sources SHOULD list all sources.

### 11.3 Collection Method

Signal providers MUST declare collection method:

| Collection Method | Description |
|-------------------|-------------|
| `opt_in_panel` | Users explicitly joined a research panel |
| `account_registration` | Data collected during account registration |
| `survey` | Data collected through surveys |
| `transactional` | Data collected through purchases or transactions |
| `behavioral_tracking` | Data collected through site/app tracking (with consent) |
| `contextual_crawl` | Data collected through content crawling and analysis |
| `inference` | Data inferred or modeled from other signals |
| `public_aggregation` | Data aggregated from public sources |

### 11.4 Chain of Custody

For signals involving multiple entities, providers SHOULD document chain of custody:

```json
{
  "provenance": {
    "chain_of_custody": [
      {
        "entity": "Original Data Collector Inc",
        "role": "data_collector",
        "timestamp": "2026-01-15T10:00:00Z"
      },
      {
        "entity": "Data Processor Ltd",
        "role": "data_processor",
        "timestamp": "2026-01-16T14:00:00Z"
      },
      {
        "entity": "Signal Provider Co",
        "role": "signal_publisher",
        "timestamp": "2026-01-17T08:00:00Z"
      }
    ]
  }
}
```

### 11.5 Verification

Providers MAY include cryptographic verification:

```json
{
  "provenance": {
    "verification_method": "http_message_signature",
    "verification_url": "https://example.com/.well-known/opensignals/verify"
  }
}
```

Governance agents MAY verify provenance by calling verification endpoints.

---

## 12. Freshness Model

The freshness model tracks signal recency and update frequency.

### 12.1 Freshness Fields

```json
{
  "provenance": {
    "last_updated": "2026-05-10T08:00:00Z",
    "update_frequency": "daily",
    "next_update_expected": "2026-05-11T08:00:00Z"
  },
  "quality": {
    "freshness_score": 0.91,
    "freshness_ttl": 86400
  }
}
```

### 12.2 Update Frequency

| Frequency | Description |
|-----------|-------------|
| `real_time` | Signal updates continuously or near-real-time |
| `hourly` | Signal updates every hour |
| `daily` | Signal updates once per day |
| `weekly` | Signal updates once per week |
| `monthly` | Signal updates once per month |
| `quarterly` | Signal updates once per quarter |
| `on_demand` | Signal updates when requested by activation |

### 12.3 Freshness TTL

`freshness_ttl` (in seconds) indicates how long agents SHOULD cache the signal before re-verification:

- `3600`: Re-verify every hour
- `86400`: Re-verify every day
- `604800`: Re-verify every week

Agents SHOULD NOT use signals beyond their `freshness_ttl` without re-fetching the manifest.

---

## 13. Audit Model

The audit model defines how signal usage is logged and made available for accountability.

### 13.1 Audit Requirements

```json
{
  "governance": {
    "audit_required": true,
    "audit_retention_days": 90,
    "audit_endpoint": "https://audit.example.com/opensignals/log"
  }
}
```

### 13.2 Audit Event Structure

When a signal is activated, audit agents MUST log an event:

```json
{
  "event_type": "signal_activated",
  "timestamp": "2026-05-10T10:30:00Z",
  "signal_id": "outdoor-enthusiasts",
  "signal_manifest_version": "2026-05-10T08:00:00Z",
  "brand": "premium-spirits-co",
  "campaign_id": "spring-campaign-2026",
  "buyer_agent": "media-optimizer-agent-v2",
  "governance_agent": "brand-policy-engine",
  "decision_mode": "approve_with_human",
  "human_approver": "jane.smith@brand.com",
  "trust_score": 0.87,
  "use_case": "contextual_targeting",
  "platform": "dsp-platform-x",
  "geographic_scope": ["GB", "IE"],
  "category": "alcohol",
  "policy_bindings": [
    "alcohol_age_restriction",
    "uk_advertising_standards"
  ],
  "reasoning": "Signal approved for contextual targeting after human review. Individual profiling disabled per alcohol policy."
}
```

### 13.3 Audit Query and Export

Platforms SHOULD provide audit query APIs:

```
GET /opensignals/audit?brand=premium-spirits-co&start=2026-05-01&end=2026-05-31
```

Audit trails SHOULD be exportable in JSON or CSV formats for regulatory reporting.

---

## 14. Policy Binding Model

Policy binding attaches brand-specific rules to signals before activation.

### 14.1 Policy Binding Object

```json
{
  "policy_binding": {
    "brand": "premium-spirits-co",
    "policy_version": "2026-q1",
    "bindings": [
      {
        "policy_id": "alcohol_age_restriction",
        "policy_name": "UK Alcohol Age Targeting",
        "enforcement": "mandatory",
        "parameters": {
          "minimum_age": 25,
          "age_verification_required": true
        }
      },
      {
        "policy_id": "no_individual_profiling",
        "policy_name": "No Individual Profiling for Alcohol",
        "enforcement": "mandatory",
        "parameters": {
          "profiling_allowed": false,
          "aggregate_only": true
        }
      }
    ],
    "bound_at": "2026-05-10T10:00:00Z",
    "bound_by": "governance-agent-v1"
  }
}
```

### 14.2 Enforcement Levels

| Enforcement | Description |
|-------------|-------------|
| `mandatory` | Policy MUST be enforced; violation blocks activation |
| `recommended` | Policy SHOULD be enforced; violation triggers warning |
| `advisory` | Policy provides guidance; no enforcement |

### 14.3 Policy Binding in Workflows

Policy binding occurs during `bind_signal_policy` task:

```
1. Buyer agent requests signal verification
2. Governance agent evaluates signal against brand policy
3. Governance agent binds relevant policies to signal
4. Bound signal is returned to buyer agent with policy metadata
5. Buyer agent includes policy bindings in activation request
6. Execution platform enforces bound policies
```

---

## 15. Bounded Autonomy Model

The bounded autonomy model defines when human approval is required.

### 15.1 Decision Modes

OpenSignals defines five decision modes:

| Decision Mode | Description | Human Involvement |
|---------------|-------------|-------------------|
| `observe` | Agent observes but does not act | Human makes all decisions |
| `recommend` | Agent recommends actions | Human reviews and approves before action |
| `approve_with_human` | Agent proposes actions requiring approval | Human must approve each action |
| `autonomous_with_limits` | Agent acts autonomously within trust thresholds | Human sets thresholds and reviews audit trails |
| `autonomous_full` | Agent acts fully autonomously | Human reviews audit trails post-activation |

### 15.2 Governance Object

```json
{
  "governance": {
    "decision_mode": "approve_with_human",
    "autonomous_trust_threshold": 0.90,
    "human_approval_required_for_categories": ["alcohol", "gambling", "pharma", "finance"],
    "human_approval_required_for_trust_below": 0.75,
    "approval_workflow_url": "https://governance.brand.com/approve"
  }
}
```

### 15.3 Decision Mode Logic

```
IF signal.category IN human_approval_required_for_categories:
  decision_mode = approve_with_human

ELSE IF signal.overall_trust_score < human_approval_required_for_trust_below:
  decision_mode = approve_with_human

ELSE IF signal.overall_trust_score >= autonomous_trust_threshold:
  decision_mode = autonomous_with_limits

ELSE:
  decision_mode = recommend
```

### 15.4 Approval Workflow

For signals requiring human approval:

1. Buyer agent calls `verify_signal`
2. Governance agent returns `approval_required: true`
3. Governance agent notifies human approver
4. Human reviews signal manifest, trust score and reasoning
5. Human approves or rejects via approval workflow UI
6. Governance agent returns decision to buyer agent
7. If approved, buyer agent proceeds to activation

Approval workflows SHOULD complete within a reasonable timeframe (e.g., 1 business day for non-urgent, 1 hour for time-sensitive campaigns).

---

## 16. Protocol Tasks

OpenSignals defines seven core protocol tasks. Signal providers, buyer agents, governance agents and audit agents implement these tasks through RESTful APIs, MCP tools, A2A skills or other transport mechanisms.

### 16.1 Task: get_signal_manifest

**Purpose**: Retrieve the full OpenSignals manifest for a signal.

**Implemented by**: Signal providers

**Request**:
```json
{
  "task": "get_signal_manifest",
  "signal_id": "outdoor-enthusiasts"
}
```

**Response**:
```json
{
  "task": "get_signal_manifest",
  "signal_id": "outdoor-enthusiasts",
  "manifest": {
    "protocol": "opensignals",
    "version": "0.1",
    "signal_id": "outdoor-enthusiasts",
    "name": "Outdoor Recreation Enthusiasts",
    "signal_type": "audience",
    "status": "active",
    "owner": { ... },
    "provider": { ... },
    "provenance": { ... },
    "quality": { ... },
    "permissioning": { ... },
    "governance": { ... }
  }
}
```

**HTTP Implementation** (RECOMMENDED):
```
GET https://signals.example.com/.well-known/opensignals/outdoor-enthusiasts
Accept: application/json
```

---

### 16.2 Task: verify_signal

**Purpose**: Check if a signal is valid and permissioned for a specific use case.

**Implemented by**: Governance agents

**Request**:
```json
{
  "task": "verify_signal",
  "signal_id": "outdoor-enthusiasts",
  "manifest_url": "https://signals.example.com/.well-known/opensignals/outdoor-enthusiasts",
  "context": {
    "brand": "premium-spirits-co",
    "campaign_id": "spring-campaign-2026",
    "market": "GB",
    "category": "alcohol",
    "intended_use": "contextual_targeting",
    "buyer_agent": "media-optimizer-v2"
  }
}
```

**Response**:
```json
{
  "task": "verify_signal",
  "signal_id": "outdoor-enthusiasts",
  "decision": "approved_with_conditions",
  "approval_required": true,
  "approval_status": "pending",
  "approval_request_id": "apr_987xyz",
  "conditions": [
    "human_approval_required",
    "audit_required",
    "no_individual_profiling"
  ],
  "trust_score": 0.87,
  "trust_band": "trusted",
  "policy_bindings": [
    {
      "policy_id": "alcohol_age_restriction",
      "enforcement": "mandatory"
    }
  ],
  "decision_reasoning": "Signal approved for contextual targeting after human review. Individual-level profiling prohibited for alcohol category.",
  "valid_until": "2026-05-11T08:00:00Z"
}
```

**Decision Values**:
- `approved`: Signal is approved for immediate activation
- `approved_with_conditions`: Signal approved with attached conditions (e.g., audit required)
- `rejected`: Signal is rejected for this use case
- `approval_pending`: Signal requires human approval (use `approval_request_id` to poll status)

---

### 16.3 Task: score_signal

**Purpose**: Score a signal against a specific brand objective.

**Implemented by**: Governance agents or buyer agents

**Request**:
```json
{
  "task": "score_signal",
  "signal_id": "outdoor-enthusiasts",
  "manifest_url": "https://signals.example.com/.well-known/opensignals/outdoor-enthusiasts",
  "objective": {
    "brand": "premium-spirits-co",
    "campaign_goal": "awareness",
    "target_audience": "affluent_outdoor_enthusiasts",
    "kpis": ["reach", "brand_lift"],
    "category": "alcohol",
    "market": "GB"
  }
}
```

**Response**:
```json
{
  "task": "score_signal",
  "signal_id": "outdoor-enthusiasts",
  "objective_alignment_score": 0.89,
  "reasoning": "Signal strongly aligns with target audience. High coverage and proven brand lift in similar alcohol campaigns in GB market.",
  "trust_score": 0.87,
  "expected_performance": {
    "reach_estimate": 2400000,
    "confidence_level": "high",
    "historical_lift": 0.12
  },
  "recommendation": "strong_fit",
  "risks": [
    "Requires human approval for alcohol category"
  ]
}
```

**Recommendation Values**:
- `strong_fit`: Signal is highly recommended for this objective
- `good_fit`: Signal is recommended
- `moderate_fit`: Signal is acceptable but not optimal
- `weak_fit`: Signal is not recommended
- `not_suitable`: Signal should not be used

---

### 16.4 Task: bind_signal_policy

**Purpose**: Attach brand policy rules to a signal before activation.

**Implemented by**: Governance agents

**Request**:
```json
{
  "task": "bind_signal_policy",
  "signal_id": "outdoor-enthusiasts",
  "brand": "premium-spirits-co",
  "policy_version": "2026-q1",
  "campaign_id": "spring-campaign-2026",
  "category": "alcohol",
  "market": "GB",
  "intended_use": "contextual_targeting"
}
```

**Response**:
```json
{
  "task": "bind_signal_policy",
  "signal_id": "outdoor-enthusiasts",
  "policy_binding": {
    "brand": "premium-spirits-co",
    "policy_version": "2026-q1",
    "bindings": [
      {
        "policy_id": "alcohol_age_restriction",
        "policy_name": "UK Alcohol Age Targeting",
        "enforcement": "mandatory",
        "parameters": {
          "minimum_age": 25,
          "age_verification_required": true
        }
      },
      {
        "policy_id": "no_individual_profiling",
        "policy_name": "No Individual Profiling for Alcohol",
        "enforcement": "mandatory",
        "parameters": {
          "profiling_allowed": false,
          "aggregate_only": true
        }
      }
    ],
    "bound_at": "2026-05-10T10:00:00Z",
    "bound_by": "governance-agent-v1",
    "binding_id": "bind_456def"
  }
}
```

Policy bindings SHOULD be included in subsequent activation requests to ensure execution platforms enforce rules.

---

### 16.5 Task: audit_signal_usage

**Purpose**: Record how a signal was used after activation.

**Implemented by**: Audit agents or execution platforms

**Request**:
```json
{
  "task": "audit_signal_usage",
  "signal_id": "outdoor-enthusiasts",
  "event": {
    "event_type": "signal_activated",
    "timestamp": "2026-05-10T10:30:00Z",
    "brand": "premium-spirits-co",
    "campaign_id": "spring-campaign-2026",
    "buyer_agent": "media-optimizer-v2",
    "governance_agent": "brand-policy-engine",
    "decision_mode": "approve_with_human",
    "human_approver": "jane.smith@brand.com",
    "trust_score": 0.87,
    "use_case": "contextual_targeting",
    "platform": "dsp-platform-x",
    "geographic_scope": ["GB", "IE"],
    "category": "alcohol",
    "policy_bindings": ["alcohol_age_restriction", "no_individual_profiling"],
    "activation_details": {
      "impressions_planned": 5000000,
      "budget_allocated": 50000,
      "start_date": "2026-05-15",
      "end_date": "2026-05-31"
    }
  }
}
```

**Response**:
```json
{
  "task": "audit_signal_usage",
  "signal_id": "outdoor-enthusiasts",
  "audit_id": "aud_789ghi",
  "status": "logged",
  "timestamp": "2026-05-10T10:30:15Z",
  "retention_until": "2026-08-08T10:30:15Z"
}
```

Audit logs MUST be retained for the duration specified in `audit_retention_days` (default: 90 days).

---

### 16.6 Task: revoke_signal

**Purpose**: Withdraw trust from a signal (e.g., due to quality degradation, compliance violation).

**Implemented by**: Signal providers or governance agents

**Request**:
```json
{
  "task": "revoke_signal",
  "signal_id": "outdoor-enthusiasts",
  "revocation_reason": "quality_degradation",
  "revocation_details": "Coverage dropped below acceptable threshold due to data source loss.",
  "revoked_by": "data-quality-monitor",
  "revoked_at": "2026-05-10T12:00:00Z",
  "effective_immediately": true
}
```

**Response**:
```json
{
  "task": "revoke_signal",
  "signal_id": "outdoor-enthusiasts",
  "status": "revoked",
  "revocation_id": "rev_321jkl",
  "revoked_at": "2026-05-10T12:00:00Z",
  "notification_sent_to": [
    "active_buyers",
    "governance_agents"
  ]
}
```

**Revocation Reasons**:
- `quality_degradation`: Signal quality fell below acceptable standards
- `compliance_violation`: Signal violated regulatory or policy requirements
- `permission_revoked`: User consent was withdrawn
- `provider_request`: Provider voluntarily withdrew signal
- `security_incident`: Security breach or data compromise

When a signal is revoked:
1. Signal status MUST change to `suspended` or `deprecated`
2. Active campaigns using the signal SHOULD be notified
3. Future activations MUST be blocked until signal is reinstated

---

### 16.7 Task: submit_signal_outcome_feedback

**Purpose**: Feed campaign results back into signal trust scoring.

**Implemented by**: Buyer agents or measurement platforms

**Request**:
```json
{
  "task": "submit_signal_outcome_feedback",
  "signal_id": "outdoor-enthusiasts",
  "campaign_id": "spring-campaign-2026",
  "brand": "premium-spirits-co",
  "outcome_period": {
    "start": "2026-05-15",
    "end": "2026-05-31"
  },
  "performance": {
    "impressions_delivered": 4800000,
    "reach": 2300000,
    "brand_lift": 0.14,
    "click_through_rate": 0.008,
    "conversion_rate": 0.003,
    "cost_per_outcome": 4.20
  },
  "quality_assessment": {
    "signal_accuracy": "high",
    "signal_stability": "stable",
    "issues_encountered": []
  },
  "recommendation": "continue_using"
}
```

**Response**:
```json
{
  "task": "submit_signal_outcome_feedback",
  "signal_id": "outdoor-enthusiasts",
  "feedback_id": "fb_654mno",
  "status": "received",
  "timestamp": "2026-06-01T09:00:00Z",
  "outcome_score_updated": true,
  "new_outcome_score": 0.85
}
```

Signal providers SHOULD incorporate outcome feedback into `outcome_score` calculations. Governance agents MAY adjust trust thresholds based on aggregated outcome data.

---

## 17. Integration Models

This section describes conceptual integration approaches for OpenSignals with existing protocols. These are design possibilities, not formal specifications.

### 17.1 AdCP Integration (Conceptual)

OpenSignals can extend AdCP responses with trust metadata:

**AdCP `get_signals` Response with OpenSignals Extension**:
```json
{
  "task": "get_signals",
  "signals": [
    {
      "signal_id": "outdoor-enthusiasts",
      "name": "Outdoor Recreation Enthusiasts",
      "coverage": 2400000,
      "cpm": 3.50,
      "open_signals": {
        "manifest_url": "https://signals.example.com/.well-known/opensignals/outdoor-enthusiasts",
        "overall_trust_score": 0.87,
        "trust_band": "trusted",
        "verification_required": true,
        "audit_required": true,
        "decision_mode": "approve_with_human",
        "last_verified": "2026-05-10T08:00:00Z"
      }
    }
  ]
}
```

**Workflow**:
```
1. Buyer agent calls AdCP get_signals
2. SSP/provider returns signals with opensignals extension
3. Buyer agent calls OpenSignals verify_signal for each signal
4. Buyer agent calls AdCP activate_signal for approved signals
5. Buyer agent calls OpenSignals audit_signal_usage after activation
```

This integration does not require changes to AdCP core protocol. The `open_signals` field is an optional extension.

### 17.2 AAMP Trust Pillar Mapping (Conceptual)

AAMP's Trust and Transparency pillar includes:
- Agent registry for transparency
- Trust metadata for agent behavior
- Audit trails for accountability

OpenSignals complements AAMP by providing signal-level trust metadata:

| AAMP Concept | OpenSignals Equivalent |
|--------------|------------------------|
| Agent identity and registration | Signal provider identity in manifest |
| Agent capability declaration | Signal type and valid use cases |
| Agent behavior audit | Signal usage audit trail |
| Trust metadata | OpenSignal trust scores |
| Governance controls | Bounded autonomy model and policy binding |

OpenSignals manifests could be linked from AAMP agent registry entries for signal providers.

### 17.3 OpenRTB Extension (Conceptual)

OpenSignals trust scores could be included in OpenRTB bid requests as extensions:

**OpenRTB 2.x Extension**:
```json
{
  "imp": [
    {
      "id": "1",
      "ext": {
        "opensignals": {
          "signal_id": "outdoor-enthusiasts",
          "trust_score": 0.87,
          "trust_band": "trusted",
          "policy_bindings": ["alcohol_age_restriction"],
          "audit_id": "aud_789ghi"
        }
      }
    }
  ]
}
```

This allows SSPs and publishers to see which signals were used and their trust levels.

### 17.4 MCP Integration (Conceptual)

OpenSignals tasks could be exposed as MCP tools:

**MCP Tool: opensignals_verify_signal**:
```json
{
  "name": "opensignals_verify_signal",
  "description": "Verify if an advertising signal is trusted for a specific brand and use case",
  "inputSchema": {
    "type": "object",
    "properties": {
      "signal_id": { "type": "string" },
      "brand": { "type": "string" },
      "category": { "type": "string" },
      "intended_use": { "type": "string" }
    },
    "required": ["signal_id", "brand"]
  }
}
```

**MCP Resource: opensignals://manifests/{signal_id}**:
```json
{
  "uri": "opensignals://manifests/outdoor-enthusiasts",
  "mimeType": "application/json",
  "name": "Outdoor Recreation Enthusiasts Signal Manifest"
}
```

Agents could query signal trust through MCP calls integrated into LLM workflows.

### 17.5 A2A Integration (Conceptual)

OpenSignals verification could be exposed as A2A skills:

**A2A Skill Declaration**:
```json
{
  "agent_card": {
    "agent_id": "governance-agent-v1",
    "capabilities": {
      "skills": [
        {
          "skill_id": "verify_signal_trust",
          "description": "Verify advertising signal trust for brand policy compliance",
          "input_schema": { ... },
          "output_schema": { ... }
        }
      ]
    }
  }
}
```

Buyer agents could delegate signal verification to governance agents through A2A task delegation.

---

## 18. Security Considerations

### 18.1 Manifest Integrity

Signal providers SHOULD sign manifests using HTTP Message Signatures (RFC 9421) or similar cryptographic methods. Governance agents SHOULD verify signatures before trusting manifest data.

### 18.2 Provenance Verification

Chain of custody claims SHOULD be verifiable through independent verification endpoints. Governance agents MAY reject signals with unverifiable provenance.

### 18.3 Authentication and Authorization

API endpoints implementing OpenSignals tasks SHOULD require authentication (OAuth 2.0, API keys, mTLS). Authorization SHOULD be enforced based on brand and agent identity.

### 18.4 Audit Trail Security

Audit logs MUST be tamper-evident. Implementations SHOULD use append-only logs with cryptographic hashing or distributed ledgers where appropriate.

### 18.5 Denial of Service

Implementations SHOULD rate-limit verification requests to prevent abuse. Signal providers MAY cache verification results for a reasonable TTL.

### 18.6 Data Minimization

Verification requests SHOULD NOT include individual-level data. Aggregate context (brand, category, market) SHOULD be sufficient for most trust assessments.

---

## 19. Privacy Considerations

### 19.1 No Individual Data in Manifests

OpenSignals manifests MUST NOT contain individual-level user data. All metadata MUST be aggregate.

### 19.2 Consent Transparency

Manifests MUST declare consent scope clearly. Users SHOULD be able to verify how their data is permissioned through provider privacy policies.

### 19.3 Right to Revoke

Providers SHOULD implement mechanisms for users to revoke consent. Revoked consent SHOULD trigger signal status updates (`suspended` or usage restriction changes).

### 19.4 Geographic and Regulatory Compliance

Implementations MUST respect geographic restrictions declared in permissioning models. Signals MUST comply with GDPR (EU), CCPA (California), and other applicable privacy regulations.

### 19.5 Sensitive Categories

Signals involving sensitive categories (GDPR Article 9) MUST declare `sensitive_categories_allowed: false` unless explicit consent exists.

---

## 20. Compliance and Brand Safety

### 20.1 Regulated Categories

Signals used for regulated categories (alcohol, gambling, pharmaceuticals, financial services) MUST:
- Require human approval (`decision_mode: approve_with_human`)
- Enforce category-specific policies (age restrictions, geographic limits)
- Log audit trails for regulatory reporting
- Comply with market-specific advertising regulations

### 20.2 Brand Safety Integration

Governance agents SHOULD integrate with brand safety platforms to:
- Verify content adjacency safety
- Check publisher blocklists and allowlists
- Validate contextual suitability
- Monitor for inappropriate content placement

### 20.3 Children's Advertising

Signals targeting or involving children MUST:
- Declare `children_allowed: false` unless compliant with COPPA, GDPR-K, and local regulations
- Enforce strict age verification
- Prohibit behavioral profiling of children
- Require enhanced human oversight

### 20.4 Political and Advocacy Advertising

Signals used for political or advocacy campaigns SHOULD:
- Declare political affiliation or advocacy category
- Support transparency reporting requirements
- Comply with election-specific regulations
- Enable audit trail access for election officials

---

## 21. Conformance

This section specifies conformance requirements using RFC 2119 keywords. See [conformance.md](conformance.md) for detailed conformance testing criteria.

### 21.1 Signal Provider Conformance

A conforming Signal Provider:

1. MUST publish an OpenSignal Manifest for each signal containing all required fields (Section 8.2.1)
2. MUST use signal types from the standard taxonomy or declare `custom` with documentation (Section 7)
3. MUST declare provenance including data sources and collection method (Section 11)
4. MUST calculate and publish trust scores for all seven dimensions (Section 9)
5. MUST declare permissioning including valid use cases and consent scope (Section 10)
6. MUST implement the `get_signal_manifest` task (Section 16.1)
7. SHOULD publish manifests at well-known URLs (Section 8.4)
8. SHOULD update manifests when signal properties change materially
9. SHOULD implement the `revoke_signal` task (Section 16.6)
10. MAY implement cryptographic verification for provenance (Section 11.5)

### 21.2 Buyer Agent Conformance

A conforming Buyer Agent:

1. MUST call `verify_signal` before activating signals (Section 16.2)
2. MUST respect `decision` values returned by governance agents
3. MUST NOT activate signals in restricted geographies or categories (Section 10.4)
4. MUST respect `decision_mode` and obtain human approval when required (Section 15)
5. MUST log signal usage through `audit_signal_usage` (Section 16.5)
6. SHOULD call `score_signal` to assess objective alignment (Section 16.3)
7. SHOULD submit outcome feedback via `submit_signal_outcome_feedback` (Section 16.7)
8. SHOULD cache manifests according to `freshness_ttl` (Section 12.3)
9. MAY implement custom trust scoring adjustments based on brand-specific performance data

### 21.3 Governance Agent Conformance

A conforming Governance Agent:

1. MUST implement the `verify_signal` task (Section 16.2)
2. MUST evaluate signals against brand policy and regulatory requirements
3. MUST return decisions (`approved`, `approved_with_conditions`, `rejected`, `approval_pending`) with reasoning
4. MUST enforce bounded autonomy modes (Section 15)
5. MUST implement the `bind_signal_policy` task (Section 16.4)
6. SHOULD implement the `score_signal` task (Section 16.3)
7. SHOULD provide human approval workflows for regulated categories
8. SHOULD integrate with brand safety platforms
9. MAY customize trust score weights based on brand priorities

### 21.4 Audit Agent Conformance

A conforming Audit Agent:

1. MUST implement the `audit_signal_usage` task (Section 16.5)
2. MUST log all required fields in audit events (Section 13.2)
3. MUST retain audit logs for declared `audit_retention_days` (default: 90 days)
4. SHOULD provide queryable audit trail APIs
5. SHOULD support audit export for regulatory reporting
6. MAY implement tamper-evident audit logs

### 21.5 Execution Platform Conformance

A conforming Execution Platform:

1. SHOULD enforce trust thresholds before activating signals
2. SHOULD respect policy bindings included in activation requests
3. SHOULD integrate OpenSignals metadata into bid requests or insertion orders
4. SHOULD log signal activations to audit agents
5. MAY provide outcome feedback to signal providers

---

## 22. Governance Considerations

### 22.1 Protocol Governance

OpenSignals is an open-source protocol. Governance of the specification should involve:
- Open community participation through GitHub
- Transparent decision-making for protocol changes
- Compatibility with industry standards bodies (IAB Tech Lab, W3C)
- Neutral stewardship without vendor control

### 22.2 Industry Adoption

For OpenSignals to achieve industry adoption:
- Signal providers should publish manifests alongside existing signal documentation
- Buyer platforms should integrate verification workflows
- Governance vendors should expose OpenSignals-compatible APIs
- Industry working groups (AAMP, AdCP) should consider formal integration

### 22.3 Certification and Accreditation

While OpenSignals does not define certification, industry bodies MAY:
- Certify signal providers for manifest accuracy
- Accredit governance agents for policy enforcement
- Audit platforms for conformance to specification
- Establish trust registries for verified signals

### 22.4 Dispute Resolution

Disputes regarding signal trust, policy enforcement or audit trails should be resolved through:
- Contractual agreements between parties
- Industry arbitration mechanisms
- Regulatory oversight where applicable

---

## 23. Future Roadmap

### 23.1 Planned Enhancements (v0.2 and beyond)

1. **Formal AdCP Extension**: Standardized OpenSignals fields in AdCP `get_signals` responses
2. **AAMP Integration**: Alignment with AAMP trust pillar specifications
3. **Federated Trust Registries**: Cross-platform trust score sharing
4. **Enhanced Provenance**: Zero-knowledge proofs for privacy-preserving provenance verification
5. **Dynamic Trust Scoring**: Real-time trust score updates based on continuous monitoring
6. **Signal Composability**: Trust scoring for combined or derived signals
7. **Outcome Feedback Loops**: Automated trust score adjustments based on campaign performance
8. **Regulatory Templates**: Pre-built policy bindings for GDPR, CCPA, COPPA, industry regulations

### 23.2 Research Areas

1. Decentralized trust verification using blockchain or distributed ledgers
2. AI-driven anomaly detection for signal quality degradation
3. Cross-border signal permissioning for global campaigns
4. Privacy-preserving trust scoring using differential privacy
5. Standardized outcome measurement taxonomies

### 23.3 Community Feedback

The protocol maintainers welcome feedback on:
- Practical implementation challenges
- Integration experiences with AdCP, AAMP, OpenRTB
- Trust scoring model improvements
- Additional signal types or use cases
- Governance and audit requirements

---

## 24. References

### 24.1 Normative References

- **RFC 2119**: Key words for use in RFCs to Indicate Requirement Levels. [https://datatracker.ietf.org/doc/html/rfc2119](https://datatracker.ietf.org/doc/html/rfc2119)
- **JSON Schema**: JSON Schema Specification. [https://json-schema.org](https://json-schema.org)
- **ISO 8601**: Date and time format standard.
- **ISO 3166-1 alpha-2**: Two-letter country codes.

### 24.2 Informative References

- **AdCP (Ad Context Protocol)**: [https://adcontextprotocol.org](https://adcontextprotocol.org)
- **AdCP GitHub**: [https://github.com/adcontextprotocol/adcp](https://github.com/adcontextprotocol/adcp)
- **IAB Tech Lab AAMP**: [https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/](https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/)
- **IAB Tech Lab AdCOM**: [https://github.com/InteractiveAdvertisingBureau/AdCOM](https://github.com/InteractiveAdvertisingBureau/AdCOM)
- **IAB Tech Lab OpenRTB**: [https://github.com/InteractiveAdvertisingBureau/openrtb2.x](https://github.com/InteractiveAdvertisingBureau/openrtb2.x)
- **Model Context Protocol (MCP)**: [https://modelcontextprotocol.io](https://modelcontextprotocol.io)
- **MCP Specification**: [https://modelcontextprotocol.io/specification/2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25)
- **Agent2Agent (A2A) Protocol**: [https://a2a-protocol.org](https://a2a-protocol.org)
- **A2A Specification**: [https://a2a-protocol.org/latest/specification/](https://a2a-protocol.org/latest/specification/)
- **RFC 9421 (HTTP Message Signatures)**: [https://datatracker.ietf.org/doc/html/rfc9421](https://datatracker.ietf.org/doc/html/rfc9421)
- **GDPR**: General Data Protection Regulation (EU)
- **CCPA**: California Consumer Privacy Act

---

## Appendix A: Change Log

### Version 0.1 (May 2026)

- Initial draft specification
- Core manifest structure defined
- Seven-dimension trust score model
- Bounded autonomy model with five decision modes
- Seven protocol tasks specified
- Conceptual integration models for AdCP, AAMP, MCP, A2A

---

## Appendix B: Acknowledgments

This specification was developed with reference to public documentation from:

- AdCP and the Ad Context Protocol community
- IAB Tech Lab's AAMP initiative and working groups
- IAB Tech Lab's OpenRTB, OpenDirect and AdCOM specifications
- Model Context Protocol specification and community
- Agent2Agent Protocol specification and community

The authors thank the advertising technology community for their ongoing work to standardize agentic advertising infrastructure.

---

**Document Status**: Draft RFC v0.1
**Last Updated**: May 2026
**License**: Apache 2.0 (code), Creative Commons Attribution 4.0 International (documentation)
**Repository**: [https://github.com/opensignals-protocol/opensignals-protocol](https://github.com/opensignals-protocol/opensignals-protocol)
