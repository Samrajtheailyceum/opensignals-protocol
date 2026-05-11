# OpenSignals Natural Language Integration Guide

**The easiest way to verify advertising signals: Just talk to your AI**

## What This Guide Is

This guide shows how **anyone** can use OpenSignals Protocol by simply talking to an AI assistant like Claude, ChatGPT, or Gemini. No coding required. No technical knowledge needed. Just natural conversation.

If you can send a message, you can verify advertising signals, check compliance, and ensure your campaigns use trustworthy data.

## Who This Guide Is For

- **Brand Managers** who need to ensure campaigns are compliant
- **Media Buyers** who want to verify signal quality before spending budget
- **Compliance Officers** who need to audit signal usage
- **Agency Teams** who manage campaigns for multiple clients
- **Marketers** who want better signal transparency
- **Anyone** who works with advertising data and wants to know it's trustworthy

**No technical background needed.**

---

## Table of Contents

1. [The Simple Concept](#the-simple-concept)
2. [How to Use OpenSignals Today](#how-to-use-opensignals-today)
3. [Real Conversation Examples](#real-conversation-examples)
4. [Platform-Specific Integration](#platform-specific-integration)
5. [Works With Any AI](#works-with-any-ai)
6. [Super Simple Activation](#super-simple-activation)
7. [Embedding in Your Workflow](#embedding-in-your-workflow)
8. [For Technical Teams](#for-technical-teams)

---

## The Simple Concept

OpenSignals makes advertising signals transparent and verifiable. Instead of guessing whether a signal is trustworthy, you can **ask an AI to check it for you**.

### Before OpenSignals:
```
You: "Should I use this audience signal for my alcohol campaign?"
You: *Manually reviews 50-page PDF documentation*
You: *Emails legal team for compliance check*
You: *Waits 3 days for approval*
You: *Still not sure if it's safe*
```

### With OpenSignals:
```
You: "Should I use the outdoor-recreation-enthusiasts signal
     for my UK alcohol campaign?"

AI: "Let me check that signal for you..."
    [AI verifies signal using OpenSignals]

    "This signal is APPROVED WITH CONDITIONS:
    - Trust score: 0.87 (Trusted)
    - Human approval required (alcohol category)
    - No individual profiling allowed
    - Age verification required (25+)
    - Audit trail required

    The signal is safe for contextual targeting in the UK.
    I recommend getting final approval from Sarah in legal."
```

**That's it. No coding. No manual research. Just ask.**

---

## How to Use OpenSignals Today

### Method 1: Via Claude Desktop (Easiest)

If you use Claude Desktop, OpenSignals can be integrated as an MCP server:

1. **Install the OpenSignals MCP server** (see [MCP Server Guide](../mcp-server/README.md))
2. **Restart Claude Desktop**
3. **Start asking questions**

That's it. Claude now has access to OpenSignals verification tools.

**Example:**
```
You: "List all available advertising signals"

Claude: [Uses OpenSignals to list signals with trust scores]

You: "I need signals for a pharma campaign in California.
     What's compliant?"

Claude: [Checks compliance rules and recommends approved signals]
```

### Method 2: Via ChatGPT (Coming Soon)

OpenSignals will be available as a ChatGPT plugin:

1. **Install the OpenSignals plugin** from the ChatGPT plugin store
2. **Enable it in your conversation**
3. **Ask questions about signals**

### Method 3: Via Any Platform with API Access

If your platform supports custom tools or APIs:

1. **Connect to OpenSignals API** (your tech team does this once)
2. **Talk to your AI** as normal
3. **AI verifies signals automatically**

No need to understand the API. Just talk naturally.

---

## Real Conversation Examples

### Example 1: Verifying a Signal (Alcohol Campaign)

**Scenario:** You're a brand manager at a spirits company planning a UK campaign.

```
You: "I'm planning an alcohol campaign in the United Kingdom targeting
     outdoor enthusiasts aged 25+. Can I use the outdoor-recreation-enthusiasts
     signal from DataProvider Co?"

Claude: "Let me verify that signal for your use case..."

[Claude calls: verify_signal(
  signal_id: "outdoor-recreation-enthusiasts",
  category: "alcohol",
  market: "GB",
  intended_use: "contextual_targeting"
)]

Claude: "Signal Verification Complete:

DECISION: Approved with Conditions

Trust Score: 0.87/1.00 (Trusted band)

✓ APPROVED for contextual targeting in UK
✗ Individual profiling NOT ALLOWED (alcohol restrictions)

CONDITIONS:
1. Human approval required (alcohol category)
2. Age verification mandatory (minimum age: 25 in UK)
3. Audit trail required for regulatory compliance
4. No individual-level targeting allowed

COMPLIANCE FRAMEWORKS:
- UK CAP Code (Alcohol Advertising)
- UK Advertising Standards

REASONING:
This signal has good provenance (first-party behavioral data) and
strong trust scores. However, UK alcohol advertising law requires
human approval before activation. The signal can only be used for
contextual targeting, not individual profiling.

NEXT STEPS:
1. Get approval from your legal/compliance team
2. Configure your campaign for contextual targeting only
3. Set age gates to 25+ (UK alcohol advertising minimum)
4. Activate signal with audit logging enabled

Would you like me to draft the approval request for your legal team?"

You: "Yes, please draft the request."

Claude: [Generates approval request with all relevant compliance info]
```

### Example 2: Checking Compliance Requirements

**Scenario:** You're launching a gambling campaign and want to know the rules.

```
You: "What are the compliance requirements for gambling advertising
     in Nevada, USA?"

Claude: "Let me check the gambling advertising rules for Nevada..."

[Claude calls: check_compliance(
  category: "gambling",
  market: "US-NV"
)]

Claude: "Gambling Advertising Compliance - Nevada, USA

RESTRICTED: Yes (Highly regulated)

AGE REQUIREMENTS:
- Minimum age: 21 years
- Age verification mandatory

ALLOWED USES:
✓ Contextual targeting (content-based)
✗ Individual profiling (prohibited)
✗ Lookalike modeling (prohibited)

PROHIBITED USES:
- No behavioral targeting of individuals
- No targeting based on financial vulnerability
- No retargeting of self-excluded individuals

COMPLIANCE REQUIREMENTS:
- Human approval mandatory before activation
- Self-exclusion list checking required
- Audit trail required for all activations
- Responsible gambling messaging required

COMPLIANCE FRAMEWORKS:
- Nevada Gaming Control Board Regulations
- American Gaming Association Responsible Gaming Code

GEOGRAPHIC NOTES:
- Some US markets prohibit gambling advertising entirely:
  - Utah (US-UT): PROHIBITED
  - Hawaii (US-HI): PROHIBITED

RECOMMENDATION:
Proceed with human oversight. Ensure all signals used for this
campaign support age verification and respect self-exclusion lists.

Would you like me to find compliant signals for your Nevada
gambling campaign?"

You: "Yes, find compliant signals."

Claude: [Lists available signals with compliance status]
```

### Example 3: Scoring Signals for a Campaign

**Scenario:** You have 3 possible signals and want to know which is best.

```
You: "I'm running a retail fashion campaign targeting young professionals
     in major US cities. Compare these signals:

     1. verified-attention-quality
     2. retail-commerce-signal
     3. outdoor-recreation-enthusiasts

     Which should I use?"

Claude: "Let me score each signal for your retail fashion campaign..."

[Claude calls: score_signal() for each with retail context]

Claude: "Signal Comparison for Retail Fashion Campaign:

═══════════════════════════════════════════════════════════

SIGNAL 1: verified-attention-quality
Trust Score: 0.94 (Highly Trusted)
Objective Alignment: 0.72 (Good Fit)

✓ Excellent trust score and provenance
✓ Great for measuring campaign effectiveness
✗ Attention measurement, not audience targeting
✗ Doesn't directly reach fashion enthusiasts

RECOMMENDATION: Use for measurement, not targeting
BEST FOR: Optimizing ad viewability and attention

───────────────────────────────────────────────────────────

SIGNAL 2: retail-commerce-signal
Trust Score: 0.91 (Highly Trusted)
Objective Alignment: 0.93 (Strong Fit)

✓ Excellent trust score
✓ First-party commerce data from retail transactions
✓ Strong alignment with retail fashion objective
✓ Proven performance in fashion campaigns (+18% conversion)
✓ Good coverage in major US cities

RECOMMENDATION: ⭐ HIGHLY RECOMMENDED (Best choice)
BEST FOR: Targeting likely fashion purchasers

───────────────────────────────────────────────────────────

SIGNAL 3: outdoor-recreation-enthusiasts
Trust Score: 0.87 (Trusted)
Objective Alignment: 0.58 (Moderate Fit)

✓ Good trust score
✓ Good provenance and quality
✗ Audience is outdoor enthusiasts, not fashion focused
✗ Lower alignment with fashion retail objective
~ Could work for outdoor fashion/activewear subset

RECOMMENDATION: Consider only for outdoor fashion lines
BEST FOR: Activewear or outdoor fashion subcategories

═══════════════════════════════════════════════════════════

FINAL RECOMMENDATION:

Primary Signal: retail-commerce-signal (highest alignment)
Measurement: verified-attention-quality (track performance)
Consider: outdoor-recreation-enthusiasts (for activewear only)

EXPECTED PERFORMANCE:
- Reach: ~12M young professionals in major US cities
- Historical lift: +18% for fashion retail campaigns
- Trust level: Highly trusted, can be activated automatically

NEXT STEPS:
1. Activate retail-commerce-signal as primary targeting
2. Add verified-attention-quality for measurement
3. Set up conversion tracking
4. Budget allocation: 80% retail-commerce, 20% test outdoor signal

Would you like me to help configure these signals in your DSP?"
```

### Example 4: Auditing Signal Usage

**Scenario:** Your compliance officer needs to know what signals were used.

```
You: "We ran a spring alcohol campaign in the UK (campaign ID: spring-2026-uk).
     What signals did we use and was everything compliant?"

Claude: "Let me check the audit trail for that campaign..."

[Claude retrieves audit logs]

Claude: "Campaign Audit Report: spring-2026-uk

CAMPAIGN DETAILS:
- Category: Alcohol
- Market: United Kingdom
- Duration: May 15 - May 31, 2026
- Status: Completed

SIGNALS USED:

1. outdoor-recreation-enthusiasts
   - Activated: May 15, 2026 at 10:30 UTC
   - Trust Score: 0.87
   - Human Approver: jane.smith@brand.com
   - Compliance Status: ✓ COMPLIANT
   - Use Case: Contextual targeting only
   - Policy Bindings:
     * UK Alcohol Age Restriction (25+)
     * No Individual Profiling
   - Audit ID: aud_789ghi

2. premium-cocktail-contexts
   - Activated: May 16, 2026 at 14:22 UTC
   - Trust Score: 0.88
   - Human Approver: jane.smith@brand.com
   - Compliance Status: ✓ COMPLIANT
   - Use Case: Contextual targeting
   - Policy Bindings:
     * UK CAP Code compliance
     * Age verification required
   - Audit ID: aud_790jkl

COMPLIANCE SUMMARY:
✓ All signals verified before activation
✓ Human approval obtained for all activations (alcohol category)
✓ Age restrictions enforced (25+ UK minimum)
✓ Individual profiling disabled (alcohol policy)
✓ Audit trails complete
✓ No violations detected

PERFORMANCE:
- Impressions: 4.8M
- Reach: 2.3M
- Brand Lift: +14%
- Compliance: 100%

REGULATORY NOTES:
- Campaign fully compliant with UK CAP Code
- All signals meet Portman Group standards
- Audit logs retained for 90 days (regulatory requirement)

This campaign met all compliance requirements. Audit logs are
available for regulatory review if needed.

Would you like me to generate a formal compliance report?"

You: "Yes, generate the report for our records."

Claude: [Generates detailed compliance report in PDF format]
```

### Example 5: Getting Trust Recommendations

**Scenario:** You want AI to recommend the best signals for your needs.

```
You: "I'm a brand manager for an organic food company. We want to run
     a campaign promoting our sustainable farming practices. What signals
     should I use? Budget is $500K, targeting US consumers who care
     about sustainability."

Claude: "Let me find the best signals for your sustainable food campaign..."

[Claude searches signals, scores them for sustainability/food alignment]

Claude: "Sustainable Food Campaign Signal Recommendations

CAMPAIGN PROFILE:
- Brand: Organic food company
- Objective: Promote sustainable farming
- Target: Sustainability-conscious US consumers
- Budget: $500,000
- Category: General (food/retail)

═══════════════════════════════════════════════════════════

RECOMMENDED SIGNAL #1: sustainability-signal
Trust Score: 0.92 (Highly Trusted) ⭐
Alignment: 0.96 (Perfect Fit)

WHY THIS SIGNAL:
✓ Identifies consumers actively interested in sustainability
✓ First-party data from eco-conscious behaviors
✓ 85% precision score (highly accurate)
✓ Excellent coverage: 8.5M US consumers
✓ Proven performance: +24% conversion for sustainable brands
✓ Fresh data (updated daily)

PROVENANCE:
- Source: First-party survey + behavioral data
- Collection: Opt-in panel (explicit consent)
- Transparency: Full methodology documentation

COST: ~$6-8 CPM
ESTIMATED REACH: 8.5M consumers
BUDGET ALLOCATION: $300K (60%)

───────────────────────────────────────────────────────────

RECOMMENDED SIGNAL #2: retail-commerce-signal
Trust Score: 0.91 (Highly Trusted)
Alignment: 0.84 (Strong Fit)

WHY THIS SIGNAL:
✓ Identifies organic food purchasers
✓ First-party transaction data from grocery/retail
✓ High purchase intent (recent buyers)
✓ Good for driving conversions
✓ Complements sustainability signal nicely

PROVENANCE:
- Source: First-party transactional data
- Collection: Purchase history (with consent)
- Transparency: Clear data lineage

COST: ~$5-7 CPM
ESTIMATED REACH: 12M consumers (overlap with signal #1)
BUDGET ALLOCATION: $150K (30%)

───────────────────────────────────────────────────────────

RECOMMENDED SIGNAL #3: verified-attention-quality
Trust Score: 0.94 (Highly Trusted)
Alignment: 0.68 (Measurement)

WHY THIS SIGNAL:
✓ Measure attention quality (not targeting)
✓ Optimize ad placement for maximum impact
✓ Verify your message is being seen
✓ Industry-leading measurement standard

COST: ~$2-4 CPM uplift
BUDGET ALLOCATION: $50K (10% for measurement)

═══════════════════════════════════════════════════════════

TOTAL STRATEGY:

Primary Targeting: sustainability-signal (60%)
Secondary Targeting: retail-commerce-signal (30%)
Measurement Layer: verified-attention-quality (10%)

EXPECTED RESULTS:
- Total Reach: ~15M unique consumers
- Frequency: 3-4 impressions per person
- Expected Conversion Lift: +20-25%
- Brand Awareness Lift: +18-22%

COMPLIANCE STATUS:
✓ All signals verified for general category
✓ No human approval required (non-regulated)
✓ GDPR & CCPA compliant
✓ No restricted uses or geographies

CONFIDENCE LEVEL: High
All recommended signals have proven performance in sustainable
food/CPG campaigns and excellent trust scores.

NEXT STEPS:
1. Review signal manifests (I can show you details)
2. Approve budget allocation
3. Set up campaign in your DSP
4. I'll help configure signals correctly

Would you like me to show you the detailed manifests for any
of these signals, or help you set up the campaign?"

You: "This looks perfect. Help me set up the campaign."

Claude: [Provides step-by-step setup guidance]
```

---

## Platform-Specific Integration

OpenSignals works with the major advertising platforms. Here's how to integrate it with each:

### The Trade Desk

**What brand managers need to know:**

OpenSignals can verify signals before you activate them in The Trade Desk platform.

**How to use it:**

```
You: "I'm setting up a campaign in The Trade Desk. Can you verify
     the 'outdoor-recreation-enthusiasts' signal for alcohol advertising
     in California?"

AI: [Verifies signal for The Trade Desk alcohol use case]
    "Signal verified. Here's how to activate it in TTD:
     1. Navigate to Data > Third-Party Data
     2. Search for 'outdoor-recreation-enthusiasts'
     3. Apply these restrictions:
        - Age: 21+ (California minimum)
        - Geography: California only
        - Use contextual targeting (no behavioral)
     4. Enable audit logging
     5. Get human approval before activation"
```

**Technical note:** Your tech team can integrate OpenSignals verification into The Trade Desk API workflows. The brand manager just talks to the AI - the AI handles the verification automatically.

### Google DV360

**What brand managers need to know:**

OpenSignals helps ensure DV360 audience segments are trustworthy and compliant.

**How to use it:**

```
You: "I'm creating a line item in DV360 for a pharma campaign.
     Which audience segments are compliant for pharmaceutical
     advertising in the US?"

AI: [Checks compliance for pharma category]
    "For pharma in the US, these DV360 segments are compliant:

     ✓ Contextual health content segments
     ✗ Individual health condition targeting (prohibited by policy)

     In DV360:
     1. Use 'Affinity Categories > Health & Wellness'
     2. Apply contextual targeting only
     3. Exclude sensitive health conditions
     4. Enable frequency capping
     5. Get approval from compliance before launching"
```

**Technical note:** OpenSignals can be integrated with DV360 API to automatically filter segments by trust score and compliance status.

### Amazon DSP

**What brand managers need to know:**

OpenSignals validates Amazon audience signals and commerce data.

**How to use it:**

```
You: "I want to use Amazon's 'in-market for outdoor gear' audience
     for our sporting goods campaign. Is this signal trustworthy?"

AI: [Verifies Amazon audience signal]
    "Amazon's 'in-market for outdoor gear' signal:

     Trust Score: 0.89 (Trusted)
     Provenance: First-party shopping behavior
     Freshness: Updated daily
     Compliance: CCPA compliant

     ✓ Highly trustworthy signal
     ✓ Perfect fit for sporting goods campaign
     ✓ No special restrictions needed

     Recommended bid strategy:
     - CPM: $8-12 (premium audience)
     - Frequency cap: 5 per week
     - Budget allocation: 40% of campaign"
```

**Technical note:** Amazon DSP signals can be verified through OpenSignals API before campaign activation.

### Meta (Facebook/Instagram)

**What brand managers need to know:**

OpenSignals helps verify Meta's audience targeting options for compliance.

**How to use it:**

```
You: "I'm running a financial services campaign on Facebook. What
     targeting options are compliant with finance advertising rules?"

AI: [Checks Meta targeting for finance compliance]
    "Financial Services Campaign - Meta Targeting Compliance:

     ✓ ALLOWED:
     - Interest-based targeting (finance, investing)
     - Behavioral: Financial decision-makers
     - Lookalike audiences (with restrictions)
     - Geographic targeting

     ✗ PROHIBITED:
     - Detailed targeting based on debt/credit
     - Sensitive financial categories
     - Targeting financial vulnerability indicators

     META SPECIAL AD CATEGORY:
     - You must select 'Credit' or 'Employment' category
     - This limits some targeting options automatically
     - Human approval required before launch

     Recommended approach:
     1. Select 'Credit' special ad category in Meta
     2. Use broad interest targeting only
     3. Let Meta's algorithm optimize
     4. Get compliance team approval"
```

**Technical note:** Meta's advertising policies are built into the OpenSignals compliance rules for finance/credit categories.

### Custom DSP or Platform

**What brand managers need to know:**

OpenSignals works with any advertising platform through APIs.

**How your tech team integrates it:**

1. **Connect to OpenSignals API** (one-time setup)
2. **Add verification step** before signal activation
3. **Display trust scores** in your platform UI
4. **Log audit trails** for compliance

**What you do as a brand manager:**

Nothing changes. Just talk to your AI assistant, and it uses your platform's OpenSignals integration automatically.

```
You: "Set up a campaign on our custom DSP using sustainable
     consumer segments."

AI: [Verifies signals through your platform's OpenSignals integration]
    "I've verified all sustainable consumer segments in your DSP.
     Here are the trusted options..." [shows results]
```

---

## Works With Any AI

OpenSignals is **LLM-agnostic**. It works with any AI that can call APIs or use tools.

### Claude (via MCP)

**Status:** Available now

Claude Desktop supports OpenSignals through the Model Context Protocol (MCP):

```
Installation (one-time):
1. Install OpenSignals MCP server
2. Restart Claude Desktop
3. Start asking questions

Example:
You: "List available signals"
Claude: [Uses MCP to call OpenSignals]
        "Here are all available signals..."
```

**Best for:** Brand managers who use Claude Desktop for campaign planning

### ChatGPT (via Plugins/Actions)

**Status:** Integration available

ChatGPT can use OpenSignals through custom actions:

```
Setup (one-time, tech team):
1. Create OpenSignals custom action
2. Configure API endpoint
3. Enable for your organization

Usage:
You: "Verify this signal for alcohol advertising"
ChatGPT: [Uses OpenSignals action]
         "Signal verification complete..."
```

**Best for:** Teams already using ChatGPT Enterprise

### Google Gemini (via Extensions)

**Status:** Integration available

Gemini can integrate OpenSignals through extensions:

```
Setup (tech team):
1. Build Gemini extension for OpenSignals
2. Deploy to Google Cloud
3. Enable for your organization

Usage:
You: "Check compliance for gambling signals"
Gemini: [Uses OpenSignals extension]
        "Compliance check complete..."
```

**Best for:** Organizations using Google Workspace and Gemini

### Open Source LLMs (via API)

**Status:** Works with any LLM

Any AI that can call APIs can use OpenSignals:

- Llama (Meta)
- Mistral
- Anthropic Claude API
- OpenAI API
- Any custom LLM deployment

**How it works:**
1. Your AI makes HTTP requests to OpenSignals API
2. Parses JSON responses
3. Presents results in natural language

```python
# Behind the scenes (you don't write this, your tech team does)
response = requests.post("https://opensignals-api.example.com/verify",
    json={
        "signal_id": "outdoor-enthusiasts",
        "category": "alcohol",
        "market": "GB"
    })

result = response.json()
# AI converts to natural language for you
```

**Best for:** Custom AI deployments and specialized use cases

### Any Future LLM

Because OpenSignals uses standard APIs and protocols:

- Any new AI can integrate it
- No vendor lock-in
- No proprietary dependencies
- Future-proof architecture

**This means:** Whatever AI assistant you use in 2025, 2026, or 2030, it can use OpenSignals.

---

## Super Simple Activation

The simplest possible interactions. Just talk naturally.

### Example 1: One-Sentence Verification

```
You: "Is outdoor-recreation-enthusiasts signal safe for UK alcohol ads?"

AI: "Yes, with conditions: human approval required, no individual
     profiling, age 25+. Trust score: 0.87."
```

Done. 10 seconds.

### Example 2: Quick Compliance Check

```
You: "Can I advertise gambling in Utah?"

AI: "No. Gambling advertising is prohibited in Utah."
```

Done. 5 seconds.

### Example 3: Signal Recommendation

```
You: "I need signals for sustainable fashion in California. What do you recommend?"

AI: "Use 'sustainability-signal' (trust: 0.92) + 'retail-commerce-signal'
     (trust: 0.91). Both compliant, no restrictions."
```

Done. 15 seconds.

### Example 4: Audit Request

```
You: "Did we use compliant signals last month?"

AI: "Checked all signals. 100% compliant. 5 signals used, all verified,
     all had human approval where required."
```

Done. 10 seconds.

### Example 5: Trust Score Check

```
You: "What's the trust score for signal X?"

AI: "0.87. Trusted band. Good provenance, fresh data, GDPR compliant."
```

Done. 5 seconds.

**The pattern:**

1. Ask a question in plain English
2. AI verifies using OpenSignals
3. Get answer in seconds
4. Make confident decision

**No forms. No clicks. No technical knowledge. Just talk.**

---

## Embedding in Your Workflow

### Embed in DSP Workflow

**Scenario:** You want every signal to be verified before it goes live.

**How it works:**

```
Your DSP workflow before OpenSignals:
1. Select signal
2. Configure campaign
3. Launch
4. Hope it's compliant

Your DSP workflow with OpenSignals:
1. Select signal
2. AI automatically verifies signal
3. Shows trust score + compliance status
4. Flags if human approval needed
5. Configure campaign
6. Launch with confidence
```

**What you do differently:** Nothing. The verification happens automatically in the background. You just see a trust badge next to each signal.

**Example:**

```
DSP Signal Selector:

[Signal: outdoor-recreation-enthusiasts]
[Trust Score: 0.87 ⭐ Trusted]
[Compliance: ✓ Approved for general, ⚠ Requires approval for alcohol]
[Provenance: First-party behavioral data]

[Add to Campaign Button]
```

**Technical setup (one-time):** Your tech team adds OpenSignals verification API to your DSP's signal activation workflow.

### Add Trust Scores to Bid Requests

**Scenario:** You want publishers to see that you're using trusted signals.

**How it works:**

When you bid on ad inventory, include OpenSignals trust scores in the bid request:

```
OpenRTB Bid Request (with OpenSignals):
{
  "imp": [{
    "id": "1",
    "ext": {
      "opensignals": {
        "signal_id": "outdoor-enthusiasts",
        "trust_score": 0.87,
        "verified_at": "2026-05-11T10:00:00Z"
      }
    }
  }]
}
```

**What you tell the AI:**

```
You: "Include OpenSignals trust scores in all my bid requests"

AI: [Configures DSP to append trust metadata]
    "Done. All bid requests now include signal trust scores."
```

**Why this matters:** Publishers can see you're using verified, trustworthy signals. This can improve your win rate on premium inventory.

### Create an OpenSignals Compliance Dashboard

**Scenario:** Your compliance officer wants to monitor all signal usage.

**What the dashboard shows:**

```
OPENSIGNALS COMPLIANCE DASHBOARD
Last 30 Days

SIGNALS USED: 12
✓ All verified: 12/12 (100%)
✓ Human approvals: 5/5 required approvals obtained
✓ Compliance violations: 0
✓ Audit logs: Complete

TRUST SCORE DISTRIBUTION:
Highly Trusted (0.90+): 4 signals (33%)
Trusted (0.75-0.89): 7 signals (58%)
Limited Trust (0.50-0.74): 1 signal (8%)

REGULATED CAMPAIGNS:
Alcohol: 2 campaigns (100% compliant)
Gambling: 1 campaign (100% compliant)
Finance: 1 campaign (100% compliant)

ALERTS: 0
APPROVALS PENDING: 0
```

**How to ask the AI for a report:**

```
You: "Show me our OpenSignals compliance dashboard for last month"

AI: [Generates dashboard with all metrics]
```

**Technical setup:** Dashboard pulls data from OpenSignals audit logs. Your tech team sets this up once, then you can ask the AI for reports anytime.

### Build an OpenSignals Signal Marketplace

**Scenario:** You want to create a curated marketplace of trusted signals.

**How it works:**

1. **Import signals** from multiple providers
2. **Verify each signal** using OpenSignals
3. **Display trust scores** prominently
4. **Let buyers filter** by trust score, category, compliance
5. **Enable one-click activation** for approved signals

**Example marketplace:**

```
TRUSTED SIGNAL MARKETPLACE
Powered by OpenSignals

[Filter: Trust Score > 0.80] [Filter: Alcohol Compliant] [Search]

┌─────────────────────────────────────────────────────────┐
│ outdoor-recreation-enthusiasts                          │
│ Trust Score: 0.87 ⭐ Trusted                            │
│ Provider: DataProvider Co                               │
│ Coverage: 2.4M US consumers                             │
│ CPM: $3.50 - $5.00                                      │
│ Compliance: ✓ General, ⚠ Alcohol (approval required)   │
│                                                          │
│ [View Full Manifest] [Add to Campaign]                  │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ sustainability-signal                                   │
│ Trust Score: 0.92 ⭐ Highly Trusted                     │
│ Provider: GreenData Inc                                 │
│ Coverage: 8.5M US consumers                             │
│ CPM: $6.00 - $8.00                                      │
│ Compliance: ✓ All categories                            │
│                                                          │
│ [View Full Manifest] [Add to Campaign]                  │
└─────────────────────────────────────────────────────────┘
```

**What you ask the AI:**

```
You: "Show me all signals with trust score above 0.85 that are
     compliant for alcohol advertising"

AI: [Filters marketplace using OpenSignals verification]
    "Found 3 signals that meet your criteria..."
```

**Technical setup:** Marketplace pulls OpenSignals manifests for all signals, displays trust metadata, and enables filtering/search.

---

## For Technical Teams

While this guide is for non-technical users, here's what technical teams need to know to enable the simple experiences above.

### Integration Methods

**Method 1: MCP Server (Easiest for Claude)**

Install the OpenSignals MCP server:

```bash
cd opensignals-protocol/mcp-server
./install.sh
```

Configure Claude Desktop:

```json
{
  "mcpServers": {
    "opensignals-protocol": {
      "command": "/path/to/venv/bin/python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

**Method 2: REST API (Universal)**

Call OpenSignals HTTP endpoints:

```javascript
// Verify a signal
const response = await fetch('https://governance.brand.com/opensignals/verify', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    signal_id: 'outdoor-enthusiasts',
    category: 'alcohol',
    market: 'GB',
    intended_use: 'contextual_targeting'
  })
});

const result = await response.json();
// Returns: { decision, trust_score, conditions, policy_bindings, reasoning }
```

**Method 3: Python SDK (For Custom Apps)**

```python
from opensignals import OpenSignalsClient

client = OpenSignalsClient()

# Verify signal
result = client.verify_signal(
    signal_id='outdoor-enthusiasts',
    category='alcohol',
    market='GB',
    intended_use='contextual_targeting'
)

print(f"Decision: {result.decision}")
print(f"Trust Score: {result.trust_score}")
```

**Method 4: Embed in Existing Systems**

Add OpenSignals verification to your existing workflow:

```python
# In your DSP signal activation workflow
def activate_signal(signal_id, campaign_context):
    # Add this verification step
    verification = opensignals.verify_signal(signal_id, campaign_context)

    if verification.decision == 'rejected':
        raise SignalNotApprovedError(verification.reasoning)

    if verification.approval_required:
        # Trigger human approval workflow
        approval_id = request_human_approval(signal_id, verification)
        wait_for_approval(approval_id)

    # Proceed with activation
    activate_on_platform(signal_id, campaign_context)

    # Log for audit
    opensignals.audit_signal_usage(signal_id, campaign_context)
```

### API Endpoints

**Verify Signal:**
```
POST /opensignals/verify
Body: { signal_id, context: { brand, category, market, intended_use } }
Returns: { decision, trust_score, conditions, policy_bindings, reasoning }
```

**Get Signal Manifest:**
```
GET /.well-known/opensignals/{signal_id}
Returns: Complete OpenSignals manifest JSON
```

**Check Compliance:**
```
GET /opensignals/compliance?category=alcohol&market=GB
Returns: { compliance_requirements, restrictions, minimum_age, frameworks }
```

**Score Signal:**
```
POST /opensignals/score
Body: { signal_id, objective: { campaign_goal, target_audience, kpis } }
Returns: { objective_alignment_score, recommendation, reasoning }
```

**Audit Signal Usage:**
```
POST /opensignals/audit
Body: { signal_id, event_type, context, activation_details }
Returns: { audit_id, status, retention_until }
```

### Example Integration: Adding to The Trade Desk

```javascript
// Add verification before TTD activation
class TTDCampaignManager {
  async activateSignal(signalId, campaignConfig) {
    // Verify with OpenSignals first
    const verification = await this.openSignals.verify({
      signal_id: signalId,
      category: campaignConfig.category,
      market: campaignConfig.market,
      intended_use: campaignConfig.intended_use
    });

    // Check decision
    if (verification.decision === 'rejected') {
      throw new Error(`Signal not approved: ${verification.reasoning}`);
    }

    // Handle human approval if needed
    if (verification.approval_required) {
      const approved = await this.requestHumanApproval(verification);
      if (!approved) {
        throw new Error('Human approval denied');
      }
    }

    // Activate in TTD
    const ttdResult = await this.ttdClient.activateAudience({
      data_element_id: signalId,
      advertiser_id: campaignConfig.advertiser_id,
      // Attach trust metadata
      metadata: {
        opensignals_verified: true,
        trust_score: verification.trust_score,
        verified_at: new Date().toISOString()
      }
    });

    // Log audit trail
    await this.openSignals.audit({
      signal_id: signalId,
      event_type: 'signal_activated',
      platform: 'the_trade_desk',
      context: campaignConfig,
      trust_score: verification.trust_score
    });

    return ttdResult;
  }
}
```

### Example Integration: Adding to DV360

```python
# Add verification to DV360 line item creation
class DV360CampaignManager:
    def create_line_item_with_verified_signals(self, line_item_config):
        # Verify all audience segments
        verified_segments = []

        for segment_id in line_item_config.audience_segments:
            verification = self.opensignals.verify_signal(
                signal_id=segment_id,
                category=line_item_config.category,
                market=line_item_config.market,
                intended_use='targeting'
            )

            if verification.decision in ['approved', 'approved_with_conditions']:
                verified_segments.append({
                    'segment_id': segment_id,
                    'trust_score': verification.trust_score,
                    'conditions': verification.conditions
                })
            else:
                # Log rejected segment
                logger.warning(f"Segment {segment_id} rejected: {verification.reasoning}")

        if not verified_segments:
            raise NoApprovedSignalsError("No segments passed verification")

        # Create DV360 line item with verified segments only
        line_item = self.dv360_client.create_line_item(
            advertiser_id=line_item_config.advertiser_id,
            targeting={
                'audience_segments': [s['segment_id'] for s in verified_segments]
            },
            # Attach OpenSignals metadata
            partner_data={
                'opensignals_verified': True,
                'verified_segments': verified_segments
            }
        )

        # Audit each segment activation
        for segment in verified_segments:
            self.opensignals.audit_signal_usage(
                signal_id=segment['segment_id'],
                event_type='signal_activated',
                platform='dv360',
                context=line_item_config,
                trust_score=segment['trust_score']
            )

        return line_item
```

### Schema Validation

Validate manifests before processing:

```python
import jsonschema

# Load schema
with open('schemas/v0.1/open-signal-manifest.schema.json') as f:
    schema = json.load(f)

# Validate manifest
try:
    jsonschema.validate(manifest, schema)
    print("Manifest is valid")
except jsonschema.ValidationError as e:
    print(f"Manifest validation failed: {e.message}")
```

### Error Handling

Handle common errors gracefully:

```python
try:
    result = opensignals.verify_signal(signal_id, context)
except SignalNotFoundError:
    # Signal doesn't have an OpenSignals manifest
    # Fall back to manual review or reject
    logger.warning(f"Signal {signal_id} has no OpenSignals manifest")
    result = ManualReviewRequired(signal_id)

except ComplianceViolationError as e:
    # Signal violates compliance rules
    logger.error(f"Compliance violation: {e.message}")
    raise

except NetworkError:
    # Manifest fetch failed
    # Use cached manifest or fail gracefully
    result = use_cached_manifest(signal_id)
```

### Caching Strategy

Cache manifests to reduce latency:

```python
from functools import lru_cache
import time

class ManifestCache:
    def __init__(self, ttl=3600):  # 1 hour default
        self.cache = {}
        self.ttl = ttl

    def get(self, signal_id):
        if signal_id in self.cache:
            cached_at, manifest = self.cache[signal_id]
            if time.time() - cached_at < self.ttl:
                return manifest
        return None

    def set(self, signal_id, manifest):
        self.cache[signal_id] = (time.time(), manifest)

    def fetch_with_cache(self, signal_id, manifest_url):
        # Check cache
        manifest = self.get(signal_id)
        if manifest:
            return manifest

        # Fetch from source
        manifest = fetch_manifest(manifest_url)

        # Cache
        self.set(signal_id, manifest)

        return manifest
```

---

## Real-World Use Cases

### Use Case 1: Agency Managing 50 Brands

**Challenge:** Agency needs to verify signals for 50 different clients across multiple categories (retail, alcohol, pharma, finance, gambling).

**OpenSignals Solution:**

```
Agency Media Buyer: "I need to set up campaigns for these 5 clients today:
1. Premium spirits brand (alcohol, UK)
2. Online casino (gambling, Nevada)
3. Pain medication (pharma, US)
4. Credit card (finance, nationwide)
5. Organic groceries (general, California)

For each, find compliant signals and tell me which need human approval."

AI: [Verifies signals for all 5 campaigns in parallel]

"Campaign Verification Complete:

1. PREMIUM SPIRITS (Alcohol, UK)
   Recommended: outdoor-recreation-enthusiasts, premium-cocktail-contexts
   ⚠ Human approval required for both
   Trust scores: 0.87, 0.88
   Next step: Submit to client legal team

2. ONLINE CASINO (Gambling, Nevada)
   Recommended: contextual-entertainment-signal
   ⚠ Human approval required
   Trust score: 0.85
   Restriction: No behavioral targeting, contextual only

3. PAIN MEDICATION (Pharma, US)
   Recommended: contextual-health-content
   ⚠ Human approval required
   Trust score: 0.90
   Restriction: No health condition targeting

4. CREDIT CARD (Finance, US)
   Recommended: financial-decision-makers, retail-commerce-signal
   ⚠ Human approval required for both
   Trust scores: 0.88, 0.91
   Next step: Compliance review

5. ORGANIC GROCERIES (General, CA)
   Recommended: sustainability-signal, retail-commerce-signal
   ✓ No human approval needed (general category)
   Trust scores: 0.92, 0.91
   Action: Can activate immediately

SUMMARY:
- Total signals recommended: 9
- Requiring human approval: 7 (regulated categories)
- Ready to activate: 2 (general category)

I've drafted approval requests for all 7 regulated signals.
Would you like me to send them to the respective compliance teams?"
```

**Time saved:** 8-10 hours of manual research reduced to 2 minutes.

### Use Case 2: Compliance Officer Monthly Audit

**Challenge:** Compliance officer needs to audit all signal usage for regulatory report.

**OpenSignals Solution:**

```
Compliance Officer: "Generate a compliance audit report for all campaigns
                     last month. Include trust scores, approvals, violations."

AI: [Queries OpenSignals audit logs]

"COMPLIANCE AUDIT REPORT
May 2026

CAMPAIGNS AUDITED: 47
SIGNALS USED: 23 unique signals
TOTAL ACTIVATIONS: 156

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMPLIANCE STATUS:
✓ Verified signals: 156/156 (100%)
✓ Human approvals obtained: 45/45 (100%)
✓ Audit logs complete: 156/156 (100%)
✓ Policy violations: 0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BY CATEGORY:
General (non-regulated): 89 activations (✓ 100% compliant)
Alcohol: 28 activations (✓ 100% compliant)
Gambling: 15 activations (✓ 100% compliant)
Pharma: 12 activations (✓ 100% compliant)
Finance: 12 activations (✓ 100% compliant)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRUST SCORE DISTRIBUTION:
Highly Trusted (0.90+): 78 activations (50%)
Trusted (0.75-0.89): 72 activations (46%)
Limited Trust (0.50-0.74): 6 activations (4%)

All limited trust signals had human approval.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REGULATED CATEGORY COMPLIANCE:

Alcohol (28 activations):
✓ Human approval: 28/28
✓ Age verification enforced: 28/28
✓ Individual profiling disabled: 28/28
✓ Audit trails complete: 28/28

Gambling (15 activations):
✓ Human approval: 15/15
✓ Age verification (21+): 15/15
✓ Self-exclusion checks: 15/15
✓ No behavioral targeting: 15/15

Pharma (12 activations):
✓ Human approval: 12/12
✓ Contextual targeting only: 12/12
✓ No health data targeting: 12/12

Finance (12 activations):
✓ Human approval: 12/12
✓ Age verification (18+): 12/12
✓ No vulnerability targeting: 12/12

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

APPROVERS:
jane.smith@brand.com: 23 approvals
john.doe@brand.com: 15 approvals
sarah.jones@brand.com: 7 approvals

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINDINGS:
✓ No compliance violations detected
✓ All regulatory requirements met
✓ Audit trail complete and exportable
✓ All signals verified before activation

RECOMMENDATION:
Current compliance processes are working effectively.
Continue monthly audits.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Detailed logs available for export in CSV/PDF format.
Would you like me to generate the formal regulatory report?"
```

**Time saved:** 2-3 days of manual audit reduced to 2 minutes.

### Use Case 3: Brand Manager Learning Curve

**Challenge:** New brand manager doesn't understand signal verification or compliance.

**OpenSignals Solution:**

```
New Brand Manager: "I'm new to this. Can you explain what I need to
                    do to run a compliant campaign?"

AI: "I'll walk you through it step by step.

STEP 1: UNDERSTAND YOUR CAMPAIGN CATEGORY

First, tell me: What type of product are you advertising?
- General products (no restrictions)
- Alcohol
- Gambling
- Pharmaceuticals
- Financial services
- Other regulated category"

New Brand Manager: "We sell premium whiskey, so alcohol."

AI: "Got it. Alcohol is a regulated category. Here's what that means:

ALCOHOL ADVERTISING REQUIREMENTS:
✓ Every signal needs human approval (legal/compliance team)
✓ Age restrictions apply (minimum age varies by country)
✓ You can only use contextual targeting (not individual profiling)
✓ All activations must be logged for audits

Don't worry - I'll help you with all of this.

STEP 2: TELL ME ABOUT YOUR CAMPAIGN

Where are you advertising and who are you targeting?"

New Brand Manager: "UK market, targeting adults 25+ who enjoy premium
                    spirits and outdoor activities."

AI: "Perfect. Let me find signals that match your needs...

[Verifies signals for UK alcohol campaign]

STEP 3: RECOMMENDED SIGNALS

I found 2 signals that are perfect for your campaign:

1. outdoor-recreation-enthusiasts
   ⭐ Trust Score: 0.87 (Trusted)
   👥 Reach: 2.4M UK adults 25+
   💰 Cost: £3.50-5.00 CPM
   ✓ Compliant for UK alcohol advertising
   ⚠ Needs approval from legal team

2. premium-cocktail-contexts
   ⭐ Trust Score: 0.88 (Trusted)
   👥 Reach: 4.5M UK adults
   💰 Cost: £4.50-6.00 CPM
   ✓ Compliant for UK alcohol advertising
   ⚠ Needs approval from legal team

STEP 4: NEXT ACTIONS

Here's what you need to do:

1. I'll create approval requests for both signals
2. You send them to your legal/compliance team
3. They review and approve (usually 1-2 days)
4. Once approved, you activate the signals
5. I'll log everything for audit trail

Would you like me to draft the approval requests now?"

New Brand Manager: "Yes please!"

AI: [Generates detailed approval requests with all compliance info]

"Approval requests ready. I've included:
- Signal trust scores and provenance
- UK alcohol advertising compliance info
- Age restriction requirements (25+)
- Contextual targeting confirmation
- Links to full signal manifests

Send these to your legal team. When they approve, just tell me
and I'll help you activate the campaign.

Any questions about the process?"

New Brand Manager: "This is so much easier than I expected. Thank you!"
```

**Learning curve:** Reduced from weeks to 5 minutes.

---

## Summary: The Power of Natural Language

OpenSignals Protocol makes advertising signal verification as simple as having a conversation.

### What You've Learned:

1. **You don't need to be technical** - Just talk to your AI assistant
2. **Verification happens in seconds** - No more days of manual research
3. **Works with any AI** - Claude, ChatGPT, Gemini, or custom LLMs
4. **Integrates anywhere** - DSPs, APIs, dashboards, marketplaces
5. **Compliance is automatic** - AI checks all the rules for you
6. **Audit trails are built-in** - Everything is logged automatically

### The Future of Signal Verification:

```
OLD WAY (Manual):
- Read documentation (hours)
- Check compliance rules (hours)
- Email legal team (days)
- Wait for approval (days)
- Hope you got it right (stress)

NEW WAY (AI + OpenSignals):
- Ask AI one question (seconds)
- Get verified answer (seconds)
- Make confident decision (seconds)
- Launch compliant campaign (minutes)
- Sleep well knowing it's audited (peace of mind)
```

### Get Started Today:

1. **If you use Claude Desktop:** Install the MCP server (15 minutes)
2. **If you use another AI:** Ask your tech team to integrate the API (1-2 days)
3. **If you're a developer:** See the [technical documentation](../README.md)

### Questions?

- **Documentation:** [Main README](../README.md)
- **Technical Specs:** [Protocol Specification](../specs/opensignals-v0.1.md)
- **Examples:** [Signal Examples](../examples/)
- **MCP Server:** [MCP Server Guide](../mcp-server/README.md)
- **Community:** [GitHub Discussions](https://github.com/Samrajtheailyceum/opensignals-protocol/discussions)

---

**OpenSignals Protocol: Making advertising signals trustworthy, transparent, and accessible to everyone.**

**No code required. Just talk.**

---

**Last Updated:** May 11, 2026
**Version:** 1.0
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
