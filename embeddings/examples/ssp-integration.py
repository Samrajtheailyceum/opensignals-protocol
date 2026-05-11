"""
OpenSignals SSP Integration Example

Complete workflow for Supply-Side Platform integration
"""

import sys
sys.path.append('..')
from python.opensignals_client import OpenSignalsClient


class SSPIntegration:
    """Example SSP with OpenSignals trust verification"""

    def __init__(self):
        self.opensignals = OpenSignalsClient(
            endpoint='https://verify.opensignals.org/v1',
            cache_enabled=True,
            cache_ttl=3600
        )

    def handle_bid_request(self, bid_request):
        """
        Handle incoming bid request with signal verification

        Args:
            bid_request: OpenRTB bid request

        Returns:
            Enhanced bid request with trust data
        """
        signals = bid_request.get('user', {}).get('data', [])
        brand = bid_request.get('site', {}).get('publisher', {}).get('name', 'unknown')
        geo = bid_request.get('device', {}).get('geo', {})
        market = geo.get('country', 'US')

        # Determine category (simplified)
        category = self._determine_category(bid_request)

        # Verify all signals
        verification_results = []
        approved_signals = []

        for signal in signals:
            signal_id = signal.get('id')
            if not signal_id:
                continue

            result = self.opensignals.verify(
                signal_id=signal_id,
                brand=brand,
                market=market,
                category=category
            )

            verification_results.append({
                'signal_id': signal_id,
                'decision': result.decision,
                'trust_score': result.trust_score,
                'cached': result.cached
            })

            # Only include approved signals
            if result.decision in ['approved', 'approved_with_conditions']:
                approved_signals.append(signal)

        # Update bid request with verified signals only
        if bid_request.get('user') and 'data' in bid_request['user']:
            bid_request['user']['data'] = approved_signals

        # Add OpenSignals extension
        if 'ext' not in bid_request:
            bid_request['ext'] = {}

        bid_request['ext']['opensignals'] = {
            'verified': True,
            'signals_checked': len(signals),
            'signals_approved': len(approved_signals),
            'trust_scores': [r['trust_score'] for r in verification_results],
            'avg_trust_score': sum(r['trust_score'] for r in verification_results) / len(verification_results) if verification_results else 0.0
        }

        return bid_request

    def log_impression(self, impression_data):
        """
        Log impression for audit trail

        Args:
            impression_data: Impression event data
        """
        signal_id = impression_data.get('signal_id')
        if not signal_id:
            return

        try:
            self.opensignals.audit(
                signal_id=signal_id,
                campaign_id=impression_data.get('campaign_id'),
                agent_id=impression_data.get('buyer_id', 'unknown'),
                activation_id=impression_data.get('impression_id'),
                trust_score_at_use=impression_data.get('trust_score', 0.0),
                placement_id=impression_data.get('placement_id'),
                creative_id=impression_data.get('creative_id')
            )
        except Exception as e:
            print(f"Audit logging failed: {e}")

    def _determine_category(self, bid_request):
        """Determine campaign category from bid request"""
        # Simplified category detection
        site = bid_request.get('site', {})
        cat = site.get('cat', [])

        if any('IAB9' in c for c in cat):  # Alcohol/tobacco
            return 'alcohol'
        elif any('IAB7-39' in c for c in cat):  # Gambling
            return 'gambling'
        elif any('IAB7-34' in c for c in cat):  # Pharma
            return 'pharmaceutical'
        else:
            return 'general'


# Example usage
if __name__ == '__main__':
    ssp = SSPIntegration()

    # Example bid request
    bid_request = {
        'id': 'bid-123',
        'site': {
            'publisher': {'name': 'premium-publisher'},
            'cat': ['IAB1']
        },
        'device': {
            'geo': {'country': 'GB'}
        },
        'user': {
            'data': [
                {'id': 'outdoor-recreation-enthusiasts', 'name': 'Outdoor Enthusiasts'},
                {'id': 'premium-auto-intenders', 'name': 'Auto Buyers'}
            ]
        }
    }

    # Process bid request
    enhanced_request = ssp.handle_bid_request(bid_request)

    print("Original signals:", len(bid_request['user']['data']))
    print("Approved signals:", len(enhanced_request['user']['data']))
    print("Trust data:", enhanced_request['ext']['opensignals'])

    # After impression
    ssp.log_impression({
        'signal_id': 'outdoor-recreation-enthusiasts',
        'campaign_id': 'camp-456',
        'buyer_id': 'buyer-789',
        'impression_id': 'imp-123',
        'trust_score': 0.87,
        'placement_id': 'placement-001',
        'creative_id': 'creative-500'
    })
