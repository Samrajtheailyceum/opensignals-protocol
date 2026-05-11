# Brand-Side Use Case: Premium Spirits Campaign

**Version**: 0.1
**Status**: Draft
**Last Updated**: May 2026

---

## Overview

This document presents a complete, practical example of the OpenSignals Protocol in action from a brand-side perspective. It demonstrates how a regulated drinks brand uses OpenSignals to run a premium cocktail campaign in Great Britain with full governance, compliance, and audit capabilities.

This use case is designed to be executive-readable and credible, showing real-world workflow from brief to activation to audit.

---

## The Brand

**Company**: Keelson Spirits Ltd
**Product**: Keelson Premium Gin
**Market Position**: Premium craft spirits, £40-45 per bottle
**Target Demographic**: Affluent adults 25-45, interested in craft cocktails and premium home entertaining
**Geographic Focus**: Great Britain (England, Scotland, Wales)

---

## Business Challenge

Keelson Spirits wants to launch a new seasonal campaign promoting premium cocktail recipes featuring Keelson Gin. The campaign will run in Great Britain during the summer cocktail season (June-August 2026).

### Key Requirements

1. **Regulatory Compliance**: Alcohol advertising in Great Britain is strictly regulated under the UK CAP Code and Portman Group Code of Practice
2. **Age Restriction**: All advertising must target adults aged 18+ only
3. **Brand Safety**: Content must be premium, aspirational, and avoid any association with excessive consumption or youth appeal
4. **Transparency**: Full audit trail required for regulatory reporting and internal compliance reviews
5. **Performance**: Campaign must reach 3M+ adults in target demographic with measurable brand lift

### Campaign Brief

**Campaign Name**: "Summer Craft Cocktails by Keelson"
**Objective**: Drive brand awareness and purchase consideration
**Budget**: £150,000
**Duration**: 12 weeks (June 1 - August 23, 2026)
**KPIs**:
- Reach: 3M+ unique adults 25-45
- Brand awareness lift: +6%
- Purchase consideration lift: +8%
- Ad recall: 35%+

**Target Audience**: Adults 25-45 interested in premium food and drink, entertaining at home, craft cocktails

**Content Strategy**: Contextual targeting on premium food, drink, lifestyle, and entertainment editorial content

---

## The OpenSignals Workflow

### Phase 1: Campaign Planning and Signal Discovery

**Date**: May 15, 2026
**Actors**: Campaign Manager (Sarah Thompson), Media Buying Agent (autonomous AI)

Sarah provides the campaign brief to the media buying agent through a conversational interface:

```
Sarah: "I need to plan a campaign for Keelson Gin targeting
        adults 25-45 in Great Britain who are interested in
        craft cocktails and premium entertaining. Budget is
        £150,000 for 12 weeks starting June 1st. This is an
        alcohol campaign so we need full compliance with UK
        regulations."
```

The buyer agent interprets the brief and begins signal discovery using AdCP:

**Agent Action**: Call AdCP `get_signals`

**Request**:
```json
{
  "task": "get_signals",
  "context": {
    "brand": "keelson-spirits",
    "product": "keelson-premium-gin",
    "objective": "brand_awareness_and_consideration",
    "category": "alcohol",
    "market": "GB",
    "target_demographic": "adults_25_45",
    "interests": ["premium_food_drink", "craft_cocktails", "home_entertaining"],
    "budget": 150000,
    "currency": "GBP",
    "duration_weeks": 12
  }
}
```

