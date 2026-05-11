# OpenSignals and AAMP Trust & Transparency Pillar: Conceptual Mapping

**Status**: Conceptual Integration Design
**Version**: 0.1
**Date**: May 2026
**Disclaimer**: This document describes a conceptual mapping between OpenSignals Protocol and the AAMP (Agentic Advertising Management Protocols) Trust and Transparency pillar. This is NOT an official integration specification or endorsed by the IAB Tech Lab AAMP working group. Implementation would require formal coordination between both protocol communities.

---

## Executive Summary

The **OpenSignals Protocol** provides a practical implementation layer for **signal-level trust verification** that aligns with and complements the **AAMP Trust and Transparency pillar**. While AAMP establishes the architectural framework for agent trust, identity, and governance in agentic advertising systems, OpenSignals provides the signal-specific metadata, verification workflows, and audit mechanisms needed to operationalize trust at the data layer.

This document maps OpenSignals concepts to AAMP's Trust and Transparency requirements and shows how they work together to create trustworthy agentic advertising ecosystems.

---

## 1. Introduction to AAMP

### 1.1 What is AAMP?

**AAMP (Agentic Advertising Management Protocols)** is an IAB Tech Lab initiative defining standards for autonomous AI agents in advertising. AAMP consists of three pillars:

1. **Foundations (ARTF - Agentic Runtime and Trust Framework)**
   - Agent identity and registration
   - Runtime framework for agent execution
   - Trust models for agent-to-agent communication

2. **Protocols**
   - Extensions to OpenRTB for agentic bidding
   - Extensions to AdCOM for agentic object models
   - Extensions to OpenDirect for programmatic direct buying by agents

3. **Trust and Transparency**
   - Mechanisms for verifying agent behavior
   - Audit trails for agent decisions
   - Governance controls for agent autonomy
   - Transparency in agent decision-making

**Reference**: [IAB Tech Lab AAMP Specification](https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/)

### 1.2 The Trust and Transparency Challenge

AAMP's Trust and Transparency pillar addresses the fundamental challenge of agentic advertising: **How do advertisers trust autonomous agents to make appropriate decisions about media buying, signal activation, and campaign optimization?**

Key requirements include:
- **Agent identity and registration**: Who is the agent and what can it do?
- **Decision transparency**: Why did the agent make this decision?
- **Audit trails**: What did the agent do and when?
- **Bounded autonomy**: When does the agent need human approval?
- **Governance controls**: How do we enforce brand policy on agent behavior?

---

## 2. OpenSignals and AAMP: Complementary Layers

### 2.1 Where They Intersect

OpenSignals and AAMP operate at different but complementary layers:

| Layer | AAMP Focus | OpenSignals Focus |
|-------|------------|-------------------|
| **Agent Layer** | Agent identity, capabilities, runtime framework | Signal provider identity, governance agent roles |
| **Trust Layer** | Agent trust metadata, behavior verification | Signal trust metadata, quality scoring |
| **Data Layer** | *(Not explicitly specified)* | **Signal manifests, provenance, permissioning** |
| **Governance Layer** | Agent autonomy controls, approval workflows | Signal verification, policy binding, audit trails |
| **Transparency Layer** | Agent decision transparency | Signal explainability, methodology transparency |

**Key Insight**: AAMP provides the **agent-level trust framework**, while OpenSignals provides the **signal-level trust verification layer**. Together, they enable trustworthy agentic advertising.

### 2.2 Conceptual Integration Model

```
┌─────────────────────────────────────────────────────────────┐
│                    AAMP Trust Framework                      │
│  (Agent Identity, Registration, Governance, Audit)          │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ├─ Agent Registry
                      ├─ Agent Trust Metadata
                      ├─ Bounded Autonomy Controls
                      └─ Agent Audit Trails
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              OpenSignals Trust Verification Layer            │
│   (Signal Manifests, Trust Scores, Verification, Audit)     │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ├─ Signal Discovery (AdCP)
                      ├─ Signal Trust Assessment
                      ├─ Signal Verification
                      ├─ Policy Binding
                      └─ Signal Usage Audit
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│           Execution Layer (OpenRTB, OpenDirect)              │
│        (Bidding, Direct Buying, Ad Serving)                 │
└─────────────────────────────────────────────────────────────┘
```

