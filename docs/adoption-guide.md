# OpenSignals Protocol - Adoption Guide

This guide helps organizations adopt the OpenSignals Protocol based on their role in the advertising ecosystem. Whether you're a signal provider, buyer, platform, or agency, this guide provides a clear path to implementation.

## Overview

OpenSignals adoption typically follows these stages:

1. **Evaluation** (1-2 weeks): Understand the protocol and assess fit
2. **Planning** (2-4 weeks): Design your integration approach
3. **Implementation** (4-8 weeks): Build and test your integration
4. **Pilot** (4-8 weeks): Test in production with limited scope
5. **Scale** (Ongoing): Expand to full production deployment

Total timeline: 3-6 months from evaluation to full production.

---

## Adoption by Role

Select your role to jump to the relevant section:

- [Signal Providers](#adoption-guide-for-signal-providers)
- [Demand-Side Platforms (DSPs)](#adoption-guide-for-demand-side-platforms-dsps)
- [Agencies and Buyers](#adoption-guide-for-agencies-and-buyers)
- [Brands](#adoption-guide-for-brands)
- [Supply-Side Platforms (SSPs)](#adoption-guide-for-supply-side-platforms-ssps)
- [Governance and Compliance Teams](#adoption-guide-for-governance-and-compliance-teams)

---

## Adoption Guide for Signal Providers

Signal providers include data companies, publishers, measurement firms, and any organization that provides targeting, measurement, or contextual signals.

### Why Adopt OpenSignals?

- **Differentiation**: Stand out with transparent trust metadata
- **Trust**: Build buyer confidence in your signals
- **Compliance**: Demonstrate regulatory adherence
- **Automation**: Enable automated signal evaluation by agents
- **Competitive Advantage**: Be early to support agentic workflows

### Phase 1: Evaluation (1-2 weeks)

#### Week 1: Learn the Protocol

- [ ] Read the [main README](../README.md)
- [ ] Review [protocol specification](../specs/opensignals-v0.1.md)
- [ ] Study [signal manifest examples](../examples/)
- [ ] Review [trust scoring methodology](../specs/opensignals-v0.1.md#trust-score-model)

#### Week 2: Assess Fit

- [ ] Inventory your current signals
- [ ] Review your data provenance documentation
- [ ] Assess your permission and consent management
- [ ] Evaluate your compliance frameworks
- [ ] Identify gaps in trust metadata

**Decision Point**: Does OpenSignals align with your product strategy?

### Phase 2: Planning (2-4 weeks)

#### Identify Priority Signals

Start with:
- High-volume signals
- Premium signals with strong provenance
- Signals used by strategic customers
- Signals with clear compliance documentation

**Recommendation**: Pilot with 3-5 signals before scaling to full catalog.

#### Design Manifest Structure

For each signal, document:

1. **Provenance**:
   - Data sources
   - Collection methods
   - Processing steps
   - Update frequency

2. **Permissioning**:
   - Consent basis (explicit, legitimate interest, etc.)
   - Usage rights and restrictions
   - Geographic or category limitations

3. **Quality Metrics**:
   - Coverage (reach)
   - Precision (accuracy)
   - Freshness (recency)
   - Historical performance

4. **Compliance**:
   - Regulatory frameworks (GDPR, CCPA, etc.)
   - Industry certifications
   - Brand safety verification

#### Calculate Trust Scores

Implement scoring across 7 dimensions:

| Dimension | Weight | Your Score | Calculation Method |
|-----------|--------|------------|-------------------|
| Provenance | 20% | _____ | Transparency and lineage clarity |
| Permissioning | 20% | _____ | Consent quality and clarity |
| Freshness | 15% | _____ | Time since last update |
| Quality | 20% | _____ | Coverage × precision |
| Explainability | 10% | _____ | Methodology documentation quality |
| Outcome Relevance | 10% | _____ | Historical performance |
| Compliance Safety | 5% | _____ | Regulatory adherence |

**Overall Trust Score** = Weighted average of all dimensions

#### Technical Architecture

Decide on:

**Manifest Hosting**:
- [ ] `.well-known/opensignals/` endpoints (recommended)
- [ ] Custom API endpoints
- [ ] CDN distribution for scale

**Verification API** (optional but recommended):
- [ ] In-house build
- [ ] Third-party service
- [ ] Defer to buyers

**Audit Logging**:
- [ ] Internal audit database
- [ ] Third-party audit service
- [ ] Defer to buyers

#### Resource Planning

**Team Requirements**:
- **Engineering**: 1-2 FTE for 4-8 weeks (manifest generation, API development)
- **Data Team**: 0.5 FTE for 2-4 weeks (provenance documentation, score calculation)
- **Product/Legal**: 0.25 FTE for 2-4 weeks (policy review, compliance validation)

**Technology**:
- JSON schema validation tools
- API framework (if building verification API)
- Hosting infrastructure
- Monitoring and analytics

### Phase 3: Implementation (4-8 weeks)

#### Week 1-2: Create Manifests

For each pilot signal:

1. **Generate manifest JSON**:
   ```bash
   # Use the reference implementation as a starting point
   python tools/generate_manifest.py --signal-id your-signal-id
   ```

2. **Validate against schema**:
   ```bash
   jsonschema -i your-manifest.json schemas/v0.1/open-signal-manifest.schema.json
   ```

3. **Calculate trust scores**:
   - Document methodology
   - Calculate dimension scores
   - Compute weighted average
   - Review with stakeholders

4. **Review for accuracy**:
   - Data team validates provenance
   - Legal validates permissions and compliance
   - Product validates quality metrics

#### Week 3-4: Host Manifests

**Option 1: Static Hosting (Simplest)**
```nginx
# Nginx configuration
location /.well-known/opensignals/ {
    alias /var/www/opensignals-manifests/;
    add_header Access-Control-Allow-Origin *;
    add_header Content-Type application/json;
}
```

**Option 2: Dynamic API (Recommended)**
```python
# Python/FastAPI example
@app.get("/.well-known/opensignals/{signal_id}")
async def get_manifest(signal_id: str):
    manifest = load_manifest(signal_id)
    return JSONResponse(content=manifest)
```

**Option 3: CDN Distribution (For Scale)**
- Upload manifests to S3/CloudFront or similar
- Enable CORS
- Set appropriate cache headers (15-60 minutes)

#### Week 5-6: Implement Verification API (Optional)

If you want to support verification requests:

```python
@app.post("/opensignals/verify")
async def verify_signal(request: VerifySignalRequest):
    # Load signal manifest
    manifest = load_manifest(request.signal_id)

    # Check against brand policy
    decision = check_policy(manifest, request)

    # Return verification result
    return VerifySignalResponse(
        decision=decision.status,
        trust_score=manifest.quality.overall_trust_score,
        conditions=decision.conditions,
        policy_bindings=decision.policies
    )
```

#### Week 7-8: Testing and Validation

- [ ] Validate all manifests against JSON schema
- [ ] Test API endpoints (uptime, latency, error handling)
- [ ] Verify CORS configuration
- [ ] Test with reference implementation
- [ ] Load test for expected traffic
- [ ] Security audit (authentication, rate limiting, input validation)

**Acceptance Criteria**:
- All manifests validate successfully
- API returns correct responses for valid requests
- API handles errors gracefully
- Latency < 200ms at 95th percentile
- 99.9% uptime

### Phase 4: Pilot (4-8 weeks)

#### Launch with Select Partners

- [ ] Identify 2-3 friendly buyers/agencies for pilot
- [ ] Provide manifests and API documentation
- [ ] Offer integration support
- [ ] Set up monitoring and alerting

#### Collect Feedback

- [ ] Weekly sync calls with pilot partners
- [ ] Track usage metrics (API calls, errors, latency)
- [ ] Gather feedback on manifest clarity and completeness
- [ ] Identify gaps or pain points
- [ ] Iterate on manifests and documentation

#### Metrics to Track

- API uptime and latency
- Manifest fetch rate
- Verification request rate
- Error rates and types
- Trust score distribution
- Feedback sentiment

#### Iterate

Based on feedback:
- Update trust scores
- Clarify provenance documentation
- Add missing compliance flags
- Improve API error messages
- Enhance monitoring

### Phase 5: Scale (Ongoing)

#### Expand Signal Coverage

- [ ] Roll out to all signals (prioritize by volume/revenue)
- [ ] Automate manifest generation
- [ ] Set up scheduled manifest updates
- [ ] Implement version control for manifests

#### Operationalize

- [ ] Monitor trust score trends
- [ ] Set up alerts for score degradation
- [ ] Automate compliance checks
- [ ] Integrate with existing data pipeline

#### Promote Adoption

- [ ] Add "OpenSignals Certified" badge to marketing
- [ ] Include manifest URLs in AdCP responses
- [ ] Evangelize to buyers and agencies
- [ ] Share case studies and success stories

#### Continuous Improvement

- [ ] Collect outcome feedback from campaigns
- [ ] Use feedback to improve trust scores
- [ ] Update provenance documentation as data sources change
- [ ] Stay current with OpenSignals specification updates

### Success Metrics

**Short-term** (First 6 months):
- 100% of pilot signals have manifests
- 95%+ manifest validation success rate
- 99.9% API uptime
- 5+ pilot partners using manifests

**Long-term** (12+ months):
- 100% of signal catalog has manifests
- 50%+ of buyers checking manifests before activation
- Measurable increase in signal adoption due to trust transparency
- Industry recognition as an OpenSignals early adopter

---

## Adoption Guide for Demand-Side Platforms (DSPs)

DSPs enable buyers to activate signals across inventory. OpenSignals helps DSPs provide trust assessment before signal activation.

### Why Adopt OpenSignals?

- **Risk Mitigation**: Reduce brand risk from untrusted signals
- **Compliance**: Support regulatory requirements (GDPR, CCPA, brand safety)
- **Differentiation**: Offer advanced trust assessment capabilities
- **Automation**: Enable agents to evaluate signals autonomously
- **Transparency**: Provide audit trails for advertisers

### Phase 1: Evaluation (1-2 weeks)

- [ ] Review OpenSignals specification
- [ ] Assess current signal evaluation process
- [ ] Identify gaps in trust assessment
- [ ] Evaluate technical integration points
- [ ] Estimate ROI (reduced brand risk, increased buyer confidence)

### Phase 2: Planning (2-4 weeks)

#### Integration Architecture

Decide on integration points:

**Signal Discovery**:
- [ ] Extend existing signal catalog with OpenSignals metadata
- [ ] Add manifest fetching to signal onboarding process
- [ ] Display trust scores in UI

**Signal Activation**:
- [ ] Add verification step before activation
- [ ] Implement policy checking against brand rules
- [ ] Support human approval workflows (for low trust or regulated)

**Audit and Reporting**:
- [ ] Log signal activations with trust metadata
- [ ] Provide audit dashboard for advertisers
- [ ] Enable outcome feedback submission

#### Technical Components

1. **Manifest Fetcher**: Fetch and cache OpenSignals manifests
2. **Verification Engine**: Check signals against brand policies
3. **Policy Store**: Store brand-specific trust policies
4. **Audit Logger**: Log all signal activations
5. **Reporting Dashboard**: Visualize trust metrics

#### Resource Planning

- **Engineering**: 2-3 FTE for 6-10 weeks
- **Product**: 0.5 FTE for planning and requirements
- **UX**: 0.5 FTE for dashboard design

### Phase 3: Implementation (6-10 weeks)

#### Week 1-3: Manifest Fetching

Implement manifest fetcher:

```python
class ManifestFetcher:
    def __init__(self, cache_ttl=3600):
        self.cache = {}
        self.cache_ttl = cache_ttl

    async def fetch_manifest(self, signal_id, manifest_url):
        # Check cache
        if signal_id in self.cache:
            cached_at, manifest = self.cache[signal_id]
            if time.time() - cached_at < self.cache_ttl:
                return manifest

        # Fetch from provider
        async with httpx.AsyncClient() as client:
            response = await client.get(manifest_url)
            response.raise_for_status()
            manifest = response.json()

        # Validate against schema
        validate(manifest, OPENSIGNALS_SCHEMA)

        # Cache
        self.cache[signal_id] = (time.time(), manifest)

        return manifest
```

#### Week 4-6: Verification Engine

Implement policy checking:

```python
class VerificationEngine:
    def verify_signal(self, manifest, brand_policy):
        # Check trust score threshold
        if manifest.quality.overall_trust_score < brand_policy.min_trust_score:
            return VerificationResult(
                decision="rejected",
                reason="Below trust threshold"
            )

        # Check category restrictions
        if manifest.category in brand_policy.prohibited_categories:
            return VerificationResult(
                decision="rejected",
                reason="Prohibited category"
            )

        # Check consent basis
        if brand_policy.required_consent == "explicit":
            if manifest.permissioning.consent_basis != "explicit":
                return VerificationResult(
                    decision="rejected",
                    reason="Explicit consent required"
                )

        # Check geographic restrictions
        if not set(manifest.geographic_coverage).intersection(brand_policy.markets):
            return VerificationResult(
                decision="rejected",
                reason="No coverage in target markets"
            )

        # Determine if human approval needed
        human_approval = (
            manifest.quality.overall_trust_score < 0.75 or
            manifest.category in brand_policy.regulated_categories
        )

        return VerificationResult(
            decision="approved" if not human_approval else "approved_with_conditions",
            trust_score=manifest.quality.overall_trust_score,
            conditions=["human_approval_required"] if human_approval else [],
            policy_bindings=brand_policy.compliance_frameworks
        )
```

#### Week 7-8: UI Integration

Add trust visualization to signal selection UI:

- Display trust score badge (color-coded by score range)
- Show provenance summary
- Indicate if human approval needed
- Link to full manifest

#### Week 9-10: Testing and Pilot

- [ ] Unit tests for all components
- [ ] Integration tests with real manifests
- [ ] Load testing for manifest fetching
- [ ] UI/UX testing with internal users
- [ ] Pilot with 2-3 friendly advertisers

### Phase 4: Scale (Ongoing)

- [ ] Roll out to all advertisers
- [ ] Monitor adoption metrics
- [ ] Iterate based on feedback
- [ ] Expand to all signal providers

### Success Metrics

- 80%+ of signals have OpenSignals manifests
- 50%+ of campaigns use trust verification
- 95%+ advertiser satisfaction with trust transparency
- Measurable reduction in brand safety incidents

---

## Adoption Guide for Agencies and Buyers

Agencies and buyers use OpenSignals to ensure signals meet brand standards before activation.

### Why Adopt OpenSignals?

- **Brand Safety**: Ensure signals meet brand guidelines
- **Compliance**: Support regulated categories (alcohol, pharma)
- **Performance**: Select higher-quality signals
- **Transparency**: Provide clients with trust audit trails
- **Automation**: Enable agents to make trustworthy decisions

### Quick Start (For Immediate Use)

If you need to start using OpenSignals today:

1. **Fetch Manifests**: Request `.well-known/opensignals/{signal_id}` URLs from providers
2. **Review Trust Scores**: Check if `overall_trust_score` meets your threshold (e.g., 0.75+)
3. **Check Provenance**: Review data sources and collection methods
4. **Verify Permissions**: Ensure consent basis aligns with use case
5. **Log Activation**: Record which signals were used and why

### Full Adoption (4-8 weeks)

For systematic integration:

1. **Define Brand Policies**: Set trust thresholds, consent requirements, compliance needs
2. **Automate Verification**: Build or integrate verification tools
3. **Human Approval Workflows**: Set up approval process for low-trust or regulated signals
4. **Audit Dashboard**: Track signal usage and trust metrics
5. **Outcome Feedback**: Submit campaign results to improve trust scores

See the [reference implementation](../reference-implementation/python/) for example code.

### Success Metrics

- 100% of campaigns use trust verification
- Zero brand safety incidents from signals
- 50%+ improvement in signal selection confidence
- Positive client feedback on transparency

---

## Adoption Guide for Brands

Brands define trust policies and governance rules for signal usage.

### Why Adopt OpenSignals?

- **Control**: Define which signals are acceptable for your brand
- **Compliance**: Ensure regulatory adherence
- **Risk Management**: Reduce brand safety incidents
- **Transparency**: Audit trail for signal usage
- **Performance**: Focus spend on high-quality signals

### Getting Started (2-4 weeks)

#### Step 1: Define Trust Policies

Create brand policy document:

```json
{
  "brand": "your-brand-name",
  "categories": ["general", "alcohol", "pharma"],
  "policies_by_category": {
    "general": {
      "min_trust_score": 0.75,
      "required_consent_basis": "legitimate_interest",
      "human_approval_required": false
    },
    "alcohol": {
      "min_trust_score": 0.90,
      "required_consent_basis": "explicit",
      "prohibited_uses": ["individual_profiling"],
      "human_approval_required": true,
      "compliance_frameworks": ["uk_alcohol_advertising_code"]
    }
  },
  "compliance_requirements": {
    "gdpr": true,
    "ccpa": true,
    "brand_safety_verification": true
  }
}
```

#### Step 2: Communicate to Partners

- [ ] Share policies with agency partners
- [ ] Brief DSPs on requirements
- [ ] Educate internal stakeholders

#### Step 3: Monitor and Audit

- [ ] Review signal usage reports monthly
- [ ] Audit compliance with policies
- [ ] Adjust policies based on learnings

### Success Metrics

- 100% of signals verified against brand policies
- Zero compliance violations
- Positive stakeholder confidence in signal governance

---

## Adoption Guide for Supply-Side Platforms (SSPs)

SSPs connect signal providers with demand. OpenSignals helps SSPs provide trust metadata to buyers.

### Why Adopt OpenSignals?

- **Value-Add**: Differentiate by providing trust transparency
- **Quality Signal**: Attract premium buyers with transparent provenance
- **Compliance**: Support regulatory requirements
- **Automation**: Enable programmatic trust assessment

### Implementation Approach

SSPs have two options:

**Option 1: Pass-Through**
- Include OpenSignals manifest URLs in signal metadata
- Let buyers fetch manifests directly from providers
- Log usage for providers

**Option 2: Aggregate**
- Fetch and cache manifests from providers
- Provide unified API for buyers to access manifests
- Offer value-added trust scoring or enrichment

**Recommendation**: Start with Option 1, evolve to Option 2 based on demand.

### Success Metrics

- 80%+ of signal providers publishing manifests
- 50%+ of buyers using manifests
- Increased signal activation rates due to trust transparency

---

## Adoption Guide for Governance and Compliance Teams

Governance teams ensure signals meet regulatory and brand standards.

### Why Adopt OpenSignals?

- **Automation**: Automate compliance checks
- **Audit Trails**: Comprehensive logging for regulatory requirements
- **Risk Mitigation**: Prevent activation of non-compliant signals
- **Transparency**: Clear documentation of provenance and permissions

### Implementation Focus

1. **Policy Definitions**: Define machine-readable brand policies
2. **Verification Workflows**: Automate policy checking
3. **Human Approval**: Build approval workflows for high-risk signals
4. **Audit Dashboard**: Visualize signal usage and compliance
5. **Reporting**: Generate compliance reports for regulators

### Success Metrics

- 100% of regulated signals require human approval
- Zero compliance violations
- 50%+ reduction in manual review time through automation

---

## Common Adoption Challenges

### Challenge 1: Trust Score Consistency

**Problem**: Different providers calculate trust scores differently.

**Solution**:
- Document scoring methodology in manifests
- Normalize scores internally if needed
- Focus on dimension scores (provenance, quality, etc.) not just overall score
- Set clear thresholds based on your risk tolerance

### Challenge 2: Incomplete Manifests

**Problem**: Some signals lack complete trust metadata.

**Solution**:
- Start with signals that have good documentation
- Work with providers to fill gaps
- Use default scores for missing data (e.g., 0.50 for unknown provenance)
- Incentivize complete manifests through preferential treatment

### Challenge 3: Integration Complexity

**Problem**: Integrating OpenSignals into existing workflows is complex.

**Solution**:
- Start small (3-5 pilot signals)
- Use reference implementation as starting point
- Automate incrementally (manifests first, then verification, then audit)
- Leverage existing tools where possible

### Challenge 4: Performance Overhead

**Problem**: Fetching manifests adds latency.

**Solution**:
- Cache manifests aggressively (15-60 minutes)
- Fetch manifests asynchronously
- Pre-fetch manifests for commonly used signals
- Use CDN for manifest distribution

### Challenge 5: Low Provider Adoption

**Problem**: Not all signal providers publish manifests yet.

**Solution**:
- Prioritize providers who do
- Communicate demand to providers
- Share business case for adoption
- Collaborate on pilot programs

---

## Getting Help

### Resources

- **Documentation**: [../README.md](../README.md), [../specs/](../specs/)
- **Examples**: [../examples/](../examples/)
- **Reference Implementation**: [../reference-implementation/python/](../reference-implementation/python/)
- **FAQ**: [FAQ.md](FAQ.md)

### Community

- **GitHub Discussions**: Ask questions, share experiences
- **GitHub Issues**: Report bugs, request features
- **Community Calls**: (Coming soon - see [ROADMAP.md](../ROADMAP.md))

### Professional Support

While OpenSignals is open-source, professional support may become available through:
- Implementation consultants
- Integration partners
- Managed services

Check the [project website](https://github.com/Samrajtheailyceum/opensignals-protocol) for updates.

---

## Adoption Checklist

Use this checklist to track your adoption progress:

### Evaluation Phase
- [ ] Reviewed OpenSignals documentation
- [ ] Assessed fit for organization
- [ ] Identified stakeholders
- [ ] Estimated resources needed
- [ ] Got leadership buy-in

### Planning Phase
- [ ] Defined integration scope
- [ ] Designed technical architecture
- [ ] Allocated resources (people, budget, time)
- [ ] Created project plan
- [ ] Identified pilot partners (if applicable)

### Implementation Phase
- [ ] Set up development environment
- [ ] Built/integrated core components
- [ ] Created/consumed manifests
- [ ] Implemented verification (if applicable)
- [ ] Set up monitoring and logging
- [ ] Completed testing

### Pilot Phase
- [ ] Launched with limited scope
- [ ] Collected usage metrics
- [ ] Gathered feedback
- [ ] Iterated on implementation
- [ ] Documented learnings

### Scale Phase
- [ ] Rolled out to production
- [ ] Expanded to full scope
- [ ] Operationalized (monitoring, alerting, support)
- [ ] Promoted adoption internally/externally
- [ ] Measured success metrics

---

**Ready to adopt?** Start with the [Quick Start Guide](../README.md#quick-start) or open a [GitHub Discussion](https://github.com/Samrajtheailyceum/opensignals-protocol/discussions) to ask questions.

**Last Updated**: 2026-05-11