**Response** (includes OpenSignals metadata):
```json
{
  "task": "get_signals",
  "signals": [
    {
      "signal_id": "premium-cocktail-contexts",
      "name": "Premium Cocktail & Spirits Content Contexts",
      "signal_type": "contextual",
      "provider": "ContextIQ Media Solutions",
      "coverage": 45000000,
      "estimated_reach_gb": 8200000,
      "cpm_range": {
        "min": 4.50,
        "max": 12.00,
        "currency": "GBP"
      },
      "open_signals": {
        "manifest_url": "https://contextiq.example.com/.well-known/opensignals/premium-cocktail-contexts",
        "overall_trust_score": 0.88,
        "verification_required": true,
        "audit_required": true,
        "category": "regulated",
        "subcategory": "alcohol",
        "human_approval_required": true,
        "last_verified": "2026-05-10T14:00:00Z"
      }
    },
    {
      "signal_id": "premium-lifestyle-audience",
      "name": "Premium Lifestyle Enthusiasts",
      "signal_type": "audience",
      "provider": "AudienceScope Data",
      "coverage": 12500000,
      "estimated_reach_gb": 2100000,
      "cpm_range": {
        "min": 8.00,
        "max": 15.00,
        "currency": "GBP"
      },
      "open_signals": {
        "manifest_url": "https://audiencescope.example.com/.well-known/opensignals/premium-lifestyle-audience",
        "overall_trust_score": 0.76,
        "verification_required": true,
        "audit_required": true,
        "category": "regulated",
        "subcategory": "alcohol",
        "human_approval_required": true,
        "individual_profiling": true,
        "last_verified": "2026-05-08T10:00:00Z"
      }
    }
  ]
}
```

The agent identifies two candidate signals and presents them to Sarah with recommendation:

```
Agent: "I've found 2 signals that match your requirements:

1. Premium Cocktail & Spirits Content Contexts
   - Type: Contextual targeting (no individual profiling)
   - Coverage: 8.2M adults in GB
   - Trust Score: 0.88 (Trusted)
   - CPM: £4.50-12.00
   - Compliance: Fully compliant, human approval required

2. Premium Lifestyle Enthusiasts
   - Type: Audience targeting (individual profiling)
   - Coverage: 2.1M adults in GB
   - Trust Score: 0.76 (Trusted with Conditions)
   - CPM: £8.00-15.00
   - Compliance: May require additional review

Recommendation: Signal 1 (contextual) is better suited for
alcohol campaigns due to higher trust score, no individual
profiling concerns, and lower CPM. I recommend proceeding
with full verification."
```

Sarah agrees and instructs the agent to proceed with verification.

---

### Phase 2: Trust Verification

**Date**: May 15, 2026
**Actors**: Buyer Agent, Governance Agent

The buyer agent retrieves the full OpenSignal Manifest and requests verification from the governance agent.

**Agent Action 1**: Call OpenSignals `get_signal_manifest`

**Request**:
```
GET https://contextiq.example.com/.well-known/opensignals/premium-cocktail-contexts
```

**Response**: [Full manifest - see `/Users/samrajmatharu/opensignals-protocol/examples/alcohol-contextual-signal.json`]

Key manifest highlights:
- **Trust Score**: 0.88 overall (Provenance: 0.92, Freshness: 0.95, Compliance: 0.94)
- **Category**: Regulated / Alcohol
- **Data Sources**: Contextual page analysis, no behavioral tracking
- **Permissioning**: No individual profiling, contextual use only
- **Market Restrictions**: Age 18+ in GB, complies with UK CAP Code and Portman Group Code
- **Human Approval**: Required
- **Audit Frequency**: Per activation
- **Third-Party Verification**: TAG Brand Safety Certified, MRC Viewability Accredited

**Agent Action 2**: Call OpenSignals `verify_signal`

**Request**:
```json
{
  "task": "verify_signal",
  "signal_id": "premium-cocktail-contexts",
  "brand": "keelson-spirits",
  "product": "keelson-premium-gin",
  "market": "GB",
  "category": "alcohol",
  "intended_use": "contextual_targeting",
  "campaign_objective": "brand_awareness_and_consideration",
  "target_age_range": "25-45"
}
```

The governance agent performs comprehensive verification checks:

**Verification Process**:

1. **Market Compliance Check**:
   - ✓ Signal is permitted in Great Britain
   - ✓ Minimum age 18+ declared in manifest matches UK law
   - ✓ Signal complies with UK CAP Code alcohol advertising rules
   - ✓ Signal complies with Portman Group Code of Practice

2. **Category Permission Check**:
   - ✓ Signal explicitly permits alcohol category use
   - ✓ No youth appeal content (blocked in manifest)
   - ✓ No prohibited content adjacency (health, educational content blocked)

3. **Permissioning Check**:
   - ✓ Contextual signal only (no individual profiling)
   - ✓ No cross-site tracking
   - ✓ No behavioral targeting components
   - ✓ Complies with privacy best practices for alcohol advertising