**Workflow**:
1. AAMP registers and authenticates buyer agent
2. Agent discovers signals via AdCP (extended with OpenSignals metadata)
3. OpenSignals verifies signal trust and binds brand policy
4. Agent executes media buying via OpenRTB/OpenDirect
5. OpenSignals logs signal usage for audit
6. AAMP logs agent behavior for transparency

---

## 3. Mapping OpenSignals to AAMP Trust Pillar

### 3.1 Agent Registry and Signal Provider Identity

#### AAMP Requirement
AAMP requires agents to be registered with identity metadata including:
- Agent ID and name
- Capabilities and skills
- Owner organization
- Trust credentials

#### OpenSignals Implementation
OpenSignals manifests declare **signal provider identity** similarly:
```json
{
  "owner": {
    "organization": "Example Data Co",
    "contact": "signals@example.com",
    "country": "US",
    "registration": "12-3456789"
  },
  "provider": {
    "name": "Example Data Co",
    "url": "https://example.com",
    "support_contact": "support@example.com",
    "documentation_url": "https://docs.example.com"
  }
}
```

#### Conceptual Mapping
Signal providers could be registered in the **AAMP Agent Registry** as "Signal Provider Agents" with:
- Agent type: `signal_provider`
- Capabilities: List of signal IDs they provide
- Trust metadata: Link to OpenSignals manifests
- Verification endpoint: OpenSignals `get_signal_manifest` endpoint

**Example AAMP Agent Card for Signal Provider**:
```json
{
  "agent_card": {
    "agent_id": "example-data-co-signal-provider",
    "agent_type": "signal_provider",
    "organization": "Example Data Co",
    "capabilities": {
      "signal_ids": [
        "outdoor-enthusiasts",
        "sustainability-consumers",
        "premium-travelers"
      ],
      "opensignals_manifest_base_url": "https://example.com/.well-known/opensignals/"
    },
    "trust_metadata": {
      "registration_date": "2025-03-01T00:00:00Z",
      "verification_status": "verified",
      "certifications": ["iso_27001", "soc2_type2"]
    }
  }
}
```

### 3.2 Bounded Autonomy and Decision Modes

#### AAMP Requirement
AAMP defines bounded autonomy controls specifying when agents can act autonomously vs. requiring human approval.

#### OpenSignals Implementation
OpenSignals defines **five decision modes** in signal governance:

| OpenSignals Decision Mode | AAMP Alignment | Human Involvement |
|--------------------------|----------------|-------------------|
| `observe` | Fully manual | Agent observes only; human makes all decisions |
| `recommend` | Human-in-the-loop | Agent recommends; human reviews and approves before action |
| `approve_with_human` | Human-in-the-loop | Agent proposes; human must approve each action |
| `autonomous_with_limits` | Bounded autonomy | Agent acts autonomously within trust thresholds; human reviews audit trails |
| `autonomous_full` | Full autonomy | Agent acts fully autonomously; human reviews post-activation |

#### Conceptual Mapping
OpenSignals decision modes could be integrated with **AAMP's autonomy controls**:

```json
{
  "aamp_governance": {
    "agent_id": "media-optimizer-v2",
    "autonomy_level": "bounded",
    "opensignals_decision_mode": "approve_with_human",
    "trust_threshold": 0.75,
    "human_approval_required_for": {
      "categories": ["alcohol", "gambling", "pharma"],
      "trust_scores_below": 0.75,
      "signals_with_limited_provenance": true
    },
    "approval_workflow_endpoint": "https://governance.brand.com/approve"
  }
}
```

### 3.3 Regulated Category Governance

#### AAMP Requirement
AAMP emphasizes **category-specific governance** for regulated industries (alcohol, gambling, pharmaceuticals, financial services).

#### OpenSignals Implementation
OpenSignals provides explicit **category governance controls**:

```json
{
  "governance": {
    "category": "alcohol",
    "human_approval_required": true,
    "audit_required": true,
    "compliance_frameworks": [
      "uk_advertising_standards_authority",
      "portman_group_code_of_practice"
    ],
    "policy_references": [
      {
        "policy_name": "UK Alcohol Advertising Standards",
        "policy_url": "https://www.asa.org.uk/codes-and-rulings/advertising-codes/broadcast-code/alcohol.html",
        "applies_to_markets": ["GB"]
      }
    ]
  },
  "permissioning": {
    "category_restrictions": ["alcohol_allowed_age_25_plus"],
    "age_verification_required": true,
    "geographic_restrictions": []
  }
}
```

