# OpenSignals Protocol Examples

This directory contains example OpenSignals manifests demonstrating different signal types, use cases, and trust levels.

## Overview

Each example manifest showcases:
- Complete OpenSignals Protocol v0.1 structure
- Trust scoring across multiple dimensions
- Provenance and data lineage documentation
- Permissioning and compliance metadata
- Real-world use case scenarios

## Example Manifests

### 1. Alcohol Contextual Signal
**File**: [alcohol-contextual-signal.json](alcohol-contextual-signal.json)

A contextual targeting signal for premium spirits advertising in regulated markets.

**Key Features**:
- **Regulated Category**: Alcohol advertising with strict governance
- **Trust Score**: 0.91 (highly trusted with conditions)
- **Human Approval**: Required before activation
- **Market Restrictions**: Geographic restrictions for certain markets
- **Compliance**: UK Advertising Standards Authority certified

**Use Case**: A premium whisky brand targeting contextually relevant content in the UK market. The signal targets content related to premium spirits, luxury lifestyle, and fine dining, while ensuring compliance with UK alcohol advertising regulations.

**Trust Profile**:
- Provenance: Transparent, first-party and vetted third-party sources
- Permissioning: Clear consent basis, contextual-only usage
- Compliance: High compliance score (0.95) with UK standards
- Explainability: Clear methodology for context classification

**Example Verification**:
```bash
curl -X POST https://governance.brand.com/opensignals/verify \
  -d '{"signal_id": "premium-spirits-contextual-uk", "category": "alcohol", "market": "GB"}'
```

---

### 2. Attention Signal
**File**: [attention-signal.json](attention-signal.json)

A measurement signal predicting ad viewability and attention quality.

**Key Features**:
- **Signal Type**: Measurement/quality prediction
- **Trust Score**: 0.88 (highly trusted)
- **Data Source**: Eye-tracking studies and viewability data
- **Industry Validated**: Third-party verified methodology
- **Real-time Scoring**: Updated per ad placement

**Use Case**: Media buyers optimizing campaign placements based on predicted attention quality. The signal combines viewability predictions, eye-tracking data, and contextual factors to score each ad placement opportunity.

**Trust Profile**:
- Provenance: Academic research and controlled eye-tracking studies
- Quality: High precision (0.89) and coverage (0.85)
- Outcome Relevance: Strong correlation with brand lift (0.92)
- Explainability: Transparent methodology with published research

**Example Usage**:
```json
{
  "placement_id": "homepage-banner-above-fold",
  "attention_signal": {
    "predicted_attention_score": 0.78,
    "viewability_probability": 0.85,
    "expected_dwell_time_seconds": 2.3,
    "trust_score": 0.88
  }
}
```

---

### 3. Retail Commerce Signal
**File**: [retail-commerce-signal.json](retail-commerce-signal.json)

A first-party commerce intent signal from a major retailer.

**Key Features**:
- **Signal Type**: First-party commerce intent
- **Trust Score**: 0.94 (very high trust)
- **Data Source**: Retailer's own transaction and browsing data
- **Consent Basis**: Explicit opt-in with clear disclosure
- **High Precision**: Purchase intent accuracy of 0.91

**Use Case**: A consumer electronics brand targeting shoppers with demonstrated purchase intent for smartphones. The signal is built from the retailer's own shopping data, providing high-quality first-party signals with clear provenance.

**Trust Profile**:
- Provenance: Direct first-party data with full lineage
- Permissioning: Explicit consent with transparent usage terms
- Freshness: Daily updates (0.96 freshness score)
- Quality: High precision (0.91) and coverage (0.94)

**Example Activation**:
```json
{
  "campaign_id": "smartphone-launch-q2-2026",
  "signal_id": "retail-commerce-smartphone-intent",
  "targeting": {
    "intent_threshold": 0.7,
    "lookback_window_days": 30,
    "expected_reach": 850000
  }
}
```

---

### 4. Sustainability Signal
**File**: [sustainability-signal.json](sustainability-signal.json)

An audience signal identifying environmentally conscious consumers.

**Key Features**:
- **Signal Type**: Audience/interest-based
- **Trust Score**: 0.83 (trusted with governance checks)
- **Data Source**: Survey data and behavioral indicators
- **Focus**: Environmental values and sustainable purchasing
- **Brand-Safe**: High relevance for purpose-driven marketing

**Use Case**: An eco-friendly consumer goods brand targeting consumers with demonstrated interest in sustainability and environmental issues. The signal combines survey responses, content engagement, and purchase behavior.

**Trust Profile**:
- Provenance: Mixed sources (survey, behavioral, first-party)
- Permissioning: Legitimate interest with opt-out available
- Quality: Good precision (0.81) with strong outcome relevance (0.86)
- Compliance: GDPR and CCPA compliant

**Example Targeting**:
```json
{
  "campaign_id": "earth-day-sustainable-products-2026",
  "signal_id": "sustainability-conscious-audience",
  "targeting": {
    "sustainability_score_min": 0.7,
    "include_segments": [
      "active_eco_shoppers",
      "climate_advocates",
      "sustainable_lifestyle"
    ],
    "expected_reach": 3200000
  }
}
```

---

## Understanding Trust Scores

Each example includes a multi-dimensional trust score. Here's how to interpret them:

### Overall Trust Score Ranges