4. **Trust Score Assessment**:
   - ✓ Overall trust score 0.88 (Trusted band)
   - ✓ Provenance score 0.92 (transparent data sources)
   - ✓ Freshness score 0.95 (updated hourly)
   - ✓ Compliance score 0.94 (third-party verified)

5. **Provenance Verification**:
   - ✓ Chain of custody verified
   - ✓ Data sources clearly declared (contextual page analysis)
   - ✓ Collection method appropriate (automated NLP + human review)
   - ✓ Third-party audit report available and reviewed

6. **Brand Safety Check**:
   - ✓ TAG Brand Safety Certified
   - ✓ Content categories appropriate (premium food/drink, lifestyle)
   - ✓ Blocked categories appropriate (children, youth, health, gambling)

7. **Bounded Autonomy Assessment**:
   - ⚠ Human approval required (regulated category: alcohol)
   - ⚠ Audit logging mandatory
   - Decision mode: `approve_with_human`

**Response**:
```json
{
  "task": "verify_signal",
  "signal_id": "premium-cocktail-contexts",
  "decision": "approved_with_conditions",
  "trust_score": 0.88,
  "trust_band": "trusted",
  "conditions": [
    "human_approval_required",
    "audit_required",
    "no_individual_profiling",
    "age_verification_required",
    "contextual_use_only"
  ],
  "policy_bindings_required": [
    "alcohol_age_restriction_gb",
    "uk_cap_code_compliance",
    "portman_group_code_compliance",
    "no_youth_appeal"
  ],
  "decision_reasoning": "Signal approved for contextual targeting only. Trust score 0.88 indicates high reliability. Signal is compliant with UK alcohol advertising regulations. No individual profiling ensures privacy compliance. Human approval required due to regulated alcohol category. Audit logging mandatory for regulatory reporting.",
  "verification_timestamp": "2026-05-15T14:23:18Z",
  "governance_agent": "keelson-policy-engine-v2",
  "verified_by": "governance@keelson.com"
}
```

---

### Phase 3: Policy Binding and Human Approval

**Date**: May 16, 2026
**Actors**: Governance Agent, Compliance Officer (James Wilson)

The governance agent binds brand-specific policies to the signal and routes the activation request for human approval.

**Agent Action**: Call OpenSignals `bind_signal_policy`

**Request**:
```json
{
  "task": "bind_signal_policy",
  "signal_id": "premium-cocktail-contexts",
  "brand": "keelson-spirits",
  "campaign_id": "summer-craft-cocktails-2026",
  "policies": [
    "alcohol_age_restriction_gb",
    "uk_cap_code_compliance",
    "portman_group_code_compliance",
    "keelson_brand_safety_standards"
  ]
}
```

**Response**:
```json
{
  "task": "bind_signal_policy",
  "signal_id": "premium-cocktail-contexts",
  "bindings": [
    {
      "policy_id": "alcohol_age_restriction_gb",
      "policy_name": "UK Alcohol Age Restriction",
      "enforcement_level": "mandatory",
      "parameters": {
        "minimum_age": 18,
        "age_verification_method": "platform_age_gate",
        "geographic_scope": ["GB"]
      },
      "violation_action": "block_activation"
    },
    {
      "policy_id": "uk_cap_code_compliance",
      "policy_name": "UK CAP Code Alcohol Advertising Rules",
      "enforcement_level": "mandatory",
      "parameters": {
        "no_youth_appeal": true,
        "no_excessive_consumption_imagery": true,
        "responsible_messaging_only": true,
        "no_health_claims": true
      },
      "violation_action": "block_activation",
      "reference_url": "https://www.asa.org.uk/codes-and-rulings/advertising-codes/broadcast-code/alcohol.html"
    },
    {
      "policy_id": "portman_group_code_compliance",
      "policy_name": "Portman Group Code of Practice",
      "enforcement_level": "mandatory",
      "parameters": {
        "no_appeal_to_under_18s": true,
        "responsible_drinking_messaging": true,
        "no_association_with_illicit_drugs": true,
        "no_association_with_dangerous_activities": true
      },
      "violation_action": "block_activation",
      "reference_url": "https://www.portmangroup.org.uk/codes/code-of-practice/"
    },
    {
      "policy_id": "keelson_brand_safety_standards",
      "policy_name": "Keelson Brand Safety Standards",
      "enforcement_level": "recommended",
      "parameters": {
        "premium_contexts_only": true,
        "no_controversial_content_adjacency": true,
        "minimum_viewability_threshold": 0.70,
        "maximum_invalid_traffic_threshold": 0.02
      },
      "violation_action": "warn_and_log"
    }
  ],
  "binding_timestamp": "2026-05-16T09:15:22Z",
  "bound_by": "keelson-policy-engine-v2"
}
```

