# OpenSignals Protocol - Frequently Asked Questions

This FAQ addresses common questions about the OpenSignals Protocol, its purpose, implementation, and relationship to other advertising standards.

## General Questions

### What is OpenSignals Protocol?

OpenSignals Protocol is an open trust layer for advertising signals used by AI agents. It provides a standardized way to declare, verify, score, permission, and audit signals before they are activated in advertising campaigns.

Think of it as a "trust passport" for advertising signals that helps agents answer: "Should I trust this signal for my brand and use case?"

### Why was OpenSignals created?

The advertising industry is rapidly building infrastructure for AI agents to discover inventory, buy media, and optimize campaigns. However, there's a gap: agents need a way to assess whether signals are trustworthy before activating them.

OpenSignals addresses this by providing:
- **Trust metadata** for signals (provenance, quality, permissions)
- **Verification workflows** to check signals against brand policies
- **Audit trails** for compliance and transparency
- **Trust scoring** across multiple dimensions

### Who should use OpenSignals?

OpenSignals is designed for:

- **Signal Providers** (data companies, publishers, SSPs): Publish trust metadata for your signals
- **Demand-Side Platforms**: Verify signals before activation
- **Agencies and Buyers**: Ensure signals meet brand safety and compliance requirements
- **Brands**: Define signal trust policies for your campaigns
- **Governance Systems**: Implement automated policy checking and audit trails
- **AI Agent Developers**: Build trust assessment into signal discovery and activation workflows

### Is OpenSignals a replacement for AdCP, AAMP, or OpenRTB?

No. OpenSignals **complements** existing standards:

- **AdCP**: Provides signal discovery and activation. OpenSignals adds trust verification between discovery and activation.
- **AAMP**: Industry framework for agentic advertising. OpenSignals implements the trust and transparency pillar.
- **OpenRTB/OpenDirect**: Execution layer for programmatic. OpenSignals operates above this, helping agents decide which signals to use.

Think of it as an additional layer, not a replacement.

### What problem does OpenSignals solve?

Before OpenSignals, advertising agents had no standardized way to:
1. Assess signal provenance and data quality
2. Verify permissions and consent
3. Check compliance with brand policies
4. Audit signal usage for regulatory requirements
5. Score signals against brand objectives

OpenSignals provides machine-readable trust metadata and APIs to solve these problems.

## Technical Questions

### How do I implement OpenSignals?

Implementation depends on your role:

**For Signal Providers**:
1. Create OpenSignals manifests for your signals (JSON format)
2. Host manifests at `.well-known/opensignals/{signal_id}` endpoints
3. Include trust metadata (provenance, permissions, quality scores)
4. Implement verification API (optional but recommended)

**For Demand-Side Systems**:
1. Fetch OpenSignals manifests when discovering signals
2. Verify signals against brand policies before activation
3. Log signal usage for audit trails
4. Submit outcome feedback to improve trust scores

**For Governance Systems**:
1. Define brand policies compatible with OpenSignals
2. Implement verification API for policy checking
3. Create approval workflows for low-trust or regulated signals
4. Build audit dashboards

See [Implementation Guides](../reference-implementation/) for detailed instructions.

### What format are OpenSignals manifests?

OpenSignals manifests are JSON documents following a defined schema. Example:

```json
{
  "protocol": "opensignals",
  "version": "0.1",
  "signal_id": "example-signal",
  "name": "Example Signal",
  "signal_type": "audience",
  "status": "active",
  "owner": {
    "organization": "Example Co",
    "contact": "signals@example.com"
  },
  "provenance": {
    "data_sources": ["first_party_behavioral"],
    "collection_method": "opt_in_panel",
    "last_updated": "2026-05-10T08:00:00Z"
  },
  "quality": {
    "overall_trust_score": 0.87,
    "coverage_score": 0.82,
    "freshness_score": 0.91,
    "precision_score": 0.85
  }
}
```

See [Schema Documentation](../schemas/) for complete specifications.

### How are trust scores calculated?

Trust scores are multi-dimensional, combining:

1. **Provenance** (20%): Data source transparency
2. **Permissioning** (20%): Consent and usage rights
3. **Freshness** (15%): How recently updated
4. **Quality** (20%): Coverage and precision
5. **Explainability** (10%): How well signal can be explained
6. **Outcome Relevance** (10%): Historical performance
7. **Compliance Safety** (5%): Regulatory adherence