#### Conceptual Mapping
OpenSignals category governance could feed into **AAMP's regulated category controls**:

- **Signal-level restrictions** (OpenSignals) inform **agent-level restrictions** (AAMP)
- **Policy binding** (OpenSignals) ensures agents respect category-specific rules
- **Audit trails** (both layers) provide regulatory compliance evidence

**Example Workflow for Alcohol Campaign**:
1. AAMP registers buyer agent with `category: alcohol` capability
2. Agent discovers signals via AdCP with OpenSignals extensions
3. OpenSignals verifies signal has `alcohol_allowed_age_25_plus` category restriction
4. OpenSignals binds UK alcohol policies to signal
5. AAMP requires human approval before agent activates signal
6. Both OpenSignals and AAMP log audit trails for regulatory reporting

### 3.4 Audit Trails and Accountability

#### AAMP Requirement
AAMP requires comprehensive **audit trails** for agent behavior including:
- What decisions were made
- When decisions were made
- Why decisions were made (reasoning)
- Who (agent or human) made the decision

#### OpenSignals Implementation
OpenSignals defines **signal usage audit events**:

```json
{
  "task": "audit_signal_usage",
  "event": {
    "event_type": "signal_activated",
    "timestamp": "2026-05-11T10:30:00Z",
    "signal_id": "outdoor-enthusiasts",
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
    "policy_bindings": ["alcohol_age_restriction", "uk_advertising_standards"],
    "reasoning": "Signal approved for contextual targeting after human review. Individual profiling disabled per alcohol policy."
  }
}
```

#### Conceptual Mapping
OpenSignals audit events could be integrated with **AAMP audit trails**:

```json
{
  "aamp_audit_event": {
    "event_type": "signal_activation",
    "timestamp": "2026-05-11T10:30:00Z",
    "agent_id": "media-optimizer-v2",
    "agent_action": "activate_signal",
    "opensignals_audit_id": "aud_789ghi",
    "signal_id": "outdoor-enthusiasts",
    "signal_trust_score": 0.87,
    "decision_mode": "approve_with_human",
    "human_approver": "jane.smith@brand.com",
    "policy_bindings": ["alcohol_age_restriction", "uk_advertising_standards"],
    "reasoning": "Signal approved for contextual targeting after human review.",
    "related_aamp_events": [
      "agent_discovery_event_123",
      "agent_verification_event_456"
    ]
  }
}
```

**Unified Audit Trail**:
- AAMP logs **agent-level events** (agent registered, agent discovered signals, agent requested approval)
- OpenSignals logs **signal-level events** (signal verified, signal scored, signal activated)
- Both systems cross-reference via `agent_id` and `signal_id`
- Regulators and auditors can query both layers for complete transparency

### 3.5 Trust Metadata and Transparency

#### AAMP Requirement
AAMP requires agents to provide **trust metadata** including:
- Agent capabilities and limitations
- Decision-making methodology
- Performance history
- Compliance certifications

#### OpenSignals Implementation
OpenSignals provides **signal trust metadata** with similar structure:

```json
{
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
  "transparency": {
    "explainability": "very_high",
    "explanation": "Full methodology documentation with transparent data sources...",
    "methodology_url": "https://example.com/methodology",
    "user_transparency_portal": "https://privacy.example.com/my-data"
  },
  "verification": {
    "verification_method": "third_party_audit",
    "third_party_auditor": "Media Rating Council",
    "certifications": ["MRC_Accredited", "TAG_Certified"]
  }
}
```

#### Conceptual Mapping
Signal trust metadata could complement agent trust metadata in a **unified trust model**:

```json
{
  "unified_trust_assessment": {
    "agent_trust": {
      "agent_id": "media-optimizer-v2",
      "agent_trust_score": 0.91,
      "agent_certifications": ["aamp_certified", "soc2_type2"]
    },
    "signal_trust": {
      "signal_id": "outdoor-enthusiasts",
      "signal_trust_score": 0.87,
      "signal_certifications": ["opensignals_v0.1_compliant"]
    },
    "combined_trust_assessment": {
      "overall_trust": 0.89,
      "reasoning": "High-trust agent using trusted signal with verified provenance and compliance",
      "recommendation": "approved_with_audit"
    }
  }
}
```