**Human Approval Workflow**:

The governance agent generates an approval request and sends it to the compliance officer:

**Approval Request Email**:
```
To: James Wilson <james.wilson@keelson.com>
From: Keelson Policy Engine <governance@keelson.com>
Subject: [ACTION REQUIRED] Signal Activation Approval - Summer Craft Cocktails Campaign
Priority: Normal

Campaign: Summer Craft Cocktails by Keelson
Signal: Premium Cocktail & Spirits Content Contexts
Provider: ContextIQ Media Solutions
Budget: £150,000
Duration: 12 weeks (June 1 - August 23, 2026)

APPROVAL REQUEST

The media buying agent has requested approval to activate the following
signal for the Summer Craft Cocktails campaign:

Signal Details:
- Signal ID: premium-cocktail-contexts
- Type: Contextual targeting (page-level content analysis)
- Trust Score: 0.88 (Trusted)
- Provider: ContextIQ Media Solutions
- Third-Party Certifications: TAG Brand Safety, MRC Viewability

Verification Summary:
✓ Compliant with UK CAP Code alcohol advertising rules
✓ Compliant with Portman Group Code of Practice
✓ Age restriction 18+ enforced
✓ No individual profiling (contextual only)
✓ TAG Brand Safety Certified
✓ Third-party verified and audited

Policy Bindings (Mandatory):
✓ UK Alcohol Age Restriction (18+)
✓ UK CAP Code Compliance
✓ Portman Group Code Compliance
✓ Keelson Brand Safety Standards

Trust Score Breakdown:
- Provenance: 0.92 (Excellent)
- Permissioning: 0.85 (Good)
- Freshness: 0.95 (Excellent)
- Quality: 0.87 (Good)
- Compliance: 0.94 (Excellent)

Risk Assessment: LOW
- Contextual targeting only (no privacy concerns)
- Third-party verified and certified
- Compliant with all applicable regulations
- No youth appeal or prohibited content adjacency

Recommendation: APPROVE

Please review the attached signal manifest and audit report, then
approve or reject this activation request.

[Approve] [Reject] [Request More Information]

View full signal manifest: [link]
View third-party audit report: [link]
View policy bindings: [link]

Approval ID: approval-2026-05-16-001
Generated: 2026-05-16T09:20:00Z
```

**Compliance Officer Review**:

James Wilson reviews the request, examines the signal manifest, reviews the third-party audit report, and confirms compliance with Keelson's internal standards. He approves the activation:

**Approval Record**:
```json
{
  "approval_id": "approval-2026-05-16-001",
  "signal_id": "premium-cocktail-contexts",
  "campaign_id": "summer-craft-cocktails-2026",
  "decision": "approved",
  "approved_by": "James Wilson",
  "approver_role": "Compliance Officer",
  "approver_email": "james.wilson@keelson.com",
  "approval_timestamp": "2026-05-16T14:35:47Z",
  "approval_reasoning": "Signal is fully compliant with UK alcohol advertising regulations and Keelson brand safety standards. Contextual targeting approach eliminates privacy concerns. Third-party certifications and audit report confirm quality and brand safety. Approved for activation.",
  "conditions_acknowledged": [
    "audit_required",
    "age_verification_required",
    "contextual_use_only",
    "policy_bindings_enforced"
  ],
  "digital_signature": "sha256:a7b3c9d2e1f4g5h6i7j8k9l0m1n2o3p4"
}
```

---

### Phase 4: Signal Activation

**Date**: May 17, 2026
**Actors**: Buyer Agent, Execution Platform (DSP)

With human approval secured, the buyer agent activates the signal through AdCP.

**Agent Action**: Call AdCP `activate_signal`

