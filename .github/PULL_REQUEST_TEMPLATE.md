## Description

Provide a clear and concise description of your changes.

### What does this PR do?

Summarize the changes in this pull request.

### Why is this change needed?

Explain the motivation or problem this PR addresses.

## Type of Change

What type of change does this PR introduce?

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Schema change
- [ ] Example addition or improvement
- [ ] Integration guide
- [ ] Reference implementation improvement
- [ ] Test improvement
- [ ] Configuration change
- [ ] Other (please describe): _____________

## Related Issues

Link any related issues:

- Fixes #issue_number
- Relates to #issue_number
- Part of #issue_number

## Changes Made

Provide a detailed list of changes:

- Change 1
- Change 2
- Change 3

### Files Changed

List the key files modified:

- `path/to/file1`: Description of changes
- `path/to/file2`: Description of changes

## Affected Components

Which components are affected by this PR?

- [ ] Protocol specification (specs/)
- [ ] JSON schemas (schemas/)
- [ ] Reference implementation (reference-implementation/)
- [ ] Examples (examples/)
- [ ] Integration documentation (integrations/)
- [ ] Core documentation (docs/)
- [ ] GitHub Actions / CI
- [ ] Tests
- [ ] Other: _____________

## Breaking Changes

Does this PR introduce breaking changes?

- [ ] Yes (describe below)
- [ ] No

If yes, describe the breaking changes and migration path:

### Breaking Change Details

What will break?

### Migration Guide

How should users migrate to the new version?

### Deprecation Notice

What is being deprecated?

## Schema Changes

If this PR changes JSON schemas:

- [ ] Schema validation tests updated
- [ ] Examples updated to match new schema
- [ ] Schema version incremented (if needed)
- [ ] Documentation updated

### Schema Change Details

Describe schema changes:

```json
{
  "old_schema": "...",
  "new_schema": "..."
}
```

## Testing

How have you tested these changes?

### Test Environment

- OS: _____________
- Python Version: _____________
- Other relevant environment details: _____________

### Manual Testing

Describe manual testing performed:

1. Test scenario 1
2. Test scenario 2
3. ...

### Automated Tests

- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Schema validation tests pass
- [ ] Integration tests pass (if applicable)

### Test Commands Run

```bash
# Commands used for testing
python -m pytest tests/
python validate.py
```

### Test Results

Paste relevant test results:

```
Test results here
```

## Documentation

How is this change documented?

- [ ] Code comments added/updated
- [ ] README updated
- [ ] Specification updated (specs/)
- [ ] Examples added/updated
- [ ] Integration guide updated
- [ ] API documentation updated
- [ ] Changelog updated
- [ ] No documentation needed

### Documentation Changes

List documentation changes:

- Updated: path/to/doc.md
- Added: path/to/new-doc.md

## Examples

If applicable, provide examples demonstrating the changes:

### Before

```json
{
  "before_example": "here"
}
```

### After

```json
{
  "after_example": "here"
}
```

## Backward Compatibility

How does this affect backward compatibility?

- [ ] Fully backward compatible
- [ ] Backward compatible with deprecation warnings
- [ ] Breaking change (requires major version bump)
- [ ] Not applicable

### Compatibility Notes

Explain compatibility considerations:

## Performance Impact

Does this change affect performance?

- [ ] No performance impact
- [ ] Improves performance
- [ ] May decrease performance (explain why acceptable)
- [ ] Performance impact unknown/not measured

### Performance Details

If applicable, provide performance metrics:

## Security Considerations

Are there any security implications?

- [ ] No security impact
- [ ] Improves security
- [ ] Potential security implications (described below)
- [ ] Security review needed

### Security Details

Describe security considerations:

## Deployment Notes

Special deployment considerations:

- [ ] No special deployment needed
- [ ] Requires configuration changes
- [ ] Requires data migration
- [ ] Requires infrastructure changes
- [ ] Other: _____________

### Deployment Steps

If special deployment is needed:

1. Step 1
2. Step 2
3. ...

## Rollback Plan

If this needs to be rolled back:

1. Rollback step 1
2. Rollback step 2
3. ...

## Screenshots / Diagrams

If applicable, add screenshots or diagrams:

## Additional Context

Add any other context about the pull request here.

## Pre-Submission Checklist

Before submitting, ensure you have:

### Code Quality
- [ ] Code follows project style guidelines
- [ ] Self-reviewed my own code
- [ ] Commented complex or hard-to-understand areas
- [ ] No unnecessary console logs or debug code
- [ ] No TODOs or FIXMEs (or they are documented)

### Testing
- [ ] All existing tests pass
- [ ] Added tests for new functionality
- [ ] Manual testing completed
- [ ] Edge cases considered and tested

### Documentation
- [ ] Updated relevant documentation
- [ ] Added code comments where needed
- [ ] Updated CHANGELOG.md
- [ ] Updated README if needed
- [ ] Added examples if needed

### Schema & Validation
- [ ] JSON schemas are valid
- [ ] Examples validate against schemas
- [ ] Schema tests pass
- [ ] No breaking schema changes (or properly versioned)

### Git
- [ ] Commits are atomic and well-described
- [ ] Branch is up to date with base branch
- [ ] No merge conflicts
- [ ] Commit messages follow project conventions

### Legal / Licensing
- [ ] No proprietary or copyrighted code included
- [ ] All dependencies are compatible with Apache 2.0 license
- [ ] Attribution added for external code/resources

## Reviewer Notes

Any specific areas you'd like reviewers to focus on?

## Post-Merge Actions

After merge, what actions are needed?

- [ ] Update external documentation
- [ ] Announce changes
- [ ] Update related projects
- [ ] Deploy to production
- [ ] Other: _____________

---

**Contributor Checklist:**
- [ ] I have read and followed the [Contributing Guidelines](../CONTRIBUTING.md)
- [ ] I have read and agree to follow the [Code of Conduct](../CODE_OF_CONDUCT.md)
- [ ] I understand this project uses Apache 2.0 license
- [ ] I have the right to contribute this code
- [ ] I agree to license my contributions under Apache 2.0

---

Thank you for contributing to OpenSignals Protocol!
