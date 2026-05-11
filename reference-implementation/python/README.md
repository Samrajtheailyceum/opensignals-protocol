# OpenSignals Protocol - Python FastAPI Reference Implementation

A production-quality reference implementation of the OpenSignals Protocol using FastAPI. This implementation demonstrates the core protocol operations with realistic but simplified business logic suitable for learning and adaptation.

## Overview

This reference implementation provides a working REST API server that implements the following OpenSignals Protocol operations:

- **Manifest Validation** - Validate signal manifests against the schema
- **Signal Verification** - Verify signal compliance with policies and regulations
- **Trust Scoring** - Calculate trust scores based on quality metrics
- **Audit Logging** - Create comprehensive audit trails for signal usage

## Features

- Full OpenSignals Protocol v0.1 schema compliance
- JSON Schema validation using Draft 2020-12
- Production-quality FastAPI server with OpenAPI documentation
- Comprehensive request/response validation with Pydantic
- Structured logging for audit and debugging
- In-memory data storage (easily replaceable with database)
- Realistic but simplified business logic
- Health check endpoint for monitoring
- Interactive API documentation at `/docs`

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

## Installation

1. **Navigate to the Python implementation directory:**

```bash
cd reference-implementation/python/
```

2. **Create a virtual environment (recommended):**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

## Running the Server

Start the FastAPI development server:

```bash
python server.py
```

Or use uvicorn directly:

```bash
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

The server will start on `http://localhost:8000`

## API Endpoints

### Health Check

```bash
GET /health
```

Returns the health status of the API service.

**Example:**
```bash
curl http://localhost:8000/health
```

### Validate Manifest

```bash
POST /validate-manifest
```

Validates a signal manifest against the OpenSignals schema.

**Example:**
```bash
curl -X POST http://localhost:8000/validate-manifest \
  -H "Content-Type: application/json" \
  -d @sample_request.json
```

Or using the example from the sample file:
```bash
curl -X POST http://localhost:8000/validate-manifest \
  -H "Content-Type: application/json" \
  -d "$(jq '.validate_manifest_example' sample_request.json)"
```

### Verify Signal

```bash
POST /verify-signal
```

Verifies signal compliance against policies, regulations, and usage restrictions.

**Example:**
```bash
curl -X POST http://localhost:8000/verify-signal \
  -H "Content-Type: application/json" \
  -d "$(jq '.verify_signal_example' sample_request.json)"
```

### Score Signal

```bash
POST /score-signal
```

Calculates trust scores based on signal quality metrics.

**Example:**
```bash
curl -X POST http://localhost:8000/score-signal \
  -H "Content-Type: application/json" \
  -d "$(jq '.score_signal_example' sample_request.json)"
```

### Audit Signal Usage

```bash
POST /audit-signal-usage
```

Logs signal usage events for audit and compliance purposes.

**Example:**
```bash
curl -X POST http://localhost:8000/audit-signal-usage \
  -H "Content-Type: application/json" \
  -d "$(jq '.audit_usage_example' sample_request.json)"
```

### List Signals (Convenience Endpoint)

```bash
GET /signals
```

Lists all registered signals in the system.

**Example:**
```bash
curl http://localhost:8000/signals
```

### List Audit Logs (Convenience Endpoint)

```bash
GET /audit-logs?limit=100&event_type=signal_usage
```

Retrieves audit logs, optionally filtered by event type.

**Example:**
```bash
curl "http://localhost:8000/audit-logs?limit=10"
```

## Interactive API Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

These interfaces allow you to explore the API, view schemas, and test endpoints directly from your browser.

## Project Structure

```
reference-implementation/python/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── server.py                 # FastAPI server implementation
├── validator.py              # Schema validation helpers
└── sample_request.json       # Example requests for all endpoints
```

## Architecture

### server.py

The main FastAPI application with all endpoint implementations:

- **Request/Response Models**: Pydantic models for type safety and validation
- **Endpoint Handlers**: Business logic for each protocol operation
- **In-Memory Storage**: Simple dictionaries for demo (replace with database in production)
- **Error Handling**: HTTP exceptions with appropriate status codes
- **Logging**: Structured logging for debugging and audit

### validator.py

Schema validation utilities:

- **OpenSignalsValidator**: Main validator class for all schema types
- **Schema Loading**: Automatic loading of JSON schemas from the schemas directory
- **Validation Methods**: Dedicated methods for each document type
- **Helper Functions**: Trust score calculation, compliance checking, etc.

### sample_request.json

Example requests for all endpoints:

- `validate_manifest_example` - Example manifest validation request
- `verify_signal_example` - Example signal verification request
- `score_signal_example` - Example trust scoring request
- `audit_usage_example` - Example audit logging request

## Testing the Implementation

### 1. Start the Server

```bash
python server.py
```

### 2. Validate a Manifest

```bash
curl -X POST http://localhost:8000/validate-manifest \
  -H "Content-Type: application/json" \
  -d "$(jq '.validate_manifest_example' sample_request.json)" | jq
```

Expected response:
```json
{
  "valid": true,
  "errors": null,
  "warnings": null,
  "signal_id": "test-signal-123"
}
```