---

## 4. Practical Integration Scenarios

### 4.1 Scenario: Regulated Category Campaign (Alcohol)

**Context**: Premium spirits brand in UK market wants to run awareness campaign using autonomous agent.

**AAMP Layer**:
1. Register buyer agent with `category: alcohol` capability
2. Specify bounded autonomy: `human_approval_required_for: ["alcohol"]`
3. Configure audit trail retention: 365 days (regulatory requirement)

**OpenSignals Layer**:
1. Agent discovers signals via AdCP with OpenSignals extensions
2. Filter signals by `trust_band: highly_trusted` or `trusted`
3. Call `verify_signal` for each candidate signal with `category: alcohol`
4. Call `bind_signal_policy` to attach UK alcohol advertising policies
5. Signals requiring human approval trigger AAMP approval workflow
6. Approved signals are activated with full audit trail

**Outcome**: Compliant alcohol campaign with dual-layer governance (agent + signal) and complete audit trail.

### 4.2 Scenario: Privacy-Safe Contextual Targeting

**Context**: Brand wants fully autonomous contextual targeting without user tracking.

**AAMP Layer**:
1. Register buyer agent with `autonomy_level: full` for contextual signals
2. No human approval required for privacy-safe contextual signals

**OpenSignals Layer**:
1. Agent discovers contextual signals with `consent_scope: consent_not_required`
2. Verify signals have `individual_profiling_allowed: false`
3. Confirm `trust_band: highly_trusted`
4. Activate autonomously without human review
5. Optional audit logging for transparency

**Outcome**: Fast, autonomous contextual targeting with privacy-by-design and trust verification.

### 4.3 Scenario: Third-Party Data Quality Assessment

**Context**: Agent evaluates third-party modeled segment with limited provenance.

**AAMP Layer**:
1. Agent performs due diligence on data provider via AAMP registry
2. Check provider's agent card for certifications and trust metadata

**OpenSignals Layer**:
1. Retrieve signal manifest with provenance and quality scores
2. Trust score: 0.68 (limited trust band)
3. Provenance score: 0.61 (low - unknown data sources)
4. Decision mode: `approve_with_human` required
5. Governance agent flags quality concerns and recommends human review

**Outcome**: Low-quality signal identified and flagged for human assessment before potential rejection.

---

## 5. Alignment with AAMP Trust Principles

### 5.1 Transparency

**AAMP Principle**: Agents must provide transparent decision-making with explainable reasoning.

**OpenSignals Alignment**:
- Every trust score includes reasoning fields
- Manifests declare methodology and data sources
- Verification responses include decision reasoning
- Audit trails capture full context of signal usage

### 5.2 Accountability

**AAMP Principle**: Agent behavior must be auditable with clear accountability for decisions.

**OpenSignals Alignment**:
- Signal usage logged with agent ID, human approver, and timestamp
- Policy bindings recorded for regulatory compliance
- Audit retention matches regulatory requirements
- Cross-referencing between agent events and signal events

### 5.3 Bounded Autonomy

**AAMP Principle**: Agents operate within defined autonomy boundaries with human oversight where appropriate.

**OpenSignals Alignment**:
- Five decision modes from observe to autonomous_full
- Trust score thresholds trigger human approval
- Category-specific restrictions enforce human review
- Approval workflows integrate with governance agents

### 5.4 Governance

**AAMP Principle**: Brand policy and regulatory compliance must be enforced on agent behavior.

**OpenSignals Alignment**:
- Policy binding attaches brand rules to signals before activation
- Category restrictions prevent misuse of signals
- Compliance frameworks declared and verified
- Governance agents enforce rules through verification workflow

---

## 6. Benefits of AAMP + OpenSignals Integration

### 6.1 For Advertisers
- **Unified trust assessment** across both agents and signals
- **Stronger governance** with dual-layer controls
- **Better compliance** through comprehensive audit trails
- **Risk mitigation** through trust-based decision workflows

### 6.2 For Signal Providers
- **Trust differentiation** via standardized trust scores
- **AAMP registry presence** via agent card integration
- **Interoperability** with agentic advertising systems
- **Compliance demonstration** through manifest transparency

### 6.3 For Platforms and DSPs
- **Trust-aware signal activation** reduces compliance risk
- **Automated governance** through protocol integration
- **Audit trail export** for regulatory reporting
- **Differentiated inventory** through trust metadata

