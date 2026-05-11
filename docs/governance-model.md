# OpenSignals Protocol Governance Model

**Version**: 0.1
**Status**: Draft
**Last Updated**: May 2026

---

## Overview

This document defines the governance model for the OpenSignals Protocol itself—how the protocol is maintained, evolved, and stewarded as an open standard. It covers protocol governance, not signal governance (which is covered in the protocol specification).

The governance model aims to ensure OpenSignals remains:
- **Open**: Transparent processes, public documentation, open participation
- **Neutral**: No vendor capture, no preferential treatment, fair access for all participants
- **Stable**: Backward compatibility, versioned specifications, clear deprecation policies
- **Responsive**: Timely updates, security patches, community-driven improvements
- **Credible**: Clear authority, accountable decision-making, documented rationale

---

## Governance Structure

### Roles and Responsibilities

#### 1. Protocol Maintainers

**Role**: Core team responsible for day-to-day protocol maintenance, specification updates, and project administration.

**Responsibilities**:
- Review and merge pull requests
- Maintain specification documentation
- Publish protocol versions and releases
- Manage GitHub repository and issues
- Facilitate working group coordination
- Respond to security disclosures
- Publish meeting notes and decisions
- Ensure documentation quality and consistency

**Membership**: Initial maintainers are the protocol authors. Additional maintainers may be added through community consensus and demonstrated contribution.

**Term**: Ongoing, with annual review. Maintainers may step down or be removed through community consensus if inactive or acting against protocol interests.

**Current Maintainers** (as of v0.1):
- To be determined as project matures

**Communication**:
- GitHub: `@opensignals-protocol/maintainers`
- Email: `maintainers@opensignals-protocol.org` (when established)

#### 2. Working Groups

**Role**: Subject-matter expert groups focused on specific aspects of the protocol.

**Proposed Working Groups**:

**Trust and Scoring Working Group**
- Focus: Trust score models, dimension weights, scoring algorithms
- Scope: Refinement of trust dimensions, scoring methodology, trust band definitions
- Output: Recommendations for trust model updates, scoring best practices

**Permissioning and Privacy Working Group**
- Focus: Consent models, usage restrictions, privacy compliance
- Scope: GDPR/CCPA compliance patterns, consent scope definitions, permissioning frameworks
- Output: Permissioning model updates, privacy compliance guidance

**Integration Working Group**
- Focus: AdCP, AAMP, OpenRTB, MCP, A2A integrations
- Scope: Integration patterns, compatibility testing, reference implementations
- Output: Integration guides, compatibility matrices, example implementations

**Compliance and Regulation Working Group**
- Focus: Regulatory compliance, category restrictions, market-specific requirements
- Scope: Alcohol, gambling, pharma, finance, children's advertising regulations
- Output: Compliance frameworks, category-specific extensions, regulatory guidance

**Schema and Data Standards Working Group**
- Focus: JSON schemas, manifest structures, data formats
- Scope: Schema versioning, backward compatibility, extension mechanisms
- Output: Schema updates, validation tooling, migration guides

**Governance and Audit Working Group**
- Focus: Bounded autonomy, audit trails, policy binding
- Scope: Approval workflows, audit retention, governance patterns
- Output: Governance framework refinements, audit best practices

**Formation**: Working groups are proposed by community members or maintainers and approved through GitHub discussion. Minimum 3 participants required to form a working group.

**Communication**: Each working group maintains a GitHub Discussion board and publishes meeting notes.

#### 3. Contributors

**Role**: Community members who contribute code, documentation, examples, integrations, or feedback.

**How to Contribute**:
- Submit pull requests for specification updates
- Propose new features or extensions through GitHub Issues
- Contribute reference implementations
- Share integration examples
- Provide feedback on proposals
- Participate in working group discussions

**Recognition**: Contributors are acknowledged in release notes and specification documents.

#### 4. Advisory Board (Future)

**Role**: Industry advisors providing guidance on adoption, compatibility, and standards alignment.

**Status**: Not yet formed. As OpenSignals matures and adoption grows, an advisory board may be established to provide strategic guidance and industry liaison.

**Potential Composition**:
- Advertising industry standards bodies (IAB Tech Lab, etc.)
- Brand-side representatives (advertisers, agencies)
- Supply-side representatives (publishers, SSPs)
- Platform representatives (DSPs, DMPs, CDPs)
- Data provider representatives
- Privacy and regulatory experts

