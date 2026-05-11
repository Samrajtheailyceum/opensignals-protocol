# Contributing to OpenSignals Protocol

Thank you for your interest in contributing to OpenSignals Protocol. This document provides guidelines for contributing to the protocol specification, schemas, examples and reference implementations.

## Project Goals

OpenSignals Protocol aims to create a practical, implementable standard for signal trust verification in agentic advertising. The protocol should:

- Complement existing standards (AdCP, AAMP, OpenRTB) rather than replace them
- Remain vendor-neutral and avoid marketing claims
- Focus on real-world signal trust challenges
- Be clear, precise and implementable
- Maintain credibility with brands, agencies, platforms and standards bodies

## How to Contribute

### Reporting Issues

Use GitHub Issues to report:

- Specification ambiguities or errors
- Schema validation problems
- Missing use cases or signal types
- Integration challenges with existing protocols
- Documentation improvements

When opening an issue, please:

- Use a clear, descriptive title
- Provide context about the problem
- Include specific examples where relevant
- Tag appropriately (`spec-question`, `schema`, `integration-example`, `documentation`)

### Proposing Protocol Changes

For significant changes to the protocol specification:

1. **Open an issue first** to discuss the proposal
2. Clearly describe the problem being solved
3. Explain why existing mechanisms are insufficient
4. Provide concrete examples of the proposed change
5. Consider backwards compatibility implications
6. Wait for community feedback before submitting a pull request

### Submitting Pull Requests

1. **Fork the repository** and create a feature branch
2. **Make your changes** following the style guidelines below
3. **Test your changes**:
   - For schema changes, validate against example files
   - For code changes, run tests with `pytest tests/`
   - For documentation, check spelling and formatting
4. **Write clear commit messages** explaining why the change is needed
5. **Submit a pull request** with a detailed description

### Adding New Schemas

When proposing a new JSON schema:

1. Place it in `schemas/v0.1/` with a descriptive filename
2. Use JSON Schema Draft 2020-12
3. Include `$schema`, `$id`, `title`, `description`, `type` and `required` fields
4. Add validation rules (enums, formats, ranges) where appropriate
5. Provide at least one example file that validates against the schema
6. Update `specs/opensignals-v0.1.md` to reference the new schema
7. Run validation tests: `python reference-implementation/python/validator.py`

### Adding Signal Types

To propose a new signal type for the `signal_type` enum:

1. Open an issue with the `signal-type-proposal` label
2. Describe the signal type and its use cases
3. Explain why it cannot be classified under existing types
4. Provide at least one complete example manifest
5. Consider trust scoring implications for this signal type
6. Document any special compliance or policy considerations

### Adding Examples

Example manifests help implementers understand the protocol. When contributing an example:

1. Place JSON files in `examples/` with descriptive filenames
2. Ensure the example validates against `open-signal-manifest.schema.json`
3. Use realistic but fictional data (no real brand names or proprietary data)
4. Include comments (if using JSON5) or a companion README explaining the scenario
5. Demonstrate specific trust or governance challenges where relevant

### Contributing Integration Examples

Integration examples show how OpenSignals works with existing protocols:

**AdCP integrations** (`integrations/adcp/`):
- Must be clearly labelled as conceptual examples
- Should reference official AdCP documentation
- Must not claim official endorsement
- Should demonstrate practical extension points

**AAMP mappings** (`integrations/aamp/`):
- Focus on conceptual alignment with AAMP's Trust and Transparency pillar
- Reference official AAMP documentation where possible
- Avoid claiming formal integration without confirmation
- Explain how OpenSignals complements AAMP goals

**Other protocols**:
- Create a new subdirectory under `integrations/`
- Include a README explaining the relationship
- Cite official sources
- Distinguish confirmed integrations from conceptual mappings

### Documentation Guidelines

All documentation should be:

- **Clear**: Use plain language where possible
- **Precise**: Avoid ambiguity in specifications
- **Neutral**: No vendor-specific marketing claims
- **Cited**: Reference official sources for compatibility claims
- **Honest**: Distinguish conceptual from confirmed integrations

