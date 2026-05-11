#!/usr/bin/env python3
"""
Test script for OpenSignals MCP Server

This script validates the server implementation without requiring
a full MCP client connection.
"""

import json
import sys
from pathlib import Path

# Add server to path
sys.path.insert(0, str(Path(__file__).parent))

def test_imports():
    """Test that all required imports work."""
    print("Testing imports...")
    try:
        from server import (
            get_available_signals,
            calculate_trust_score,
            verify_signal_compliance,
            check_category_compliance,
            create_audit_log,
            load_json_file
        )
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False


def test_get_signals():
    """Test signal discovery."""
    print("\nTesting signal discovery...")
    try:
        from server import get_available_signals
        signals = get_available_signals()
        print(f"✓ Found {len(signals)} signals:")
        for signal in signals:
            print(f"  - {signal['signal_id']}: {signal['name']} (trust: {signal['overall_trust_score']})")
        return len(signals) > 0
    except Exception as e:
        print(f"✗ Signal discovery failed: {e}")
        return False


def test_trust_scoring():
    """Test trust score calculation."""
    print("\nTesting trust score calculation...")
    try:
        from server import get_available_signals, load_json_file, calculate_trust_score
        signals = get_available_signals()
        if not signals:
            print("✗ No signals available for testing")
            return False

        signal = signals[0]
        manifest = load_json_file(Path(signal['file_path']))
        if not manifest:
            print("✗ Failed to load manifest")
            return False

        trust_score = calculate_trust_score(manifest)
        print(f"✓ Trust score calculated for {signal['signal_id']}:")
        print(f"  Overall: {trust_score['scores']['overall']:.2f}")
        print(f"  Trust Band: {trust_score['trust_band']}")
        print(f"  Autonomy: {trust_score['autonomy_recommendation']}")
        return True
    except Exception as e:
        print(f"✗ Trust scoring failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_verification():
    """Test signal verification."""
    print("\nTesting signal verification...")
    try:
        from server import get_available_signals, load_json_file, verify_signal_compliance
        signals = get_available_signals()
        if not signals:
            print("✗ No signals available for testing")
            return False

        signal = signals[0]
        manifest = load_json_file(Path(signal['file_path']))
        if not manifest:
            print("✗ Failed to load manifest")
            return False

        # Test general category
        context = {
            "category": "general",
            "market": "US",
            "intended_use": "targeting"
        }
        verification = verify_signal_compliance(manifest, context)
        print(f"✓ Verification for general category:")
        print(f"  Decision: {verification['decision']}")
        print(f"  Trust Score: {verification['trust_score']:.2f}")
        print(f"  Approval Required: {verification['approval_required']}")

        # Test sensitive category
        context_alcohol = {
            "category": "alcohol",
            "market": "GB",
            "intended_use": "contextual_targeting"
        }
        verification_alcohol = verify_signal_compliance(manifest, context_alcohol)
        print(f"\n✓ Verification for alcohol category:")
        print(f"  Decision: {verification_alcohol['decision']}")
        print(f"  Approval Required: {verification_alcohol['approval_required']}")
        print(f"  Conditions: {len(verification_alcohol['conditions'])} applied")

        return True
    except Exception as e:
        print(f"✗ Verification failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_compliance_check():
    """Test compliance checking."""
    print("\nTesting compliance checking...")
    try:
        from server import check_category_compliance

        # Test alcohol in UK
        compliance = check_category_compliance("alcohol", "GB")
        print(f"✓ Alcohol compliance in GB:")
        print(f"  Restricted: {compliance['is_restricted']}")
        print(f"  Human Approval: {compliance['compliance_requirements']['human_approval_required']}")
        print(f"  Min Age: {compliance['compliance_requirements']['minimum_age']}")

        # Test gambling in US
        compliance_gambling = check_category_compliance("gambling", "US")
        print(f"\n✓ Gambling compliance in US:")
        print(f"  Restricted: {compliance_gambling['is_restricted']}")
        print(f"  Recommendation: {compliance_gambling['recommendation']}")

        return True
    except Exception as e:
        print(f"✗ Compliance check failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_audit_logging():
    """Test audit logging."""
    print("\nTesting audit logging...")
    try:
        from server import create_audit_log

        context = {
            "brand": "test-brand",
            "campaign_id": "test-campaign",
            "buyer_agent": "test-agent",
            "category": "general"
        }

        audit = create_audit_log("test-signal", "signal_activated", context)
        print(f"✓ Audit log created:")
        print(f"  Audit ID: {audit['audit_id']}")
        print(f"  Event Type: {audit['event_type']}")
        print(f"  Status: {audit['status']}")

        return True
    except Exception as e:
        print(f"✗ Audit logging failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("OpenSignals MCP Server Test Suite")
    print("=" * 60)

    tests = [
        ("Imports", test_imports),
        ("Signal Discovery", test_get_signals),
        ("Trust Scoring", test_trust_scoring),
        ("Signal Verification", test_verification),
        ("Compliance Checking", test_compliance_check),
        ("Audit Logging", test_audit_logging),
    ]

    results = []
    for name, test_func in tests:
        result = test_func()
        results.append((name, result))

    print("\n" + "=" * 60)
    print("Test Results")
    print("=" * 60)

    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {name}")

    passed = sum(1 for _, result in results if result)
    total = len(results)

    print(f"\nPassed: {passed}/{total}")

    if passed == total:
        print("\n✓ All tests passed!")
        return 0
    else:
        print(f"\n✗ {total - passed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
