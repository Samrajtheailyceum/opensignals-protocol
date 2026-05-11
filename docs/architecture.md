# OpenSignals Protocol Architecture

**Version**: 0.1
**Status**: Draft
**Last Updated**: May 2026

---

## Overview

This document explains the OpenSignals Protocol architecture, including its position in the advertising technology stack, the protocol layer model, and the complete workflow from signal discovery to audit and feedback.

---

## Protocol Layer Model

OpenSignals operates as a trust verification layer that sits between signal discovery protocols (like AdCP) and execution platforms (like OpenRTB, OpenDirect). It does not replace existing infrastructure; instead, it adds standardized trust metadata and governance controls.

### The Four-Layer Stack

```
┌─────────────────────────────────────────────────────────────────┐
│                      Brand Policy Layer                          │
│                                                                   │
│  • Brand safety rules and compliance requirements                │
│  • Category restrictions (alcohol, gambling, pharma, finance)    │
│  • Market-specific regulations (GDPR, CCPA, age restrictions)    │
│  • Human approval workflows for regulated categories             │
│  • Trust score thresholds and bounded autonomy settings          │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
                               ▲
                               │ Brand policy enforcement
                               │ Approval workflows
                               │
┌─────────────────────────────────────────────────────────────────┐
│                    OpenSignals Protocol                          │
│               (Trust Verification & Governance)                  │
│                                                                   │
│  • Trust scoring across 7 dimensions                             │
│  • Signal verification (validity, permissioning, freshness)      │
│  • Provenance tracking and chain of custody                      │
│  • Policy binding (attach brand rules to signals)                │
│  • Audit trail (record usage with full context)                  │
│  • Bounded autonomy controls                                     │
│  • Outcome feedback loops                                        │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
                               ▲
                               │ Signal manifests
                               │ Trust metadata
                               │
┌─────────────────────────────────────────────────────────────────┐
│                 Signal Discovery Layer (AdCP)                    │
│                                                                   │
│  • get_signals: Discover available signals                       │
│  • activate_signal: Activate signals after trust verification    │
│  • Signal catalogs and search                                    │
│  • Coverage, pricing, and availability information               │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
                               ▲
                               │ Bid requests
                               │ Activation commands
                               │
┌─────────────────────────────────────────────────────────────────┐
│               Execution Layer (AAMP ARTF)                        │
│                                                                   │
│  • OpenRTB: Real-time bidding auctions                           │
│  • OpenDirect: Direct buying workflows                           │
│  • DSP/SSP platforms: Demand and supply-side execution           │
│  • Ad servers: Creative serving and tracking                     │
│  • Measurement platforms: Attribution and performance            │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### Layer Responsibilities

#### Brand Policy Layer
The top layer defines brand-specific rules, compliance requirements, and governance constraints. This layer is configured by brand policy owners (advertisers, agencies, legal teams) and enforced by governance agents.

**Key responsibilities:**
- Define which categories are allowed (e.g., no alcohol, no gambling)
- Set geographic restrictions based on market regulations
- Configure trust score thresholds for autonomous activation
- Define approval workflows for regulated categories
- Maintain brand safety blocklists and allowlists

#### OpenSignals Protocol Layer
The trust verification layer provides standardized mechanisms for assessing signal trustworthiness before activation. This layer is implemented by governance agents, signal providers, and audit agents.

**Key responsibilities:**
- Publish OpenSignal Manifests with trust metadata
- Verify signals against brand policy and compliance rules
- Score signals across provenance, permissioning, freshness, quality, explainability, outcome relevance, and compliance dimensions
- Bind brand policies to signals before activation
- Record audit trails with full context
- Manage bounded autonomy controls
- Process outcome feedback to improve trust scores

#### Signal Discovery Layer (AdCP)
The discovery layer enables agents to find, evaluate, and activate signals. AdCP provides the standard interface; OpenSignals extends it with trust metadata.

**Key responsibilities:**
- Catalog available signals with coverage and pricing
- Provide signal search and filtering
- Enable signal discovery through get_signals
- Execute signal activation through activate_signal
- Optionally include OpenSignals trust metadata in responses

#### Execution Layer (AAMP ARTF)
The execution layer handles the actual media buying, serving, and measurement. This layer uses signals that have been discovered and verified through the upper layers.

**Key responsibilities:**
- Execute real-time bidding through OpenRTB
- Process direct buying orders through OpenDirect
- Serve creative and track impressions
- Measure attribution and campaign performance
- Log signal usage for audit trails

---

## OpenSignals Position in the Stack

OpenSignals sits **between discovery and activation**, providing a trust checkpoint before signals flow into execution platforms.

### Without OpenSignals

```
Signal Discovery → Signal Activation → Execution
     (AdCP)              (AdCP)         (OpenRTB)

