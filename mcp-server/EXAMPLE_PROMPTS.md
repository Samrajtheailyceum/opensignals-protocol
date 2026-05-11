# Example Prompts for OpenSignals MCP Server

This document provides example prompts that AI agents (like Claude) can use to interact with the OpenSignals Protocol MCP server. These prompts demonstrate real agentic advertising workflows.

## Discovery and Exploration

### Basic Signal Discovery

```
List all available advertising signals
```

```
Show me signals with a trust score above 0.85
```

```
What attention measurement signals are available?
```

```
Find all signals suitable for retail campaigns
```

### Detailed Signal Information

```
Get the full manifest for the verified-attention-quality signal
```

```
Show me the trust scores for the outdoor-recreation-enthusiasts signal
```

```
What data sources does the retail-commerce-signal use?
```

## Compliance Checking

### Pre-Campaign Compliance

```
I'm planning an alcohol campaign in the UK. What compliance requirements apply?
```

```
What are the rules for gambling advertising in the United States?
```

```
Can I advertise pharmaceuticals in California? What restrictions apply?
```

```
What age restrictions apply for alcohol advertising in France?
```

### Signal-Specific Verification

```
I need to use the outdoor-recreation-enthusiasts signal for a UK alcohol campaign targeting premium spirits buyers. Check if this is compliant.
```

```
Verify if the sustainability-signal is permitted for financial services advertising in Germany
```

```
Can I use the attention-signal for pharmaceutical advertising in the US market?
```

```
Check compliance for using the retail-commerce-signal in a gambling campaign in Nevada
```

## Full Campaign Workflow

### Example 1: Alcohol Campaign

```
I'm a media buyer for a premium spirits brand. We want to run a campaign in the United Kingdom targeting outdoor enthusiasts aged 25+. The campaign budget is £200,000.

1. First, tell me what compliance requirements apply for alcohol advertising in the UK
2. Then find signals that would be suitable and compliant
3. For each signal, check if it's permitted for this use case
4. Show me the trust scores
5. Recommend which signals to use and explain why
```

**Expected Agent Flow:**
1. Call `check_compliance(category="alcohol", market="GB")`
2. Call `list_signals()` to see available signals
3. For promising signals, call `verify_signal()` with alcohol context
4. Call `score_signal()` for verified signals
5. Present recommendations with trust scores and compliance status

### Example 2: Attention Measurement

```
I need to measure attention quality for our video ad campaign.

1. What attention measurement signals are available?
2. Show me their trust scores
3. Get the full details for the highest-rated attention signal
4. Verify it's suitable for general video advertising in the US
```

**Expected Agent Flow:**
1. Call `list_signals(signal_type="attention")`
2. For each signal, show trust scores from manifest
3. Call `get_signal_manifest()` for top signal
4. Call `verify_signal()` with measurement use case

### Example 3: Multi-Market Campaign

```
We're launching a financial services campaign in the US, UK, and Germany.

1. Check compliance requirements for finance in each market
2. Find signals that work across all three markets
3. Verify each signal for financial services use
4. Calculate trust scores
5. Recommend the best cross-market signal strategy
```

**Expected Agent Flow:**
1. Call `check_compliance(category="finance", market=X)` for each market
2. Call `list_signals()` and filter by geographic coverage
3. Call `verify_signal()` for each market
4. Call `score_signal()` for approved signals
5. Compare and recommend

### Example 4: Signal Comparison

```
Compare these three signals for our retail campaign:
- verified-attention-quality
- retail-commerce-signal
- outdoor-recreation-enthusiasts

Tell me:
1. Trust scores for each
2. Which is most suitable for retail
3. Compliance status
4. Your recommendation
```

**Expected Agent Flow:**
1. For each signal, call `get_signal_manifest()`
2. Call `score_signal()` for each with retail context
3. Call `verify_signal()` for each with retail category
4. Compare and recommend based on scores + compliance

## Audit and Governance

### Logging Signal Usage

```
We just activated the outdoor-recreation-enthusiasts signal for our spring campaign (campaign ID: spring-2026-uk-spirits). Log this for compliance audit.
```

**Expected Agent Flow:**
```json
{
  "tool": "audit_signal_usage",
  "arguments": {
    "signal_id": "outdoor-recreation-enthusiasts",
    "event_type": "signal_activated",
    "context": {
      "campaign_id": "spring-2026-uk-spirits",
      "brand": "premium-spirits-co",
      "category": "alcohol",
      "market": "GB"
    }
  }
}
```

### Approval Workflow

```
The governance team approved using the retail-commerce-signal for our fashion campaign.
- Campaign: summer-fashion-2026
- Approver: sarah.jones@fashion-brand.com
- Trust score from verification: 0.91

Log this approval.
```

**Expected Agent Flow:**
```json
{
  "tool": "audit_signal_usage",
  "arguments": {
    "signal_id": "retail-commerce-signal",
    "event_type": "signal_verified",
    "context": {
      "campaign_id": "summer-fashion-2026",
      "human_approver": "sarah.jones@fashion-brand.com",
      "trust_score": 0.91,
      "category": "general"
    }
  }
}
```

## Advanced Workflows

### Autonomous Decision Making

```
Act as an autonomous media buying agent. You have a brief for:
- Brand: Premium Outdoor Gear Co
- Budget: $500,000
- Market: United States
- Category: General retail
- Objective: Drive traffic to e-commerce site
- Target: Outdoor enthusiasts, active lifestyle

Autonomously:
1. Find compliant signals
2. Verify them
3. Score them against the objective
4. Select the best 2-3 signals
5. Create activation plan
6. Log your decisions for audit

Make decisions automatically for any signal with trust score above 0.85 and no human approval requirements.
```

