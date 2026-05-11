# OpenSignals Protocol Roadmap

This roadmap outlines the planned development of the OpenSignals Protocol from its current draft status (v0.1) toward a production-ready, industry-adopted standard.

## Status: Draft RFC v0.1 (May 2026)

The protocol is currently in its initial draft phase. This roadmap is subject to change based on community feedback and industry requirements.

---

## Phase 1: Foundation and Validation (Q2-Q3 2026)

**Goal**: Establish core protocol stability and gather industry feedback.

### v0.1.x - Draft Refinement
**Timeline**: May - July 2026

- [x] Initial protocol specification release
- [x] Core JSON schemas for manifests, verification, and audit
- [x] Python reference implementation
- [x] AdCP integration examples
- [ ] **Community Feedback Collection**
  - Gather feedback from advertising practitioners
  - Collect input from data providers, DSPs, SSPs
  - Engage with agency partners and brand marketers
  - Present to standards bodies for review
- [ ] **Protocol Validation**
  - Validate schemas with real-world signal data
  - Test integration patterns with existing ad tech stacks
  - Iterate on trust score calculation methodology
  - Refine policy binding framework
- [ ] **Documentation Improvements**
  - Add more integration examples (OpenRTB, OpenDirect)
  - Create implementation guides for different roles
  - Develop troubleshooting and FAQ sections
  - Add video walkthroughs and tutorials

### v0.2.0 - Stabilization Release
**Timeline**: August - September 2026

- [ ] **Schema Enhancements**
  - Add support for composite signals (signals derived from multiple sources)
  - Enhance provenance tracking for data lineage
  - Add versioning support for signal manifests
  - Introduce signal deprecation lifecycle
- [ ] **API Improvements**
  - Standardize error responses and status codes
  - Add pagination for batch operations
  - Introduce webhook support for async verification
  - Add support for bulk signal verification
- [ ] **Security Hardening**
  - Add cryptographic signature support for manifests
  - Define authentication/authorization requirements
  - Add rate limiting recommendations
  - Introduce trust chain verification
- [ ] **Testing and Validation**
  - Comprehensive test suite for all schemas
  - Conformance test suite for implementations
  - Performance benchmarks for reference implementation
  - Security audit of protocol and reference code

---

## Phase 2: Industry Integration (Q4 2026 - Q1 2027)

**Goal**: Enable production pilots with industry partners.

### v0.3.0 - Production Readiness
**Timeline**: October - December 2026

- [ ] **Production-Grade Reference Implementation**
  - Add authentication and authorization
  - Implement proper error handling and logging
  - Add monitoring and observability hooks
  - Create Docker/Kubernetes deployment configurations
  - Add horizontal scaling support
- [ ] **Integration Tooling**
  - CLI tool for signal manifest creation and validation
  - SDKs for popular languages (Python, JavaScript/TypeScript, Java)
  - OpenAPI/Swagger specifications
  - Postman collections and API testing tools
- [ ] **Ecosystem Integration**
  - Formal AdCP extension specification
  - AAMP trust layer reference implementation
  - MCP server implementation for signal trust queries
  - OpenRTB extension for signal trust metadata
- [ ] **Governance Framework**
  - Define protocol governance model
  - Establish working groups for specialization areas
  - Create contribution and review process
  - Set up steering committee for major decisions

### v0.4.0 - Pilot Release
**Timeline**: January - March 2027

- [ ] **Pilot Program Launch**
  - Recruit 3-5 pilot partners (brands, agencies, data providers)
  - Deploy pilot implementations in sandbox environments
  - Collect real-world usage data and feedback
  - Iterate on protocol based on pilot learnings
- [ ] **Enhanced Features**
  - Add support for signal bundles and packages
  - Introduce signal marketplace metadata
  - Add cost/pricing information to manifests
  - Support for signal performance prediction
- [ ] **Monitoring and Analytics**
  - Dashboard for signal trust health monitoring
  - Analytics for signal usage patterns
  - Trust score trend tracking
  - Compliance audit reporting tools
- [ ] **Documentation Expansion**
  - Case studies from pilot implementations
  - Best practices from real-world deployments
  - Common integration patterns and anti-patterns
  - Regulatory compliance guides by region

---

## Phase 3: Standardization and Adoption (Q2-Q4 2027)

**Goal**: Achieve industry-wide standardization and broad adoption.

### v1.0.0 - First Stable Release
**Timeline**: April - June 2027

- [ ] **Protocol Maturity**
  - Finalize v1.0 specification with breaking change commitment
  - Complete security audit by third-party firm
  - Achieve feature parity across reference implementations
  - Publish formal conformance requirements
- [ ] **Standards Body Engagement**
  - Submit protocol to IAB Tech Lab for consideration
  - Present to W3C and other relevant standards bodies
  - Seek endorsement from AdCP and AAMP initiatives
  - Engage with regional advertising associations
