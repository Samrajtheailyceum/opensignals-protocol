# OpenSignals MCP Server Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     AI Agent (Claude)                        │
│                                                              │
│  "Verify if outdoor-recreation signal is compliant          │
│   for alcohol advertising in the UK"                        │
└───────────────────────┬──────────────────────────────────────┘
                        │ Natural Language
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              Model Context Protocol (MCP)                    │
│                   JSON-RPC 2.0 / stdio                       │
└───────────────────────┬──────────────────────────────────────┘
                        │ Tool Calls & Resources
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│            OpenSignals MCP Server (server.py)                │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                   Tools Layer                         │  │
│  │  • get_signal_manifest   • verify_signal             │  │
│  │  • score_signal          • audit_signal_usage        │  │
│  │  • list_signals          • check_compliance          │  │
│  └──────────────────────────────────────────────────────┘  │
│                            │                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                  Business Logic                       │  │
│  │  • Trust Scoring Engine                              │  │
│  │  • Compliance Verification Engine                    │  │
│  │  • Audit Log Generator                               │  │
│  │  • Policy Binding Engine                             │  │
│  └──────────────────────────────────────────────────────┘  │
│                            │                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                  Resources Layer                      │  │
│  │  • Signal Manifests (opensignals://manifests/*)      │  │
│  │  • JSON Schemas (opensignals://schemas/*)            │  │
│  │  • Documentation (opensignals://docs/*)              │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────┬──────────────────────────────────────┘
                        │ File System I/O
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│           OpenSignals Protocol Repository                    │
│                                                              │
│  examples/                   schemas/v0.1/                   │
│  ├── attention-signal.json   ├── open-signal-manifest...    │
│  ├── alcohol-contextual...   ├── verify-signal-request...   │
│  ├── retail-commerce...      ├── trust-score.schema.json    │
│  └── sustainability...       └── audit-signal-usage...       │
│                                                              │
│  specs/                      docs/                           │
│  └── opensignals-v0.1.md    └── (various documentation)      │
└─────────────────────────────────────────────────────────────┘
```

## Component Architecture

### 1. Tools Layer (6 tools)

```
┌──────────────────────────────────────────────────────────────┐
│                      MCP Tools                               │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  get_signal_manifest(signal_id)                             │
│  ├─ Load manifest from examples/                            │
│  └─ Return complete signal metadata                         │
│                                                              │
│  verify_signal(signal_id, context) ⭐ PRIMARY TOOL          │
│  ├─ Load manifest                                           │
│  ├─ Check signal status                                     │
│  ├─ Verify geographic restrictions                          │
│  ├─ Check permitted uses                                    │
│  ├─ Calculate trust score                                   │
│  ├─ Apply category compliance rules                         │
│  ├─ Determine human approval requirement                    │
│  └─ Return decision + conditions + reasoning                │
│                                                              │
│  score_signal(signal_id, context?)                          │
│  ├─ Load manifest                                           │
│  ├─ Extract quality scores                                  │
│  ├─ Calculate 7-dimensional breakdown                       │
│  ├─ Determine trust band                                    │
│  └─ Return scores + recommendation                          │
│                                                              │
│  audit_signal_usage(signal_id, event_type, context)         │
│  ├─ Generate audit ID                                       │
│  ├─ Create audit log entry                                  │
│  ├─ Set retention period (90 days)                          │
│  └─ Return audit receipt                                    │
│                                                              │
│  list_signals(filters?)                                     │
│  ├─ Scan examples/ directory                                │
│  ├─ Load all manifests                                      │
│  ├─ Apply filters (type, status, trust score)              │
│  └─ Return signal list                                      │
│                                                              │
│  check_compliance(category, market)                         │
│  ├─ Load category rules                                     │
│  ├─ Check market restrictions                               │
│  ├─ Return compliance requirements                          │
│  └─ Provide recommendation                                  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 2. Trust Scoring Engine

```
┌──────────────────────────────────────────────────────────────┐
│               Trust Scoring Engine                           │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Input: Signal Manifest + Optional Context                  │
│                                                              │
│  Dimension Extraction:                                       │
│  ├─ Coverage Score (from quality.coverage_score)            │
│  ├─ Freshness Score (from quality.freshness_score)          │
│  ├─ Precision Score (from quality.precision_score)          │
│  ├─ Stability Score (from quality.stability_score)          │
│  ├─ Explainability Score (from quality.explainability_score)│
│  ├─ Compliance Score (from quality.compliance_safety_score) │
│  └─ Overall Score (from quality.overall_trust_score)        │
│                                                              │
│  Detail Enrichment:                                          │
│  ├─ Coverage: geographic_markets, reach_estimate            │
│  ├─ Freshness: last_updated, update_frequency               │
│  ├─ Precision: methodology                                  │
│  ├─ Stability: signal status                                │
│  ├─ Explainability: transparency level                      │
│  └─ Compliance: frameworks                                  │
│                                                              │
│  Trust Band Calculation:                                     │
│  ├─ 0.90-1.00 → highly_trusted                             │
│  ├─ 0.75-0.89 → trusted                                    │
│  ├─ 0.50-0.74 → limited_trust                              │
│  ├─ 0.25-0.49 → low_trust                                  │
│  └─ 0.00-0.24 → unsafe                                     │
│                                                              │
│  Autonomy Recommendation:                                    │
│  ├─ highly_trusted → autonomous_with_limits                 │
│  ├─ trusted → approve_with_human                            │
│  ├─ limited_trust → recommend                               │
│  ├─ low_trust → observe                                     │
│  └─ unsafe → blocked                                        │
│                                                              │
│  Output: Complete Trust Score Object                         │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 3. Compliance Verification Engine

```
┌──────────────────────────────────────────────────────────────┐
│           Compliance Verification Engine                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Input: Manifest + Context (category, market, intended_use) │
│                                                              │
│  Step 1: Signal Status Check                                │
│  ├─ IF status NOT IN [active, experimental]                 │
│  └─ THEN reject (signal not available)                      │
│                                                              │
│  Step 2: Geographic Restriction Check                       │
│  ├─ Load permissioning.usage_restrictions.geographic_...    │
│  ├─ IF market IN restricted_markets                         │
│  └─ THEN reject (market restricted)                         │
│                                                              │
│  Step 3: Permitted Use Check                                │
│  ├─ Load permissioning.permitted_uses                       │
│  ├─ IF intended_use NOT IN permitted_uses                   │
│  └─ THEN reject (use case not allowed)                      │
│                                                              │
│  Step 4: Trust Score Calculation                            │
│  ├─ Call trust_scoring_engine()                             │
│  └─ Get overall_trust_score + trust_band                    │
│                                                              │
│  Step 5: Category Compliance Rules                          │
│  ├─ Load rules for category (alcohol, gambling, etc.)      │
│  ├─ Apply human_approval_required flag                      │
│  ├─ Apply age_restrictions                                  │
│  ├─ Apply prohibited_uses                                   │
│  └─ Apply audit_required flag                               │
│                                                              │
│  Step 6: Trust Threshold Check                              │
│  ├─ IF trust_score < 0.75                                  │
│  └─ THEN human_approval_required = true                     │
│                                                              │
│  Step 7: Decision Generation                                │
│  ├─ IF trust_score >= 0.75 AND no human approval           │
│  │   THEN decision = "approved"                             │
│  ├─ ELSE IF trust_score >= 0.50                            │
│  │   THEN decision = "approved_with_conditions"             │
│  └─ ELSE decision = "rejected"                              │
│                                                              │
│  Step 8: Condition Assembly                                 │
│  ├─ Add human_approval_required (if applicable)             │
│  ├─ Add sensitive_category_X (if applicable)                │
│  ├─ Add audit_required (if applicable)                      │
│  ├─ Add no_individual_profiling_for_X (if applicable)       │
│  └─ Add age_verification_required (if applicable)           │
│                                                              │
│  Step 9: Policy Binding                                     │
│  ├─ IF category = alcohol                                   │
│  │   THEN bind alcohol_age_restriction policy               │
│  ├─ IF category = gambling                                  │
│  │   THEN bind gambling_self_exclusion policy               │
│  └─ (etc for other categories)                              │
│                                                              │
│  Output: Verification Decision Object                        │
│  ├─ decision (approved/approved_with_conditions/rejected)   │
│  ├─ approval_required (boolean)                             │
│  ├─ trust_score (number)                                    │
│  ├─ trust_band (string)                                     │
│  ├─ conditions (array)                                      │
│  ├─ policy_bindings (array)                                 │
│  └─ reasoning (string)                                      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 4. Compliance Rules Database

```
┌──────────────────────────────────────────────────────────────┐
│                 Compliance Rules                             │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ALCOHOL:                                                    │
│  ├─ human_approval_required: true                           │
│  ├─ age_restrictions: true                                  │
│  ├─ minimum_age: 25 (GB, IE) | 21 (US, others)             │
│  ├─ prohibited_uses: [individual_profiling, behavioral...]  │
│  ├─ allowed_uses: [contextual_targeting, geographic...]     │
│  ├─ audit_required: true                                    │
│  ├─ restricted_markets: [SA, AE]                            │
│  └─ compliance_frameworks: [local_alcohol_standards]        │
│                                                              │
│  GAMBLING:                                                   │
│  ├─ human_approval_required: true                           │
│  ├─ age_restrictions: true                                  │
│  ├─ minimum_age: 21                                         │
│  ├─ prohibited_uses: [individual_profiling, lookalike...]   │
│  ├─ allowed_uses: [contextual_targeting]                    │
│  ├─ audit_required: true                                    │
│  ├─ restricted_markets: [US-UT, AE, SA]                     │
│  ├─ self_exclusion_required: true                           │
│  └─ compliance_frameworks: [gambling_commission_rules]      │
│                                                              │
│  PHARMA:                                                     │
│  ├─ human_approval_required: true                           │
│  ├─ prohibited_uses: [individual_profiling, health_data...] │
│  ├─ allowed_uses: [contextual_targeting, geographic...]     │
│  ├─ audit_required: true                                    │
│  ├─ compliance_frameworks: [fda_guidelines, ema_guidelines] │
│  └─ prescription_restrictions: true                         │
│                                                              │
│  FINANCE:                                                    │
│  ├─ human_approval_required: true                           │
│  ├─ age_restrictions: true                                  │
│  ├─ minimum_age: 18                                         │
│  ├─ prohibited_uses: [financial_vulnerability_targeting]    │
│  ├─ allowed_uses: [contextual_targeting, demographic...]    │
│  ├─ audit_required: true                                    │
│  ├─ compliance_frameworks: [financial_advertising_standards]│
│  └─ risk_warnings_required: true                            │
│                                                              │
│  GENERAL:                                                    │
│  ├─ human_approval_required: false                          │
│  ├─ audit_required: false                                   │
│  └─ compliance_frameworks: [general_advertising_standards]  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 5. Data Flow - Typical Agent Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  Step 1: Agent Receives Campaign Brief                      │
│  Brand: Premium Spirits Co                                  │
│  Category: Alcohol                                          │
│  Market: GB (United Kingdom)                                │
│  Objective: Awareness + Brand Lift                          │
│  Budget: £200,000                                           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 2: check_compliance(category="alcohol", market="GB")  │
│  Returns: Compliance rules + restrictions                   │
│  → Human approval required                                  │
│  → Age 25+ required                                         │
│  → Contextual targeting only                                │
│  → Audit required                                           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 3: list_signals(filters)                              │
│  Returns: 4 available signals                               │
│  → attention-signal (trust: 0.94)                           │
│  → outdoor-recreation (trust: 0.85)                         │
│  → retail-commerce (trust: 0.88)                            │
│  → sustainability (trust: 0.82)                             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 4: For each promising signal...                       │
│                                                              │
│  4a. get_signal_manifest(signal_id)                         │
│  → Returns full manifest with metadata                      │
│                                                              │
│  4b. verify_signal(signal_id, context)                      │
│  → context = {category: alcohol, market: GB, use: ...}     │
│  → Returns: approved_with_conditions                        │
│  → Conditions: [human_approval, audit, no_profiling, ...]  │
│                                                              │
│  4c. score_signal(signal_id, context)                       │
│  → Returns 7D trust score + trust band                      │
│  → Recommendation: approve_with_human                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 5: Agent Analysis & Selection                         │
│  → Filter out rejected signals                              │
│  → Rank by trust score + objective alignment               │
│  → Select: outdoor-recreation (best fit for audience)       │
│  → Prepare recommendation for human                         │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 6: Human Approval Workflow                            │
│  Agent presents:                                            │
│  → Signal: outdoor-recreation-enthusiasts                   │
│  → Trust score: 0.85                                        │
│  → Reasoning: Strong audience fit, proven brand lift        │
│  → Conditions: Contextual only, no profiling               │
│  Human approves: ✓                                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 7: Signal Activation (via AdCP or other protocol)     │
│  → Activate signal with policy bindings                     │
│  → Campaign goes live                                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 8: audit_signal_usage(...)                            │
│  → Log activation event                                     │
│  → Record: signal_id, campaign_id, approver, trust_score   │
│  → Create audit trail for compliance                        │
│  → Returns: audit_id, retention_until                       │
└─────────────────────────────────────────────────────────────┘
```

## File Organization

```
mcp-server/
├── server.py                    # Main implementation (1000+ lines)
│   ├── Helper Functions
│   │   ├── load_json_file()
│   │   ├── load_text_file()
│   │   ├── get_available_signals()
│   │   ├── calculate_trust_score()
│   │   ├── verify_signal_compliance()
│   │   ├── create_audit_log()
│   │   └── check_category_compliance()
│   ├── MCP Resources
│   │   ├── list_resources()
│   │   └── read_resource()
│   ├── MCP Tools
│   │   ├── list_tools()
│   │   └── call_tool()
│   └── Main Entry Point
│       └── main()
│
├── requirements.txt             # Dependencies
├── config.json                  # MCP configuration
├── .env.example                 # Environment template
├── install.sh                   # Installation script
├── test_server.py              # Test suite
│
└── Documentation
    ├── README.md               # Complete guide (600+ lines)
    ├── EXAMPLE_PROMPTS.md      # 50+ agent prompts
    ├── ARCHITECTURE.md         # This file
    └── IMPLEMENTATION_SUMMARY.md # Overview
```

## Technology Stack

```
┌─────────────────────────────────────────────────────────────┐
│                     Technology Stack                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Protocol Layer:                                             │
│  └─ Model Context Protocol (MCP) 1.0+                       │
│                                                              │
│  Implementation:                                             │
│  ├─ Python 3.8+                                             │
│  ├─ mcp SDK (Python)                                        │
│  ├─ asyncio (async support)                                 │
│  └─ JSON-RPC 2.0 (stdio transport)                          │
│                                                              │
│  Data Format:                                                │
│  ├─ JSON (manifests, schemas, responses)                    │
│  └─ Markdown (documentation)                                │
│                                                              │
│  Data Source:                                                │
│  └─ Local file system (no network required)                 │
│                                                              │
│  Integration:                                                │
│  ├─ Claude Desktop (primary)                                │
│  ├─ Any MCP-compatible client                               │
│  └─ stdio interface (universal)                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Performance Characteristics

```
┌─────────────────────────────────────────────────────────────┐
│                     Performance Metrics                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Server Startup:                                             │
│  ├─ Cold start: ~100ms                                      │
│  ├─ Import time: ~50ms                                      │
│  └─ Initialization: ~50ms                                   │
│                                                              │
│  Tool Operations:                                            │
│  ├─ list_signals: 10-20ms (4 signals)                      │
│  ├─ get_signal_manifest: 5-10ms                             │
│  ├─ verify_signal: 15-30ms                                  │
│  ├─ score_signal: 10-20ms                                   │
│  ├─ check_compliance: <5ms (in-memory lookup)               │
│  └─ audit_signal_usage: <5ms (log generation)               │
│                                                              │
│  Resource Operations:                                        │
│  ├─ Read manifest: 5-10ms                                   │
│  ├─ Read schema: 5-10ms                                     │
│  └─ Read docs: 10-20ms                                      │
│                                                              │
│  Memory Footprint:                                           │
│  ├─ Base server: ~30MB                                      │
│  ├─ With manifests loaded: ~50MB                            │
│  └─ Peak during operation: ~60MB                            │
│                                                              │
│  Scalability:                                                │
│  ├─ Concurrent requests: Async (unlimited)                  │
│  ├─ Signal limit: Thousands (file system bound)             │
│  └─ Response time: O(1) for most operations                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Security Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Security Model                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Network Security:                                           │
│  ├─ No network connections (local only)                     │
│  ├─ No external API calls                                   │
│  └─ Stdio transport (process isolation)                     │
│                                                              │
│  Authentication:                                             │
│  ├─ No credentials required                                 │
│  ├─ No API keys needed                                      │
│  └─ Local file system permissions only                      │
│                                                              │
│  Data Privacy:                                               │
│  ├─ No PII in manifests                                     │
│  ├─ No user tracking                                        │
│  ├─ Audit logs contain no PII                               │
│  └─ Privacy-preserving by design                            │
│                                                              │
│  Access Control:                                             │
│  ├─ File system permissions                                 │
│  ├─ Process isolation via MCP                               │
│  └─ Read-only manifest access                               │
│                                                              │
│  Compliance:                                                 │
│  ├─ GDPR-compliant (no personal data)                       │
│  ├─ CCPA-compliant (no data sale)                           │
│  └─ OpenSignals privacy standards                           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

Built for production use in agentic advertising workflows.