**Request**:
```json
{
  "task": "activate_signal",
  "signal_id": "premium-cocktail-contexts",
  "campaign_id": "summer-craft-cocktails-2026",
  "brand": "keelson-spirits",
  "budget": 150000,
  "currency": "GBP",
  "start_date": "2026-06-01T00:00:00Z",
  "end_date": "2026-08-23T23:59:59Z",
  "opensignals_context": {
    "trust_score": 0.88,
    "verification_decision": "approved_with_conditions",
    "approval_id": "approval-2026-05-16-001",
    "approver": "James Wilson",
    "policy_bindings": [
      "alcohol_age_restriction_gb",
      "uk_cap_code_compliance",
      "portman_group_code_compliance",
      "keelson_brand_safety_standards"
    ],
    "conditions": [
      "audit_required",
      "age_verification_required",
      "contextual_use_only"
    ],
    "governance_agent": "keelson-policy-engine-v2",
    "verification_timestamp": "2026-05-15T14:23:18Z"
  },
  "targeting": {
    "geographic": ["GB"],
    "content_contexts": ["premium_food_drink", "craft_cocktails", "home_entertaining"],
    "inventory_types": ["display", "video", "native"],
    "age_gate": "18+"
  }
}
```

**Execution Platform Response**:
```json
{
  "task": "activate_signal",
  "status": "activated",
  "campaign_id": "summer-craft-cocktails-2026",
  "signal_id": "premium-cocktail-contexts",
  "activation_id": "activation-2026-05-17-4782",
  "activation_timestamp": "2026-05-17T10:12:33Z",
  "platform": "premiumreach-dsp",
  "policy_enforcement_status": {
    "alcohol_age_restriction_gb": "enforced",
    "uk_cap_code_compliance": "enforced",
    "portman_group_code_compliance": "enforced",
    "keelson_brand_safety_standards": "enforced"
  },
  "estimated_delivery": {
    "impressions": "10M-15M",
    "reach": "3M-4M unique adults",
    "start_date": "2026-06-01",
    "end_date": "2026-08-23"
  },
  "audit_endpoint": "https://audit.premiumreach-dsp.com/v1/opensignals/audit",
  "message": "Signal activated successfully with all policy bindings enforced. Age verification gate active. Audit logging enabled."
}
```

The buyer agent confirms activation to Sarah:

```
Agent: "Signal activated successfully. Campaign 'Summer Craft
        Cocktails by Keelson' is scheduled to run June 1 -
        August 23, 2026 with £150,000 budget. All compliance
        policies are enforced. Estimated reach: 3-4M adults in
        Great Britain. Full audit logging is enabled. You will
        receive weekly performance reports."
```

---

### Phase 5: Campaign Audit Trail

**Date**: May 17, 2026 (immediately after activation)
**Actors**: Execution Platform, Audit Agent

The execution platform logs the activation to the audit trail.

**Agent Action**: Call OpenSignals `audit_signal_usage`

**Request**:
```json
{
  "task": "audit_signal_usage",
  "audit_event": {
    "signal_id": "premium-cocktail-contexts",
    "brand": "keelson-spirits",
    "campaign_id": "summer-craft-cocktails-2026",
    "buyer_agent": "keelson-media-bot-v3",
    "governance_agent": "keelson-policy-engine-v2",
    "decision_mode": "approve_with_human",
    "trust_score": 0.88,
    "use_case": "contextual_targeting",
    "platform": "premiumreach-dsp",
    "geographic_scope": ["GB"],
    "category": "alcohol",
    "subcategory": "spirits_gin",
    "approval_id": "approval-2026-05-16-001",
    "approver": "James Wilson",
    "approver_role": "Compliance Officer",
    "policy_bindings": [
      {
        "policy_id": "alcohol_age_restriction_gb",
        "enforcement_level": "mandatory",
        "enforcement_status": "enforced"
      },
      {
        "policy_id": "uk_cap_code_compliance",
        "enforcement_level": "mandatory",
        "enforcement_status": "enforced"
      },
      {
        "policy_id": "portman_group_code_compliance",
        "enforcement_level": "mandatory",
        "enforcement_status": "enforced"
      },
      {
        "policy_id": "keelson_brand_safety_standards",
        "enforcement_level": "recommended",
        "enforcement_status": "enforced"
      }
    ],
    "activation_timestamp": "2026-05-17T10:12:33Z",
    "activation_id": "activation-2026-05-17-4782",
    "spend_allocated": 150000,
    "currency": "GBP",
    "campaign_start_date": "2026-06-01T00:00:00Z",
    "campaign_end_date": "2026-08-23T23:59:59Z",
    "verification_timestamp": "2026-05-15T14:23:18Z",
    "approval_timestamp": "2026-05-16T14:35:47Z"
  }
}
```