Each dimension is scored 0.0 to 1.0, and the overall score is a weighted average.

Signal providers calculate and publish these scores. Buyers can validate or adjust scores based on their own criteria.

### Where should OpenSignals manifests be hosted?

Best practice is the `.well-known` URI pattern:

```
https://your-domain.com/.well-known/opensignals/{signal_id}
```

This follows web standards (RFC 8615) and makes manifests discoverable.

You can also:
- Embed manifest URLs in AdCP responses
- Provide manifest URLs in HTTP `Link` headers
- Use custom API endpoints (document in integration guides)

### Do I need to implement all OpenSignals tasks?

No. Implement what makes sense for your use case:

**Minimum viable implementation**:
- Host signal manifests
- Include basic trust scores

**Recommended implementation**:
- Host manifests
- Implement `verify_signal` API
- Log audit trails

**Full implementation**:
- All of the above
- Plus: `score_signal`, `bind_signal_policy`, `revoke_signal`, `submit_signal_outcome_feedback`

Start small and expand as needed.

### Is there a reference implementation?

Yes. A Python reference implementation is available in [reference-implementation/python/](../reference-implementation/python/).

It includes:
- FastAPI server with verification endpoints
- JSON Schema validation
- Basic trust score calculation
- Example requests and responses

This is for **demonstration purposes only** and is **not production-ready**. Use it as a starting point for your own implementation.

## Integration Questions

### How does OpenSignals integrate with AdCP?

AdCP responses can include an `open_signals` extension:

```json
{
  "task": "get_signals",
  "signals": [
    {
      "signal_id": "example-signal",
      "name": "Example Signal",
      "coverage": 1000000,
      "cpm": 5.00,
      "open_signals": {
        "manifest_url": "https://provider.com/.well-known/opensignals/example-signal",
        "overall_trust_score": 0.87,
        "verification_required": true,
        "audit_required": true
      }
    }
  ]
}
```

Agents can then:
1. Fetch the full OpenSignals manifest
2. Verify the signal against brand policy
3. Activate via AdCP if approved

See [AdCP Integration Guide](../integrations/adcp/) for details.

### How does OpenSignals relate to AAMP?

AAMP is the IAB Tech Lab's framework for agentic advertising with three pillars:
1. Foundations (ARTF)
2. Protocols
3. Trust and Transparency

OpenSignals addresses the **Trust and Transparency pillar** by providing:
- Signal provenance tracking
- Permission verification
- Quality assessment
- Audit trails
- Compliance verification

See [AAMP Integration Guide](../integrations/aamp/) for conceptual mapping.

### Can OpenSignals work with OpenRTB?

Yes, conceptually. OpenSignals operates **before** OpenRTB:

```
1. Discover signals (AdCP or similar)
2. Verify signals (OpenSignals)
3. Activate signals in campaigns
4. Execute via OpenRTB auctions
```

OpenSignals helps agents decide **which signals** to include in OpenRTB bid requests, but doesn't modify OpenRTB itself.

### Does OpenSignals require changes to existing infrastructure?

Minimal changes:

**Signal Providers**: Add manifest endpoints and trust metadata
**Buyers**: Add verification checks before signal activation
**Governance Systems**: Add policy checking and audit logging

Existing infrastructure (DSPs, SSPs, ad servers) can remain unchanged. OpenSignals is an **additive layer**.

## Policy and Governance

### How do I define brand policies for OpenSignals?

Brand policies are rules that determine whether signals are acceptable for your campaigns. Example policy structure:

```json
{
  "brand": "premium-spirits-co",
  "category": "alcohol",
  "markets": ["US", "GB", "AU"],
  "rules": {
    "minimum_trust_score": 0.90,
    "required_consent_basis": "explicit",
    "prohibited_uses": ["individual_profiling"],
    "human_approval_required": true,
    "audit_required": true
  },
  "compliance_frameworks": [
    "uk_alcohol_advertising_code",
    "responsible_drinking_standards"
  ]
}
```

Policies are brand-specific. OpenSignals provides the framework; you define the rules.

### When is human approval required?

