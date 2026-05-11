# OpenSignals MCP Server - Quick Start Guide

Get up and running with the OpenSignals MCP server in under 5 minutes.

## 30-Second Setup

```bash
cd opensignals-protocol/mcp-server
./install.sh
# Follow prompts, restart Claude Desktop if configuring
```

## What You Get

An MCP server that lets AI agents:
- Discover advertising signals with trust scores
- Verify signals for compliance (alcohol, gambling, pharma, finance)
- Calculate 7-dimensional trust scores
- Log signal usage for audit trails
- Check category/market compliance rules

## Your First Prompt

After installation, in Claude Desktop:

```
List all available advertising signals and show me their trust scores
```

Expected response:
```
I found 4 advertising signals:

1. verified-attention-quality (Attention)
   Trust Score: 0.94 - Highly Trusted
   Status: Active

2. outdoor-recreation-enthusiasts (Audience)
   Trust Score: 0.85 - Trusted
   Status: Active

3. retail-commerce-signal (Commerce)
   Trust Score: 0.88 - Trusted
   Status: Active

4. sustainability-signal (Environmental)
   Trust Score: 0.82 - Trusted
   Status: Active
```

## Try These Next

### Compliance Check
```
I'm planning an alcohol campaign in the UK. What compliance requirements apply?
```

### Signal Verification
```
Verify if the outdoor-recreation-enthusiasts signal is compliant for alcohol advertising in Great Britain
```

### Trust Scoring
```
What's the detailed trust score breakdown for the attention measurement signal?
```

### Full Workflow
```
I'm a media buyer for a premium spirits brand running a UK campaign targeting outdoor enthusiasts aged 25+. Find compliant signals and recommend the best one.
```

## Understanding the Response

### Verification Response
```json
{
  "decision": "approved_with_conditions",
  "approval_required": true,
  "trust_score": 0.87,
  "trust_band": "trusted",
  "conditions": [
    "human_approval_required",
    "sensitive_category_alcohol",
    "audit_required"
  ],
  "reasoning": "Signal approved for contextual_targeting. Human approval required for alcohol category."
}
```

**Key fields:**
- `decision`: approved, approved_with_conditions, or rejected
- `approval_required`: true if human must approve before activation
- `trust_score`: 0-1 score (0.75+ is trusted)
- `conditions`: What restrictions apply

### Trust Score Response
```json
{
  "scores": {
    "coverage": 0.89,
    "freshness": 0.98,
    "precision": 0.93,
    "stability": 0.95,
    "explainability": 0.95,
    "compliance": 0.97,
    "overall": 0.94
  },
  "trust_band": "highly_trusted",
  "autonomy_recommendation": "autonomous_with_limits"
}
```

**Trust bands:**
- 0.90-1.00: Highly trusted (can be autonomous)
- 0.75-0.89: Trusted (needs governance checks)
- 0.50-0.74: Limited trust (human review)
- Below 0.50: Don't use without explicit approval

## Common Workflows

### 1. Pre-Campaign Compliance Check

```
What are the rules for gambling advertising in the US?
```

Use this to understand requirements BEFORE searching for signals.

### 2. Signal Discovery

```
Show me all attention measurement signals with trust score above 0.85
```

Use filters to narrow down candidates quickly.

### 3. Compliance Verification

```
Check if the retail-commerce-signal is compliant for financial services advertising in Germany
```

ALWAYS verify before activation, especially for regulated categories.

### 4. Audit Logging

```
Log that we activated the outdoor-recreation signal for campaign spring-2026-uk with human approval from jane.smith@brand.com
```

Required for regulated categories, recommended for all.

## Compliance Categories

### Alcohol
- Human approval: Required
- Age: 25+ (UK), 21+ (US)
- Uses: Contextual only
- Restricted: Saudi Arabia, UAE

### Gambling
- Human approval: Required
- Age: 21+
- Uses: Contextual only
- Restricted: Utah, Saudi Arabia, UAE

### Pharma
- Human approval: Required
- Uses: Contextual, geographic
- No health data targeting
- FDA/EMA guidelines apply

### Finance
- Human approval: Required
- Age: 18+
- No vulnerability targeting
- Risk warnings required

