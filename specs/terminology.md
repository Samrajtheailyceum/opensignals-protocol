# OpenSignals Protocol: Terminology

**Version**: 0.1
**Status**: Draft
**Last Updated**: May 2026

---

## Overview

This document defines key terms used throughout the OpenSignals Protocol specification. Terms are organized alphabetically within categories for ease of reference.

## Terminology Conventions

- **Normative terms** (MUST, SHOULD, MAY) are defined according to RFC 2119
- **Technical terms** specific to OpenSignals are defined below
- **Industry terms** reference existing advertising and agentic protocol definitions where applicable

---

## Core Protocol Terms

### Advertising Signal

Structured data describing audiences, contexts, inventory, behaviors or other targeting attributes used in advertising decision-making. Signals may describe user attributes (audience signals), content attributes (contextual signals), performance metrics (outcome signals), or other advertising-relevant dimensions.

**Examples**: demographic segments, interest categories, contextual classifications, attention metrics, commerce behaviors, geographic patterns.

### Audit Agent

An agent or system that records, analyzes and reports signal usage for accountability and compliance. Audit agents implement the `audit_signal_usage` task and maintain tamper-evident audit trails.

**Related terms**: Audit Trail, Audit Event, Audit Retention

### Audit Trail

A chronological record of signal usage events including who activated a signal, when, for what purpose, under what policy, and with what approval. Audit trails enable post-activation accountability and regulatory reporting.

**Required fields**: signal_id, timestamp, brand, campaign_id, buyer_agent, governance_agent, decision_mode, trust_score, use_case, platform, geographic_scope, category.

### Bounded Autonomy

A model for controlling the level of autonomy granted to buyer agents when activating signals. The model defines five decision modes ranging from full human control (observe) to full autonomy (autonomous_full). Decision modes are selected based on signal trust scores, category restrictions, and brand policy.

**Related terms**: Decision Mode, Human Approval, Approval Workflow

### Brand Policy Owner

The human stakeholder (advertiser, agency, brand manager) who defines brand policy, approval requirements, trust thresholds, and category restrictions for signal usage. Brand policy owners review audit trails and approve high-risk signal activations.

**Related terms**: Brand Policy, Policy Binding, Governance Agent

### Buyer Agent

An autonomous or semi-autonomous AI agent acting on behalf of an advertiser or agency to discover, evaluate, and activate advertising signals. Buyer agents must verify signals before activation and respect bounded autonomy constraints.

**Related terms**: Media Buying Agent, Campaign Planning Agent, Optimization Agent

### Decision Mode

The level of autonomy granted to a buyer agent for signal activation. OpenSignals defines five decision modes: `observe`, `recommend`, `approve_with_human`, `autonomous_with_limits`, and `autonomous_full`. Decision mode is determined by trust score, category, and brand policy.

**Related terms**: Bounded Autonomy, Human Approval Required, Autonomous Activation

### Execution Platform

A platform that executes media buying decisions made by agents, such as DSPs, SSPs, ad servers, or direct buying platforms. Execution platforms may enforce signal trust thresholds and log signal activations to audit agents.

**Related terms**: DSP, SSP, Ad Server, Programmatic Platform

### Governance Agent

An agent or system responsible for enforcing brand policy, compliance rules, and approval workflows. Governance agents implement the `verify_signal`, `score_signal`, and `bind_signal_policy` tasks. They evaluate signals against brand policy and regulatory requirements before activation.

**Related terms**: Policy Enforcement, Compliance Engine, Brand Safety Platform

### OpenSignal Manifest

A JSON document that declares signal properties, trust metadata, provenance, permissioning, quality metrics, and governance requirements. Each signal must have a corresponding manifest. Manifests are published by signal providers at well-known URLs or through signal discovery protocols.

**Related terms**: Manifest Structure, Manifest Discovery, Manifest Versioning

### Policy Binding

