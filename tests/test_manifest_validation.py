"""
OpenSignals Protocol v0.1 - Manifest Validation Tests

Tests for validating OpenSignal manifests against the JSON schema.
"""

import json
import os
import sys
from pathlib import Path

import pytest

# Add reference implementation to path
sys.path.insert(0, str(Path(__file__).parent.parent / "reference-implementation" / "python"))

try:
    from validator import OpenSignalsValidator
except ImportError:
    pytest.skip("Validator module not available", allow_module_level=True)


@pytest.fixture
def validator():
    """Create a validator instance."""
    return OpenSignalsValidator()


@pytest.fixture
def examples_dir():
    """Get the examples directory path."""
    return Path(__file__).parent.parent / "examples"


@pytest.fixture
def alcohol_signal(examples_dir):
    """Load the alcohol contextual signal example."""
    with open(examples_dir / "alcohol-contextual-signal.json") as f:
        return json.load(f)


@pytest.fixture
def attention_signal(examples_dir):
    """Load the attention signal example."""
    with open(examples_dir / "attention-signal.json") as f:
        return json.load(f)


@pytest.fixture
def retail_signal(examples_dir):
    """Load the retail commerce signal example."""
    with open(examples_dir / "retail-commerce-signal.json") as f:
        return json.load(f)


@pytest.fixture
def sustainability_signal(examples_dir):
    """Load the sustainability signal example."""
    with open(examples_dir / "sustainability-signal.json") as f:
        return json.load(f)


class TestManifestValidation:
    """Test manifest validation against schema."""

    def test_alcohol_signal_valid(self, validator, alcohol_signal):
        """Test that the alcohol contextual signal passes validation."""
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert is_valid, f"Alcohol signal should be valid. Errors: {errors}"

    def test_attention_signal_valid(self, validator, attention_signal):
        """Test that the attention signal passes validation."""
        is_valid, errors = validator.validate_manifest(attention_signal)
        assert is_valid, f"Attention signal should be valid. Errors: {errors}"

    def test_retail_signal_valid(self, validator, retail_signal):
        """Test that the retail commerce signal passes validation."""
        is_valid, errors = validator.validate_manifest(retail_signal)
        assert is_valid, f"Retail signal should be valid. Errors: {errors}"

    def test_sustainability_signal_valid(self, validator, sustainability_signal):
        """Test that the sustainability signal passes validation."""
        is_valid, errors = validator.validate_manifest(sustainability_signal)
        assert is_valid, f"Sustainability signal should be valid. Errors: {errors}"


class TestManifestRequiredFields:
    """Test required fields in manifests."""

    def test_missing_signal_id_fails(self, validator, alcohol_signal):
        """Test that missing signal_id fails validation."""
        del alcohol_signal["signal_id"]
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert not is_valid, "Manifest without signal_id should fail"
        assert any("signal_id" in str(e).lower() for e in errors)

    def test_missing_name_fails(self, validator, alcohol_signal):
        """Test that missing name fails validation."""
        del alcohol_signal["name"]
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert not is_valid, "Manifest without name should fail"

    def test_missing_signal_type_fails(self, validator, alcohol_signal):
        """Test that missing signal_type fails validation."""
        del alcohol_signal["signal_type"]
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert not is_valid, "Manifest without signal_type should fail"

    def test_missing_status_fails(self, validator, alcohol_signal):
        """Test that missing status fails validation."""
        del alcohol_signal["status"]
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert not is_valid, "Manifest without status should fail"


