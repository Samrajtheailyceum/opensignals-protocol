# OpenSignals + AdCP Integration

This directory contains examples and documentation for integrating OpenSignals Protocol with [Ad Context Protocol (AdCP)](https://adcontextprotocol.org/).

## Overview

AdCP provides signal discovery and activation through tasks like `get_signals` and `activate_signal`. OpenSignals extends AdCP by adding trust metadata that enables agents to assess signal trustworthiness before activation.

## Integration Pattern

OpenSignals operates as a **trust verification layer** between AdCP's signal discovery and signal activation steps:

```
┌─────────────────────────────────────┐
│   1. Discover Signals (AdCP)        │
│   get_signals → List of available   │
│   signals with coverage and pricing │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   2. Verify Trust (OpenSignals)     │
│   verify_signal → Check trust,      │
│   compliance, and permissions       │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   3. Activate Signal (AdCP)         │
│   activate_signal → Use trusted     │
│   signal in campaign                │
└─────────────────────────────────────┘
```

## How It Works

### Step 1: Signal Discovery via AdCP

An advertising agent uses AdCP to discover available signals:

```json
{
  "task": "get_signals",
  "filters": {
    "signal_type": "audience",
    "category": "outdoor_recreation",
    "min_coverage": 1000000
  }
}
```

### Step 2: AdCP Response with OpenSignals Extension

The AdCP response includes OpenSignals trust metadata:

```json
{
  "task": "get_signals",
  "signals": [
    {
      "signal_id": "outdoor-recreation-enthusiasts",
      "name": "Outdoor Recreation Enthusiasts",
      "signal_type": "audience",
      "coverage": 2400000,
      "cpm": 3.50,
      "currency": "USD",
      "geo": ["US", "CA", "GB"],
      "open_signals": {
        "manifest_url": "https://signals.example.com/.well-known/opensignals/outdoor-recreation-enthusiasts",
        "overall_trust_score": 0.87,
        "verification_required": true,
        "audit_required": true,
        "policy_categories": ["general"],
        "last_verified": "2026-05-10T08:00:00Z",
        "compliance_flags": []
      }
    }
  ]
}
```

See [get-signals-with-opensignals.json](get-signals-with-opensignals.json) for a complete example.

### Step 3: Fetch OpenSignals Manifest

The agent retrieves the full OpenSignals manifest:

```bash
curl https://signals.example.com/.well-known/opensignals/outdoor-recreation-enthusiasts
```

### Step 4: Verify Signal Against Brand Policy

Before activating the signal, the agent verifies it against brand policies:

```bash
curl -X POST https://governance.brand.com/opensignals/verify \
  -H "Content-Type: application/json" \
  -d '{
    "signal_id": "outdoor-recreation-enthusiasts",
    "brand": "premium-outdoor-gear",
    "market": "US",
    "category": "general",
    "intended_use": "audience_targeting"
  }'
```

Response:

```json
{
  "decision": "approved",
  "trust_score": 0.87,
  "conditions": [],
  "policy_bindings": ["standard_brand_safety"],
  "decision_reasoning": "Signal approved for audience targeting. No special conditions required."
}
```

### Step 5: Activate Signal via AdCP

Once verified, the agent activates the signal through AdCP:

```json
{
  "task": "activate_signal",
  "signal_id": "outdoor-recreation-enthusiasts",
  "campaign_id": "summer-camping-2026",
  "activation_context": {
    "opensignals_verification": {
      "verified": true,
      "verification_timestamp": "2026-05-11T10:30:00Z",
      "trust_score": 0.87,
      "policy_bindings": ["standard_brand_safety"],
      "audit_id": "audit-12345"
    }
  }
}
```

## Extension Schema

### OpenSignals Extension in AdCP `get_signals` Response

Each signal in the AdCP response can include an `open_signals` object:

```typescript
{
  "open_signals": {
    "manifest_url": string,              // URL to full OpenSignals manifest
    "overall_trust_score": number,       // 0.0 to 1.0
    "verification_required": boolean,    // Must verify before activation?
    "audit_required": boolean,           // Must audit after activation?
    "policy_categories": string[],       // ["general", "alcohol", "pharma", etc.]
    "last_verified": string,             // ISO 8601 timestamp
    "compliance_flags": string[],        // ["gdpr_compliant", "ccpa_compliant", etc.]
    "human_approval_required": boolean,  // Optional: requires human review
    "restricted_markets": string[]       // Optional: ISO country codes where restricted
  }
}
```

See [adcp-extension-example.json](adcp-extension-example.json) for the complete schema.

## Example Files

This directory contains:

- **[get-signals-with-opensignals.json](get-signals-with-opensignals.json)**: Complete example of AdCP `get_signals` response with OpenSignals extension
- **[adcp-extension-example.json](adcp-extension-example.json)**: Schema and examples for the OpenSignals extension format

## Integration Checklist

If you're implementing OpenSignals support in an AdCP-compatible system:

### For Signal Providers (SSPs, Data Providers)
- [ ] Create OpenSignals manifests for all signals
- [ ] Host manifests at `.well-known/opensignals/{signal_id}` endpoints
- [ ] Include `open_signals` extension in AdCP `get_signals` responses
- [ ] Implement signal verification API endpoints
- [ ] Set up audit trail logging

### For Demand-Side Systems (DSPs, Agencies)
- [ ] Parse `open_signals` extension from AdCP responses
- [ ] Fetch and validate OpenSignals manifests
- [ ] Implement trust verification checks before activation
- [ ] Bind brand policies to signals
- [ ] Log signal usage for audit purposes
- [ ] Submit outcome feedback to update trust scores

### For Governance Systems
- [ ] Define brand policy rules compatible with OpenSignals
- [ ] Implement verification API for policy checking
- [ ] Create approval workflows for low-trust or regulated signals
- [ ] Build audit dashboards for signal usage
- [ ] Set up compliance monitoring and alerting

## Implementation Considerations

### When to Verify Signals

**Always verify** signals in these scenarios:
- Regulated categories (alcohol, pharma, gambling, finance)
- New or untested signals (trust score < 0.75)
- Signals with recent provenance changes
- High-budget or brand-critical campaigns
- Markets with strict advertising regulations

**May skip verification** in these scenarios:
- Highly trusted signals (trust score > 0.90)
- Frequently used signals with proven track record
- Internal first-party signals
- Low-risk, low-budget campaigns
- Testing and development environments

### Caching Strategies

To optimize performance:
- Cache OpenSignals manifests for 15-60 minutes
- Cache verification decisions for similar use cases
- Implement cache invalidation on manifest updates
- Use CDN for manifest distribution

### Error Handling

If OpenSignals verification fails:
- **Blocking Errors**: Prevent signal activation (missing manifest, policy violation)
- **Non-Blocking Warnings**: Log and proceed with caution (expired manifest, low trust score)
- **Fallback Behavior**: Define default policies when OpenSignals is unavailable

## Real-World Example: Alcohol Campaign

A complete example of an alcohol campaign workflow using AdCP + OpenSignals:

### 1. Brand Brief
- **Brand**: Premium Spirits Co
- **Product**: Single Malt Whisky
- **Market**: United Kingdom
- **Target**: Adults 25+ interested in premium spirits
- **Restrictions**: Must comply with UK alcohol advertising standards

### 2. Signal Discovery (AdCP)
Agent queries AdCP for relevant signals:

```json
{
  "task": "get_signals",
  "filters": {
    "signal_type": "contextual",
    "keywords": ["premium", "spirits", "whisky", "luxury"],
    "geo": ["GB"],
    "category": "alcohol"
  }
}
```

### 3. Response with OpenSignals
AdCP returns signals with trust metadata:

```json
{
  "signals": [
    {
      "signal_id": "premium-spirits-contextual-uk",
      "name": "Premium Spirits Context",
      "signal_type": "contextual",
      "coverage": 500000,
      "cpm": 8.50,
      "geo": ["GB"],
      "open_signals": {
        "manifest_url": "https://signals.example.com/.well-known/opensignals/premium-spirits-contextual-uk",
        "overall_trust_score": 0.92,
        "verification_required": true,
        "audit_required": true,
        "policy_categories": ["alcohol"],
        "compliance_flags": ["uk_advertising_standards_authority"],
        "human_approval_required": true,
        "restricted_markets": ["SA", "AE"]
      }
    }
  ]
}
```

### 4. Trust Verification (OpenSignals)
Agent verifies signal against brand policy:

```json
{
  "signal_id": "premium-spirits-contextual-uk",
  "brand": "premium-spirits-co",
  "market": "GB",
  "category": "alcohol",
  "intended_use": "contextual_targeting"
}
```

Response:

```json
{
  "decision": "approved_with_conditions",
  "trust_score": 0.92,
  "conditions": [
    "human_approval_required",
    "age_restriction_25plus",
    "no_individual_profiling"
  ],
  "policy_bindings": [
    "uk_alcohol_advertising_code",
    "responsible_drinking_messaging"
  ],
  "decision_reasoning": "Signal approved for contextual use. Individual profiling prohibited. Requires human review before activation. Must include responsible drinking messaging."
}
```

### 5. Human Approval
Governance agent routes to human for approval. Human reviews and approves.

### 6. Signal Activation (AdCP)
Agent activates signal with policy bindings:

```json
{
  "task": "activate_signal",
  "signal_id": "premium-spirits-contextual-uk",
  "campaign_id": "whisky-holiday-2026",
  "activation_context": {
    "opensignals_verification": {
      "verified": true,
      "trust_score": 0.92,
      "human_approved": true,
      "policy_bindings": [
        "uk_alcohol_advertising_code",
        "responsible_drinking_messaging"
      ]
    }
  }
}
```

### 7. Audit Trail (OpenSignals)
Signal usage is logged for compliance:

```json
{
  "signal_id": "premium-spirits-contextual-uk",
  "campaign_id": "whisky-holiday-2026",
  "brand": "premium-spirits-co",
  "market": "GB",
  "activation_timestamp": "2026-05-15T12:00:00Z",
  "policy_bindings": ["uk_alcohol_advertising_code"],
  "human_approved": true
}
```

## Technical Specifications

### Manifest Discovery

OpenSignals manifests should be discoverable via:

1. **Direct URL**: Included in AdCP `open_signals.manifest_url`
2. **Well-Known URI**: `https://{domain}/.well-known/opensignals/{signal_id}`
3. **HTTP Headers**: `Link: <manifest-url>; rel="opensignals"`

### Authentication

When fetching manifests or calling verification APIs:
- Use OAuth 2.0 or API key authentication
- Include authentication in `Authorization` header
- Support token refresh for long-running agents

### Rate Limiting

Implementations should respect rate limits:
- Check `X-RateLimit-*` headers
- Implement exponential backoff on errors
- Cache manifests to reduce API calls

## Testing

### Test Signal with OpenSignals Extension

A test signal is available for integration testing:

**Signal ID**: `test-signal-opensignals-demo`

**Manifest URL**: `https://demo.opensignals.org/.well-known/opensignals/test-signal-opensignals-demo`

This test signal can be used to validate AdCP + OpenSignals integration without affecting production systems.

## Resources

- **AdCP Specification**: https://adcontextprotocol.org/
- **AdCP GitHub**: https://github.com/adcontextprotocol/adcp
- **OpenSignals Specification**: [../../specs/opensignals-v0.1.md](../../specs/opensignals-v0.1.md)
- **OpenSignals Examples**: [../../examples/](../../examples/)

## Support and Questions

- **GitHub Issues**: https://github.com/Samrajtheailyceum/opensignals-protocol/issues
- **Label**: Use `adcp-integration` label for AdCP-specific questions
- **Discussions**: https://github.com/Samrajtheailyceum/opensignals-protocol/discussions

## Contributing

We welcome examples, implementations, and feedback on the AdCP integration pattern. See [../../CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

---

**Last Updated**: 2026-05-11