Problem: No standardized trust verification
         No governance checkpoint
         No audit trail
         Risk of activating low-quality or non-compliant signals
```

### With OpenSignals

```
Signal Discovery → Trust Verification → Signal Activation → Execution
     (AdCP)          (OpenSignals)           (AdCP)         (OpenRTB)

Benefit: Standardized trust assessment
         Governance checkpoint before activation
         Complete audit trail
         Bounded autonomy controls
         Outcome feedback loops
```

---

## Complete Workflow

The OpenSignals workflow follows six stages: Discovery, Trust Verification, Governance, Activation, Audit, and Feedback.

### Stage 1: Discovery

**Actor**: Buyer Agent
**Goal**: Find signals relevant to campaign objectives

```
┌──────────────┐
│ Brand Brief  │  Campaign: Premium cocktail recipes
│              │  Market: Great Britain
└──────┬───────┘  Category: Alcohol
       │          Objective: Drive brand awareness
       ▼
┌──────────────────────────────┐
│ Buyer Agent                  │
│ Calls: AdCP get_signals      │
│                              │
│ Request:                     │
│ - Objective: brand_awareness │
│ - Category: alcohol          │
│ - Market: GB                 │
│ - Budget: £150,000           │
└──────┬───────────────────────┘
       │
       ▼
┌────────────────────────────────────┐
│ Signal Provider (AdCP)             │
│ Returns signals with OpenSignals   │
│ metadata:                          │
│                                    │
│ Signal: premium-cocktail-contexts  │
│ - Coverage: 45M                    │
│ - CPM: £4.50-£12.00                │
│ - Trust Score: 0.88                │
│ - Manifest URL: [...]              │
│ - Verification Required: Yes       │
│ - Category: regulated/alcohol      │
└────────────────────────────────────┘
```

### Stage 2: Trust Verification

**Actor**: Governance Agent
**Goal**: Verify signal is valid, permissioned, and compliant

```
┌─────────────────────────────────┐
│ Buyer Agent                     │
│ Calls: OpenSignals              │
│        get_signal_manifest      │
│                                 │
│ Request: premium-cocktail-      │
│          contexts               │
└──────┬──────────────────────────┘
       │
       ▼
┌────────────────────────────────────────┐
│ Signal Provider                        │
│ Returns: OpenSignal Manifest           │
│                                        │
│ {                                      │
│   "signal_id": "premium-cocktail-...", │
│   "signal_type": "contextual",         │
│   "category": "regulated/alcohol",     │
│   "quality": {                         │
│     "overall_trust_score": 0.88,       │
│     "provenance_score": 0.92,          │
│     "permissioning_score": 0.85,       │
│     "freshness_score": 0.95            │
│   },                                   │
│   "governance": {                      │
│     "human_approval_required": true,   │
│     "audit_required": true,            │
│     "market_restrictions": {...}       │
│   },                                   │
│   "provenance": {                      │
│     "data_sources": ["contextual"],    │
│     "collection_method": "nlp",        │
│     "chain_of_custody": [...]          │
│   }                                    │
│ }                                      │
└────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────┐
│ Buyer Agent                     │
│ Calls: OpenSignals verify_signal│
│                                 │
│ Request:                        │
│ - signal_id: premium-cocktail-  │
│   contexts                      │
│ - brand: premium-spirits-co     │
│ - market: GB                    │
│ - category: alcohol             │
│ - use_case: contextual_targeting│
└──────┬──────────────────────────┘
       │
       ▼