**Style guidelines:**

- Use British English spelling in documentation
- Use RFC 2119 keywords (MUST, SHOULD, MAY) appropriately in specifications
- Use present tense in specifications
- Use markdown for formatting
- Include code blocks with appropriate language tags
- Provide examples for complex concepts

### Code Style

**Python reference implementation:**

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Include docstrings for public functions
- Keep code simple and readable (this is a reference implementation, not production code)
- Add comments explaining non-obvious logic
- Write tests for new functionality

**JSON schemas and examples:**

- Use 2-space indentation
- Use snake_case for field names
- Include descriptions for all fields
- Validate schemas before committing

## Community Standards

### Code of Conduct

This project follows a standard Code of Conduct. All contributors must:

- Be respectful and inclusive
- Welcome diverse perspectives
- Focus on what is best for the protocol and community
- Show empathy towards other community members
- Avoid personal attacks or inflammatory language

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for full details.

### Avoiding Vendor Capture

OpenSignals Protocol is intended to be a neutral standard. To maintain neutrality:

- **Do not** promote specific vendors, platforms or products in specifications
- **Do not** design features that only work with specific vendors
- **Do** consider multi-vendor scenarios in examples
- **Do** keep integrations generic and extensible

### Source Citation Requirements

When referencing existing standards or protocols:

1. **Cite official sources**: Link to official documentation, not blog posts or secondary sources
2. **Quote accurately**: Do not misrepresent what other protocols do
3. **Update SOURCES.md**: Add new sources to the sources table
4. **Avoid overreach**: Do not claim compatibility without evidence

If you are unsure whether a compatibility claim is accurate, phrase it cautiously:

- ✅ "OpenSignals could complement AdCP by providing trust metadata"
- ❌ "OpenSignals integrates seamlessly with AdCP"

- ✅ "This example shows how OpenSignals concepts map to AAMP's trust goals"
- ❌ "OpenSignals is AAMP-compliant"

### What Not to Contribute

Please do not submit:

- Vendor-specific marketing materials
- Proprietary or confidential information
- Real customer data or personally identifiable information
- Changes that duplicate functionality already covered by AdCP, AAMP or other standards
- Defensive or comparative language about other protocols
- Personal disputes or grievances

## Governance and Decision Making

As an early-stage protocol:

- **Maintainers** review and merge pull requests
- **Major changes** require discussion in GitHub Issues before pull requests
- **Breaking changes** require community consensus and will trigger a version increment
- **Disputes** are resolved through discussion and maintainer decision

As the protocol matures, more formal governance may be established.

## Versioning

OpenSignals Protocol uses semantic versioning:

- **Major version** (1.0): Breaking changes to core protocol tasks or schemas
- **Minor version** (0.1, 0.2): Backwards-compatible additions (new signal types, new optional fields)
- **Patch version** (0.1.1): Clarifications and bug fixes

Current version: **0.1** (Draft RFC)

## Testing Requirements

All pull requests should include appropriate tests:

- **Schema changes**: Add validation tests in `tests/test_manifest_validation.py`
- **Protocol changes**: Update reference implementation and add integration tests
- **Examples**: Ensure examples validate against current schemas

Run tests before submitting:

```bash
cd reference-implementation/python
python -m pytest ../../tests/
```

## Getting Help

If you need help contributing:

- Open a discussion issue with the `question` label
- Review existing issues and pull requests for examples
- Check the [specification](specs/opensignals-v0.1.md) for technical details
- Review [example manifests](examples/) for practical guidance

## Recognition

Contributors will be recognized in release notes and documentation. Significant contributions may be acknowledged in the specification itself.

## License

By contributing to OpenSignals Protocol, you agree that your contributions will be licensed under:

- **Code**: Apache License 2.0
- **Documentation**: Creative Commons Attribution 4.0 International (CC BY 4.0)

See [LICENSE](LICENSE) for details.

## Questions?

Open an issue with the `question` label or start a discussion in GitHub Discussions.

Thank you for helping make OpenSignals Protocol a credible, practical standard for signal trust in agentic advertising.