**Function**: Advisory only; does not have decision-making authority over protocol specifications.

---

## Decision-Making Process

### Principles

1. **Rough Consensus and Running Code**: Favor practical implementation experience over theoretical debate. Working implementations carry weight in decision-making.

2. **Transparency**: All proposals, discussions, and decisions are public and documented.

3. **Inclusivity**: All stakeholders (brands, agencies, platforms, data providers, publishers, technologists) have equal voice.

4. **Meritocracy**: Good ideas and well-reasoned arguments matter more than organizational affiliation.

5. **Backward Compatibility**: Breaking changes require extraordinary justification and must include migration paths.

### Decision Flow

#### Minor Updates (Documentation, Examples, Bug Fixes)

**Process**:
1. Contributor submits pull request
2. Maintainer reviews for accuracy and clarity
3. Maintainer merges (typically within 1 week)

**Approval**: Single maintainer approval sufficient

**Timeline**: 1-7 days

#### Moderate Updates (Schema Extensions, New Fields, Clarifications)

**Process**:
1. Contributor opens GitHub Issue proposing change
2. Community discussion period (minimum 2 weeks)
3. Contributor submits pull request with proposed change
4. Maintainers review for compatibility and clarity
5. If consensus: merge; if contentious: escalate to working group

**Approval**: Two maintainer approvals OR working group consensus

**Timeline**: 2-6 weeks

#### Major Updates (Protocol Version, Core Model Changes, Breaking Changes)

**Process**:
1. Contributor or working group submits formal proposal as GitHub Issue with `proposal` label
2. Proposal includes: problem statement, proposed solution, impact analysis, migration path
3. Community discussion period (minimum 4 weeks)
4. Working group review (if applicable)
5. Maintainers publish summary of feedback and recommendation
6. If consensus: draft specification update
7. Public comment period on draft (minimum 2 weeks)
8. Final review and approval by maintainers
9. Publication of new protocol version

**Approval**: Consensus of maintainers + no sustained opposition from working groups

**Timeline**: 2-6 months

**Breaking Changes**: Require new major version number (e.g., v0.1 → v1.0). Must include migration guide and deprecation timeline.

---

## Versioning

### Semantic Versioning

OpenSignals follows semantic versioning: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (incompatible with previous version)
- **MINOR**: New features, backward-compatible additions
- **PATCH**: Bug fixes, documentation updates, clarifications

**Examples**:
- `0.1.0` → `0.1.1`: Documentation fix (PATCH)
- `0.1.0` → `0.2.0`: New trust dimension added (MINOR, backward-compatible)
- `0.1.0` → `1.0.0`: Core manifest structure changed (MAJOR, breaking)

### Version Status

Each protocol version has a status:

- **Draft**: Under development, subject to change, not recommended for production
- **Candidate**: Feature-complete, ready for testing and feedback
- **Released**: Stable, recommended for production use
- **Deprecated**: Superseded by newer version, support ending soon
- **Retired**: No longer supported, migration required

**Current Status**: v0.1 is Draft (as of May 2026)

### Deprecation Policy

**Timeline**:
- **Announcement**: Deprecation announced at least 12 months before retirement
- **Support Period**: Deprecated versions receive security patches but no new features
- **Migration Guide**: Published with deprecation announcement
- **Retirement**: Version retired after support period ends

**Example Timeline**:
- January 2027: v1.0 released, v0.1 marked deprecated
- January 2028: v0.1 support ends, v0.1 marked retired

---

## Change Proposal Process

### Submitting a Proposal

1. **Open a GitHub Issue** with the `proposal` label
2. **Use the Proposal Template**:

```markdown
## Proposal: [Brief Title]

### Problem Statement
What problem does this proposal solve?

### Current State
How does the protocol handle this today?

### Proposed Solution
What change do you propose?

### Impact Analysis
- Who does this affect? (signal providers, buyers, platforms, etc.)
- Is this backward-compatible?
- What are the trade-offs?

### Implementation Considerations
- Schema changes required?
- Documentation updates required?
- Reference implementation needed?

### Alternatives Considered
What other approaches did you consider and why did you reject them?

### Migration Path (if breaking change)
How do implementers migrate from current version to proposed version?

### References
Links to related issues, discussions, specifications, or implementations
```

3. **Engage in Discussion**: Respond to feedback, refine proposal based on input

4. **Iterate**: Update proposal based on community feedback

5. **Working Group Review**: If relevant, request review from applicable working group