Human approval is typically required for:
- **Regulated categories** (alcohol, pharma, gambling, finance)
- **Low trust scores** (below brand threshold, e.g., < 0.75)
- **New or untested signals** (no historical performance)
- **High-risk campaigns** (brand-critical, large budgets)
- **Compliance-sensitive markets** (strict regulations)

Define human approval triggers in your brand policies.

### How do I handle regulated categories like alcohol?

For regulated categories:

1. **Set high trust thresholds** (e.g., 0.90+)
2. **Require explicit consent** (not legitimate interest)
3. **Enable human approval workflows**
4. **Log comprehensive audit trails**
5. **Bind category-specific policies** (e.g., UK alcohol code)
6. **Restrict individual-level targeting** (contextual only)

See the [Alcohol Contextual Signal Example](../examples/alcohol-contextual-signal.json) for a complete reference.

### What audit information should be logged?

Audit logs should include:
- Signal ID and manifest version
- Verification timestamp and decision
- Trust score at time of activation
- Brand, market, and category
- Policy bindings applied
- Human approval records (if applicable)
- Campaign ID and context
- Usage metrics and outcomes

This supports regulatory compliance and transparency requirements.

## Trust and Security

### How do I verify signal provenance?

OpenSignals manifests include a `provenance` object:

```json
{
  "provenance": {
    "data_sources": ["first_party_behavioral", "survey"],
    "collection_method": "opt_in_panel",
    "processing_steps": ["deduplication", "quality_filtering"],
    "last_updated": "2026-05-10T08:00:00Z",
    "update_frequency": "daily",
    "lineage_documentation": "https://provider.com/lineage/signal-123"
  }
}
```

Review this to understand:
- Where data comes from
- How it was collected
- How it was processed
- When it was last updated

For high-trust use cases, verify lineage documentation and audit data sources.

### Can signals be cryptographically signed?

The current specification (v0.1) doesn't require signatures, but implementations can add them.

Future versions may include:
- Cryptographic signatures for manifests
- Certificate-based trust chains
- Blockchain-based immutable audit logs

See [ROADMAP.md](../ROADMAP.md) for planned features.

### What if a signal's trust score changes?

Signal providers should:
1. Update the manifest with new scores
2. Notify active users (via webhooks or API notifications)
3. Explain the reason for the change
4. Provide historical score tracking

Buyers should:
1. Re-verify signals periodically
2. Set up monitoring for score changes
3. Have policies for handling score degradation
4. Consider caching duration (15-60 minutes recommended)

### How do I handle signals with no OpenSignals manifest?

Options:
1. **Block**: Reject signals without manifests (safest for regulated categories)
2. **Default score**: Assign a default low trust score (e.g., 0.50)
3. **Human review**: Route to human for manual assessment
4. **Allowlist**: Maintain an allowlist of pre-approved signals

Define your approach in brand policies.

## Adoption and Ecosystem

### Is OpenSignals officially endorsed by industry bodies?

**No** (as of May 2026). OpenSignals is an independent open-source project, not endorsed by:
- IAB Tech Lab
- AdCP / AgenticAdvertising.Org
- Any standards body

The goal is to create a practical implementation that addresses real needs, then seek standardization through appropriate channels.

### Who is using OpenSignals in production?

OpenSignals is currently in **draft status** (v0.1). There are no confirmed production deployments yet.

The project is seeking pilot partners to test the protocol in real-world scenarios. If you're interested, open a GitHub Discussion or Issue.

### How can I contribute to OpenSignals?

Ways to contribute:
- **Feedback**: Share feedback on the specification via GitHub Issues
- **Examples**: Contribute signal manifest examples
- **Integrations**: Share integration patterns with other protocols
- **Implementations**: Build reference implementations in other languages
- **Documentation**: Improve guides, fix typos, add tutorials
- **Testing**: Help validate the protocol in real-world scenarios
- **Advocacy**: Spread the word in the advertising community

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

### Is there a governance model for OpenSignals?

Currently, OpenSignals is maintained by the open-source community with informal governance.

As adoption grows, a formal governance model will be established (see [ROADMAP.md](../ROADMAP.md)), potentially including:
- Steering committee
- Working groups for specialization areas
- Formal contribution and review processes
- Versioning and release management

### What's the long-term vision for OpenSignals?