The process of attaching brand-specific policy rules to a signal before activation. Policy bindings declare which brand policies apply (e.g., alcohol age restrictions, no individual profiling), their enforcement level (mandatory, recommended, advisory), and policy parameters. Bound policies are included in activation requests to ensure execution platforms enforce rules.

**Related terms**: Brand Policy, Enforcement Level, Policy Parameters

### Signal Provider

An organization that creates, maintains, and publishes advertising signals. Signal providers must publish OpenSignal Manifests, maintain signal quality, declare provenance and permissioning, and implement the `get_signal_manifest` task.

**Examples**: Data providers, publishers, SSPs, measurement vendors, research firms, DMPs, CDPs.

### Trust Score

A numerical score (0.00 to 1.00) representing the trustworthiness of a signal across multiple dimensions. OpenSignals defines seven trust dimensions: provenance, permissioning, freshness, quality, explainability, outcome relevance, and compliance safety. The overall trust score is a weighted sum of dimension scores.

**Related terms**: Trust Dimension, Trust Band, Trust Score Reasoning

### Trust Band

A categorical classification of trust scores into five bands: Highly Trusted (0.90-1.00), Trusted (0.75-0.89), Limited Trust (0.50-0.74), Low Trust (0.25-0.49), and Unsafe/Invalid (0.00-0.24). Bands provide decision guidance for activation workflows.

---

## Trust Score Dimensions

### Provenance Score

A trust dimension measuring data source transparency and chain of custody. Provenance scoring evaluates whether data sources are clearly declared, collection methods are documented, and data lineage can be traced from source to signal.

**Scoring factors**: data source transparency, collection method clarity, chain of custody verification.

**Weight**: 20% of overall trust score.

### Permissioning Score

A trust dimension measuring consent transparency and usage rights clarity. Permissioning scoring evaluates whether consent is explicitly granted for advertising use, usage constraints are documented, and users can revoke consent.

**Scoring factors**: consent scope, usage restrictions, right to revoke.

**Weight**: 20% of overall trust score.

### Freshness Score

A trust dimension measuring signal recency and update frequency. Freshness scoring evaluates how recently the signal was updated and how frequently it is refreshed. Freshness requirements vary by signal type.

**Scoring factors**: time since last update, update frequency.

**Weight**: 15% of overall trust score.

### Quality Score

A trust dimension measuring signal coverage, precision, and stability. Quality scoring evaluates whether the signal reaches the intended audience (coverage), accurately represents declared attributes (precision), and maintains consistent composition over time (stability).

**Scoring factors**: coverage, precision, stability.

**Weight**: 20% of overall trust score.

### Explainability Score

A trust dimension measuring how well the signal can be explained to stakeholders and regulators. Explainability scoring evaluates documentation quality, transparency of signal composition, and interpretability for non-technical stakeholders.

**Scoring factors**: documentation quality, transparency, interpretability.

**Weight**: 10% of overall trust score.

### Outcome Relevance Score

A trust dimension measuring historical performance against similar brand objectives. Outcome scoring evaluates whether the signal has driven outcomes in similar campaigns, whether performance is validated by third-party verification, and how recent performance measurements are.

**Scoring factors**: past performance, validation, recency of outcomes.

**Weight**: 10% of overall trust score.

### Compliance Safety Score

A trust dimension measuring adherence to regulations and brand safety standards. Compliance scoring evaluates regulatory compliance (GDPR, CCPA, category-specific regulations), brand safety certification, and risk assessment for content adjacency.

**Scoring factors**: regulatory compliance, brand safety certification, risk assessment.

**Weight**: 5% of overall trust score.

---

## Signal Types

### Audience Signal

A signal describing user attributes, behaviors, or segments. Audience signals are used for demographic targeting, interest-based targeting, lookalike modeling, and behavioral segmentation.

**Examples**: age/gender demographics, interest categories, purchase propensity, lifestyle segments.

### Contextual Signal

A signal describing content, page, or environment attributes. Contextual signals are used for contextual targeting, brand safety, and adjacency controls.