6. **Maintainer Decision**: Maintainers approve, reject, or request more information

### Proposal Lifecycle

```
Open → Discussion → Working Group Review (if needed) → Maintainer Review →
  → Approved → Implementation → Testing → Merged
  → Rejected (with reasoning)
  → Deferred (revisit later)
```

### Proposal Labels

- `proposal:draft` - Under development
- `proposal:discussion` - Open for community feedback
- `proposal:review` - Ready for maintainer review
- `proposal:approved` - Approved, implementation in progress
- `proposal:implemented` - Implementation complete, ready to merge
- `proposal:rejected` - Rejected (with documented reasoning)
- `proposal:deferred` - Revisit in future version

---

## Schema Updates

### Schema Versioning

JSON schemas are versioned alongside the protocol: `/schemas/v0.1/`, `/schemas/v1.0/`, etc.

### Adding Fields (Backward-Compatible)

**Process**:
1. Propose new field via GitHub Issue
2. Define field purpose, data type, validation rules, and whether required or optional
3. Add field to schema with `"description"` explaining purpose
4. Update manifest examples to demonstrate usage
5. Submit pull request with schema update + documentation

**Approval**: Two maintainer approvals

**Timeline**: 2-4 weeks

**Impact**: Existing implementations continue to work (new field is optional unless explicitly required)

### Changing Fields (Breaking Change)

**Process**:
1. Propose change via formal proposal (see above)
2. Justify why change cannot be backward-compatible
3. Define migration path (e.g., old field supported for 12 months, then removed)
4. Draft new major version schema
5. Publish migration guide

**Approval**: Maintainer consensus + no sustained opposition

**Timeline**: 3-6 months

**Impact**: Major version bump required, implementers must migrate

### Removing Fields (Breaking Change)

**Process**:
1. Mark field as `"deprecated": true` in schema with deprecation notice
2. Document replacement field or pattern
3. Maintain deprecated field for at least 12 months
4. After deprecation period, remove field in new major version

**Approval**: Maintainer consensus

**Timeline**: 12+ months from deprecation to removal

---

## Extension Registry

### Purpose

The Extension Registry allows organizations to define custom signal types, trust dimensions, policy types, or other extensions without modifying the core protocol.

### Extension Namespace

Extensions use namespaced identifiers: `{organization}.{extension_type}.{extension_name}`

**Examples**:
- `acme-corp.signal_type.retail_foot_traffic`
- `example-dsp.trust_dimension.fraud_risk`
- `brand-co.policy_type.celebrity_endorsement_rules`

### Registering an Extension

1. **Create Extension Documentation** (README format):
   - Extension identifier
   - Purpose and use case
   - Schema definition (if applicable)
   - Compatibility requirements
   - Contact information

2. **Submit Pull Request** to `/extensions/registry.md` with extension entry:

```markdown
### acme-corp.signal_type.retail_foot_traffic

**Organization**: ACME Corporation
**Contact**: extensions@acme-corp.com
**Documentation**: https://acme-corp.com/opensignals/retail-foot-traffic
**Version**: 1.0
**Status**: Active
**Description**: Measures foot traffic patterns near retail locations using
anonymized mobile device signals. Compliant with GDPR and CCPA.
**Schema**: https://acme-corp.com/opensignals/schemas/retail-foot-traffic.json
```

3. **Maintainer Review**: Ensure extension does not conflict with core protocol or existing extensions

4. **Approval and Publication**: Extension listed in public registry

### Extension Guidelines

**DO**:
- Use namespaced identifiers to avoid conflicts
- Document extensions clearly and publicly
- Maintain backward compatibility within your extension
- Follow OpenSignals principles (transparency, permissioning, audit)

**DO NOT**:
- Modify core protocol fields or structures
- Use extension mechanisms to circumvent core protocol requirements (e.g., skipping audit trails)
- Register extensions that violate privacy or ethical standards
- Claim core protocol endorsement of your extension

---

## Security Disclosures

### Reporting Security Issues

**DO NOT** open public GitHub Issues for security vulnerabilities.

**Instead**:
1. Email security concerns to: `security@opensignals-protocol.org` (when established)
2. Include: description of vulnerability, affected versions, proof of concept (if available)
3. Maintainers will respond within 72 hours

**Temporary Contact** (until security email established):
- Open a private security advisory via GitHub Security Advisories

### Security Response Process

