# OpenSignals Protocol - Quick Start

## For Publishers & SSPs

### 1. Embed OpenSignals in 5 Minutes

**Option A: JavaScript Widget (Recommended)**

Add this to your ad server:

```html
<!-- Add to <head> -->
<script src="https://cdn.opensignals.org/v0.1/opensignals.min.js"></script>

<!-- Initialize -->
<script>
OpenSignals.init({
  endpoint: 'https://verify.opensignals.org/v1',
  autoVerify: true,
  cacheResults: true,
  cacheTTL: 3600 // 1 hour
});
</script>

<!-- Verify signals before bidding -->
<script>
async function checkSignalBeforeBid(signalId, campaign) {
  const result = await OpenSignals.verify({
    signal_id: signalId,
    brand: campaign.brand,
    market: campaign.market,
    category: campaign.category
  });

  if (result.decision === 'approved' || result.decision === 'approved_with_conditions') {
    // Proceed with bid
    return { allow: true, trust_score: result.trust_score };
  } else {
    // Block signal
    return { allow: false, reason: result.reasoning };
  }
}
</script>
```

**Option B: Server-Side API (Python)**

```python
import requests

def verify_signal(signal_id, brand, market, category):
    response = requests.post(
        'https://verify.opensignals.org/v1/verify',
        json={
            'signal_id': signal_id,
            'brand': brand,
            'market': market,
            'category': category
        },
        headers={'Authorization': 'Bearer YOUR_API_KEY'}
    )
    return response.json()

# Before activating signal
result = verify_signal('outdoor-enthusiasts', 'premium-brand', 'GB', 'alcohol')
if result['decision'] in ['approved', 'approved_with_conditions']:
    activate_signal(signal_id, campaign_id)
```

**Option C: Self-Hosted**

```bash
# Clone and run
git clone https://github.com/Samrajtheailyceum/opensignals-protocol
cd opensignals-protocol/reference-implementation/python
pip install -r requirements.txt
python server.py

# Now available at http://localhost:8000
```

### 2. SSP Integration

**Pre-Bid Verification**

```python
# In your bid request handler
def handle_bid_request(bid_request):
    signals_used = bid_request.get('signals', [])

    # Verify all signals
    verification_results = []
    for signal in signals_used:
        result = verify_signal(
            signal['id'],
            bid_request['buyer']['brand'],
            bid_request['geo']['market'],
            bid_request['category']
        )
        verification_results.append(result)

    # Add trust scores to bid request
    bid_request['ext']['opensignals'] = {
        'signals_verified': True,
        'trust_scores': [r['trust_score'] for r in verification_results],
        'all_approved': all(r['decision'] != 'blocked' for r in verification_results)
    }

    return bid_request
```

**Post-Bid Audit**

```python
# After impression served
def log_impression(impression):
    requests.post(
        'https://verify.opensignals.org/v1/audit',
        json={
            'signal_id': impression['signal_id'],
            'campaign_id': impression['campaign_id'],
            'agent_id': impression['buyer_id'],
            'activation_id': impression['impression_id'],
            'timestamp': impression['timestamp'],
            'trust_score_at_use': impression['trust_score']
        }
    )
```

### 3. For Publishers

**Signal Manifest Publishing**

Create a manifest for your audience signals:

```json
{
  "protocol": "opensignals",
  "version": "0.1",
  "signal_id": "your-premium-audience",
  "name": "Your Premium Audience",
  "signal_type": "audience",
  "status": "active",
  "owner": {
    "organization": "Your Publisher",
    "contact": "data@yoursite.com"
  },
  "provenance": {
    "data_sources": ["first_party_authenticated"],
    "collection_method": "explicit_opt_in",
    "last_updated": "2026-05-11T08:00:00Z"
  },
  "permissioning": {
    "consent_scope": "advertising_personalization",
    "valid_use_cases": ["audience_targeting"],
    "geographic_restrictions": []
  },
  "quality": {
    "overall_trust_score": 0.85,
    "coverage_score": 0.82,
    "freshness_score": 0.91,
    "precision_score": 0.85
  }
}
```

**Publish at**:
```
https://yoursite.com/.well-known/opensignals/your-premium-audience
```

### 4. Performance

**Latency**: < 50ms with caching
**Caching**: Recommended TTL 1-6 hours
**Rate Limiting**: 10,000 requests/minute per API key

### 5. Testing

**Validate your manifest**:
```bash
curl -X POST https://verify.opensignals.org/v1/validate-manifest \
  -H "Content-Type: application/json" \
  -d @your-manifest.json
```

**Test verification**:
```bash
curl -X POST https://verify.opensignals.org/v1/verify \
  -H "Content-Type: application/json" \
  -d '{
    "signal_id": "your-premium-audience",
    "brand": "test-brand",
    "market": "US",
    "category": "general"
  }'
```

---

## Need Help?

- **API Docs**: [https://docs.opensignals.org](reference-implementation/python/README.md)
- **Examples**: [examples/](examples/)
- **Issues**: [GitHub Issues](https://github.com/Samrajtheailyceum/opensignals-protocol/issues)