**Examples**: content categories, page topics, sentiment analysis, brand safety classifications.

### Geographic Signal

A signal describing location, region, or geo-behavioral patterns. Geographic signals are used for local advertising, geo-fencing, and regional campaigns.

**Examples**: DMA, zip code, city, country, store proximity, travel patterns.

### Temporal Signal

A signal describing time-based patterns or seasonality. Temporal signals are used for dayparting, event-based marketing, and seasonal campaigns.

**Examples**: time of day, day of week, seasonal trends, event-driven patterns.

### Commerce Signal

A signal describing purchase behavior, intent, or transaction data. Commerce signals are used for retargeting, conversion optimization, and commerce media.

**Examples**: purchase history, shopping cart abandonment, product views, category affinity.

### Attention Signal

A signal describing viewability, engagement, or attention metrics. Attention signals are used for attention-based buying and viewability optimization.

**Examples**: viewability score, dwell time, scroll depth, attention seconds.

### Creative Signal

A signal describing creative performance or A/B test results. Creative signals are used for creative optimization, dynamic creative, and format selection.

**Examples**: creative variation performance, format effectiveness, message testing results.

### Environmental Signal

A signal describing sustainability, carbon impact, or ethical sourcing. Environmental signals are used for sustainable advertising, ESG reporting, and brand values alignment.

**Examples**: carbon footprint, renewable energy usage, sustainable sourcing certification.

### Compliance Signal

A signal describing regulatory adherence or certification status. Compliance signals are used for age verification, consent management, and category restrictions.

**Examples**: age verification status, consent flags, regulatory approvals.

### Outcome Signal

A signal describing performance, conversion, or lift measurement. Outcome signals are used for attribution, incrementality testing, and performance forecasting.

**Examples**: conversion rates, brand lift, incrementality, ROAS predictions.

### Brand Safety Signal

A signal describing content classification or risk assessment. Brand safety signals are used for brand safety targeting, exclusion lists, and sensitive content avoidance.

**Examples**: brand safety scores, content risk ratings, suitability classifications.

### Custom Signal

A provider-defined signal type not covered by the standard taxonomy. Custom signals must include detailed documentation in the manifest description field.

---

## Provenance Terms

### Data Source

The origin of data used to construct a signal. OpenSignals defines a standard data source taxonomy including first-party transactional, first-party behavioral, first-party declared, second-party, third-party aggregated, third-party modeled, survey, public data, contextual analysis, and measurement.

**Related terms**: Provenance, Collection Method, Chain of Custody

### Collection Method

The methodology used to collect data for a signal. OpenSignals defines standard collection methods including opt-in panel, account registration, survey, transactional, behavioral tracking, contextual crawl, inference, and public aggregation.

**Related terms**: Data Source, Provenance, Consent Scope

### Chain of Custody

The documented lineage of data as it passes through multiple entities from source to signal. Chain of custody includes entity names, roles (data collector, data processor, signal publisher), and timestamps for each handoff.

**Related terms**: Provenance, Data Lineage, Verification

### Provenance Verification

The process of validating provenance claims through cryptographic signatures, third-party verification, or independent audits. Verification methods include HTTP Message Signatures, zero-knowledge proofs, or provider-specific verification endpoints.

**Related terms**: Cryptographic Verification, HTTP Message Signatures, Trust Verification

---

## Permissioning Terms

### Valid Use Case

A declared advertising use case for which a signal is permitted. OpenSignals defines standard use cases including targeting, frequency capping, attribution, measurement, optimization, research, and forecasting. Buyer agents must not use signals for use cases not declared as valid.

**Related terms**: Permissioning, Consent Scope, Usage Restrictions

### Consent Scope

The type and extent of user consent for advertising use. OpenSignals defines consent scopes including explicit opt-in, opt-in, legitimate interest, contractual, and consent not required. Consent scope determines permissible activation scenarios.

