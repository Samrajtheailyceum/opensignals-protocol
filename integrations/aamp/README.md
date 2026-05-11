# OpenSignals + AAMP Integration

This directory contains documentation for integrating OpenSignals Protocol with [IAB Tech Lab's Agentic Advertising Management Protocols (AAMP)](https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/).

## Overview

AAMP is the IAB Tech Lab's comprehensive framework for agentic advertising, built on three pillars:

1. **Foundations (ARTF)**: Agent Registry and Trust Framework
2. **Protocols**: Communication and transaction protocols
3. **Trust and Transparency**: Verification, auditing, and compliance

OpenSignals specifically addresses the **Trust and Transparency pillar** by providing machine-readable signal trust metadata and verification workflows.

## Conceptual Mapping

OpenSignals complements AAMP's trust goals with a practical implementation framework:

```
┌─────────────────────────────────────────────────────┐
│              AAMP Framework (IAB Tech Lab)          │
├─────────────────────────────────────────────────────┤
│  Pillar 1: Foundations (ARTF)                       │
│  - Agent Registry                                   │
│  - Trust Framework                                  │
│  - Identity and Authentication                      │
└───────────────────┬─────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────┐
│  Pillar 2: Protocols                                │
│  - Signal Discovery (AdCP, etc.)                    │
│  - Inventory Access                                 │
│  - Transaction Management                           │
└───────────────────┬─────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────┐
│  Pillar 3: Trust and Transparency                   │
│  ┌───────────────────────────────────────────────┐ │
│  │    OpenSignals Protocol (Trust Layer)        │ │
│  │  - Signal Verification                        │ │
│  │  - Trust Scoring                              │ │
│  │  - Policy Binding                             │ │
│  │  - Audit Trails                               │ │
│  └───────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

## AAMP Trust Layer Requirements

AAMP defines several trust and transparency requirements that OpenSignals addresses:

### 1. Signal Provenance Tracking

**AAMP Requirement**: Agents must be able to trace the origin and lineage of signals.

**OpenSignals Implementation**: The `provenance` object in signal manifests provides:
- Data source declarations
- Collection methods
- Processing history
- Last updated timestamps
- Data lineage documentation

Example:

```json
{
  "provenance": {
    "data_sources": ["first_party_behavioral", "survey"],
    "collection_method": "opt_in_panel",
    "processing_steps": [
      "deduplication",
      "quality_filtering",
      "demographic_modeling"
    ],
    "last_updated": "2026-05-10T08:00:00Z",
    "update_frequency": "daily",
    "lineage_documentation": "https://provider.com/data-lineage/signal-123"
  }
}
```

### 2. Permission and Consent Verification

**AAMP Requirement**: Verify that signal usage is properly permissioned and consented.

**OpenSignals Implementation**: The `permissioning` object provides:
- Consent basis declarations
- Usage rights and restrictions
- Territorial and category limitations
- Data sharing permissions

Example:

```json
{
  "permissioning": {
    "consent_basis": "legitimate_interest",
    "usage_rights": ["targeting", "measurement", "optimization"],
    "restrictions": {
      "prohibited_uses": ["individual_profiling"],
      "geographic_restrictions": ["CN", "RU"],
      "category_restrictions": ["alcohol", "gambling"]
    },
    "data_sharing_allowed": false,
    "privacy_policy_url": "https://provider.com/privacy"
  }
}
```

### 3. Signal Quality Assessment

**AAMP Requirement**: Agents need objective measures of signal quality and reliability.

**OpenSignals Implementation**: Multi-dimensional quality scoring:

```json
{
  "quality": {
    "overall_trust_score": 0.87,
    "coverage_score": 0.82,
    "freshness_score": 0.91,
    "precision_score": 0.85,
    "explainability_score": 0.89,
    "outcome_relevance_score": 0.84,
    "compliance_safety_score": 0.95
  }
}
```

### 4. Audit and Accountability

**AAMP Requirement**: Comprehensive audit trails for signal usage and outcomes.

**OpenSignals Implementation**: Structured audit logging:

```json
{
  "signal_id": "audience-signal-123",
  "audit_timestamp": "2026-05-11T14:00:00Z",
  "agent_id": "buyer-agent-456",
  "brand": "premium-brand-co",
  "campaign_id": "campaign-789",
  "usage_context": {
    "intended_use": "audience_targeting",
    "market": "US",
    "category": "general"
  },
  "verification_result": {
    "verified": true,
    "trust_score": 0.87,
    "policy_bindings": ["brand_safety_standard"]
  },
  "human_approval": {
    "required": false,
    "obtained": false
  },
  "outcome_metrics": {
    "impressions": 1000000,
    "clicks": 15000,
    "conversions": 500
  }
}
```

### 5. Compliance and Regulatory Adherence

**AAMP Requirement**: Ensure compliance with advertising regulations and standards.

**OpenSignals Implementation**: Compliance flags and policy bindings:

```json
{
  "compliance": {
    "regulatory_frameworks": [
      "gdpr",
      "ccpa",
      "uk_advertising_standards"
    ],
    "industry_certifications": [
      "iab_gold_standard",
      "trustworthy_accountability_group"
    ],
    "brand_safety_verified": true,
    "last_compliance_audit": "2026-04-01T00:00:00Z"
  }
}
```

## Integration with AAMP Components

### ARTF (Agent Registry and Trust Framework)

OpenSignals manifests can reference ARTF agent identities:

```json
{
  "owner": {
    "organization": "Example Data Co",
    "artf_agent_id": "urn:artf:agent:example-data-co",
    "artf_trust_level": "verified",
    "contact": "signals@example.com"
  },
  "provider": {
    "name": "Example Data Co",
    "artf_agent_id": "urn:artf:agent:example-data-co",
    "url": "https://example.com"
  }
}
```

### AAMP Protocol Layer

OpenSignals verification can be invoked within AAMP protocol workflows:

```
1. Agent discovers signal via AAMP-compliant protocol
2. Agent fetches OpenSignals manifest
3. Agent verifies signal against brand policy (OpenSignals)
4. Agent activates signal via AAMP transaction protocol
5. Agent logs usage via OpenSignals audit API
6. Agent submits outcome feedback (OpenSignals)
```

### AAMP Trust and Transparency Pillar

OpenSignals implements specific trust capabilities:

| AAMP Trust Capability | OpenSignals Implementation |
|----------------------|---------------------------|
| Signal provenance tracking | `provenance` object in manifest |
| Permission verification | `permissioning` object and `verify_signal` API |
| Quality assessment | Multi-dimensional trust scoring |
| Audit trails | `audit_signal_usage` API and audit schemas |
| Compliance verification | `compliance` flags and policy binding |
| Human oversight | `human_approval_required` flags |
| Outcome tracking | `submit_signal_outcome_feedback` API |

## Practical Example: AAMP-Compliant Workflow

### Scenario
A brand wants to run a regulated alcohol campaign using AAMP-compliant agents.

### Step-by-Step Workflow

#### 1. Agent Authentication (ARTF)
Buyer agent authenticates via AAMP ARTF:

```
GET /artf/register
Authorization: Bearer {token}

{
  "agent_id": "buyer-agent-premium-spirits",
  "agent_type": "buyer",
  "organization": "Premium Spirits Agency",
  "trust_level": "verified"
}
```

#### 2. Signal Discovery (AAMP Protocol)
Agent discovers signals via AAMP-compliant protocol:

```
GET /signals?category=alcohol&market=GB&signal_type=contextual

{
  "signals": [
    {
      "signal_id": "premium-spirits-context-uk",
      "name": "Premium Spirits Context",
      "opensignals_manifest": "https://provider.com/.well-known/opensignals/premium-spirits-context-uk"
    }
  ]
}
```

#### 3. Trust Verification (OpenSignals)
Agent verifies signal trust:

```
POST /opensignals/verify

{
  "signal_id": "premium-spirits-context-uk",
  "brand": "premium-spirits-co",
  "market": "GB",
  "category": "alcohol",
  "intended_use": "contextual_targeting"
}

Response:
{
  "decision": "approved_with_conditions",
  "trust_score": 0.91,
  "conditions": ["human_approval_required", "audit_required"],
  "policy_bindings": ["uk_alcohol_code", "responsible_drinking"]
}
```

#### 4. Human Approval (AAMP Governance)
For regulated categories, human approval is required per AAMP guidelines.

#### 5. Signal Activation (AAMP Protocol)
Agent activates signal via AAMP transaction protocol:

```
POST /aamp/activate

{
  "signal_id": "premium-spirits-context-uk",
  "campaign_id": "holiday-whisky-2026",
  "artf_agent_id": "buyer-agent-premium-spirits",
  "opensignals_verification": {
    "verified": true,
    "trust_score": 0.91,
    "human_approved": true
  }
}
```

#### 6. Audit Trail (OpenSignals)
Usage is logged for AAMP transparency requirements:

```
POST /opensignals/audit

{
  "signal_id": "premium-spirits-context-uk",
  "agent_id": "buyer-agent-premium-spirits",
  "campaign_id": "holiday-whisky-2026",
  "brand": "premium-spirits-co",
  "activation_timestamp": "2026-05-15T10:00:00Z",
  "policy_bindings": ["uk_alcohol_code"],
  "human_approved": true
}
```

#### 7. Outcome Feedback (OpenSignals)
Campaign results feed back into trust scoring:

```
POST /opensignals/outcome_feedback

{
  "signal_id": "premium-spirits-context-uk",
  "campaign_id": "holiday-whisky-2026",
  "outcome_metrics": {
    "impressions": 500000,
    "clicks": 7500,
    "conversions": 250,
    "ctr": 0.015,
    "conversion_rate": 0.033
  },
  "outcome_assessment": "exceeded_expectations"
}
```

## AAMP Compliance Checklist

Organizations implementing OpenSignals to meet AAMP trust requirements should:

### Signal Providers
- [ ] Publish OpenSignals manifests for all signals
- [ ] Include ARTF agent IDs in manifest metadata
- [ ] Document provenance and data lineage
- [ ] Declare consent basis and permissions clearly
- [ ] Provide quality scores and update frequencies
- [ ] Maintain compliance with AAMP audit requirements

### Demand-Side Platforms and Agencies
- [ ] Verify signals using OpenSignals before activation
- [ ] Check trust scores against brand policies
- [ ] Obtain human approval for regulated categories
- [ ] Log signal usage via OpenSignals audit APIs
- [ ] Submit outcome feedback to improve trust models
- [ ] Integrate with ARTF for agent authentication

### Governance and Compliance Systems
- [ ] Define brand policies compatible with OpenSignals
- [ ] Implement verification workflows for AAMP trust checks
- [ ] Create approval processes for low-trust signals
- [ ] Build audit dashboards meeting AAMP transparency standards
- [ ] Monitor compliance across all signal usage

## Implementation Guidance

### Trust Score Alignment with AAMP

AAMP emphasizes multi-dimensional trust. OpenSignals trust scores should be interpreted as:

- **0.90 - 1.00**: High trust (AAMP "verified" level)
- **0.75 - 0.89**: Moderate trust (AAMP "validated" level)
- **0.50 - 0.74**: Limited trust (requires human review per AAMP)
- **0.00 - 0.49**: Low trust (block or escalate per AAMP guidelines)

### Policy Binding Best Practices

When binding brand policies to signals:

1. Reference specific AAMP compliance frameworks
2. Include relevant regulatory standards (GDPR, CCPA, etc.)
3. Document any restrictions or special handling requirements
4. Ensure policies are machine-readable and agent-executable

### Audit Trail Requirements

AAMP requires comprehensive audit trails. OpenSignals audit records should include:

- ARTF agent IDs for all parties
- Timestamps (ISO 8601 format)
- Verification decisions and trust scores
- Human approval records (where applicable)
- Outcome metrics and performance data
- Policy bindings and compliance flags

## Technical Specifications

### Manifest Format Extensions for AAMP

OpenSignals manifests can be extended with AAMP-specific metadata:

```json
{
  "protocol": "opensignals",
  "version": "0.1",
  "aamp_integration": {
    "artf_agent_id": "urn:artf:agent:provider-123",
    "aamp_compliant": true,
    "aamp_version": "1.0",
    "trust_pillar_coverage": [
      "provenance_tracking",
      "permission_verification",
      "quality_assessment",
      "audit_trails",
      "compliance_verification"
    ]
  }
}
```

### API Endpoints for AAMP Integration

OpenSignals implementations supporting AAMP should expose:

- `GET /.well-known/opensignals/{signal_id}`: Manifest retrieval
- `POST /opensignals/verify`: Trust verification with ARTF agent context
- `POST /opensignals/audit`: Audit logging with AAMP metadata
- `POST /opensignals/outcome_feedback`: Performance feedback

## Resources

- **AAMP Overview**: https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/
- **IAB Tech Lab**: https://iabtechlab.com/
- **OpenSignals Specification**: [../../specs/opensignals-v0.1.md](../../specs/opensignals-v0.1.md)
- **AAMP Trust Layer Mapping**: [aamp-trust-layer-mapping.md](aamp-trust-layer-mapping.md)

## Status and Disclaimer

**Status**: Conceptual Integration (Draft)

This integration guide represents a conceptual mapping between OpenSignals Protocol and AAMP. It is:

- **Not officially endorsed** by IAB Tech Lab
- **Not part of the AAMP specification** (as of May 2026)
- **A proposed implementation pattern** for addressing AAMP trust requirements
- **Subject to change** as AAMP evolves

Organizations implementing AAMP should consult official IAB Tech Lab documentation and guidance.

## Support and Questions

- **GitHub Issues**: https://github.com/Samrajtheailyceum/opensignals-protocol/issues
- **Label**: Use `aamp-integration` label for AAMP-specific questions
- **Discussions**: https://github.com/Samrajtheailyceum/opensignals-protocol/discussions

## Contributing

We welcome feedback on the AAMP integration pattern. If you are involved with AAMP development or implementation, your input is especially valuable. See [../../CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

---

**Last Updated**: 2026-05-11