1. **Acknowledgment**: Maintainers acknowledge receipt within 72 hours
2. **Assessment**: Evaluate severity and impact
3. **Fix Development**: Develop and test fix privately
4. **Coordinated Disclosure**: Notify affected implementers before public disclosure
5. **Public Disclosure**: Publish security advisory with fix details
6. **Patch Release**: Release patched version(s)

**Timeline**: Aim for fix within 30 days for critical issues, 90 days for moderate issues

### Security Advisory Format

```markdown
## Security Advisory: [Brief Title]

**Advisory ID**: OSSA-YYYY-NNNN (OpenSignals Security Advisory)
**Severity**: Critical / High / Medium / Low
**Affected Versions**: vX.Y.Z through vX.Y.Z
**Fixed Versions**: vX.Y.Z+
**CVE**: CVE-YYYY-NNNNN (if applicable)

### Description
Clear description of the vulnerability

### Impact
Who is affected and what is the potential harm?

### Mitigation
How can implementers protect themselves immediately?

### Resolution
How is the issue fixed in patched versions?

### Credit
Acknowledgment of security researcher (if desired)
```

---

## Compatibility Principles

### Backward Compatibility

**Commitment**: Minor and patch versions maintain backward compatibility. Existing implementations continue to work when upgrading.

**Practices**:
- New fields are optional by default
- Existing field semantics do not change
- Enumeration values are additive (new values added, existing values retained)
- Deprecations are announced at least 12 months before removal

### Forward Compatibility

**Requirement**: Implementations must gracefully ignore unknown fields to support future extensions.

**JSON Schema**: Use `"additionalProperties": true` or explicit extension fields

**Example**: If a signal manifest includes a new field `"experimental_metric"` that older implementations don't recognize, they should ignore it rather than failing validation.

### Cross-Version Compatibility

**Goal**: v0.1 manifests should be readable by v1.0 implementations (with minor field mapping if needed).

**Approach**:
- Maintain core structure across versions
- Document field mappings for breaking changes
- Provide migration tooling for major version upgrades

---

## Avoiding Vendor Capture

### Neutrality Principles

1. **No Preferential Treatment**: All participants (vendors, brands, platforms, data providers) have equal access to protocol development and decision-making.

2. **No Vendor-Specific Features**: Core protocol does not include features that only work with specific vendors' products or services.

3. **Open Participation**: Working groups, proposals, and discussions are open to all. No membership fees, no vendor prerequisites.

4. **Transparent Governance**: All decisions are documented publicly with clear rationale. No backroom deals.

5. **Extension Mechanism**: Vendor-specific features belong in extensions, not core protocol.

### Conflict of Interest Management

**Disclosure**: Contributors with vendor affiliations should disclose affiliations when proposing changes that benefit their organization.

**Recusal**: Maintainers recuse themselves from decisions where they have direct financial interest.

**Review**: Controversial proposals receive review from multiple independent parties.

### Open Source and Open Standards

**Code License**: Apache 2.0 (permissive, no patent retaliation)

**Documentation License**: Creative Commons Attribution 4.0 International (CC BY 4.0)

**Intent**: Ensure protocol can be implemented freely by anyone, with no licensing barriers.

---

## Maintaining Neutrality

### Independence

OpenSignals is an independent open-source project. It is not:
- Owned by any vendor or standards body
- Controlled by any single organization
- Developed behind closed doors

### Standards Body Alignment

While OpenSignals is independent, it aims to align with and complement industry standards:
- IAB Tech Lab (AAMP, OpenRTB, AdCOM)
- AdCP (Ad Context Protocol)
- W3C (web standards)
- IETF (internet protocols)

**Goal**: Eventual submission to a standards body (IAB Tech Lab, W3C, or similar) as the protocol matures and gains adoption.

**Current Status**: Independent open-source project, not yet submitted to standards body.

### Community Stewardship

OpenSignals succeeds only if it serves the needs of the entire advertising ecosystem:
- **Brands and Agencies**: Trust, transparency, governance
- **Data Providers**: Fair representation, clear requirements
- **Platforms**: Implementable, performant, compatible
- **Publishers**: Monetization, brand safety, quality
- **Regulators**: Compliance, audit, accountability

**Governance Goal**: Balance these interests fairly and transparently.

---

## Communication Channels

### GitHub

**Primary Communication**: All technical discussions, proposals, and decisions happen on GitHub.

- **Issues**: Bug reports, feature requests, proposals
- **Discussions**: General questions, implementation guidance, working group coordination
- **Pull Requests**: Code and documentation contributions
- **Security Advisories**: Private security disclosures