class TestTrustScoreValidation:
    """Test trust score validation rules."""

    def test_trust_score_above_one_fails(self, validator, alcohol_signal):
        """Test that trust score above 1.0 fails validation."""
        alcohol_signal["quality"]["overall_trust_score"] = 1.5
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert not is_valid, "Trust score above 1.0 should fail"

    def test_trust_score_below_zero_fails(self, validator, alcohol_signal):
        """Test that trust score below 0.0 fails validation."""
        alcohol_signal["quality"]["overall_trust_score"] = -0.1
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert not is_valid, "Trust score below 0.0 should fail"

    def test_trust_score_valid_range(self, validator, alcohol_signal):
        """Test that trust scores in valid range pass."""
        test_scores = [0.0, 0.25, 0.5, 0.75, 1.0]
        for score in test_scores:
            alcohol_signal["quality"]["overall_trust_score"] = score
            is_valid, errors = validator.validate_manifest(alcohol_signal)
            assert is_valid, f"Trust score {score} should be valid. Errors: {errors}"


class TestSignalTypeValidation:
    """Test signal type enum validation."""

    def test_invalid_signal_type_fails(self, validator, alcohol_signal):
        """Test that invalid signal_type fails validation."""
        alcohol_signal["signal_type"] = "invalid_type"
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert not is_valid, "Invalid signal_type should fail"

    def test_valid_signal_types(self, validator, alcohol_signal):
        """Test that all valid signal types pass."""
        valid_types = [
            "audience",
            "contextual",
            "geographic",
            "temporal",
            "commerce",
            "attention",
            "creative",
            "environmental",
            "compliance",
            "outcome",
            "brand_safety",
            "custom"
        ]
        for signal_type in valid_types:
            alcohol_signal["signal_type"] = signal_type
            is_valid, errors = validator.validate_manifest(alcohol_signal)
            assert is_valid, f"Signal type '{signal_type}' should be valid. Errors: {errors}"


class TestStatusValidation:
    """Test status enum validation."""

    def test_invalid_status_fails(self, validator, alcohol_signal):
        """Test that invalid status fails validation."""
        alcohol_signal["status"] = "invalid_status"
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert not is_valid, "Invalid status should fail"

    def test_valid_statuses(self, validator, alcohol_signal):
        """Test that all valid statuses pass."""
        valid_statuses = ["active", "inactive", "deprecated", "revoked", "experimental"]
        for status in valid_statuses:
            alcohol_signal["status"] = status
            is_valid, errors = validator.validate_manifest(alcohol_signal)
            assert is_valid, f"Status '{status}' should be valid. Errors: {errors}"


class TestProvenanceValidation:
    """Test provenance field validation."""

    def test_missing_provenance_fails(self, validator, alcohol_signal):
        """Test that missing provenance fails validation."""
        del alcohol_signal["provenance"]
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert not is_valid, "Manifest without provenance should fail"

    def test_provenance_with_required_fields(self, validator, alcohol_signal):
        """Test that provenance with required fields passes."""
        assert "provenance" in alcohol_signal
        assert "data_sources" in alcohol_signal["provenance"]
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert is_valid, f"Provenance with required fields should be valid. Errors: {errors}"


class TestPermissioningValidation:
    """Test permissioning field validation."""

    def test_missing_permissioning_fails(self, validator, alcohol_signal):
        """Test that missing permissioning fails validation."""
        del alcohol_signal["permissioning"]
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert not is_valid, "Manifest without permissioning should fail"

    def test_permissioning_with_valid_use_cases(self, validator, alcohol_signal):
        """Test that permissioning with valid use cases passes."""
        assert "permissioning" in alcohol_signal
        assert "valid_use_cases" in alcohol_signal["permissioning"]
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert is_valid, f"Permissioning with use cases should be valid. Errors: {errors}"


class TestQualityScoresValidation:
    """Test quality score validation."""

    def test_all_component_scores_in_range(self, validator, alcohol_signal):
        """Test that all component scores are in valid range."""
        quality = alcohol_signal["quality"]
        score_fields = [
            "coverage_score",
            "freshness_score",
            "precision_score",
            "stability_score",
            "explainability_score",
            "overall_trust_score"
        ]

        for field in score_fields:
            assert field in quality, f"Quality should have {field}"
            score = quality[field]
            assert 0.0 <= score <= 1.0, f"{field} should be between 0 and 1, got {score}"

    def test_component_score_above_one_fails(self, validator, alcohol_signal):
        """Test that component scores above 1.0 fail."""
        alcohol_signal["quality"]["coverage_score"] = 1.5
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert not is_valid, "Component score above 1.0 should fail"