### 3. Verify the Signal

```bash
curl -X POST http://localhost:8000/verify-signal \
  -H "Content-Type: application/json" \
  -d "$(jq '.verify_signal_example' sample_request.json)" | jq
```

### 4. Score the Signal

```bash
curl -X POST http://localhost:8000/score-signal \
  -H "Content-Type: application/json" \
  -d "$(jq '.score_signal_example' sample_request.json)" | jq
```

Expected response:
```json
{
  "signal_id": "verified-attention-quality",
  "overall_trust_score": 0.931,
  "dimension_scores": {
    "coverage": 0.89,
    "freshness": 0.98,
    "precision": 0.93,
    "stability": 0.91,
    "explainability": 0.95
  },
  "timestamp": "2026-05-11T12:00:00Z",
  "assessment": "excellent"
}
```

### 5. Log an Audit Event

```bash
curl -X POST http://localhost:8000/audit-signal-usage \
  -H "Content-Type: application/json" \
  -d "$(jq '.audit_usage_example' sample_request.json)" | jq
```

### 6. View Registered Signals

```bash
curl http://localhost:8000/signals | jq
```

## Configuration

### Environment Variables

You can configure the server using environment variables:

```bash
# Server configuration
export HOST="0.0.0.0"
export PORT="8000"

# Schema directory (optional)
export SCHEMA_DIR="/path/to/schemas/v0.1"

# Logging level
export LOG_LEVEL="INFO"
```

### Production Deployment

For production deployment, consider:

1. **Database Integration**: Replace in-memory storage with PostgreSQL, MongoDB, or similar
2. **Authentication**: Add OAuth2 or API key authentication
3. **Rate Limiting**: Implement rate limiting to prevent abuse
4. **Monitoring**: Add Prometheus metrics and health checks
5. **HTTPS**: Deploy behind a reverse proxy (nginx, Caddy) with TLS
6. **Horizontal Scaling**: Use Kubernetes or similar for scaling
7. **Caching**: Add Redis for caching frequently accessed signals
8. **Message Queue**: Add RabbitMQ or Kafka for asynchronous processing

Example production command:
```bash
gunicorn server:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --access-logfile - \
  --error-logfile -
```

## Extending the Implementation

### Adding Custom Validation Rules

Edit `validator.py` and add custom validation functions:

```python
def validate_custom_rule(manifest: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    # Your custom validation logic
    if manifest.get("signal_type") == "custom":
        # Custom checks
        pass
    return True, None
```

### Adding New Endpoints

Add new endpoints to `server.py`:

```python
@app.post("/custom-operation", tags=["Custom"])
async def custom_operation(request: CustomRequest):
    # Your custom logic
    return CustomResponse(...)
```

### Database Integration Example

Replace in-memory storage with a database:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "postgresql://user:password@localhost/opensignals"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Use in endpoints
@app.post("/validate-manifest")
async def validate_manifest(request: ValidateManifestRequest, db: Session = Depends(get_db)):
    # Store in database
    db_signal = SignalManifest(**request.manifest)
    db.add(db_signal)
    db.commit()
    return response
```

## Troubleshooting

### Schema Not Found Error

If you see "Schema type not found" errors, ensure the schemas directory is correctly located:

```bash
# Check schema directory
ls -la ../../schemas/v0.1/

# Set custom schema directory
export SCHEMA_DIR="/absolute/path/to/schemas/v0.1"
```

### Import Errors

Ensure all dependencies are installed:

```bash
pip install -r requirements.txt --upgrade
```

### Port Already in Use

If port 8000 is already in use, specify a different port:

```bash
uvicorn server:app --port 8001
```

## Performance Considerations

This reference implementation uses simple in-memory storage and synchronous validation. For production:

- **Async Database Operations**: Use async database drivers (asyncpg, motor)
- **Caching**: Cache validated schemas and manifests
- **Background Tasks**: Use FastAPI BackgroundTasks for audit logging
- **Connection Pooling**: Configure database connection pools
- **Request Timeouts**: Set appropriate timeout values

## Security Considerations

Before deploying to production:

1. Add authentication and authorization
2. Implement rate limiting
3. Validate and sanitize all inputs
4. Use HTTPS/TLS for all communications
5. Implement CORS policies appropriately
6. Add request signing for audit integrity
7. Encrypt sensitive data at rest
8. Implement proper logging and monitoring

## Contributing

This is a reference implementation. To contribute improvements:

1. Maintain compatibility with OpenSignals Protocol specification
2. Keep logic simple and well-documented
3. Add tests for new functionality
4. Update this README with any changes

## License

See the main repository LICENSE file for license information.

## Support

For questions about the OpenSignals Protocol:
- Protocol Specification: See `/specs/opensignals-v0.1.md`
- Schema Definitions: See `/schemas/v0.1/`
- Examples: See `/examples/`

For issues with this implementation:
- Check the logs for detailed error messages
- Verify schema files are present and valid
- Ensure all dependencies are correctly installed
- Review the interactive API docs at `/docs`

## References

- [OpenSignals Protocol Specification](../../specs/opensignals-v0.1.md)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [JSON Schema Specification](https://json-schema.org/)