**Related terms**: Consent Mechanism, Permissioning, Privacy Compliance

### Geographic Restriction

A constraint preventing signal usage in specific geographies. Geographic restrictions are declared using ISO 3166-1 alpha-2 country codes. Buyer agents must not activate signals in restricted geographies.

**Related terms**: Permissioning, Market Restrictions, Compliance

### Category Restriction

A constraint preventing signal usage for specific advertising categories. Common category restrictions include alcohol, gambling, pharma, finance, and political. Category restrictions enforce regulatory and brand policy compliance.

**Related terms**: Regulated Category, Permissioning, Brand Safety

### Individual Profiling

The use of a signal for targeting specific individuals based on personal characteristics or behaviors. If `individual_profiling_allowed` is false, agents must use the signal for aggregate or contextual targeting only.

**Related terms**: Privacy, GDPR, Aggregate Targeting

### Sensitive Categories

Categories of data requiring special protection under privacy regulations (GDPR Article 9), including health, religion, politics, sexual orientation, race, and ethnicity. If `sensitive_categories_allowed` is false, the signal must not be used for sensitive category targeting.

**Related terms**: Privacy, GDPR Article 9, Special Category Data

---

## Governance Terms

### Decision

The outcome of a signal verification request. OpenSignals defines four decision values: `approved` (signal approved for immediate activation), `approved_with_conditions` (signal approved with attached conditions), `rejected` (signal rejected for this use case), and `approval_pending` (signal requires human approval).

**Related terms**: Verification, Governance Agent, Approval Workflow

### Approval Required

A flag indicating that a signal requires human approval before activation. Approval is typically required for regulated categories (alcohol, gambling, pharma, finance), low-trust signals (trust score below threshold), or sensitive brand contexts.

**Related terms**: Bounded Autonomy, Human Approval, Decision Mode

### Approval Workflow

A human-in-the-loop process for reviewing and approving signal activations. Approval workflows notify human approvers, present signal manifests and trust scores, and record approval decisions in audit trails.

**Related terms**: Human Approval Required, Governance Agent, Brand Policy Owner

### Enforcement Level

The strictness with which a policy binding must be enforced. OpenSignals defines three enforcement levels: `mandatory` (policy must be enforced; violation blocks activation), `recommended` (policy should be enforced; violation triggers warning), and `advisory` (policy provides guidance; no enforcement).

**Related terms**: Policy Binding, Mandatory Policy, Advisory Policy

### Regulated Category

An advertising category subject to special regulatory requirements. OpenSignals identifies regulated categories including alcohol, gambling, pharma, finance, children's advertising, and political advertising. Regulated categories typically require human approval and enhanced audit trails.

**Related terms**: Category Restriction, Compliance, Human Approval Required

---

## Audit Terms

### Audit Event

A structured record of a signal activation including all context required for accountability: who activated the signal, when, for what purpose, under what policy, with what approval, and on what platform. Audit events are logged by audit agents and retained according to audit retention policies.

**Related terms**: Audit Trail, Audit Agent, Audit Retention

### Audit Retention

The duration for which audit logs must be retained. OpenSignals recommends a default retention of 90 days, with longer retention for regulated categories. Audit retention is declared in signal manifests and enforced by audit agents.

**Related terms**: Audit Trail, Compliance, Regulatory Reporting

### Audit Endpoint

A URL where audit events are sent for logging. Audit endpoints are declared in signal manifests and implemented by audit agents or execution platforms.

**Related terms**: Audit Agent, Audit Trail, Logging

---

## Protocol Task Terms

### get_signal_manifest

A protocol task for retrieving the full OpenSignal Manifest for a signal. Implemented by signal providers. May be called via direct HTTP GET to well-known URLs, AdCP extensions, MCP resources, or provider-specific APIs.

**Related terms**: Manifest Discovery, Signal Provider, Protocol Task

### verify_signal

