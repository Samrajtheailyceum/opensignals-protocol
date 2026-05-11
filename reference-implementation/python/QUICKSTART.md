# Quick Start Guide

Get the OpenSignals Protocol API running in 5 minutes!

## Prerequisites

- Python 3.9+
- pip (usually comes with Python)

## Option 1: Automatic Setup (Recommended)

```bash
# Run the quick start script
./run.sh
```

This will:
1. Create a virtual environment
2. Install all dependencies
3. Start the API server

## Option 2: Manual Setup

```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the server
python server.py
```

## Verify It's Working

### Option A: Use the browser

Open http://localhost:8000/docs in your browser

### Option B: Use curl

```bash
curl http://localhost:8000/health
```

### Option C: Run the test suite

```bash
# In another terminal, with venv activated
pip install requests  # Only needed for test script
python test_api.py
```

## Next Steps

1. Review the [full README](README.md) for detailed documentation
2. Try the example requests in `sample_request.json`
3. Explore the interactive API docs at http://localhost:8000/docs

## Quick Examples

### Validate a manifest

```bash
curl -X POST http://localhost:8000/validate-manifest \
  -H "Content-Type: application/json" \
  -d @sample_request.json
```

### Check registered signals

```bash
curl http://localhost:8000/signals
```

## Troubleshooting

**Port 8000 already in use?**
```bash
# Use a different port
uvicorn server:app --port 8001
```

**Import errors?**
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

**Schema not found?**
Ensure you're running from the Python directory and the schemas exist in `../../schemas/v0.1/`

## Getting Help

- Full documentation: See [README.md](README.md)
- API docs: http://localhost:8000/docs (when server is running)
- Protocol spec: See `../../specs/opensignals-v0.1.md`