- [ ] **Certification Program**
  - Launch conformance certification for implementations
  - Create certification test suite
  - Define certification levels (basic, advanced, regulated)
  - Establish certification authority and process
- [ ] **Enterprise Features**
  - Multi-tenant support for large organizations
  - Advanced policy engine with rule builder
  - Integration with enterprise identity providers (SSO)
  - Compliance reporting for regulated industries

### v1.1.0 - Advanced Features
**Timeline**: July - September 2027

- [ ] **AI and Machine Learning**
  - ML-based trust score prediction
  - Anomaly detection for signal quality degradation
  - Automated policy recommendation based on historical data
  - Natural language policy query interface
- [ ] **Blockchain and Decentralization (Exploratory)**
  - Research decentralized trust registry options
  - Prototype blockchain-based audit trail
  - Investigate zero-knowledge proof for privacy-preserving verification
  - Evaluate distributed signal reputation systems
- [ ] **Advanced Analytics**
  - Signal attribution modeling
  - Cross-signal correlation analysis
  - ROI prediction based on signal trust profiles
  - Automated A/B testing for signal combinations
- [ ] **Regulatory Compliance Expansion**
  - GDPR compliance toolkit
  - CCPA/CPRA compliance verification
  - Regional advertising standards integration (ASA, FTC, etc.)
  - Industry vertical compliance (alcohol, pharma, finance, gambling)

### v1.2.0 - Ecosystem Maturity
**Timeline**: October - December 2027

- [ ] **Marketplace and Discovery**
  - Public signal registry and search
  - Signal comparison and benchmarking tools
  - Reputation system for signal providers
  - Signal recommendation engine for brands
- [ ] **Community and Adoption**
  - Host first OpenSignals Summit conference
  - Launch community certification program
  - Create ambassador program for evangelists
  - Establish regional user groups
- [ ] **Performance and Scale**
  - Optimize for high-throughput verification (1M+ requests/day)
  - Edge deployment support for low-latency verification
  - CDN integration for manifest distribution
  - Multi-region redundancy and failover

---

## Phase 4: Maturity and Innovation (2028+)

**Goal**: Maintain protocol leadership while enabling next-generation features.

### Long-Term Vision

- [ ] **Protocol Extensions**
  - Signal composition and transformation language
  - Real-time signal quality monitoring and alerting
  - Automated signal refresh and validation
  - Cross-platform signal portability standards
- [ ] **Agent Intelligence**
  - Agent-to-agent signal trust negotiation protocol
  - Multi-agent coordination for signal verification
  - Autonomous signal selection based on brand objectives
  - Self-learning policy optimization
- [ ] **Privacy Innovation**
  - Differential privacy for signal trust computation
  - Federated learning for distributed trust scoring
  - Privacy-preserving signal verification techniques
  - Minimal disclosure proofs for compliance
- [ ] **Industry Expansion**
  - Extend beyond advertising to broader marketing signals
  - Apply to content recommendation trust
  - Adapt for e-commerce personalization
  - Explore application in social media and UGC platforms
- [ ] **Global Standardization**
  - Achieve ISO or similar international standard status
  - Regional implementations (EU, APAC, Americas)
  - Harmonization with global privacy and advertising regulations
  - Interoperability with international ad tech standards

---

## Key Success Metrics

### Phase 1 Success Criteria (Foundation)
- 50+ GitHub stars and 10+ community contributors
- 5+ real-world signal manifests created by external parties
- Feedback from 10+ advertising industry stakeholders
- Zero critical security vulnerabilities in reference implementation

### Phase 2 Success Criteria (Integration)
- 3-5 successful pilot implementations
- Integration with at least 2 major ad tech platforms
- 100+ signals registered in pilot environments
- Published case study from pilot partner

### Phase 3 Success Criteria (Standardization)
- 20+ certified implementations
- Endorsement or recognition from at least one standards body
- 1,000+ signals using OpenSignals protocol in production
- 50+ organizations actively using the protocol

### Phase 4 Success Criteria (Maturity)
- 10,000+ signals in production
- 500+ certified organizations
- International standard status or equivalent
- Recognized as de facto standard for signal trust in agentic advertising

---

## How to Contribute to the Roadmap

This roadmap is community-driven. You can contribute by:

- **Feedback**: Comment on roadmap items via GitHub Issues with the `roadmap` label
- **Proposals**: Submit feature proposals via GitHub Discussions
- **Implementation**: Pick up items from the roadmap and submit PRs
- **Sponsorship**: Organizations can sponsor specific roadmap items
- **Pilot Programs**: Join as a pilot partner to validate features in production

For more details, see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Roadmap Governance

The roadmap is maintained by the OpenSignals community and reviewed quarterly. Major changes require:

1. Community discussion via GitHub Discussions
2. Proposal document with rationale and impact analysis
3. Review period (minimum 2 weeks)
4. Approval by maintainers and steering committee (when established)

---

**Last Updated**: 2026-05-11

**Next Review**: 2026-08-01