**Response**:
```json
{
  "task": "audit_signal_usage",
  "audit_id": "audit-2026-05-17-9821",
  "status": "logged",
  "retention_until": "2026-11-17T10:12:33Z",
  "retention_days": 184,
  "audit_endpoint": "https://audit.keelson.com/opensignals/audit-2026-05-17-9821",
  "tamper_evident_hash": "sha256:f9e8d7c6b5a4938271605d4c3b2a1908",
  "audit_timestamp": "2026-05-17T10:12:35Z",
  "message": "Audit event logged successfully. Retention period: 184 days (extended for regulated category). Audit trail is tamper-evident and cryptographically signed."
}
```

The audit trail now contains a complete, immutable record of:
- **Who**: Keelson Media Bot v3 (buyer), Keelson Policy Engine v2 (governance), James Wilson (approver)
- **What**: premium-cocktail-contexts signal
- **When**: Activated May 17, 2026; Campaign runs June 1 - August 23, 2026
- **Where**: Great Britain
- **Why**: Summer Craft Cocktails campaign, brand awareness objective, alcohol category
- **How**: Contextual targeting only, no individual profiling
- **Under What Policy**: UK CAP Code, Portman Group Code, UK age restriction (18+), Keelson brand safety
- **Trust Score**: 0.88 (Trusted)
- **Human Approval**: Yes (James Wilson, Compliance Officer)

This audit trail can be retrieved at any time for regulatory reporting, internal compliance reviews, or campaign post-mortems.

---

### Phase 6: Campaign Execution and Monitoring

**Dates**: June 1 - August 23, 2026
**Actors**: Execution Platform, Buyer Agent, Campaign Manager

The campaign runs for 12 weeks with continuous monitoring and weekly reporting.

**Weekly Performance Report (Week 4, June 22-28, 2026)**:

```
Keelson Summer Craft Cocktails Campaign - Week 4 Report
Campaign Period: June 22-28, 2026
Signal: Premium Cocktail & Spirits Content Contexts

Performance Summary:
- Impressions Delivered: 1,247,392
- Unique Reach: 412,847 adults (cumulative: 2,134,982)
- Viewability: 79.2% (target: 70%+) ✓
- Invalid Traffic: 0.8% (target: <2%) ✓
- Average CPM: £8.45
- Spend to Date: £52,341 (total budget: £150,000)

Content Context Performance:
- Premium Food & Drink Editorial: 42% of impressions, 82% viewability
- Lifestyle & Home Entertaining: 31% of impressions, 77% viewability
- Entertainment & Culture: 27% of impressions, 76% viewability

Geographic Distribution:
- England: 78%
- Scotland: 14%
- Wales: 8%

Age Distribution:
- 25-34: 47%
- 35-44: 41%
- 45-54: 12%

Compliance Status:
✓ All policy bindings enforced
✓ Age verification active (100% of impressions age-gated 18+)
✓ No youth appeal content detected
✓ No prohibited content adjacency
✓ Zero brand safety incidents

Trust Score Performance:
- Signal continues to meet quality expectations
- Context accuracy: 94% (validated through sampling)
- No complaints or issues reported

Campaign on track to meet objectives. No action required.
```

---

### Phase 7: Campaign Completion and Outcome Feedback

**Date**: August 24, 2026
**Actors**: Buyer Agent, Measurement Platform, Signal Provider

The campaign completes successfully. Final performance metrics are measured and outcome feedback is submitted to improve the signal's trust score.

**Final Campaign Report**:

