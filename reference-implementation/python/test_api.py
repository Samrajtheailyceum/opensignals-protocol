#!/usr/bin/env python3
"""
Quick test script to verify the OpenSignals Protocol API is working correctly.

This script tests the basic functionality of all endpoints without requiring
external tools like curl or httpie.

Usage:
    python test_api.py

Note: The server must be running on http://localhost:8000
"""

import json
import sys
from datetime import datetime
from uuid import uuid4

try:
    import requests
except ImportError:
    print("Error: requests library not found.")
    print("Install it with: pip install requests")
    sys.exit(1)


BASE_URL = "http://localhost:8000"


def print_section(title):
    """Print a section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def test_health():
    """Test the health endpoint."""
    print_section("Testing Health Check")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


def test_validate_manifest():
    """Test manifest validation."""
    print_section("Testing Manifest Validation")

    manifest = {
        "protocol": "opensignals",
        "version": "0.1",
        "signal_id": "test-signal-demo",
        "name": "Test Signal Demo",
        "description": "A test signal for API demonstration purposes in the reference implementation.",
        "signal_type": "contextual",
        "status": "active",
        "owner": {
            "organization": "Test Organization",
            "contact_email": "test@example.com"
        },
        "provider": {
            "name": "Test Provider",
            "provider_id": "test-provider-demo"
        },
        "compatible_protocols": ["rtb_3.0"],
        "provenance": {
            "data_sources": [{
                "type": "first_party",
                "description": "Test data source"
            }],
            "collection_method": "deterministic",
            "update_frequency": "daily"
        },
        "permissioning": {
            "requires_consent": False,
            "privacy_compliance": ["gdpr"],
            "usage_restrictions": {
                "allowed_uses": ["targeting", "measurement"]
            }
        },
        "quality": {
            "coverage_score": 0.85,
            "freshness_score": 0.90,
            "precision_score": 0.88,
            "stability_score": 0.87,
            "explainability_score": 0.92,
            "overall_trust_score": 0.88
        },
        "freshness": {
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "next_update": "2026-05-12T00:00:00Z"
        },
        "audit": {
            "audit_log_required": True,
            "retention_period_days": 90
        }
    }

    response = requests.post(
        f"{BASE_URL}/validate-manifest",
        json={"manifest": manifest}
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


def test_score_signal():
    """Test trust scoring."""
    print_section("Testing Trust Scoring")

    request_data = {
        "signal_id": "test-signal-demo",
        "manifest": {
            "protocol": "opensignals",
            "version": "0.1",
            "signal_id": "test-signal-demo",
            "name": "Test Signal",
            "description": "Test signal for scoring demonstration",
            "signal_type": "attention",
            "status": "active",
            "owner": {
                "organization": "Test Org",
                "contact_email": "test@example.com"
            },
            "provider": {
                "name": "Test Provider",
                "provider_id": "test-001"
            },
            "compatible_protocols": ["rtb_3.0"],
            "provenance": {
                "data_sources": [{
                    "type": "first_party",
                    "description": "Test source"
                }],
                "collection_method": "deterministic",
                "update_frequency": "real_time"
            },
            "permissioning": {
                "requires_consent": True,
                "privacy_compliance": ["gdpr"],
                "usage_restrictions": {
                    "allowed_uses": ["measurement"]
                }
            },
            "quality": {
                "coverage_score": 0.92,
                "freshness_score": 0.95,
                "precision_score": 0.90,
                "stability_score": 0.88,
                "explainability_score": 0.93,
                "overall_trust_score": 0.92
            },
            "freshness": {
                "last_updated": datetime.utcnow().isoformat() + "Z",
                "next_update": "2026-05-12T00:00:00Z"
            },
            "audit": {
                "audit_log_required": True,
                "retention_period_days": 180
            }
        }
    }

    response = requests.post(
        f"{BASE_URL}/score-signal",
        json=request_data
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


def test_verify_signal():
    """Test signal verification."""
    print_section("Testing Signal Verification")

    request_data = {
        "request_id": str(uuid4()),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "signal_id": "test-signal-demo",
        "requestor": {
            "organization_id": "test-org-123",
            "organization_name": "Test Organization",
            "user_id": "user-123",
            "email": "user@test.example.com",
            "role": "compliance_officer"
        },
        "verification_type": "pre_activation",
        "context": {
            "intended_use": ["targeting", "measurement"],
            "geographic_scope": ["US", "GB"],
            "platforms": ["display", "video"]
        }
    }

    response = requests.post(
        f"{BASE_URL}/verify-signal",
        json=request_data
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


def test_audit_usage():
    """Test audit logging."""
    print_section("Testing Audit Logging")

    request_data = {
        "audit_id": str(uuid4()),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "signal_id": "test-signal-demo",
        "signal_version": "0.1",
        "event_type": "signal_usage",
        "actor": {
            "type": "user",
            "id": "user-123",
            "name": "Test User",
            "organization_id": "test-org-123",
            "role": "analyst"
        },
        "action": {
            "operation": "read",
            "resource": "signal_data",
            "outcome": "success",
            "description": "Accessed signal data for campaign analysis"
        }
    }

    response = requests.post(
        f"{BASE_URL}/audit-signal-usage",
        json=request_data
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


def test_list_signals():
    """Test listing signals."""
    print_section("Testing Signal Registry")

    response = requests.get(f"{BASE_URL}/signals")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200


def main():
    """Run all tests."""
    print("\n" + "=" * 70)
    print("  OpenSignals Protocol API - Test Suite")
    print("=" * 70)
    print(f"\nBase URL: {BASE_URL}")
    print("Make sure the server is running before running these tests!")

    # Check if server is accessible
    try:
        requests.get(BASE_URL, timeout=2)
    except requests.exceptions.ConnectionError:
        print("\nError: Cannot connect to the API server.")
        print("Please start the server with: python server.py")
        sys.exit(1)

    tests = [
        ("Health Check", test_health),
        ("Validate Manifest", test_validate_manifest),
        ("Score Signal", test_score_signal),
        ("Verify Signal", test_verify_signal),
        ("Audit Usage", test_audit_usage),
        ("List Signals", test_list_signals),
    ]

    results = []
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"\nError in {test_name}: {str(e)}")
            results.append((test_name, False))

    # Print summary
    print_section("Test Summary")
    passed = sum(1 for _, success in results if success)
    total = len(results)

    for test_name, success in results:
        status = "PASS" if success else "FAIL"
        print(f"  {status:6s} - {test_name}")

    print(f"\nResults: {passed}/{total} tests passed")

    if passed == total:
        print("\nAll tests passed successfully!")
        sys.exit(0)
    else:
        print("\nSome tests failed. Please check the output above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