A protocol task for checking if a signal is valid and permissioned for a specific use case. Implemented by governance agents. Returns a decision (approved, approved with conditions, rejected, approval pending) with reasoning and trust score.

**Related terms**: Trust Verification, Governance Agent, Protocol Task

### score_signal

A protocol task for scoring a signal against a specific brand objective. Implemented by governance agents or buyer agents. Returns an objective alignment score with expected performance estimates and recommendation.

**Related terms**: Objective Alignment, Performance Forecasting, Protocol Task

### bind_signal_policy

A protocol task for attaching brand-specific policy rules to a signal before activation. Implemented by governance agents. Returns policy bindings with enforcement levels and parameters.

**Related terms**: Policy Binding, Brand Policy, Protocol Task

### audit_signal_usage

A protocol task for recording signal usage after activation. Implemented by audit agents or execution platforms. Logs audit events with full context and returns audit ID and retention timestamp.

**Related terms**: Audit Trail, Audit Agent, Protocol Task

### revoke_signal

A protocol task for withdrawing trust from a signal due to quality degradation, compliance violation, or other issues. Implemented by signal providers or governance agents. Changes signal status and notifies active users.

**Related terms**: Signal Revocation, Trust Withdrawal, Protocol Task

### submit_signal_outcome_feedback

A protocol task for feeding campaign results back into signal trust scoring. Implemented by buyer agents or measurement platforms. Submits performance metrics and quality assessments to improve outcome scores.

**Related terms**: Outcome Feedback, Performance Measurement, Protocol Task

---

## Integration Terms

### AdCP (Ad Context Protocol)

An open protocol for signal discovery and activation. OpenSignals extends AdCP by adding trust verification between signal discovery (`get_signals`) and signal activation (`activate_signal`).

**Relationship**: OpenSignals complements AdCP with pre-activation trust assessment.

