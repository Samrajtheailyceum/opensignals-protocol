"""
OpenSignals Protocol - Schema Validation Helpers

This module provides validation utilities for the OpenSignals Protocol,
including schema validation for manifests, verification requests, and audit logs.
"""

import json
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
import jsonschema
from jsonschema import validate, ValidationError, Draft202012Validator


class OpenSignalsValidator:
    """
    Validator for OpenSignals Protocol schemas.

    Provides methods to validate signal manifests, verification requests,
    and other protocol-compliant documents against their JSON schemas.
    """

    def __init__(self, schema_dir: Optional[Path] = None):
        """
        Initialize the validator with schema directory.

        Args:
            schema_dir: Path to directory containing JSON schemas.
                       If None, uses the default schemas directory.
        """
        if schema_dir is None:
            # Default to schemas/v0.1 relative to project root
            current_dir = Path(__file__).parent
            self.schema_dir = current_dir.parent.parent / "schemas" / "v0.1"
        else:
            self.schema_dir = Path(schema_dir)

        self.schemas: Dict[str, Dict] = {}
        self._load_schemas()

    def _load_schemas(self) -> None:
        """Load all available schemas from the schema directory."""
        if not self.schema_dir.exists():
            print(f"Warning: Schema directory not found at {self.schema_dir}")
            return

        schema_files = {
            "manifest": "open-signal-manifest.schema.json",
            "verify-request": "verify-signal-request.schema.json",
            "verify-response": "verify-signal-response.schema.json",
            "audit-request": "audit-signal-usage-request.schema.json",
            "audit-response": "audit-signal-usage-response.schema.json",
        }

        for schema_type, filename in schema_files.items():
            schema_path = self.schema_dir / filename
            if schema_path.exists():
                with open(schema_path, 'r') as f:
                    self.schemas[schema_type] = json.load(f)

    def validate_manifest(self, manifest: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """
        Validate a signal manifest against the OpenSignals manifest schema.

        Args:
            manifest: The signal manifest to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        return self._validate_against_schema(manifest, "manifest")

    def validate_verify_request(self, request: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """
        Validate a verification request.

        Args:
            request: The verification request to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        return self._validate_against_schema(request, "verify-request")

    def validate_verify_response(self, response: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """
        Validate a verification response.

        Args:
            response: The verification response to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        return self._validate_against_schema(response, "verify-response")

    def validate_audit_request(self, request: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """
        Validate an audit request.

        Args:
            request: The audit request to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        return self._validate_against_schema(request, "audit-request")

    def validate_audit_response(self, response: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """
        Validate an audit response.

        Args:
            response: The audit response to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        return self._validate_against_schema(response, "audit-response")

    def _validate_against_schema(
        self,
        data: Dict[str, Any],
        schema_type: str
    ) -> Tuple[bool, Optional[str]]:
        """
        Validate data against a specific schema type.

        Args:
            data: The data to validate
            schema_type: Type of schema to validate against

        Returns:
            Tuple of (is_valid, error_message)
        """
        if schema_type not in self.schemas:
            return False, f"Schema type '{schema_type}' not found. Available schemas: {list(self.schemas.keys())}"

        try:
            validator = Draft202012Validator(self.schemas[schema_type])
            validator.validate(data)
            return True, None
        except ValidationError as e:
            error_path = " -> ".join(str(p) for p in e.path) if e.path else "root"
            error_msg = f"Validation error at {error_path}: {e.message}"
            return False, error_msg
        except Exception as e:
            return False, f"Unexpected validation error: {str(e)}"

    def get_validation_errors(self, data: Dict[str, Any], schema_type: str) -> List[str]:
        """
        Get all validation errors for a document.

        Args:
            data: The data to validate
            schema_type: Type of schema to validate against

        Returns:
            List of error messages
        """
        if schema_type not in self.schemas:
            return [f"Schema type '{schema_type}' not found"]

        errors = []
        validator = Draft202012Validator(self.schemas[schema_type])

        for error in validator.iter_errors(data):
            error_path = " -> ".join(str(p) for p in error.path) if error.path else "root"
            errors.append(f"{error_path}: {error.message}")

        return errors


def calculate_trust_score(manifest: Dict[str, Any]) -> float:
    """
    Calculate a simple trust score based on manifest quality metrics.

    This is a reference implementation that demonstrates how trust scores
    might be calculated from manifest data.

    Args:
        manifest: The signal manifest

    Returns:
        Trust score between 0.0 and 1.0
    """
    quality = manifest.get("quality", {})

    # Extract individual scores
    coverage = quality.get("coverage_score", 0.0)
    freshness = quality.get("freshness_score", 0.0)
    precision = quality.get("precision_score", 0.0)
    stability = quality.get("stability_score", 0.0)
    explainability = quality.get("explainability_score", 0.0)

    # Simple weighted average (can be customized)
    weights = {
        "coverage": 0.20,
        "freshness": 0.15,
        "precision": 0.25,
        "stability": 0.20,
        "explainability": 0.20,
    }

    trust_score = (
        coverage * weights["coverage"] +
        freshness * weights["freshness"] +
        precision * weights["precision"] +
        stability * weights["stability"] +
        explainability * weights["explainability"]
    )

    return round(trust_score, 3)


def check_usage_compliance(
    manifest: Dict[str, Any],
    intended_uses: List[str],
    geographic_scope: Optional[List[str]] = None
) -> Tuple[bool, List[str]]:
    """
    Check if intended signal usage complies with manifest restrictions.

    Args:
        manifest: The signal manifest
        intended_uses: List of intended use cases
        geographic_scope: Optional list of ISO country codes where signal will be used

    Returns:
        Tuple of (is_compliant, list of violation messages)
    """
    violations = []

    # Check allowed uses
    permissioning = manifest.get("permissioning", {})
    usage_restrictions = permissioning.get("usage_restrictions", {})
    allowed_uses = usage_restrictions.get("allowed_uses", [])
    prohibited_uses = usage_restrictions.get("prohibited_uses", [])

    # Check if intended uses are allowed
    for use in intended_uses:
        if allowed_uses and use not in allowed_uses:
            violations.append(f"Use case '{use}' is not in the allowed uses list")
        if use in prohibited_uses:
            violations.append(f"Use case '{use}' is explicitly prohibited")

    # Check geographic restrictions
    if geographic_scope:
        geo_restrictions = usage_restrictions.get("geographic_restrictions", [])
        for country in geographic_scope:
            if country in geo_restrictions:
                violations.append(f"Signal usage is restricted in country: {country}")

    is_compliant = len(violations) == 0
    return is_compliant, violations


def is_signal_active(manifest: Dict[str, Any]) -> bool:
    """
    Check if a signal is currently active and usable.

    Args:
        manifest: The signal manifest

    Returns:
        True if signal is active, False otherwise
    """
    status = manifest.get("status", "").lower()
    return status == "active"