The vision is to:
1. Establish OpenSignals as a practical, widely-adopted trust layer for advertising signals
2. Achieve standardization through IAB Tech Lab or similar bodies
3. Enable autonomous, trustworthy signal selection by AI agents
4. Support regulatory compliance and transparency in agentic advertising
5. Expand beyond advertising to broader marketing and content recommendation use cases

See [ROADMAP.md](../ROADMAP.md) for detailed plans.

## Troubleshooting

### My signal manifests aren't validating. What should I check?

Common issues:
1. **Invalid JSON syntax**: Use a JSON validator (jsonlint.com)
2. **Missing required fields**: Check against the schema
3. **Incorrect data types**: Ensure numbers are numbers, not strings
4. **Invalid timestamps**: Use ISO 8601 format (e.g., 2026-05-10T08:00:00Z)
5. **Score out of range**: Trust scores must be 0.0 to 1.0

Run the validation tests:
```bash
python tests/test_manifest_validation.py
```

### Verification API returns errors. How do I debug?

Check:
1. **Request format**: Validate against `verify-signal-request.schema.json`
2. **Authentication**: Ensure proper API credentials
3. **Signal ID**: Verify signal exists and manifest is accessible
4. **Policy configuration**: Ensure brand policies are properly defined
5. **Network**: Check firewall rules and API endpoint availability

Enable detailed logging in the reference implementation for more info.

### Trust scores seem inconsistent. What's wrong?

Possible causes:
1. **Different scoring methodologies**: Providers may use different approaches
2. **Outdated manifests**: Check `last_updated` timestamp
3. **Caching**: Clear cache if scores changed recently
4. **Calculation errors**: Verify weighted average is correct
5. **Dimension scores missing**: Ensure all 7 dimensions are scored

Publish your scoring methodology in the manifest for transparency.

### How do I handle API rate limits?

Best practices:
1. **Cache manifests**: Cache for 15-60 minutes
2. **Batch requests**: Group verification requests where possible
3. **Implement backoff**: Use exponential backoff on errors
4. **Check headers**: Respect `X-RateLimit-*` headers
5. **Paginate**: Use pagination for bulk operations

If limits are too restrictive, contact the signal provider.

## Getting Help

### Where can I ask questions?

- **GitHub Discussions**: https://github.com/Samrajtheailyceum/opensignals-protocol/discussions
- **GitHub Issues**: https://github.com/Samrajtheailyceum/opensignals-protocol/issues
- **Specification Questions**: Use the `spec-question` issue template
- **Integration Help**: Use the `integration-example` issue template

### How do I report a bug?

Use the [Bug Report template](../.github/ISSUE_TEMPLATE/bug_report.md) on GitHub Issues.

Include:
- Clear description of the bug
- Steps to reproduce
- Expected vs. actual behavior
- Code samples or schemas
- Environment details

### How do I request a feature?

Use the [Feature Request template](../.github/ISSUE_TEMPLATE/feature_request.md) on GitHub Issues.

Include:
- Problem statement
- Proposed solution
- Use case examples
- Implementation considerations

### Is there a community chat or forum?

Currently, all discussion happens on GitHub (Issues and Discussions).

As the community grows, we may establish:
- Slack or Discord channel
- Mailing list
- Regular community calls

Check [ROADMAP.md](../ROADMAP.md) for updates.

## Additional Resources

- **Main README**: [../README.md](../README.md)
- **Protocol Specification**: [../specs/opensignals-v0.1.md](../specs/opensignals-v0.1.md)
- **Examples**: [../examples/](../examples/)
- **Integration Guides**: [../integrations/](../integrations/)
- **Reference Implementation**: [../reference-implementation/python/](../reference-implementation/python/)
- **Contributing Guidelines**: [../CONTRIBUTING.md](../CONTRIBUTING.md)
- **Roadmap**: [../ROADMAP.md](../ROADMAP.md)
- **Security Policy**: [../SECURITY.md](../SECURITY.md)

---

**Didn't find your question?** Open a [GitHub Discussion](https://github.com/Samrajtheailyceum/opensignals-protocol/discussions) or [GitHub Issue](https://github.com/Samrajtheailyceum/opensignals-protocol/issues).

**Last Updated**: 2026-05-11
