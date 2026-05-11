# OpenSignals Embeddings

Easy integration for publishers, SSPs, and platforms.

## JavaScript Client

**For client-side integration:**

```html
<script src="opensignals.js"></script>
<script>
OpenSignals.init({
  endpoint: 'https://verify.opensignals.org/v1',
  apiKey: 'your-api-key',
  cacheResults: true
});

// Verify before bid
const result = await OpenSignals.verify({
  signal_id: 'outdoor-enthusiasts',
  brand: 'premium-brand',
  market: 'GB',
  category: 'alcohol'
});

if (result.decision === 'approved') {
  // Proceed with signal activation
}
</script>
```

**Features:**
- In-memory caching (configurable TTL)
- Batch verification
- Timeout handling
- < 2KB minified

## Python Client

**For server-side integration:**

```python
from opensignals_client import OpenSignalsClient

client = OpenSignalsClient(
    endpoint='https://verify.opensignals.org/v1',
    api_key='your-api-key'
)

result = client.verify('signal-id', 'brand', 'GB', 'alcohol')

if result.decision in ['approved', 'approved_with_conditions']:
    activate_signal(signal_id, campaign_id)
    
    # Log for audit
    client.audit(
        signal_id=signal_id,
        campaign_id=campaign_id,
        agent_id='buyer-123',
        activation_id=activation_id,
        trust_score_at_use=result.trust_score
    )
```

**Features:**
- Result caching
- Batch verification
- Type hints
- Async support (optional)

## Installation

**JavaScript:**
```html
<script src="https://cdn.opensignals.org/v0.1/opensignals.min.js"></script>
```

**Python:**
```bash
pip install opensignals-client
```

Or copy `opensignals_client.py` to your project.

## SSP Integration Example

See [examples/ssp-integration.py](examples/ssp-integration.py) for complete SSP workflow.

## Publisher Integration Example

See [examples/publisher-manifest.json](examples/publisher-manifest.json) for manifest creation.

## Performance

- **Latency**: < 50ms (cached: < 1ms)
- **Rate limit**: 10,000 req/min
- **Availability**: 99.9% SLA

## Self-Hosting

Run your own verification server:

```bash
git clone https://github.com/Samrajtheailyceum/opensignals-protocol
cd opensignals-protocol/reference-implementation/python
pip install -r requirements.txt
python server.py
```

Then point clients to `http://localhost:8000`