### General
- Human approval: Not required (if trust > 0.85)
- Standard advertising rules

## Example Agent Scenario

**Scenario:** Alcohol campaign in UK

**Agent workflow:**

1. **Check compliance first:**
   ```
   What compliance requirements apply for alcohol in GB?
   ```

   Response: Human approval required, age 25+, contextual only

2. **Find signals:**
   ```
   List signals suitable for UK outdoor enthusiasts
   ```

   Response: Found outdoor-recreation-enthusiasts signal

3. **Verify compliance:**
   ```
   Verify outdoor-recreation signal for alcohol in GB with contextual targeting
   ```

   Response: Approved with conditions, human approval needed

4. **Get trust score:**
   ```
   Score the outdoor-recreation signal
   ```

   Response: Trust 0.87, trusted band, good fit

5. **Get human approval** (outside MCP server)

6. **Activate signal** (via AdCP or other)

7. **Log activation:**
   ```
   Log that outdoor-recreation signal was activated for spring-2026-uk by jane.smith@brand.com
   ```

   Response: Audit logged with ID

## Troubleshooting

### Server not showing in Claude Desktop

1. Check config file exists:
   ```bash
   cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

2. Verify paths are absolute (not relative)

3. Restart Claude Desktop COMPLETELY

4. Check Claude Desktop logs for errors

### Tools not working

1. Test server directly:
   ```bash
   cd opensignals-protocol/mcp-server
   source venv/bin/activate
   python test_server.py
   ```

2. Verify examples exist:
   ```bash
   ls ../examples/*.json
   ```

### Import errors

```bash
source venv/bin/activate
pip install -r requirements.txt
```

## Files Overview

```
mcp-server/
├── server.py              # Main server (run this)
├── install.sh             # Installation script
├── requirements.txt       # Dependencies
├── config.json           # Configuration template
├── .env.example          # Environment variables
├── test_server.py        # Test suite
├── README.md             # Full documentation
├── QUICKSTART.md         # This file
├── EXAMPLE_PROMPTS.md    # 50+ example prompts
├── ARCHITECTURE.md       # Technical architecture
└── IMPLEMENTATION_SUMMARY.md  # What was built
```

## Key Concepts

### Tool = Function agents can call
- `verify_signal` - Check compliance
- `score_signal` - Calculate trust
- `list_signals` - Browse available
- `check_compliance` - Get requirements
- `audit_signal_usage` - Log activation
- `get_signal_manifest` - Get full details

### Resource = Data agents can read
- `opensignals://manifests/{id}` - Signal manifests
- `opensignals://schemas/{name}` - JSON schemas
- `opensignals://docs/{name}` - Documentation

### Trust Score = Quality metric (0-1)
- 7 dimensions: coverage, freshness, precision, stability, explainability, compliance, overall
- 5 bands: highly trusted, trusted, limited trust, low trust, unsafe
- Determines autonomy level

### Compliance = Category rules
- Alcohol, gambling, pharma, finance have strict rules
- Human approval required for sensitive categories
- Market restrictions enforced
- Age requirements checked

## Next Steps

1. **Read full documentation:**
   - `README.md` - Complete guide
   - `EXAMPLE_PROMPTS.md` - 50+ examples
   - `ARCHITECTURE.md` - Technical details

2. **Try advanced workflows:**
   - Multi-market campaigns
   - Signal comparison
   - Autonomous decision making
   - Integration with AdCP

3. **Customize:**
   - Edit `.env` for custom paths
   - Add compliance rules for new categories
   - Extend tools for your use case

4. **Integrate:**
   - Use with AdCP for signal activation
   - Include trust scores in OpenRTB bids
   - Connect to approval workflows
   - Export audit logs

## Support

- Issues: GitHub Issues with `mcp-server` label
- Documentation: See README.md
- Protocol: ../specs/opensignals-v0.1.md
- Examples: See EXAMPLE_PROMPTS.md

## One-Liner Test

```bash
cd opensignals-protocol/mcp-server && ./install.sh && source venv/bin/activate && python test_server.py
```

If you see "All tests passed!", you're good to go!

---

**Ready to build agentic advertising workflows?**

Start with: "List all available advertising signals"