```
Keelson Summer Craft Cocktails Campaign - Final Report
Campaign Period: June 1 - August 23, 2026 (12 weeks)
Signal: Premium Cocktail & Spirits Content Contexts

Final Performance:
- Total Impressions: 14,892,847
- Unique Reach: 3,421,284 adults (target: 3M+) ✓
- Total Spend: £148,762 (budget: £150,000, 99.2% delivery)
- Average CPM: £9.99
- Viewability: 78.4% (target: 70%+) ✓
- Invalid Traffic: 0.9% (target: <2%) ✓

Brand Lift Study Results (Third-Party Verified):
- Brand Awareness Lift: +8.7% (target: +6%) ✓
- Purchase Consideration Lift: +11.2% (target: +8%) ✓
- Ad Recall: 38.4% (target: 35%+) ✓
- Message Association: 72% correctly associated campaign with Keelson Gin

Compliance Performance:
✓ Zero brand safety incidents
✓ Zero policy violations
✓ 100% age-gated delivery (18+)
✓ No complaints received
✓ Full audit trail maintained

Signal Quality Assessment:
- Context Accuracy: 93.7% (excellent)
- Audience Alignment: 91.2% (excellent)
- Viewability Performance: Exceeded expectations
- Invalid Traffic: Well below industry benchmarks

ROI and Business Impact:
- Cost per Reached User: £0.43
- Cost per Awareness Point: £17,081 per point
- Estimated Incremental Revenue: £2.1M (14x ROAS)
- Campaign rated "Highly Successful" by brand team

Recommendation:
Signal 'premium-cocktail-contexts' significantly exceeded
expectations across all KPIs. Recommend continued use for
future spirits campaigns. Signal provider delivered exceptional
quality and compliance throughout.
```

**Agent Action**: Call OpenSignals `submit_signal_outcome_feedback`

**Request**:
```json
{
  "task": "submit_signal_outcome_feedback",
  "signal_id": "premium-cocktail-contexts",
  "campaign_id": "summer-craft-cocktails-2026",
  "brand": "keelson-spirits",
  "campaign_objective": "brand_awareness_and_consideration",
  "outcome_metrics": {
    "brand_awareness_lift": 0.087,
    "purchase_consideration_lift": 0.112,
    "ad_recall": 0.384,
    "reach_accuracy": 0.937,
    "audience_alignment": 0.912,
    "viewability": 0.784,
    "invalid_traffic": 0.009,
    "context_accuracy": 0.937,
    "message_association": 0.72,
    "estimated_roas": 14.0
  },
  "quality_assessment": {
    "met_expectations": true,
    "exceeded_expectations": true,
    "accuracy_rating": 0.94,
    "reliability_rating": 0.96,
    "would_use_again": true,
    "overall_satisfaction": 0.95,
    "qualitative_feedback": "Signal significantly exceeded expectations. Context accuracy was excellent, viewability performance outstanding, and compliance was flawless throughout the 12-week campaign. Signal provider was responsive and supportive. Highly recommend for future regulated category campaigns."
  },
  "compliance_assessment": {
    "policy_violations": 0,
    "brand_safety_incidents": 0,
    "complaints_received": 0,
    "audit_trail_complete": true,
    "regulatory_compliance_rating": 1.0
  },
  "performance_vs_forecast": {
    "reach_vs_forecast": 1.14,
    "impressions_vs_forecast": 1.09,
    "viewability_vs_forecast": 1.12,
    "cost_vs_forecast": 0.99
  },
  "feedback_timestamp": "2026-08-24T15:42:19Z",
  "submitted_by": "keelson-media-bot-v3",
  "measurement_verified_by": "Nielsen Brand Effect Study"
}
```

**Response**:
```json
{
  "task": "submit_signal_outcome_feedback",
  "feedback_id": "feedback-2026-08-24-5531",
  "status": "processed",
  "trust_score_updated": true,
  "previous_scores": {
    "overall_trust_score": 0.88,
    "outcome_relevance_score": 0.78,
    "quality_score": 0.87
  },
  "updated_scores": {
    "overall_trust_score": 0.90,
    "outcome_relevance_score": 0.84,
    "quality_score": 0.89
  },
  "score_changes": {
    "overall_trust_score": 0.02,
    "outcome_relevance_score": 0.06,
    "quality_score": 0.02
  },
  "feedback_timestamp": "2026-08-24T15:42:22Z",
  "processed_by": "contextiq-trust-scoring-engine",
  "message": "Feedback processed successfully. Trust scores updated based on exceptional campaign performance. Signal 'premium-cocktail-contexts' now rated 0.90 (Highly Trusted). Thank you for submitting detailed outcome data."
}
```

The signal's trust score has improved from 0.88 to 0.90 based on real-world performance, moving it into the "Highly Trusted" band. Future buyers will benefit from this validated performance data.