### 6.4 For Regulators
- **Complete transparency** from agent registration through signal activation
- **Auditable trails** with cross-referenced events
- **Compliance verification** through standardized metadata
- **Enforcement capability** via bounded autonomy controls

---

## 7. Implementation Considerations

### 7.1 Prerequisites

**AAMP Implementation Requirements**:
- Agent registry with identity management
- Bounded autonomy framework
- Audit trail infrastructure
- Approval workflow system

**OpenSignals Implementation Requirements**:
- Signal manifest publication
- Trust scoring calculation
- Verification endpoint
- Audit logging infrastructure

### 7.2 Integration Points

1. **Agent Registry**: Link signal provider agent cards to OpenSignals manifests
2. **Discovery Protocol**: Extend AdCP responses with OpenSignals metadata
3. **Governance Layer**: Connect AAMP approval workflows with OpenSignals verification
4. **Audit Infrastructure**: Cross-reference AAMP and OpenSignals audit events
5. **Trust Assessment**: Combine agent trust scores with signal trust scores

### 7.3 Governance Coordination

- **Policy Definition**: Brand policy owners define rules enforced by both layers
- **Approval Workflows**: AAMP approval workflows trigger OpenSignals verification
- **Audit Reporting**: Unified audit reports combine agent and signal events
- **Compliance Frameworks**: Shared compliance framework references (GDPR, CCPA, etc.)

---

## 8. Future Opportunities

### 8.1 Formal Integration Specification

This conceptual mapping could evolve into a **formal integration specification** through:
- IAB Tech Lab AAMP working group collaboration
- Joint protocol development between AAMP and OpenSignals communities
- Standardized extension fields in AAMP agent cards for OpenSignals
- Certified implementation guidelines

### 8.2 Federated Trust Registries

AAMP and OpenSignals could collaborate on **federated trust registries** enabling:
- Cross-platform trust score sharing
- Unified trust assessment APIs
- Trust score aggregation across multiple signals
- Decentralized trust verification

### 8.3 AI-Driven Trust Optimization

Combined AAMP + OpenSignals data could enable:
- Machine learning models predicting signal performance
- Automated trust score adjustments based on outcomes
- Anomaly detection for quality degradation
- Dynamic trust threshold optimization

---

## 9. Conclusion

The **OpenSignals Protocol** and **AAMP Trust and Transparency pillar** are highly complementary:

- **AAMP** provides the agent-level trust framework (identity, registration, governance, audit)
- **OpenSignals** provides the signal-level trust verification layer (manifests, scoring, verification, audit)
- **Together**, they enable trustworthy agentic advertising with dual-layer governance

This conceptual mapping demonstrates natural alignment and integration opportunities. While not an official specification, it provides a foundation for future formal collaboration between the AAMP and OpenSignals communities.

---

## 10. References

### AAMP Resources
- **IAB Tech Lab AAMP**: [https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/](https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/)
- **AAMP Agent Registry Specification**: *(Refer to AAMP documentation)*
- **AAMP Trust Framework**: *(Refer to AAMP documentation)*

### OpenSignals Resources
- **OpenSignals Protocol v0.1**: `opensignals-v0.1.md`
- **OpenSignals GitHub**: [https://github.com/opensignals-protocol/opensignals-protocol](https://github.com/opensignals-protocol/opensignals-protocol)
- **Conformance Specification**: `conformance.md`

### Related Standards
- **AdCP (Ad Context Protocol)**: [https://adcontextprotocol.org/](https://adcontextprotocol.org/)
- **OpenRTB**: [https://github.com/InteractiveAdvertisingBureau/openrtb2.x](https://github.com/InteractiveAdvertisingBureau/openrtb2.x)
- **AdCOM**: [https://github.com/InteractiveAdvertisingBureau/AdCOM](https://github.com/InteractiveAdvertisingBureau/AdCOM)

---

**Document Status**: Conceptual Integration Design
**Version**: 0.1
**Last Updated**: May 2026
**Authors**: OpenSignals Protocol Community
**License**: Creative Commons Attribution 4.0 International (CC BY 4.0)

**Feedback Welcome**: This is a conceptual design document intended to stimulate discussion. Feedback from the AAMP working group and IAB Tech Lab community is welcomed through the OpenSignals GitHub repository.