**Specification**: [adcontextprotocol.org](https://adcontextprotocol.org)

### AAMP (Agentic Advertising Management Protocols)

IAB Tech Lab's industry framework for agentic advertising, consisting of three pillars: Foundations (ARTF), Protocols (extensions to OpenRTB/AdCOM/OpenDirect), and Trust and Transparency. OpenSignals implements the Trust and Transparency pillar.

**Relationship**: OpenSignals provides practical implementation for AAMP's trust goals.

**Specification**: [iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/](https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/)

### MCP (Model Context Protocol)

An open protocol for LLM integration with external data sources and tools. OpenSignals tasks may be exposed as MCP tools, allowing agents to query signal trust through standardized LLM integration.

**Relationship**: Conceptual integration; OpenSignals tasks as MCP tools.

**Specification**: [modelcontextprotocol.io](https://modelcontextprotocol.io)

### A2A (Agent2Agent Protocol)

An open protocol for agent-to-agent communication. OpenSignals verification and scoring may be exposed as A2A skills, enabling buyer agents to delegate trust assessment to governance agents.

**Relationship**: Conceptual integration; OpenSignals tasks as A2A skills.

**Specification**: [a2a-protocol.org](https://a2a-protocol.org)

### OpenRTB

IAB Tech Lab's real-time bidding protocol. OpenSignals operates above the execution layer, helping agents decide which signals to include in OpenRTB bid requests. Trust scores may be included in OpenRTB extensions.

**Relationship**: OpenSignals provides pre-activation trust; OpenRTB executes transactions.

**Specification**: [github.com/InteractiveAdvertisingBureau/openrtb2.x](https://github.com/InteractiveAdvertisingBureau/openrtb2.x)

### AdCOM

IAB Tech Lab's common object model for programmatic advertising. OpenSignals references AdCOM taxonomy and enumeration patterns for signal type classification.

**Relationship**: OpenSignals aligns with AdCOM taxonomy conventions.

**Specification**: [github.com/InteractiveAdvertisingBureau/AdCOM](https://github.com/InteractiveAdvertisingBureau/AdCOM)

---

## RFC 2119 Keywords

The following keywords are used throughout the OpenSignals specification according to RFC 2119:

### MUST

This keyword indicates an absolute requirement. Implementations that do not satisfy MUST requirements are not conformant.

**Synonym**: REQUIRED, SHALL

### MUST NOT

This keyword indicates an absolute prohibition. Implementations that violate MUST NOT requirements are not conformant.

**Synonym**: SHALL NOT

### SHOULD

This keyword indicates a recommendation. There may be valid reasons to ignore SHOULD requirements, but implications must be understood.

**Synonym**: RECOMMENDED

### SHOULD NOT

This keyword indicates a recommendation against a particular behavior. There may be valid reasons to ignore SHOULD NOT requirements, but implications must be understood.

**Synonym**: NOT RECOMMENDED

### MAY

This keyword indicates an optional feature. Implementations may include or omit MAY features without affecting conformance.

**Synonym**: OPTIONAL

---

## Abbreviations

| Abbreviation | Full Term |
|--------------|-----------|
| AAMP | Agentic Advertising Management Protocols |
| A2A | Agent2Agent Protocol |
| AdCP | Ad Context Protocol |
| AdCOM | IAB Tech Lab Advertising Common Object Model |
| API | Application Programming Interface |
| ARTF | Agentic Runtime Framework (AAMP Foundations pillar) |
| CCPA | California Consumer Privacy Act |
| CDP | Customer Data Platform |
| COPPA | Children's Online Privacy Protection Act |
| CPG | Consumer Packaged Goods |
| CPM | Cost Per Thousand Impressions |
| DMP | Data Management Platform |
| DSP | Demand-Side Platform |
| ESG | Environmental, Social, and Governance |
| GDPR | General Data Protection Regulation |
| GDPR-K | GDPR provisions for children |
| HTTP | Hypertext Transfer Protocol |
| HTTPS | Hypertext Transfer Protocol Secure |
| IAB | Interactive Advertising Bureau |
| ISO | International Organization for Standardization |
| JSON | JavaScript Object Notation |
| KPI | Key Performance Indicator |
| LLM | Large Language Model |
| MCP | Model Context Protocol |
| mTLS | Mutual Transport Layer Security |
| NLP | Natural Language Processing |
| OAuth | Open Authorization |
| RFC | Request for Comments |
| ROAS | Return on Ad Spend |
| SSP | Supply-Side Platform |
| TTL | Time to Live |
| URL | Uniform Resource Locator |
| URI | Uniform Resource Identifier |
| VAST | Video Ad Serving Template |

---

## Glossary Notes

### Updates and Additions

This terminology document is versioned alongside the OpenSignals Protocol specification. When new terms are introduced or existing definitions are clarified:

1. Update the version number and last updated date
2. Add new terms in alphabetical order within appropriate sections
3. Reference the specification section where the term is formally defined
4. Update related protocol documentation to maintain consistency

### Contributing Definitions

To propose new terms or clarify existing definitions:

1. Open a GitHub issue with the `terminology` label
2. Provide the proposed term, definition, and related terms
3. Reference specific use cases where clarity is needed
4. Suggest appropriate categorization within this document

---

## References

- **OpenSignals Protocol v0.1 Specification**: [opensignals-v0.1.md](opensignals-v0.1.md)
- **OpenSignals Conformance Requirements**: [conformance.md](conformance.md)
- **RFC 2119 (Key words for RFCs)**: [https://datatracker.ietf.org/doc/html/rfc2119](https://datatracker.ietf.org/doc/html/rfc2119)
- **AdCP Documentation**: [https://adcontextprotocol.org](https://adcontextprotocol.org)
- **IAB Tech Lab AAMP**: [https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/](https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/)

---

**Document Status**: Draft
**Protocol Version**: 0.1
**Last Updated**: May 2026
**Repository**: [https://github.com/opensignals-protocol/opensignals-protocol](https://github.com/opensignals-protocol/opensignals-protocol)
