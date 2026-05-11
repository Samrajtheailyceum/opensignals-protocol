"""
OpenSignals Protocol - Python Client Library
Version: 0.1.0

Easy integration for publishers, SSPs, and platforms.
"""

import requests
import time
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class VerificationResult:
    """Result of signal verification"""
    decision: str  # approved, approved_with_conditions, blocked
    trust_score: float
    conditions: List[str]
    policy_bindings: List[str]
    reasoning: str
    cached: bool = False
    timestamp: str = None


class OpenSignalsClient:
    """
    OpenSignals Protocol Client

    Usage:
        client = OpenSignalsClient(endpoint='https://verify.opensignals.org/v1')
        result = client.verify('signal-id', 'brand', 'GB', 'alcohol')

        if result.decision in ['approved', 'approved_with_conditions']:
            # Proceed with signal activation
            pass
    """

    def __init__(
        self,
        endpoint: str = 'https://verify.opensignals.org/v1',
        api_key: Optional[str] = None,
        cache_enabled: bool = True,
        cache_ttl: int = 3600,
        timeout: int = 5
    ):
        """
        Initialize OpenSignals client

        Args:
            endpoint: API endpoint URL
            api_key: Optional API key for authentication
            cache_enabled: Enable result caching
            cache_ttl: Cache TTL in seconds
            timeout: Request timeout in seconds
        """
        self.endpoint = endpoint.rstrip('/')
        self.api_key = api_key
        self.cache_enabled = cache_enabled
        self.cache_ttl = cache_ttl
        self.timeout = timeout
        self._cache: Dict[str, tuple[Any, datetime]] = {}

    def verify(
        self,
        signal_id: str,
        brand: str,
        market: str,
        category: str,
        intended_use: str = 'targeting'
    ) -> VerificationResult:
        """
        Verify a signal against brand policy

        Args:
            signal_id: Signal identifier
            brand: Brand identifier
            market: Market code (e.g., 'GB', 'US')
            category: Campaign category (e.g., 'alcohol', 'general')
            intended_use: Intended use case

        Returns:
            VerificationResult object
        """
        # Check cache
        if self.cache_enabled:
            cached = self._get_from_cache(signal_id, brand, market, category)
            if cached:
                return VerificationResult(**cached, cached=True)

        # Make API request
        data = {
            'signal_id': signal_id,
            'brand': brand,
            'market': market,
            'category': category,
            'intended_use': intended_use
        }

        try:
            response = self._request('POST', '/verify', json=data)

            result = VerificationResult(
                decision=response.get('decision', 'error'),
                trust_score=response.get('trust_score', 0.0),
                conditions=response.get('conditions', []),
                policy_bindings=response.get('policy_bindings', []),
                reasoning=response.get('reasoning', ''),
                timestamp=response.get('timestamp')
            )

            # Cache result
            if self.cache_enabled:
                self._add_to_cache(signal_id, brand, market, category, response)

            return result

        except Exception as e:
            return VerificationResult(
                decision='error',
                trust_score=0.0,
                conditions=[],
                policy_bindings=[],
                reasoning=f'Error: {str(e)}'
            )

    def verify_batch(self, signals: List[Dict[str, str]]) -> List[VerificationResult]:
        """
        Verify multiple signals in batch

        Args:
            signals: List of signal parameters (dicts with signal_id, brand, market, category)

        Returns:
            List of VerificationResult objects
        """
        results = []
        for signal in signals:
            result = self.verify(
                signal['signal_id'],
                signal['brand'],
                signal['market'],
                signal['category'],
                signal.get('intended_use', 'targeting')
            )
            results.append(result)
        return results

    def get_manifest(self, signal_id: str) -> Dict[str, Any]:
        """
        Retrieve signal manifest

        Args:
            signal_id: Signal identifier

        Returns:
            Signal manifest dictionary
        """
        return self._request('GET', f'/manifest/{signal_id}')

    def validate_manifest(self, manifest: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate a signal manifest

        Args:
            manifest: Signal manifest to validate

        Returns:
            Validation result
        """
        return self._request('POST', '/validate-manifest', json=manifest)

    def audit(
        self,
        signal_id: str,
        campaign_id: str,
        agent_id: str,
        activation_id: str,
        trust_score_at_use: float,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Log signal usage for audit trail

        Args:
            signal_id: Signal identifier
            campaign_id: Campaign identifier
            agent_id: Agent/buyer identifier
            activation_id: Activation identifier
            trust_score_at_use: Trust score at time of activation
            **kwargs: Additional audit data

        Returns:
            Audit result
        """
        data = {
            'signal_id': signal_id,
            'campaign_id': campaign_id,
            'agent_id': agent_id,
            'activation_id': activation_id,
            'trust_score_at_use': trust_score_at_use,
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            **kwargs
        }

        return self._request('POST', '/audit', json=data)

    def _request(
        self,
        method: str,
        path: str,
        json: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """Make API request"""
        url = f"{self.endpoint}{path}"
        headers = {'Content-Type': 'application/json'}

        if self.api_key:
            headers['Authorization'] = f'Bearer {self.api_key}'

        response = requests.request(
            method,
            url,
            json=json,
            headers=headers,
            timeout=self.timeout
        )

        response.raise_for_status()
        return response.json()

    def _get_from_cache(
        self,
        signal_id: str,
        brand: str,
        market: str,
        category: str
    ) -> Optional[Dict]:
        """Get result from cache"""
        key = f"{signal_id}:{brand}:{market}:{category}"
        if key in self._cache:
            data, timestamp = self._cache[key]
            if datetime.now() - timestamp < timedelta(seconds=self.cache_ttl):
                return data
            del self._cache[key]
        return None

    def _add_to_cache(
        self,
        signal_id: str,
        brand: str,
        market: str,
        category: str,
        data: Dict
    ):
        """Add result to cache"""
        key = f"{signal_id}:{brand}:{market}:{category}"
        self._cache[key] = (data, datetime.now())

        # Limit cache size
        if len(self._cache) > 1000:
            oldest_key = min(self._cache.keys(), key=lambda k: self._cache[k][1])
            del self._cache[oldest_key]

    def clear_cache(self):
        """Clear result cache"""
        self._cache.clear()


# Convenience function
def verify_signal(
    signal_id: str,
    brand: str,
    market: str,
    category: str,
    endpoint: str = 'https://verify.opensignals.org/v1',
    api_key: Optional[str] = None
) -> VerificationResult:
    """
    Quick verification without creating a client instance

    Usage:
        from opensignals_client import verify_signal

        result = verify_signal('signal-id', 'brand', 'GB', 'alcohol')
        if result.decision == 'approved':
            # Proceed
            pass
    """
    client = OpenSignalsClient(endpoint=endpoint, api_key=api_key)
    return client.verify(signal_id, brand, market, category)