class TestFreshnessValidation:
    """Test freshness field validation."""

    def test_missing_freshness_fails(self, validator, alcohol_signal):
        """Test that missing freshness fails validation."""
        del alcohol_signal["freshness"]
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert not is_valid, "Manifest without freshness should fail"

    def test_freshness_with_update_frequency(self, validator, alcohol_signal):
        """Test that freshness with update frequency passes."""
        assert "freshness" in alcohol_signal
        assert "update_frequency_hours" in alcohol_signal["freshness"]
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert is_valid, f"Freshness with update frequency should be valid. Errors: {errors}"


class TestAuditValidation:
    """Test audit field validation."""

    def test_missing_audit_fails(self, validator, alcohol_signal):
        """Test that missing audit fails validation."""
        del alcohol_signal["audit"]
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert not is_valid, "Manifest without audit should fail"

    def test_audit_with_required_flag(self, validator, alcohol_signal):
        """Test that audit with required flag passes."""
        assert "audit" in alcohol_signal
        assert "audit_required" in alcohol_signal["audit"]
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert is_valid, f"Audit with required flag should be valid. Errors: {errors}"


class TestGovernanceValidation:
    """Test governance field validation."""

    def test_alcohol_signal_has_governance(self, validator, alcohol_signal):
        """Test that alcohol signal has governance rules."""
        assert "governance" in alcohol_signal
        assert "decision_mode" in alcohol_signal["governance"]
        assert "human_approval_required" in alcohol_signal["governance"]
        is_valid, errors = validator.validate_manifest(alcohol_signal)
        assert is_valid, f"Alcohol signal with governance should be valid. Errors: {errors}"

    def test_governance_decision_modes(self, validator, alcohol_signal):
        """Test valid governance decision modes."""
        valid_modes = [
            "observe",
            "recommend",
            "approve_with_human",
            "autonomous_with_limits",
            "autonomous_full"
        ]

        for mode in valid_modes:
            alcohol_signal["governance"]["decision_mode"] = mode
            is_valid, errors = validator.validate_manifest(alcohol_signal)
            assert is_valid, f"Decision mode '{mode}' should be valid. Errors: {errors}"


class TestTrustBandClassification:
    """Test trust band classification logic."""

    def test_highly_trusted_band(self, validator):
        """Test trust scores in highly trusted band (0.90-1.00)."""
        assert validator.get_trust_band(0.95) == "highly_trusted"
        assert validator.get_trust_band(0.90) == "highly_trusted"
        assert validator.get_trust_band(1.00) == "highly_trusted"

    def test_trusted_band(self, validator):
        """Test trust scores in trusted band (0.75-0.89)."""
        assert validator.get_trust_band(0.85) == "trusted"
        assert validator.get_trust_band(0.75) == "trusted"
        assert validator.get_trust_band(0.89) == "trusted"

    def test_limited_trust_band(self, validator):
        """Test trust scores in limited trust band (0.50-0.74)."""
        assert validator.get_trust_band(0.65) == "limited_trust"
        assert validator.get_trust_band(0.50) == "limited_trust"
        assert validator.get_trust_band(0.74) == "limited_trust"

    def test_low_trust_band(self, validator):
        """Test trust scores in low trust band (0.25-0.49)."""
        assert validator.get_trust_band(0.35) == "low_trust"
        assert validator.get_trust_band(0.25) == "low_trust"
        assert validator.get_trust_band(0.49) == "low_trust"

    def test_unsafe_band(self, validator):
        """Test trust scores in unsafe band (0.00-0.24)."""
        assert validator.get_trust_band(0.10) == "unsafe"
        assert validator.get_trust_band(0.00) == "unsafe"
        assert validator.get_trust_band(0.24) == "unsafe"


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])