┌────────────────────────────────────────┐
│ Governance Agent                       │
│ Performs verification checks:          │
│                                        │
│ ✓ Market: GB is allowed                │
│ ✓ Category: Alcohol permitted for      │
│   contextual targeting                 │
│ ✓ Age restriction: 18+ in GB           │
│ ✓ Trust score: 0.88 (Trusted)          │
│ ✓ Provenance: Verified contextual      │
│ ✓ Permissioning: No individual         │
│   profiling (compliant)                │
│ ⚠ Human approval required (regulated   │
│   category)                            │
│                                        │
│ Returns:                               │
│ {                                      │
│   "decision": "approved_with_          │
│                conditions",            │
│   "trust_score": 0.88,                 │
│   "conditions": [                      │
│     "human_approval_required",         │
│     "audit_required",                  │
│     "no_individual_profiling"          │
│   ],                                   │
│   "policy_bindings": [                 │
│     "alcohol_age_restriction_gb",      │
│     "uk_cap_code_compliance"           │
│   ]                                    │
│ }                                      │
└────────────────────────────────────────┘
```

### Stage 3: Governance

**Actor**: Governance Agent + Human Approver
**Goal**: Apply brand policy and obtain human approval if required

```
┌─────────────────────────────────┐
│ Governance Agent                │
│ Calls: OpenSignals              │
│        bind_signal_policy       │
│                                 │
│ Request:                        │
│ - signal_id: premium-cocktail-  │
│   contexts                      │
│ - brand: premium-spirits-co     │
│ - policies:                     │
│   - alcohol_age_restriction_gb  │
│   - uk_cap_code_compliance      │
│   - no_individual_profiling     │
└──────┬──────────────────────────┘
       │
       ▼
┌────────────────────────────────────────┐
│ Governance Agent                       │
│ Returns: Policy Bindings               │
│                                        │
│ {                                      │
│   "bindings": [                        │
│     {                                  │
│       "policy_id": "alcohol_age_       │
│                     restriction_gb",   │
│       "enforcement_level": "mandatory",│
│       "parameters": {                  │
│         "minimum_age": 18,             │
│         "age_verification": "required" │
│       }                                │
│     },                                 │
│     {                                  │
│       "policy_id": "uk_cap_code",      │
│       "enforcement_level": "mandatory",│
│       "parameters": {                  │
│         "no_youth_appeal": true,       │
│         "responsible_messaging": true  │
│       }                                │
│     }                                  │
│   ]                                    │
│ }                                      │
└────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────┐
│ Human Approval Workflow         │
│                                 │
│ Notification sent to:           │
│ - Brand Manager                 │
│ - Legal/Compliance Officer      │
│                                 │
│ Approval request includes:      │
│ - Signal manifest               │
│ - Trust score breakdown         │
│ - Verification decision         │
│ - Policy bindings               │
│ - Campaign context              │
│                                 │
│ Approver reviews and approves:  │
│ ✓ Approved for activation       │
│   Signed by: Jane Smith         │
│   Role: Compliance Officer      │
│   Timestamp: 2026-05-11T10:30Z  │
└─────────────────────────────────┘
```

### Stage 4: Activation

**Actor**: Buyer Agent + Execution Platform
**Goal**: Activate signal with bound policies and audit logging

```
┌─────────────────────────────────┐
│ Buyer Agent                     │
│ Calls: AdCP activate_signal     │
│                                 │
│ Request:                        │
│ - signal_id: premium-cocktail-  │
│   contexts                      │
│ - campaign_id: cocktail-2026-q2 │
│ - budget: £150,000              │
│ - opensignals_context:          │
│   - trust_score: 0.88           │
│   - policy_bindings: [...]      │
│   - approval_id: approval-12345 │
│   - audit_required: true        │
└──────┬──────────────────────────┘
       │
       ▼
┌────────────────────────────────────────┐
│ Execution Platform (DSP)               │
│                                        │
│ Receives activation request with       │
│ OpenSignals context                    │
│                                        │
│ Enforces mandatory policies:           │
│ ✓ Age restriction: 18+ targeting only  │
│ ✓ No individual profiling              │
│ ✓ Content adjacency: Premium contexts  │
│   only                                 │
│                                        │
│ Activates signal in OpenRTB bid stream │
│ Campaign: cocktail-2026-q2             │
│ Contexts: premium-cocktail-contexts    │
│ Spend: £150,000                        │
│ Duration: 30 days                      │
└────────────────────────────────────────┘
```

### Stage 5: Audit

**Actor**: Audit Agent
**Goal**: Record signal usage with full context for accountability

```
┌─────────────────────────────────┐
│ Execution Platform              │
│ Calls: OpenSignals              │
│        audit_signal_usage       │
│                                 │
│ Request:                        │
│ {                               │
│   "signal_id": "premium-        │
│                cocktail-...",   │
│   "brand": "premium-spirits-co",│
│   "campaign_id": "cocktail-     │
│                  2026-q2",      │
│   "buyer_agent": "media-bot-v2",│
│   "governance_agent": "policy-  │
│                        engine-1",│
│   "decision_mode": "approve_    │
│                     with_human",│
│   "trust_score": 0.88,          │
│   "use_case": "contextual_      │
│                targeting",      │
│   "platform": "dsp-example",    │
│   "geographic_scope": ["GB"],   │
│   "category": "alcohol",        │
│   "approval_id": "approval-     │
│                   12345",       │
│   "policy_bindings": [...],     │
│   "activation_timestamp": "...  │
│                             Z", │
│   "spend_allocated": 150000     │
│ }                               │
└──────┬──────────────────────────┘
       │
       ▼
