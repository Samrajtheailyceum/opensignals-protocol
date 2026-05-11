# OpenSignals Protocol: Conformance Requirements

**Version**: 0.1
**Status**: Draft
**Last Updated**: May 2026

---

## Overview

This document specifies detailed conformance requirements for implementations of the OpenSignals Protocol v0.1. Conformance ensures interoperability across signal providers, buyer agents, governance agents, audit agents, and execution platforms.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

---

## Table of Contents

1. [Conformance Levels](#1-conformance-levels)
2. [Signal Provider Conformance](#2-signal-provider-conformance)
3. [Buyer Agent Conformance](#3-buyer-agent-conformance)
4. [Governance Agent Conformance](#4-governance-agent-conformance)
5. [Audit Agent Conformance](#5-audit-agent-conformance)
6. [Execution Platform Conformance](#6-execution-platform-conformance)
7. [Transport and Encoding Requirements](#7-transport-and-encoding-requirements)
8. [Manifest Schema Conformance](#8-manifest-schema-conformance)
9. [Trust Scoring Conformance](#9-trust-scoring-conformance)
10. [Permissioning Conformance](#10-permissioning-conformance)
11. [Audit Trail Conformance](#11-audit-trail-conformance)
12. [Security and Privacy Conformance](#12-security-and-privacy-conformance)
13. [Error Handling Requirements](#13-error-handling-requirements)
14. [Versioning and Backward Compatibility](#14-versioning-and-backward-compatibility)
15. [Testing and Validation](#15-testing-and-validation)
16. [Conformance Certification](#16-conformance-certification)

---

## 1. Conformance Levels

OpenSignals defines three conformance levels:

### 1.1 Core Conformance

Implements all MUST and MUST NOT requirements for the entity type. Core conformance is required for claiming OpenSignals compliance.

### 1.2 Extended Conformance

Implements all MUST, MUST NOT, and SHOULD requirements. Extended conformance demonstrates best-practice implementation.

### 1.3 Full Conformance

Implements all MUST, MUST NOT, SHOULD, and documented MAY features. Full conformance demonstrates complete protocol support.

### 1.4 Conformance Claims

Implementations claiming conformance MUST:

1. Specify the entity type (Signal Provider, Buyer Agent, Governance Agent, Audit Agent, Execution Platform)
2. Specify the conformance level (Core, Extended, or Full)
3. Specify the protocol version (e.g., "OpenSignals v0.1")
4. Document any optional features implemented
5. Document any extensions or deviations from the specification

**Example conformance claim**:
```
This implementation conforms to OpenSignals Protocol v0.1 as a Signal Provider at Extended Conformance level.
Optional features: Cryptographic provenance verification, Real-time freshness updates.
Extensions: Custom signal type "brand_affinity" with extended metadata.
```

---

## 2. Signal Provider Conformance

### 2.1 Required Features (MUST)

A conforming Signal Provider:

#### 2.1.1 Manifest Publication

1. MUST publish an OpenSignal Manifest for each signal
2. MUST include all required fields as specified in Section 8.2.1 of the protocol specification:
   - `protocol` (value: "opensignals")
   - `version` (value: "0.1")
   - `signal_id` (globally unique identifier)
   - `name`
   - `signal_type`
   - `status`
   - `owner` (with organization and contact)
   - `provider` (with name and url)
   - `provenance` (complete object)
   - `quality` (complete object with all seven dimension scores)
   - `permissioning` (complete object)
   - `governance` (complete object)
3. MUST use signal types from the standard taxonomy (Section 7) or declare `custom` with documentation
4. MUST ensure manifests are valid JSON according to OpenSignals JSON Schema
5. MUST use ISO 8601 format for all timestamps and dates
6. MUST use ISO 3166-1 alpha-2 codes for all country references

#### 2.1.2 Provenance Declaration

1. MUST declare all data sources using the standard data source taxonomy
2. MUST declare collection method using the standard collection method taxonomy
3. MUST include `last_updated` timestamp in provenance object
4. MUST declare `update_frequency` using standard frequency values

#### 2.1.3 Trust Scoring

1. MUST calculate and publish trust scores for all seven dimensions:
   - `provenance_score`
   - `permissioning_score`
   - `freshness_score`
   - `quality_score`
   - `explainability_score`
   - `outcome_score`
   - `compliance_score`
2. MUST calculate `overall_trust_score` as a weighted sum (Section 9.2)
3. MUST ensure all scores are in the range 0.00 to 1.00
4. MUST include reasoning for each dimension score

#### 2.1.4 Permissioning Declaration

1. MUST declare valid use cases (at least one)
2. MUST declare consent scope
3. MUST declare geographic restrictions (empty array if none)
4. MUST declare category restrictions (empty array if none)
5. MUST declare `individual_profiling_allowed` (boolean)
6. MUST declare `sensitive_categories_allowed` (boolean)

#### 2.1.5 Governance Declaration

1. MUST declare decision mode
2. MUST declare `audit_required` (boolean)
3. MUST declare `human_approval_required_for_categories` (array, may be empty)

#### 2.1.6 Protocol Task Implementation

1. MUST implement `get_signal_manifest` task
2. MUST return manifests in valid JSON format
3. MUST include appropriate HTTP headers (Content-Type: application/json)
4. MUST return HTTP 200 for successful requests
5. MUST return appropriate error codes (404 for not found, 500 for server errors)

### 2.2 Recommended Features (SHOULD)

A conforming Signal Provider:

1. SHOULD publish manifests at well-known URLs: `https://{provider-domain}/.well-known/opensignals/{signal_id}`
2. SHOULD implement HTTPS with valid TLS certificates
3. SHOULD support HTTP caching headers (Cache-Control, ETag)
4. SHOULD implement rate limiting to prevent abuse
5. SHOULD update manifests within 24 hours of material signal changes
6. SHOULD implement the `revoke_signal` task
7. SHOULD provide `documentation_url` in provider object
8. SHOULD include `chain_of_custody` for multi-party data lineage
9. SHOULD implement cryptographic verification where appropriate
10. SHOULD respond to manifest requests within 5 seconds

### 2.3 Optional Features (MAY)

A conforming Signal Provider:

1. MAY implement cryptographic provenance verification
2. MAY provide real-time freshness updates
3. MAY implement custom signal types with extended metadata
4. MAY provide multiple manifest formats (JSON-LD, XML)
5. MAY implement content negotiation for manifest formats
6. MAY provide versioned manifest URLs
7. MAY implement webhook notifications for manifest updates
8. MAY support batch manifest requests

### 2.4 Prohibited Behaviors (MUST NOT)

A conforming Signal Provider:

1. MUST NOT include individual-level user data in manifests
2. MUST NOT return manifests with trust scores outside the 0.00-1.00 range
3. MUST NOT declare use cases that are not actually permitted
4. MUST NOT omit required fields from manifests
5. MUST NOT return manifests that fail JSON Schema validation
6. MUST NOT use non-standard signal types without documentation

---

## 3. Buyer Agent Conformance

### 3.1 Required Features (MUST)

A conforming Buyer Agent:

#### 3.1.1 Signal Verification

1. MUST call `verify_signal` before activating any signal
2. MUST include all required context fields in verification requests:
   - `brand`
   - `market`
   - `category`
   - `intended_use`
3. MUST respect verification decisions:
   - `approved`: MAY activate immediately
   - `approved_with_conditions`: MUST enforce conditions
   - `rejected`: MUST NOT activate
   - `approval_pending`: MUST wait for approval or reject
4. MUST NOT activate signals in restricted geographies declared in `geographic_restrictions`
5. MUST NOT activate signals in restricted categories declared in `category_restrictions`
6. MUST NOT use signals for use cases not declared in `valid_use_cases`

#### 3.1.2 Bounded Autonomy Compliance

1. MUST respect `decision_mode` from governance responses
2. MUST obtain human approval when `approval_required: true`
3. MUST NOT activate signals with trust scores below brand-defined thresholds
4. MUST respect `human_approval_required_for_categories`

#### 3.1.3 Audit Trail Logging

1. MUST log signal activations via `audit_signal_usage` task
2. MUST include all required audit event fields:
   - `event_type`
   - `timestamp`
   - `signal_id`
   - `brand`
   - `campaign_id`
   - `buyer_agent` (self-identification)
   - `governance_agent`
   - `decision_mode`
   - `trust_score`
   - `use_case`
   - `platform`
   - `category`
3. MUST log audit events within 1 hour of signal activation
4. MUST include policy bindings in audit events if applicable

#### 3.1.4 Individual Profiling Restrictions

1. MUST NOT perform individual profiling if `individual_profiling_allowed: false`
2. MUST NOT use signals for sensitive categories if `sensitive_categories_allowed: false`

### 3.2 Recommended Features (SHOULD)

A conforming Buyer Agent:

1. SHOULD call `score_signal` to assess objective alignment before activation
2. SHOULD cache manifests according to `freshness_ttl`
3. SHOULD re-verify signals when cache expires
4. SHOULD submit outcome feedback via `submit_signal_outcome_feedback` after campaigns complete
5. SHOULD respect `valid_until` timestamps from verification responses
6. SHOULD implement retry logic for failed verification requests
7. SHOULD provide detailed reasoning in audit events
8. SHOULD include activation details (budget, impressions, dates) in audit events
9. SHOULD monitor for signal revocation notifications
10. SHOULD implement graceful degradation when verification services are unavailable

### 3.3 Optional Features (MAY)

A conforming Buyer Agent:

1. MAY implement custom trust score adjustments based on brand-specific performance
2. MAY pre-verify signals asynchronously to reduce activation latency
3. MAY implement predictive scoring for objective alignment
4. MAY cache verification decisions for short durations (< 1 hour)
5. MAY implement A/B testing for signal effectiveness
6. MAY provide user interfaces for human approval workflows
7. MAY integrate with multiple governance agents for consensus-based verification

### 3.4 Prohibited Behaviors (MUST NOT)

A conforming Buyer Agent:

1. MUST NOT activate signals without verification
2. MUST NOT ignore verification rejections
3. MUST NOT use signals beyond their declared valid use cases
4. MUST NOT activate signals in restricted geographies or categories
5. MUST NOT skip audit logging
6. MUST NOT perform individual profiling when prohibited
7. MUST NOT bypass human approval requirements

---

## 4. Governance Agent Conformance

### 4.1 Required Features (MUST)

A conforming Governance Agent:

#### 4.1.1 Signal Verification Implementation

1. MUST implement `verify_signal` task
2. MUST evaluate signals against brand policy
3. MUST evaluate signals against regulatory requirements (GDPR, CCPA, category-specific)
4. MUST return one of four valid decisions: `approved`, `approved_with_conditions`, `rejected`, `approval_pending`
5. MUST include decision reasoning in verification responses
6. MUST include trust score in verification responses
7. MUST include trust band in verification responses
8. MUST enforce geographic restrictions
9. MUST enforce category restrictions
10. MUST determine appropriate decision mode based on:
    - Signal trust score
    - Signal category
    - Brand policy
    - Regulatory requirements

#### 4.1.2 Policy Binding Implementation

1. MUST implement `bind_signal_policy` task
2. MUST attach relevant brand policies to signals before activation
3. MUST specify enforcement level for each binding (mandatory, recommended, advisory)
4. MUST include policy parameters in bindings
5. MUST generate unique binding IDs
6. MUST include timestamp and agent identification in bindings

#### 4.1.3 Human Approval Workflows

1. MUST require human approval for signals in `human_approval_required_for_categories`
2. MUST require human approval for signals with trust scores below brand-defined thresholds
3. MUST return `approval_pending` decision when human approval is required
4. MUST provide `approval_request_id` for pending approvals
5. MUST notify human approvers when approval is required

### 4.2 Recommended Features (SHOULD)

A conforming Governance Agent:

1. SHOULD implement `score_signal` task
2. SHOULD provide objective alignment scoring
3. SHOULD include expected performance estimates in scoring responses
4. SHOULD integrate with brand safety platforms for content risk assessment
5. SHOULD implement approval workflow tracking and status endpoints
6. SHOULD provide approval history for audit purposes
7. SHOULD implement time limits for approval requests (e.g., expire after 24 hours)
8. SHOULD provide detailed reasoning for all decisions
9. SHOULD support brand-specific trust score weight customization
10. SHOULD validate manifest integrity before evaluation

### 4.3 Optional Features (MAY)

A conforming Governance Agent:

1. MAY implement multi-factor trust scoring with custom dimensions
2. MAY integrate with external compliance validation services
3. MAY provide predictive risk scoring for signal combinations
4. MAY implement consensus-based verification across multiple governance systems
5. MAY provide user interfaces for brand policy configuration
6. MAY support dynamic policy updates without service restart
7. MAY implement machine learning models for outcome prediction

### 4.4 Prohibited Behaviors (MUST NOT)

A conforming Governance Agent:

1. MUST NOT approve signals for restricted geographies
2. MUST NOT approve signals for restricted categories
3. MUST NOT skip brand policy evaluation
4. MUST NOT skip regulatory compliance checks
5. MUST NOT return decisions without reasoning
6. MUST NOT bypass human approval when required
7. MUST NOT ignore signal manifest trust scores

---

## 5. Audit Agent Conformance

### 5.1 Required Features (MUST)

A conforming Audit Agent:

#### 5.1.1 Audit Event Logging

1. MUST implement `audit_signal_usage` task
2. MUST accept audit events with all required fields
3. MUST generate unique audit IDs for each event
4. MUST timestamp each audit event upon receipt
5. MUST store audit events in tamper-evident storage
6. MUST retain audit logs for declared `audit_retention_days` (default: 90 days)
7. MUST return audit ID and retention timestamp in responses

#### 5.1.2 Audit Trail Integrity

1. MUST ensure audit logs are append-only
2. MUST protect audit logs from unauthorized modification
3. MUST implement access controls for audit log queries
4. MUST log all access to audit data for security auditing

### 5.2 Recommended Features (SHOULD)

A conforming Audit Agent:

1. SHOULD provide queryable audit trail APIs
2. SHOULD support filtering by brand, campaign, date range, signal, category
3. SHOULD support audit export in JSON and CSV formats
4. SHOULD implement cryptographic hashing for tamper evidence
5. SHOULD provide audit trail analytics and reporting
6. SHOULD implement longer retention for regulated categories (e.g., 2-7 years)
7. SHOULD notify stakeholders of unusual audit patterns (e.g., repeated rejections)
8. SHOULD integrate with SIEM systems for security monitoring
9. SHOULD provide compliance reporting templates (GDPR, CCPA, industry-specific)
10. SHOULD implement backup and disaster recovery for audit data

### 5.3 Optional Features (MAY)

A conforming Audit Agent:

1. MAY implement distributed ledger technology for immutable audit trails
2. MAY provide real-time audit dashboards
3. MAY implement anomaly detection for compliance violations
4. MAY support blockchain-based audit verification
5. MAY provide API integration with external compliance systems
6. MAY implement automated regulatory reporting
7. MAY support multi-tenancy for agency/brand segregation

### 5.4 Prohibited Behaviors (MUST NOT)

A conforming Audit Agent:

1. MUST NOT allow modification of historical audit events
2. MUST NOT delete audit logs before retention period expires
3. MUST NOT expose audit logs without proper authentication
4. MUST NOT accept audit events with missing required fields
5. MUST NOT fail to timestamp audit events
6. MUST NOT allow unauthorized access to audit data

---

## 6. Execution Platform Conformance

Execution Platform conformance is OPTIONAL. Platforms that choose to implement OpenSignals support should follow these guidelines.

### 6.1 Recommended Features (SHOULD)

A conforming Execution Platform:

1. SHOULD enforce trust thresholds before activating signals
2. SHOULD respect policy bindings included in activation requests
3. SHOULD log signal activations to audit agents
4. SHOULD integrate OpenSignals metadata into bid requests (OpenRTB) or insertion orders (OpenDirect)
5. SHOULD provide outcome feedback to signal providers
6. SHOULD validate that signals meet minimum trust scores before activation
7. SHOULD enforce geographic and category restrictions
8. SHOULD provide dashboards showing trust scores for active signals

### 6.2 Optional Features (MAY)

A conforming Execution Platform:

1. MAY implement automatic signal verification on behalf of buyer agents
2. MAY provide trust-aware optimization algorithms
3. MAY support OpenSignals extensions in OpenRTB/OpenDirect protocols
4. MAY implement signal revocation monitoring and automatic deactivation
5. MAY provide trust score reporting in campaign analytics

### 6.3 Prohibited Behaviors (MUST NOT)

A conforming Execution Platform:

1. MUST NOT activate signals that fail verification
2. MUST NOT ignore policy bindings
3. MUST NOT activate signals in restricted geographies or categories

---

## 7. Transport and Encoding Requirements

### 7.1 HTTP Transport (RECOMMENDED)

Implementations using HTTP:

1. MUST support HTTPS (TLS 1.2 or higher)
2. MUST use valid TLS certificates from recognized certificate authorities
3. MUST set `Content-Type: application/json` for JSON responses
4. MUST use standard HTTP status codes:
   - 200: Success
   - 400: Bad request (invalid input)
   - 401: Unauthorized
   - 403: Forbidden
   - 404: Not found
   - 429: Rate limit exceeded
   - 500: Internal server error
   - 503: Service unavailable
5. SHOULD implement HTTP caching where appropriate (Cache-Control, ETag)
6. SHOULD implement rate limiting (with 429 responses)
7. SHOULD support CORS for browser-based agents
8. MAY require authentication (OAuth 2.0, API keys, mTLS)

### 7.2 JSON Encoding

1. MUST use UTF-8 encoding for all JSON
2. MUST follow JSON RFC 8259
3. MUST validate against OpenSignals JSON Schemas
4. SHOULD minimize whitespace in production responses
5. SHOULD support pretty-printed JSON for debugging

### 7.3 Alternative Transports

Implementations MAY use alternative transports:
- MCP (Model Context Protocol)
- A2A (Agent2Agent Protocol)
- gRPC
- GraphQL
- Custom RPC protocols

When using alternative transports, implementations MUST maintain semantic equivalence with the HTTP specification.

---

## 8. Manifest Schema Conformance

### 8.1 Schema Validation

Signal Providers:

1. MUST ensure manifests validate against OpenSignals JSON Schema v0.1
2. MUST include all required fields
3. MUST use correct data types for all fields
4. MUST use enumerations from standard taxonomies where specified
5. SHOULD validate manifests before publication

### 8.2 Field Constraints

#### 8.2.1 String Fields

1. `signal_id`: MUST be unique, alphanumeric with hyphens, max 128 characters
2. `name`: Max 256 characters
3. URLs: MUST be valid HTTPS URLs
4. Email addresses: MUST be valid email format
5. Country codes: MUST be ISO 3166-1 alpha-2
6. Timestamps: MUST be ISO 8601 format with timezone

#### 8.2.2 Numeric Fields

1. Trust scores: MUST be 0.00 to 1.00 (inclusive)
2. `audit_retention_days`: MUST be positive integer
3. `data_retention_days`: MUST be positive integer
4. `freshness_ttl`: MUST be positive integer (seconds)

#### 8.2.3 Boolean Fields

1. MUST use JSON boolean values: `true` or `false`
2. MUST NOT use strings, numbers, or null

#### 8.2.4 Array Fields

1. Empty arrays MUST be represented as `[]`, not null
2. Array elements MUST match declared types

#### 8.2.5 Object Fields

1. Required objects MUST NOT be null
2. Optional objects MAY be omitted

---

## 9. Trust Scoring Conformance

### 9.1 Score Calculation

Signal Providers:

1. MUST calculate all seven dimension scores
2. MUST use the standard weighted formula for overall trust score:
   ```
   overall = (provenance × 0.20) + (permissioning × 0.20) + (freshness × 0.15) +
             (quality × 0.20) + (explainability × 0.10) + (outcome × 0.10) +
             (compliance × 0.05)
   ```
3. MUST ensure calculated overall score matches published score (within 0.01 tolerance for rounding)
4. MUST NOT publish scores outside 0.00-1.00 range
5. SHOULD document scoring methodology

Governance Agents:

1. MAY adjust weights based on brand priorities
2. MUST document weight adjustments in verification responses
3. MUST recalculate overall score if weights are adjusted

### 9.2 Score Reasoning

Implementations:

1. MUST provide reasoning for each dimension score
2. SHOULD provide actionable feedback for low scores
3. SHOULD reference specific manifest fields in reasoning

### 9.3 Score Freshness

Signal Providers:

1. MUST update trust scores when signal properties change materially
2. SHOULD recalculate freshness score daily
3. SHOULD recalculate outcome score when new performance data is available

---

## 10. Permissioning Conformance

### 10.1 Use Case Declaration

Signal Providers:

1. MUST declare at least one valid use case
2. MUST use standard use case values or document custom use cases
3. MUST NOT declare use cases that are not actually permitted

Buyer Agents:

1. MUST verify intended use case is in `valid_use_cases` before activation
2. MUST NOT use signals for undeclared use cases

### 10.2 Consent Scope

Signal Providers:

1. MUST declare consent scope accurately
2. MUST update consent scope if consent terms change
3. MUST honor user consent revocations

### 10.3 Geographic and Category Restrictions

Signal Providers:

1. MUST declare all geographic restrictions as ISO 3166-1 alpha-2 codes
2. MUST declare all category restrictions using standard category taxonomy

Buyer Agents and Governance Agents:

1. MUST enforce geographic restrictions
2. MUST enforce category restrictions
3. MUST NOT activate signals in restricted geographies or categories

---

## 11. Audit Trail Conformance

### 11.1 Required Audit Fields

Buyer Agents and Execution Platforms:

1. MUST include all required fields in audit events (see Section 13.2 of specification)
2. MUST use ISO 8601 timestamps
3. MUST identify buyer agent, governance agent, and platform

Audit Agents:

1. MUST validate audit events have all required fields
2. MUST reject incomplete audit events with 400 error

### 11.2 Audit Retention

Audit Agents:

1. MUST retain audit logs for declared `audit_retention_days`
2. SHOULD retain longer for regulated categories
3. MUST NOT delete logs before retention period expires

### 11.3 Audit Trail Access

Audit Agents:

1. MUST implement authentication for audit trail queries
2. MUST authorize access based on brand, agent, or stakeholder identity
3. SHOULD log all audit trail access for security purposes

---

## 12. Security and Privacy Conformance

### 12.1 Authentication

Implementations:

1. SHOULD implement authentication for all API endpoints
2. SHOULD use OAuth 2.0, API keys, or mTLS
3. SHOULD implement token expiration and rotation

### 12.2 Data Minimization

All implementations:

1. MUST NOT include individual-level user data in manifests, verification requests, or responses
2. MUST use aggregate data only
3. MUST NOT log individual user identifiers in audit trails

### 12.3 Encryption

Implementations:

1. MUST use HTTPS (TLS 1.2+) for all HTTP transport
2. SHOULD encrypt audit logs at rest
3. SHOULD encrypt sensitive configuration data

### 12.4 Privacy Compliance

Signal Providers:

1. MUST comply with GDPR, CCPA, and applicable privacy regulations
2. MUST honor user consent revocations
3. MUST support user data deletion requests

### 12.5 Security Vulnerability Response

All implementations:

1. SHOULD provide security contact information
2. SHOULD respond to vulnerability reports within 30 days
3. SHOULD publish security advisories for critical vulnerabilities

---

## 13. Error Handling Requirements

### 13.1 Error Response Format

All implementations:

1. MUST return structured error responses in JSON format:
   ```json
   {
     "error": {
       "code": "string",
       "message": "string",
       "details": "string (optional)"
     }
   }
   ```
2. MUST use appropriate HTTP status codes
3. SHOULD include actionable error messages

### 13.2 Standard Error Codes

Implementations SHOULD use these standard error codes:

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `signal_not_found` | 404 | Signal ID does not exist |
| `manifest_invalid` | 400 | Manifest fails schema validation |
| `verification_failed` | 400 | Verification request invalid or incomplete |
| `signal_restricted` | 403 | Signal restricted for requested geography or category |
| `trust_threshold_not_met` | 403 | Signal trust score below required threshold |
| `approval_required` | 202 | Human approval required (not an error; use 202 Accepted) |
| `signal_revoked` | 410 | Signal has been revoked |
| `rate_limit_exceeded` | 429 | Too many requests |
| `internal_error` | 500 | Internal server error |
| `service_unavailable` | 503 | Service temporarily unavailable |

### 13.3 Timeout Handling

Implementations:

1. SHOULD implement reasonable timeouts (e.g., 30 seconds for verification)
2. SHOULD return 503 if dependencies time out
3. SHOULD implement retry logic with exponential backoff

---

## 14. Versioning and Backward Compatibility

### 14.1 Protocol Versioning

All implementations:

1. MUST declare protocol version in manifests and responses (`version: "0.1"`)
2. MUST support version negotiation if multiple versions are implemented
3. SHOULD maintain backward compatibility within major versions

### 14.2 Manifest Versioning

Signal Providers:

1. MUST update `last_updated` timestamp when manifests change
2. SHOULD provide version history or changelog
3. MAY support versioned manifest URLs

### 14.3 Deprecation

Signal Providers:

1. SHOULD announce deprecations at least 30 days in advance
2. SHOULD update signal `status` to `deprecated` before removal
3. SHOULD provide migration guidance for deprecated signals

---

## 15. Testing and Validation

### 15.1 Manifest Validation

Signal Providers:

1. SHOULD validate manifests against JSON Schema before publication
2. SHOULD implement automated validation in CI/CD pipelines
3. SHOULD test manifest accessibility from public networks

### 15.2 Protocol Task Testing

All implementations:

1. SHOULD implement unit tests for all protocol tasks
2. SHOULD implement integration tests for cross-entity workflows
3. SHOULD test error handling and edge cases
4. SHOULD test performance under load

### 15.3 Interoperability Testing

Implementations:

1. SHOULD test interoperability with reference implementations
2. SHOULD participate in industry interoperability testing events
3. SHOULD provide test environments for integration partners

### 15.4 Conformance Test Suites

The OpenSignals community MAY provide conformance test suites. Implementations SHOULD run test suites and publish results.

---

## 16. Conformance Certification

### 16.1 Self-Certification

Implementations MAY self-certify conformance by:

1. Documenting conformance level (Core, Extended, Full)
2. Running validation tests
3. Publishing conformance claims
4. Documenting deviations or extensions

### 16.2 Third-Party Certification

Industry bodies MAY offer third-party conformance certification. Certification programs SHOULD:

1. Define objective conformance tests
2. Provide clear certification criteria
3. Issue time-limited certificates (e.g., valid for 1 year)
4. Require recertification for major version changes

### 16.3 Conformance Badges

Implementations MAY display conformance badges in documentation:

```
✓ OpenSignals v0.1 Conformant (Signal Provider, Extended)
✓ OpenSignals v0.1 Conformant (Buyer Agent, Core)
```

Badges MUST accurately represent certified conformance level.

---

## 17. Non-Conformance Handling

### 17.1 Reporting Non-Conformance

Issues with implementations claiming conformance should be reported through:

1. GitHub issues on the OpenSignals repository
2. Direct contact with the implementing organization
3. Industry standards bodies if formal certification exists

### 17.2 Consequences of Non-Conformance

Implementations found to be non-conformant:

1. SHOULD remedy issues within a reasonable timeframe
2. SHOULD update conformance claims if unable to remedy
3. MAY lose certification status if third-party certified

---

## Appendix A: Conformance Checklist

### Signal Provider Checklist

**Core Conformance (MUST)**:
- [ ] Publishes valid OpenSignal Manifests for all signals
- [ ] Includes all required fields (protocol, version, signal_id, name, type, status, owner, provider, provenance, quality, permissioning, governance)
- [ ] Uses standard signal types or documents custom types
- [ ] Declares complete provenance (sources, method, last_updated, frequency)
- [ ] Calculates all seven trust dimension scores
- [ ] Calculates overall trust score with standard weights
- [ ] Declares valid use cases and consent scope
- [ ] Declares geographic and category restrictions
- [ ] Implements get_signal_manifest task
- [ ] Returns valid JSON responses
- [ ] Uses appropriate HTTP status codes

**Extended Conformance (SHOULD)**:
- [ ] Publishes manifests at well-known URLs
- [ ] Implements HTTPS with valid certificates
- [ ] Updates manifests within 24 hours of material changes
- [ ] Implements revoke_signal task
- [ ] Includes chain of custody for multi-party data
- [ ] Responds to manifest requests within 5 seconds

**Full Conformance (MAY)**:
- [ ] Implements cryptographic provenance verification
- [ ] Provides real-time freshness updates
- [ ] Supports multiple manifest formats

### Buyer Agent Checklist

**Core Conformance (MUST)**:
- [ ] Calls verify_signal before every activation
- [ ] Includes all required context in verification requests
- [ ] Respects verification decisions (approved, rejected, pending)
- [ ] Enforces geographic and category restrictions
- [ ] Respects valid use cases
- [ ] Obtains human approval when required
- [ ] Logs audit events via audit_signal_usage
- [ ] Includes all required audit event fields
- [ ] Logs audit within 1 hour of activation
- [ ] Respects individual profiling restrictions

**Extended Conformance (SHOULD)**:
- [ ] Calls score_signal for objective alignment
- [ ] Caches manifests according to freshness_ttl
- [ ] Submits outcome feedback after campaigns
- [ ] Implements retry logic for verification failures
- [ ] Monitors for signal revocation notifications

**Full Conformance (MAY)**:
- [ ] Implements custom trust score adjustments
- [ ] Pre-verifies signals asynchronously
- [ ] Provides user interfaces for human approval

### Governance Agent Checklist

**Core Conformance (MUST)**:
- [ ] Implements verify_signal task
- [ ] Evaluates signals against brand policy
- [ ] Evaluates signals against regulatory requirements
- [ ] Returns valid decisions with reasoning
- [ ] Implements bind_signal_policy task
- [ ] Enforces geographic and category restrictions
- [ ] Requires human approval for regulated categories
- [ ] Provides approval request IDs for pending approvals

**Extended Conformance (SHOULD)**:
- [ ] Implements score_signal task
- [ ] Integrates with brand safety platforms
- [ ] Implements approval workflow tracking
- [ ] Provides detailed reasoning for all decisions
- [ ] Validates manifest integrity before evaluation

**Full Conformance (MAY)**:
- [ ] Implements custom trust scoring dimensions
- [ ] Provides predictive risk scoring
- [ ] Supports dynamic policy updates

### Audit Agent Checklist

**Core Conformance (MUST)**:
- [ ] Implements audit_signal_usage task
- [ ] Accepts events with all required fields
- [ ] Generates unique audit IDs
- [ ] Timestamps events upon receipt
- [ ] Stores events in tamper-evident storage
- [ ] Retains logs for declared retention period
- [ ] Protects logs from modification

**Extended Conformance (SHOULD)**:
- [ ] Provides queryable audit trail APIs
- [ ] Supports filtering and export
- [ ] Implements cryptographic hashing
- [ ] Provides compliance reporting templates
- [ ] Implements backup and disaster recovery

**Full Conformance (MAY)**:
- [ ] Implements distributed ledger technology
- [ ] Provides real-time audit dashboards
- [ ] Implements anomaly detection

---

## Appendix B: Conformance Testing Resources

### Test Data

The OpenSignals repository provides:
- Sample valid manifests
- Sample invalid manifests (for negative testing)
- Sample verification requests and responses
- Sample audit events

### Validation Tools

Reference implementations and validation tools:
- JSON Schema validators
- Manifest validation scripts
- Protocol task testing frameworks

### Community Support

Conformance questions:
- GitHub Issues with `conformance` label
- Community discussion forums
- Protocol specification Q&A

---

## References

- **OpenSignals Protocol v0.1 Specification**: [opensignals-v0.1.md](opensignals-v0.1.md)
- **OpenSignals Terminology**: [terminology.md](terminology.md)
- **RFC 2119 (Key words for RFCs)**: [https://datatracker.ietf.org/doc/html/rfc2119](https://datatracker.ietf.org/doc/html/rfc2119)
- **RFC 8259 (JSON)**: [https://datatracker.ietf.org/doc/html/rfc8259](https://datatracker.ietf.org/doc/html/rfc8259)
- **JSON Schema**: [https://json-schema.org](https://json-schema.org)

---

**Document Status**: Draft
**Protocol Version**: 0.1
**Last Updated**: May 2026
**Repository**: [https://github.com/opensignals-protocol/opensignals-protocol](https://github.com/opensignals-protocol/opensignals-protocol)
