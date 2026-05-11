# OpenSignals Protocol - Testing Guide

## Quick Test

Verify the repository is working:

```bash
# 1. Test JSON validity
python3 -c "import json; [json.load(open(f)) for f in ['examples/alcohol-contextual-signal.json', 'schemas/v0.1/open-signal-manifest.schema.json']]; print('✅ JSON valid')"

# 2. Test schema validation (requires jsonschema)
python3 << 'EOF'
try:
    import jsonschema
    import json

    # Load schema
    with open('schemas/v0.1/open-signal-manifest.schema.json') as f:
        schema = json.load(f)

    # Validate example
    with open('examples/alcohol-contextual-signal.json') as f:
        manifest = json.load(f)

    jsonschema.validate(manifest, schema)
    print('✅ Schema validation passed')
except ImportError:
    print('⚠️  jsonschema not installed. Run: pip install jsonschema')
except Exception as e:
    print(f'❌ Validation error: {e}')
EOF

# 3. Test Python server (requires fastapi)
cd reference-implementation/python
python3 << 'EOF'
try:
    import sys
    sys.path.insert(0, '.')
    from server import app
    print('✅ Server imports successfully')
except ImportError as e:
    print(f'⚠️  Missing dependency: {e}')
    print('Run: pip install fastapi uvicorn pydantic jsonschema')
except Exception as e:
    print(f'❌ Server error: {e}')
EOF
cd ../..

# 4. Test embeddings
python3 << 'EOF'
import sys
sys.path.insert(0, 'embeddings/python')
try:
    from opensignals_client import OpenSignalsClient, verify_signal
    print('✅ Python client imports successfully')
except Exception as e:
    print(f'❌ Client error: {e}')
EOF

# 5. Test JavaScript (syntax check)
node -c embeddings/javascript/opensignals.js 2>/dev/null && echo "✅ JavaScript syntax valid" || echo "⚠️  Node.js not installed (JS not tested)"
```

## Component Tests

### 1. Schema Validation

Test all examples validate against schemas:

```python
import json
import jsonschema
from pathlib import Path

schema_path = Path('schemas/v0.1/open-signal-manifest.schema.json')
examples_path = Path('examples')

with open(schema_path) as f:
    schema = json.load(f)

for example_file in examples_path.glob('*.json'):
    with open(example_file) as f:
        manifest = json.load(f)

    try:
        jsonschema.validate(manifest, schema)
        print(f'✅ {example_file.name}')
    except jsonschema.ValidationError as e:
        print(f'❌ {example_file.name}: {e.message}')
```

### 2. API Server

Start the reference server:

```bash
cd reference-implementation/python
pip install -r requirements.txt
python server.py &
SERVER_PID=$!

# Test health endpoint
curl http://localhost:8000/health

# Test validation
curl -X POST http://localhost:8000/validate-manifest \
  -H "Content-Type: application/json" \
  -d @../../examples/alcohol-contextual-signal.json

# Test verification
curl -X POST http://localhost:8000/verify-signal \
  -H "Content-Type: application/json" \
  -d '{
    "signal_id": "outdoor-recreation-enthusiasts",
    "brand": "premium-spirits",
    "market": "GB",
    "category": "alcohol"
  }'

# Cleanup
kill $SERVER_PID
```

### 3. Client Libraries

**Python client:**

```python
from embeddings.python.opensignals_client import verify_signal

# Note: This will fail without a running server
# For testing, use mock or start server first
result = verify_signal(
    'outdoor-enthusiasts',
    'test-brand',
    'US',
    'general',
    endpoint='http://localhost:8000'
)
print(f"Decision: {result.decision}")
print(f"Trust score: {result.trust_score}")
```

**JavaScript client:**

```html
<!DOCTYPE html>
<html>
<head>
    <script src="embeddings/javascript/opensignals.js"></script>
</head>
<body>
    <script>
        OpenSignals.init({
            endpoint: 'http://localhost:8000',
            cacheResults: true
        });

        // Test verification
        OpenSignals.verify({
            signal_id: 'outdoor-enthusiasts',
            brand: 'test-brand',
            market: 'US',
            category: 'general'
        }).then(result => {
            console.log('Decision:', result.decision);
            console.log('Trust score:', result.trust_score);
        });
    </script>
</body>
</html>
```

### 4. MCP Server

Test MCP server:

```bash
cd mcp-server
pip install -r requirements.txt
python test_server.py
```

## Integration Tests

### SSP Integration

```bash
cd embeddings/examples
python ssp-integration.py
```

Expected output:
- Original signals: 2
- Approved signals: 1-2 (depends on verification)
- Trust data with average trust score

### Publisher Manifest

Validate publisher manifest:

```bash
curl -X POST http://localhost:8000/validate-manifest \
  -H "Content-Type: application/json" \
  -d @embeddings/examples/publisher-manifest.json
```

## Performance Tests

Test verification latency:

```python
import time
from embeddings.python.opensignals_client import OpenSignalsClient

client = OpenSignalsClient(endpoint='http://localhost:8000')

# Warm up cache
client.verify('test-signal', 'test-brand', 'US', 'general')

# Measure cached performance
start = time.time()
for _ in range(100):
    client.verify('test-signal', 'test-brand', 'US', 'general')
elapsed = (time.time() - start) / 100

print(f"Average latency (cached): {elapsed*1000:.2f}ms")

# Measure uncached performance
client.clear_cache()
start = time.time()
result = client.verify('test-signal', 'test-brand', 'US', 'general')
elapsed = time.time() - start

print(f"Latency (uncached): {elapsed*1000:.2f}ms")
```

## Continuous Integration

Add to `.github/workflows/test.yml`:

```yaml
name: Test OpenSignals

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          pip install jsonschema fastapi uvicorn pydantic pytest requests

      - name: Validate JSON
        run: python3 -m json.tool examples/*.json schemas/v0.1/*.json

      - name: Validate schemas
        run: python3 -c "import json, jsonschema; jsonschema.validate(json.load(open('examples/alcohol-contextual-signal.json')), json.load(open('schemas/v0.1/open-signal-manifest.schema.json')))"

      - name: Test server imports
        run: cd reference-implementation/python && python3 -c "from server import app"

      - name: Test client imports
        run: cd embeddings/python && python3 -c "from opensignals_client import OpenSignalsClient"
```

## Known Issues

### Missing Dependencies

If tests fail with import errors:

```bash
# Install all dependencies
pip install fastapi uvicorn pydantic jsonschema pytest requests
```

### Port Already in Use

If server fails to start:

```bash
# Find and kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

### Schema Validation Errors

If examples don't validate:
1. Check schema file exists
2. Check example JSON is valid
3. Compare required fields
4. Check enums match

## Success Criteria

All tests should pass:
- ✅ All JSON files parse correctly
- ✅ All examples validate against schemas
- ✅ Server starts without errors
- ✅ API endpoints return valid responses
- ✅ Client libraries work
- ✅ Integration examples run

If any test fails, check:
1. Dependencies installed
2. Python version >= 3.7
3. File paths correct
4. Server running (for API tests)