┌────────────────────────────────────────┐
│ Audit Agent                            │
│                                        │
│ Records audit event in tamper-evident  │
│ audit trail                            │
│                                        │
│ Returns:                               │
│ {                                      │
│   "audit_id": "audit-67890",           │
│   "status": "logged",                  │
│   "retention_until": "2026-08-09T...", │
│   "audit_endpoint": "https://audit.    │
│                      example.com/..."  │
│ }                                      │
│                                        │
│ Audit trail includes:                  │
│ - Who: media-bot-v2, policy-engine-1,  │
│   Jane Smith (approver)                │
│ - What: premium-cocktail-contexts      │
│ - When: 2026-05-11T10:45:00Z           │
│ - Where: Great Britain                 │
│ - Why: Brand awareness, alcohol        │
│   campaign                             │
│ - How: Contextual targeting only       │
│ - Under what policy: UK CAP Code,      │
│   age 18+                              │
│ - Trust score: 0.88                    │
│ - Human approval: Yes (approval-12345) │
└────────────────────────────────────────┘
```

### Stage 6: Feedback

**Actor**: Buyer Agent + Measurement Platform
**Goal**: Feed campaign outcomes back into trust scoring

```
┌─────────────────────────────────┐
│ Campaign runs for 30 days       │
│                                 │
│ Performance metrics:            │
│ - Impressions: 12M              │
│ - Reach: 3.2M unique users      │
│ - Brand lift: +8.5%             │
│ - Purchase intent lift: +12.3%  │
│ - Viewability: 78%              │
│ - Invalid traffic: 0.3%         │
└──────┬──────────────────────────┘
       │
       ▼
┌─────────────────────────────────┐
│ Buyer Agent                     │
│ Calls: OpenSignals              │
│   submit_signal_outcome_feedback│
│                                 │
│ Request:                        │
│ {                               │
│   "signal_id": "premium-        │
│                cocktail-...",   │
│   "campaign_id": "cocktail-     │
│                  2026-q2",      │
│   "outcome_metrics": {          │
│     "brand_lift": 0.085,        │
│     "purchase_intent_lift":     │
│       0.123,                    │
│     "reach_accuracy": 0.94,     │
│     "viewability": 0.78,        │
│     "invalid_traffic": 0.003    │
│   },                            │
│   "quality_assessment": {       │
│     "met_expectations": true,   │
│     "accuracy_rating": 0.91,    │
│     "would_use_again": true     │
│   },                            │
│   "compliance_assessment": {    │
│     "policy_violations": 0,     │
│     "brand_safety_incidents": 0 │
│   }                             │
│ }                               │
└──────┬──────────────────────────┘
       │
       ▼