**Repository**: `https://github.com/opensignals-protocol/opensignals-protocol`

### Mailing List (Future)

**Purpose**: Announcements of new versions, security advisories, major decisions

**Frequency**: Low-traffic (monthly or less)

**Subscription**: Open to all

**Status**: To be established as project matures

### Working Group Meetings (Future)

**Purpose**: Synchronous discussion of complex topics

**Format**: Video calls, recorded and published

**Frequency**: Monthly or as needed per working group

**Status**: To be established as working groups form

### Website (Future)

**Purpose**: Public-facing documentation, examples, integration guides

**Status**: To be established; currently GitHub serves as primary documentation host

---

## Governance Evolution

### Adapting the Model

This governance model is itself subject to change as the protocol and community mature.

**Process for Governance Changes**:
1. Propose governance change via GitHub Issue with `governance` label
2. Community discussion period (minimum 4 weeks)
3. Maintainer consensus required for approval
4. Update this document and announce change

**Examples of Future Governance Evolution**:
- Establishing formal advisory board
- Creating new working groups
- Changing decision-making thresholds
- Adding maintainers
- Defining clearer escalation procedures

### Success Metrics

How will we know if governance is working?

**Indicators of Healthy Governance**:
- Active community participation (issues, PRs, discussions)
- Diverse contributor base (multiple organizations, roles, perspectives)
- Timely decision-making (proposals resolved in reasonable timeframe)
- Transparent processes (decisions documented, rationale clear)
- Growing adoption (implementations, integrations, real-world usage)
- Constructive disagreement (respectful debate, consensus-building)
- Stability (backward compatibility maintained, breaking changes rare)

**Indicators of Governance Problems**:
- Vendor capture (single organization dominates decisions)
- Stagnation (proposals languish without resolution)
- Opacity (decisions made without clear rationale)
- Fragmentation (competing forks or implementations)
- Community frustration (contributors feel unheard)

**Review**: Maintainers will review governance effectiveness annually and propose improvements as needed.

---

## Code of Conduct

All participants in the OpenSignals community must adhere to the project's Code of Conduct.

**Core Principles**:
- Be respectful and constructive
- Welcome diverse perspectives
- Focus on what is best for the protocol and community
- Show empathy and kindness
- Accept constructive criticism gracefully

**Unacceptable Behavior**:
- Harassment, trolling, or personal attacks
- Publishing others' private information without permission
- Spam, commercial solicitation, or off-topic promotion
- Intimidation or abuse

**Enforcement**: Maintainers may warn, temporarily ban, or permanently ban participants who violate the Code of Conduct.

**Full Code of Conduct**: See `/CODE_OF_CONDUCT.md` in the repository.

---

## Conclusion

The OpenSignals Protocol governance model prioritizes openness, neutrality, stability, and community participation. By maintaining transparent processes, avoiding vendor capture, ensuring backward compatibility, and enabling extensions, OpenSignals aims to serve the entire advertising ecosystem as a neutral trust infrastructure.

As the protocol matures and adoption grows, this governance model will evolve to meet the community's needs while maintaining the core principles of openness and neutrality.

---

## Quick Reference

### How Do I...?

**Report a bug**: Open a GitHub Issue with `bug` label

**Propose a new feature**: Open a GitHub Issue with `proposal` label, follow proposal template

**Contribute documentation**: Submit a pull request with changes

**Join a working group**: Comment on the working group's GitHub Discussion thread

**Report a security issue**: Email `security@opensignals-protocol.org` (or use GitHub Security Advisories until email established)

**Suggest a governance change**: Open a GitHub Issue with `governance` label

**Ask a question**: Open a GitHub Discussion in the Q&A category

**Register an extension**: Submit pull request to `/extensions/registry.md`

**Become a maintainer**: Demonstrate sustained, high-quality contribution; maintainers will reach out

---

**Related Documentation:**
- [OpenSignals Protocol v0.1 Specification](/Users/samrajmatharu/opensignals-protocol/specs/opensignals-v0.1.md)
- [Contributing Guidelines](/Users/samrajmatharu/opensignals-protocol/CONTRIBUTING.md)
- [Code of Conduct](/Users/samrajmatharu/opensignals-protocol/CODE_OF_CONDUCT.md)
- [Architecture Documentation](/Users/samrajmatharu/opensignals-protocol/docs/architecture.md)