### Governance Agent Simulation

```
Act as a brand governance agent reviewing signal usage.

Review these signal activations and tell me if they're compliant:

1. Signal: outdoor-recreation-enthusiasts
   Campaign: Alcohol brand, UK market
   Activation: Was used without human approval

2. Signal: verified-attention-quality
   Campaign: Pharma brand, US market
   Activation: Was verified and human-approved

3. Signal: sustainability-signal
   Campaign: Finance brand, Germany
   Activation: No verification performed

For each, tell me if the process was correct and what should have been done differently.
```

### Risk Assessment

```
I'm considering activating the outdoor-recreation-enthusiasts signal for a campaign. However:
- The campaign is for alcohol (high-risk category)
- The market is Saudi Arabia
- The intended use is individual profiling
- The trust score is 0.87

Should I proceed? Check compliance and explain the risks.
```

**Expected Agent Flow:**
1. Call `check_compliance(category="alcohol", market="SA")`
2. Call `verify_signal()` with full context
3. Explain why this is blocked (alcohol restricted in SA)
4. Recommend alternative approaches

## Testing and Validation

### Server Health Check

```
Test the OpenSignals MCP server by:
1. Listing all available signals
2. Getting the manifest for one signal
3. Checking compliance for alcohol in the UK
4. Calculating a trust score

Report if everything is working correctly.
```

### Schema Validation

```
Show me the OpenSignals manifest schema and explain what fields are required for a valid signal.
```

```
Get the verify-signal-request schema and explain what context information is needed for verification.
```

## Error Handling

### Invalid Signal

```
Try to get the manifest for a signal called "nonexistent-signal" and tell me what happens.
```

### Missing Context

```
Try to verify the outdoor-recreation-enthusiasts signal without specifying a category. What error do you get?
```

### Restricted Markets

```
Check if I can run a gambling campaign in Utah, USA. What does the compliance check say?
```

## Educational Queries

### Learning About Trust Scores

```
Explain how OpenSignals calculates trust scores. What are the 7 dimensions and how are they weighted?
```

```
What does a trust score of 0.87 mean? What trust band is that and what does it imply for autonomous activation?
```

### Understanding Compliance

```
Explain the difference between alcohol advertising rules in the UK versus the US. What age restrictions apply in each?
```

```
Why do some signals require human approval? Give me examples of when this is mandatory.
```

### Protocol Overview

```
Explain how the OpenSignals Protocol fits into the agentic advertising workflow. How does it relate to AdCP and OpenRTB?
```

## Integration Examples

### With AdCP

```
I'm building an AdCP-compatible agent. Show me how to:
1. Use AdCP to discover signals
2. Use OpenSignals to verify those signals
3. Use AdCP to activate verified signals
4. Use OpenSignals to audit the activation
```

### With OpenRTB

```
I'm preparing an OpenRTB bid request. I want to include trust scores for the signals I'm using. Show me:
1. How to get trust scores for my signals
2. What trust information should go in the bid request
3. How to structure this in OpenRTB extensions
```

## Real-World Scenarios

### Scenario 1: Agency Managing Multiple Brands

```
I'm an agency managing 5 brands across different categories:
- Premium spirits (alcohol)
- Online casino (gambling)
- Pain medication (pharma)
- Credit cards (finance)
- Organic food (general)

All campaigns target the UK market. For each brand:
1. What are the compliance requirements?
2. Which signals would be compliant?
3. What approval workflows are needed?

Create a governance matrix showing which signals work for which brands.
```

### Scenario 2: Real-Time Optimization

```
I'm an optimization agent running a live campaign. I need to add new signals dynamically to improve performance.

Current campaign:
- Category: General retail
- Market: US
- Performance: Below target
- Approved signals: retail-commerce-signal (currently active)

Process:
1. Find additional compliant signals with trust score > 0.80
2. Verify they're compatible with the current campaign
3. Score them for relevance
4. Recommend which to add
5. Log the decision for audit
```

### Scenario 3: Global Campaign Compliance

```
We're launching a global campaign across 20 markets for an alcoholic beverage brand.

Markets include: US, UK, FR, DE, ES, IT, AU, JP, BR, MX, CA, and others.

For each market:
1. Check if alcohol advertising is restricted
2. Identify age restrictions
3. Note prohibited uses (profiling, etc.)
4. Find signals with coverage in that market

Create a market-by-market compliance report and recommend a signal strategy.
```

## Tips for Agents

When using the OpenSignals MCP server:

1. **Always check compliance first** using `check_compliance()` before searching for signals
2. **Verify before activating** - call `verify_signal()` for EVERY signal before activation
3. **Log everything** - call `audit_signal_usage()` after activation for regulated categories
4. **Trust the trust scores** - don't activate signals below 0.50 without explicit human approval
5. **Understand the context** - category + market + intended_use matter for compliance
6. **Read the conditions** - if `approval_required: true`, you MUST get human approval
7. **Follow policy bindings** - enforce mandatory policies returned by verification
8. **Use resources** - access documentation via `opensignals://docs/*` URIs
9. **Filter intelligently** - use `list_signals()` filters to narrow candidates early
10. **Explain reasoning** - always explain trust scores and compliance decisions to humans

---

These examples demonstrate the full capabilities of the OpenSignals MCP server for real agentic advertising workflows. Use them as templates for building your own agent prompts and workflows.