┌────────────────────────────────────────┐
│ Signal Provider / Governance Agent     │
│                                        │
│ Updates trust scores based on feedback:│
│                                        │
│ Previous scores:                       │
│ - Overall: 0.88                        │
│ - Outcome relevance: 0.78              │
│ - Quality: 0.87                        │
│                                        │
│ Updated scores (after feedback):       │
│ - Overall: 0.89 (+0.01)                │
│ - Outcome relevance: 0.82 (+0.04)      │
│ - Quality: 0.88 (+0.01)                │
│                                        │
│ Returns:                               │
│ {                                      │
│   "feedback_id": "feedback-11223",     │
│   "status": "processed",               │
│   "trust_score_updated": true,         │
│   "new_overall_score": 0.89            │
│ }                                      │
└────────────────────────────────────────┘
```

---

## Key Architectural Principles

### 1. Layered Independence

Each layer operates independently and can evolve without breaking other layers. OpenSignals does not require changes to AdCP, OpenRTB, or execution platforms to function.

### 2. Trust Checkpoint Pattern

OpenSignals implements a checkpoint pattern: signals must pass through trust verification before activation. This ensures governance controls are enforced consistently.

### 3. Manifest-Driven Architecture

All trust metadata is declared in machine-readable OpenSignal Manifests. Manifests are versioned, auditable, and can be cryptographically signed for verification.

### 4. Agent Separation of Concerns

OpenSignals defines three distinct agent roles:
- **Buyer Agents**: Discover and activate signals
- **Governance Agents**: Verify trust and enforce policy
- **Audit Agents**: Record usage and maintain accountability

This separation ensures checks and balances.

### 5. Bounded Autonomy by Design

Human oversight is built into the architecture through decision modes ranging from full human control (observe) to full autonomy (autonomous_full). Decision mode is determined by trust score, category, and brand policy.

### 6. Feedback Loops for Continuous Improvement

Outcome feedback flows back to signal providers and governance agents, enabling trust scores to improve over time based on real-world performance.

### 7. Protocol Extensibility

OpenSignals is designed to be extended:
- Custom signal types can be defined
- Custom trust dimensions can be added
- Custom policy types can be registered
- Integration with future protocols (MCP, A2A) is supported

---

## Integration Points

### With AdCP

OpenSignals extends AdCP by adding trust metadata to `get_signals` responses and trust verification before `activate_signal` calls.

**AdCP without OpenSignals:**
```
get_signals → activate_signal
```

**AdCP with OpenSignals:**
```
get_signals (includes OpenSignals metadata)
  ↓
get_signal_manifest (retrieve full trust context)
  ↓
verify_signal (check trust and compliance)
  ↓
bind_signal_policy (attach brand rules)
  ↓
[human approval if required]
  ↓
activate_signal (with OpenSignals context)
  ↓
audit_signal_usage (record activation)
  ↓
submit_signal_outcome_feedback (after campaign)
```

### With OpenRTB/OpenDirect

OpenSignals trust scores and policy bindings can be included in OpenRTB bid requests or OpenDirect orders as extensions. Execution platforms can enforce mandatory policies and log activations to audit endpoints.

### With AAMP

OpenSignals implements the Trust and Transparency pillar of AAMP, providing practical mechanisms for signal-level trust verification that complement AAMP's broader agent runtime framework.

### With MCP/A2A

OpenSignals tasks can be exposed as MCP resources or A2A skills, enabling LLM-based agents to query signal trust through standardized agent communication protocols.

---

## Deployment Models

### Centralized Governance

A single governance agent verifies all signals for a brand across all buyer agents and platforms.

**Advantages:**
- Consistent policy enforcement
- Single audit trail
- Simplified compliance reporting

**Use cases:**
- Large enterprises with centralized legal/compliance teams
- Regulated categories requiring strict oversight
- Multi-platform campaigns requiring unified governance

### Distributed Governance

Each platform or buyer agent implements its own governance checks using brand policy specifications.

**Advantages:**
- No single point of failure
- Lower latency (local verification)
- Platform-specific customization

**Use cases:**
- Decentralized organizations
- High-volume, low-risk campaigns
- Agencies managing multiple clients

### Hybrid Model

Critical decisions (regulated categories, low trust scores) flow through centralized governance; routine decisions are handled locally.

**Advantages:**
- Balance between control and efficiency
- Scales better than pure centralized model
- Maintains oversight for high-risk signals

**Use cases:**
- Most enterprise deployments
- Agencies with both regulated and general campaigns
- Organizations transitioning to agent-driven workflows

---

## Summary

OpenSignals provides a structured, standardized trust verification layer that fits naturally into the advertising technology stack. By sitting between discovery and activation, it enables agents to make trust-informed decisions while maintaining governance controls, audit trails, and human oversight where needed.

The six-stage workflow—Discovery, Trust Verification, Governance, Activation, Audit, and Feedback—ensures that every signal used by an agent is declared, verified, permissioned, activated with appropriate controls, audited for accountability, and continuously improved through outcome feedback.

This architecture enables the advertising industry to adopt autonomous agents safely and responsibly, with trust and transparency built in from the start.

---

**Related Documentation:**
- [OpenSignals Protocol v0.1 Specification](/Users/samrajmatharu/opensignals-protocol/specs/opensignals-v0.1.md)
- [Brand-Side Use Case](/Users/samrajmatharu/opensignals-protocol/docs/brand-side-use-case.md)
- [Governance Model](/Users/samrajmatharu/opensignals-protocol/docs/governance-model.md)
- [Protocol Terminology](/Users/samrajmatharu/opensignals-protocol/specs/terminology.md)