| Score Range | Interpretation | Recommended Action |
|-------------|---------------|-------------------|
| 0.90 - 1.00 | Highly Trusted | Can be used autonomously (if policy allows) |
| 0.75 - 0.89 | Trusted | Use with governance checks |
| 0.50 - 0.74 | Limited Trust | Require human review |
| 0.25 - 0.49 | Low Trust | Do not activate without explicit approval |
| 0.00 - 0.24 | Unsafe | Block usage |

### Trust Dimensions

Each signal is scored across 7 dimensions:

1. **Provenance** (20% weight): Data source transparency and chain of custody
2. **Permissioning** (20% weight): Clear consent and usage rights
3. **Freshness** (15% weight): How recently the signal was updated
4. **Quality** (20% weight): Coverage, precision, and stability
5. **Explainability** (10% weight): How well the signal can be explained
6. **Outcome Relevance** (10% weight): Historical performance
7. **Compliance Safety** (5% weight): Regulatory adherence

### Example Score Breakdown

From the Retail Commerce Signal:

```json
{
  "overall_trust_score": 0.94,
  "provenance_score": 0.98,      // First-party data, full lineage
  "permissioning_score": 0.96,   // Explicit consent, clear terms
  "freshness_score": 0.96,       // Daily updates
  "precision_score": 0.91,       // High purchase intent accuracy
  "coverage_score": 0.94,        // Large, representative audience
  "explainability_score": 0.87,  // Clear methodology
  "outcome_relevance_score": 0.90, // Strong historical performance
  "compliance_safety_score": 0.93  // GDPR/CCPA compliant
}
```

---

## Comparing Signal Types

| Signal | Type | Trust Score | Best For | Requires Human Approval |
|--------|------|------------|----------|------------------------|
| Alcohol Contextual | Contextual | 0.91 | Regulated categories | Yes |
| Attention | Measurement | 0.88 | Media quality optimization | No |
| Retail Commerce | First-party intent | 0.94 | High-value conversions | No |
| Sustainability | Audience | 0.83 | Purpose-driven marketing | No |

---

## Using These Examples

### For Signal Providers

Use these examples as templates when creating your own OpenSignals manifests:

1. **Copy the structure** from the most relevant example
2. **Update metadata** (signal ID, name, owner, provider)
3. **Document provenance** with your data sources and methods
4. **Calculate trust scores** based on your signal characteristics
5. **Define permissioning** based on your consent and usage terms
6. **Add compliance flags** relevant to your markets and categories

### For Buyers and Agencies

Use these examples to understand what to look for in signal manifests:

1. **Check trust scores** against your brand's thresholds
2. **Review provenance** to understand data sources
3. **Verify permissioning** aligns with your use case
4. **Assess compliance** with your market regulations
5. **Evaluate freshness** based on campaign needs

### For Governance Systems

Use these examples to calibrate policy rules:

1. **Set trust score thresholds** by category (e.g., 0.90+ for alcohol)
2. **Define human approval triggers** (regulated categories, low trust)
3. **Create policy bindings** for different signal types
4. **Establish audit requirements** based on risk level

---

## Testing and Validation

### Validating Against JSON Schema

All examples validate against the OpenSignals Protocol schemas:

```bash
# Install dependencies
pip install jsonschema

# Validate an example
python ../tests/test_manifest_validation.py
```

### Testing API Workflows

Use these examples to test verification workflows:

```bash
# Fetch manifest
curl https://demo.opensignals.org/.well-known/opensignals/retail-commerce-smartphone-intent

# Verify signal
curl -X POST https://governance.brand.com/opensignals/verify \
  -H "Content-Type: application/json" \
  -d @verification-request-example.json

# Audit usage
curl -X POST https://governance.brand.com/opensignals/audit \
  -H "Content-Type: application/json" \
  -d @audit-request-example.json
```

---

## Adding New Examples

We welcome contributions of new example manifests. When adding examples:

### Required Elements
- [ ] Complete OpenSignals v0.1 schema compliance
- [ ] Realistic trust scores with clear justification
- [ ] Documented provenance and data sources
- [ ] Clear use case description
- [ ] Compliance and regulatory flags (where applicable)

### Best Practices
- [ ] Use real-world inspired scenarios
- [ ] Include diverse signal types (contextual, audience, measurement)
- [ ] Show different trust levels (high, medium, regulated)
- [ ] Document edge cases and special handling
- [ ] Provide verification request/response examples

### Submission Process
1. Create your manifest following the schema
2. Validate against JSON Schema
3. Add a description to this README
4. Submit a pull request with the `examples` label

See [../CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines.

---

## Additional Resources

### Schema References
- [OpenSignal Manifest Schema](../schemas/v0.1/open-signal-manifest.schema.json)
- [Trust Score Schema](../schemas/v0.1/trust-score.schema.json)
- [Verify Signal Request Schema](../schemas/v0.1/verify-signal-request.schema.json)

### Documentation
- [Protocol Specification](../specs/opensignals-v0.1.md)
- [Terminology](../specs/terminology.md)
- [Conformance Requirements](../specs/conformance.md)

### Integrations
- [AdCP Integration Examples](../integrations/adcp/)
- [AAMP Trust Layer Mapping](../integrations/aamp/)

### Reference Implementation
- [Python Reference Server](../reference-implementation/python/)

---

## Questions and Feedback

- **GitHub Issues**: https://github.com/Samrajtheailyceum/opensignals-protocol/issues
- **Label**: Use `examples` label for questions about these examples
- **Discussions**: https://github.com/Samrajtheailyceum/opensignals-protocol/discussions

---

**Last Updated**: 2026-05-11
