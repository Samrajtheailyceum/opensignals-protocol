# Security Policy

## Supported Versions

The OpenSignals Protocol is currently in draft status (v0.1). Security updates will be provided for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

The security of the OpenSignals Protocol is important to us. If you discover a security vulnerability, please follow these guidelines:

### What to Report

Please report any vulnerabilities related to:

- **Protocol Design Flaws**: Issues in the protocol specification that could enable attacks or misuse
- **Reference Implementation**: Security vulnerabilities in the Python reference server or validation code
- **Schema Vulnerabilities**: JSON Schema issues that could allow injection attacks or validation bypass
- **Authentication/Authorization Issues**: Problems with API security or access control recommendations
- **Data Privacy Concerns**: Issues that could compromise user privacy or data protection
- **Cryptographic Weaknesses**: Problems with signature verification or trust chain validation

### How to Report

**Please do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report security vulnerabilities by email to:

**[INSERT SECURITY EMAIL ADDRESS]**

You should receive a response within 48 hours. If for some reason you do not, please follow up via GitHub to ensure we received your original message.

### What to Include

Please include the following information in your report:

- **Type of vulnerability**: Brief description of the issue category
- **Affected component**: Which part of the protocol or implementation is affected
- **Steps to reproduce**: Detailed steps to reproduce the vulnerability
- **Impact assessment**: Your assessment of the potential impact
- **Suggested fix**: If you have ideas on how to address the issue (optional)
- **Proof of concept**: Code or configuration demonstrating the vulnerability (if applicable)

### Response Process

When you report a vulnerability, here's what you can expect:

1. **Acknowledgment**: We will acknowledge receipt of your vulnerability report within 48 hours
2. **Initial Assessment**: We will assess the vulnerability and provide an initial severity rating within 5 business days
3. **Investigation**: We will investigate the issue and determine appropriate remediation steps
4. **Fix Development**: We will develop and test a fix for the vulnerability
5. **Coordinated Disclosure**: We will coordinate with you on a disclosure timeline
6. **Public Disclosure**: After a fix is available, we will publicly disclose the vulnerability with appropriate credit

### Disclosure Policy

- **Embargo Period**: We request a minimum 90-day embargo period before public disclosure to allow time for fix development and deployment
- **Coordinated Disclosure**: We will coordinate disclosure timing with you and provide credit for your discovery (if desired)
- **Public Notice**: Security fixes will be clearly marked in release notes and the CHANGELOG
- **CVE Assignment**: For critical vulnerabilities, we will request CVE assignment through appropriate channels

### Security Best Practices for Implementations

If you are implementing the OpenSignals Protocol, we recommend:

#### API Security
- **Authentication**: Implement proper authentication for all API endpoints (OAuth 2.0, API keys, or JWT)
- **Authorization**: Enforce role-based access control for signal verification and scoring operations
- **Rate Limiting**: Apply rate limits to prevent abuse and denial-of-service attacks
- **Input Validation**: Validate all inputs against JSON Schema definitions
- **Output Sanitization**: Sanitize all outputs to prevent injection attacks

#### Data Protection
- **Encryption in Transit**: Use TLS 1.3+ for all API communications
- **Encryption at Rest**: Encrypt sensitive data stored in databases or file systems
- **PII Handling**: Minimize collection and storage of personally identifiable information
- **Audit Logs**: Maintain secure, tamper-evident audit logs for all signal operations
- **Data Retention**: Implement appropriate data retention and deletion policies

#### Trust and Verification
- **Signature Verification**: Verify cryptographic signatures on signal manifests where applicable
- **Certificate Validation**: Validate TLS certificates and certificate chains
- **Timestamp Validation**: Check freshness of manifests and verify timestamp authenticity
- **Policy Enforcement**: Enforce brand policy rules consistently and securely
- **Human-in-the-Loop**: Require human approval for high-risk operations (regulated categories, low trust scores)

#### Infrastructure Security
- **Dependency Management**: Keep all dependencies up-to-date with security patches
- **Secret Management**: Use secure secret management systems (not environment variables or config files)
- **Access Control**: Implement least-privilege access control for infrastructure components
- **Monitoring**: Deploy security monitoring and alerting systems
- **Incident Response**: Have an incident response plan for security breaches

#### Reference Implementation Warnings

The Python reference implementation in this repository is for **demonstration purposes only** and is **not production-ready**. Before deploying to production:

- Add proper authentication and authorization
- Implement rate limiting and DDoS protection
- Add comprehensive input validation and sanitization
- Enable TLS/HTTPS with valid certificates
- Implement secure session management
- Add security headers (HSTS, CSP, X-Frame-Options, etc.)
- Deploy Web Application Firewall (WAF)
- Conduct security audit and penetration testing
- Implement monitoring and alerting

### Security Updates

Security updates will be announced through:

- **GitHub Security Advisories**: https://github.com/Samrajtheailyceum/opensignals-protocol/security/advisories
- **Release Notes**: Clearly marked security fixes in CHANGELOG.md
- **Mailing List**: [INSERT MAILING LIST IF AVAILABLE]

### Scope

This security policy applies to:

- The OpenSignals Protocol specification (all versions)
- Reference implementations in the `reference-implementation/` directory
- JSON Schema definitions in the `schemas/` directory
- Documentation and examples that could impact security

This policy does NOT cover:

- Third-party implementations of the protocol
- Security issues in AdCP, AAMP, or other integrated protocols (report those to their respective maintainers)
- General questions about protocol usage (use GitHub Discussions instead)

### Attribution

We believe in giving credit where it's due. If you report a valid security vulnerability, we will:

- Credit you in the security advisory (if you wish)
- Include your name in the CHANGELOG for the fix (if you wish)
- Consider you for recognition in our acknowledgments section

You may remain anonymous if preferred.

## Additional Resources

- [OpenSignals Protocol Specification](specs/opensignals-v0.1.md)
- [Contributing Guidelines](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)

## Questions

If you have questions about this security policy or general security concerns (not specific vulnerabilities), please open a GitHub Discussion or Issue with the `security` label.

---

**Last Updated**: 2026-05-11