---

## Executive Summary

### What Was Accomplished

Keelson Spirits successfully launched a compliant, high-performing premium spirits campaign in Great Britain using the OpenSignals Protocol to ensure trust, transparency, and regulatory compliance.

### Key Results

- **Campaign Performance**: All KPIs exceeded targets (reach, brand lift, ad recall)
- **Regulatory Compliance**: Zero violations, zero complaints, 100% age-gated delivery
- **Efficiency**: 99.2% budget delivery, £0.43 cost per reached user
- **Business Impact**: £2.1M estimated incremental revenue, 14x ROAS
- **Trust Validation**: Signal trust score improved from 0.88 to 0.90 based on performance

### How OpenSignals Enabled Success

1. **Trust Verification Before Activation**: The governance agent verified signal compliance with UK alcohol advertising regulations before any budget was committed, eliminating regulatory risk.

2. **Clear Policy Enforcement**: Mandatory policy bindings ensured UK CAP Code, Portman Group Code, and Keelson brand standards were enforced throughout the campaign.

3. **Appropriate Human Oversight**: Human approval from the compliance officer provided necessary regulatory oversight while allowing the media buying agent to handle execution autonomously.

4. **Complete Audit Trail**: Full documentation of who approved what, when, why, and under what policies provides regulatory defensibility and internal accountability.

5. **Continuous Quality Assessment**: Weekly monitoring confirmed the signal continued to meet quality and compliance expectations throughout the 12-week campaign.

6. **Outcome Feedback Loop**: Campaign results fed back into the signal's trust score, improving future buyers' ability to assess signal quality.

### Business Value

**For the Brand**:
- Confidence in regulatory compliance
- Reduced risk of brand safety incidents
- Clear accountability and audit trail
- Efficient campaign execution with agent autonomy
- Data-driven signal selection based on trust scores

**For the Industry**:
- Standardized trust metadata across signal providers
- Consistent governance framework for regulated categories
- Reusable policy definitions and enforcement
- Transparent provenance and quality metrics
- Continuous improvement through outcome feedback

### Scalability

This workflow can be applied to:
- Other regulated categories (gambling, pharma, finance, political)
- Multiple markets with different regulatory requirements
- Campaigns ranging from £10k to £10M+
- Both contextual and audience signals
- Multiple platforms and execution partners

OpenSignals provides the trust infrastructure necessary for brands to adopt autonomous agents safely, with appropriate governance controls, human oversight, and complete transparency.

---

## Appendix: Timeline Summary

| Date | Actor | Activity |
|------|-------|----------|
| May 15 | Campaign Manager | Provides campaign brief to buyer agent |
| May 15 | Buyer Agent | Discovers signals via AdCP, retrieves OpenSignal manifests |
| May 15 | Governance Agent | Verifies signal against brand policy and regulations |
| May 16 | Governance Agent | Binds brand policies to signal, routes for human approval |
| May 16 | Compliance Officer | Reviews and approves signal activation |
| May 17 | Buyer Agent | Activates signal through AdCP |
| May 17 | Execution Platform | Enforces policies, begins campaign delivery, logs audit event |
| May 17 | Audit Agent | Records activation in tamper-evident audit trail |
| June 1 | Execution Platform | Campaign begins delivery |
| June-Aug | Execution Platform | Weekly performance reports generated and reviewed |
| Aug 23 | Execution Platform | Campaign completes delivery |
| Aug 24 | Buyer Agent | Submits outcome feedback to signal provider |
| Aug 24 | Signal Provider | Updates trust scores based on performance feedback |

**Total Time from Brief to Activation**: 2 business days (with human approval)

**Agent Autonomy Level**: Semi-autonomous (agent-driven workflow with human approval checkpoint)

---

**Related Documentation:**
- [OpenSignals Protocol Architecture](/Users/samrajmatharu/opensignals-protocol/docs/architecture.md)
- [Governance Model](/Users/samrajmatharu/opensignals-protocol/docs/governance-model.md)
- [OpenSignals Protocol v0.1 Specification](/Users/samrajmatharu/opensignals-protocol/specs/opensignals-v0.1.md)
- [Example: Alcohol Contextual Signal](/Users/samrajmatharu/opensignals-protocol/examples/alcohol-contextual-signal.json)
