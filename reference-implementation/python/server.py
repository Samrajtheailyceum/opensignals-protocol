"""
OpenSignals Protocol - FastAPI Reference Implementation

A production-quality reference implementation of the OpenSignals Protocol
using FastAPI. This server demonstrates the core protocol endpoints with
realistic but simplified business logic.

Endpoints:
    - GET  /health                  - Health check
    - POST /validate-manifest       - Validate a signal manifest
    - POST /verify-signal           - Verify signal compliance
    - POST /score-signal            - Calculate trust score
    - POST /audit-signal-usage      - Log signal usage audit events
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from uuid import uuid4, UUID
import logging

from validator import (
    OpenSignalsValidator,
    calculate_trust_score,
    check_usage_compliance,
    is_signal_active
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="OpenSignals Protocol API",
    description="Reference implementation of the OpenSignals Protocol for advertising signal transparency",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Initialize validator
validator = OpenSignalsValidator()


# Pydantic Models for Request/Response
class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str
    message: str


class ValidateManifestRequest(BaseModel):
    manifest: Dict[str, Any] = Field(..., description="The signal manifest to validate")


class ValidateManifestResponse(BaseModel):
    valid: bool
    errors: Optional[List[str]] = None
    warnings: Optional[List[str]] = None
    signal_id: Optional[str] = None


class VerifySignalRequest(BaseModel):
    request_id: str = Field(..., description="Unique request identifier (UUID)")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    signal_id: str = Field(..., description="Signal identifier to verify")
    requestor: Dict[str, Any] = Field(..., description="Information about requestor")
    verification_type: str = Field(..., description="Type of verification")
    context: Dict[str, Any] = Field(..., description="Verification context")

    @field_validator('request_id')
    @classmethod
    def validate_uuid(cls, v):
        try:
            UUID(v)
            return v
        except ValueError:
            raise ValueError('request_id must be a valid UUID')


class VerifySignalResponse(BaseModel):
    request_id: str
    response_id: str
    timestamp: datetime
    signal_id: str
    decision: str
    decision_confidence: float
    verification_results: Dict[str, Any]
    conditions: Optional[List[Dict[str, Any]]] = None
    blocking_issues: Optional[List[Dict[str, Any]]] = None
    warnings: Optional[List[Dict[str, Any]]] = None


class ScoreSignalRequest(BaseModel):
    signal_id: str = Field(..., description="Signal identifier")
    manifest: Dict[str, Any] = Field(..., description="Signal manifest to score")


class ScoreSignalResponse(BaseModel):
    signal_id: str
    overall_trust_score: float
    dimension_scores: Dict[str, float]
    timestamp: datetime
    assessment: str


class AuditSignalUsageRequest(BaseModel):
    audit_id: str = Field(..., description="Unique audit log entry ID (UUID)")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    signal_id: str = Field(..., description="Signal identifier")
    event_type: str = Field(..., description="Type of audit event")
    actor: Dict[str, Any] = Field(..., description="Actor performing the action")
    action: Dict[str, Any] = Field(..., description="Action details")


class AuditSignalUsageResponse(BaseModel):
    audit_id: str
    response_id: str
    timestamp: datetime
    status: str
    processing_result: Dict[str, Any]
    storage_details: Optional[Dict[str, Any]] = None


# In-memory storage for demo purposes
# In production, these would be stored in a database
signal_registry: Dict[str, Dict[str, Any]] = {}
audit_logs: List[Dict[str, Any]] = []


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """
    Health check endpoint.

    Returns the current health status of the API service.
    """
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now(timezone.utc),
        version="0.1.0",
        message="OpenSignals Protocol API is running"
    )


@app.post("/validate-manifest", response_model=ValidateManifestResponse, tags=["Validation"])
async def validate_manifest(request: ValidateManifestRequest):
    """
    Validate a signal manifest against the OpenSignals schema.

    This endpoint validates the structure, required fields, and data types
    of a signal manifest according to the OpenSignals Protocol specification.
    """
    logger.info(f"Validating manifest for signal: {request.manifest.get('signal_id', 'unknown')}")

    try:
        # Validate against schema
        is_valid, error_message = validator.validate_manifest(request.manifest)

        if not is_valid:
            # Get all validation errors for detailed feedback
            errors = validator.get_validation_errors(request.manifest, "manifest")
            return ValidateManifestResponse(
                valid=False,
                errors=errors if errors else [error_message],
                signal_id=request.manifest.get("signal_id")
            )

        # Additional business logic checks
        warnings = []

        # Check if trust score is below recommended threshold
        trust_score = calculate_trust_score(request.manifest)
        if trust_score < 0.7:
            warnings.append(
                f"Trust score ({trust_score:.2f}) is below recommended threshold (0.7)"
            )

        # Check if signal is active
        if not is_signal_active(request.manifest):
            warnings.append(
                f"Signal status is '{request.manifest.get('status')}', not 'active'"
            )

        # Store in registry for demo purposes
        signal_id = request.manifest.get("signal_id")
        if signal_id:
            signal_registry[signal_id] = request.manifest
            logger.info(f"Signal {signal_id} stored in registry")

        return ValidateManifestResponse(
            valid=True,
            errors=None,
            warnings=warnings if warnings else None,
            signal_id=signal_id
        )

    except Exception as e:
        logger.error(f"Error validating manifest: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal error during validation: {str(e)}"
        )


@app.post("/verify-signal", response_model=VerifySignalResponse, tags=["Verification"])
async def verify_signal(request: VerifySignalRequest):
    """
    Verify signal compliance against policies and regulations.

    This endpoint performs comprehensive verification checks including:
    - Usage rights validation
    - Geographic restriction checks
    - Consent requirement verification
    - Trust score evaluation
    - Policy compliance assessment
    """
    logger.info(f"Verifying signal: {request.signal_id} (request: {request.request_id})")

    # Validate request against schema
    is_valid, error_message = validator.validate_verify_request(request.model_dump())
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid verification request: {error_message}"
        )

    # Look up signal manifest
    manifest = signal_registry.get(request.signal_id)
    if not manifest:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Signal '{request.signal_id}' not found in registry"
        )

    # Perform verification checks
    checks_performed = []
    blocking_issues = []
    warnings = []
    decision = "approved"
    confidence = 1.0

    # Check 1: Signal status
    status_check = {
        "check_id": "status_check",
        "check_name": "Signal Status Verification",
        "category": "technical_validation",
        "status": "pass" if is_signal_active(manifest) else "fail",
        "result": {
            "message": f"Signal status is '{manifest.get('status')}'",
            "severity": "critical" if not is_signal_active(manifest) else "info"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "duration_ms": 5
    }
    checks_performed.append(status_check)

    if not is_signal_active(manifest):
        blocking_issues.append({
            "issue_id": "inactive_signal",
            "category": "technical_failure",
            "description": "Signal is not in active status",
            "severity": "critical",
            "resolution_steps": ["Contact signal provider to activate signal"]
        })
        decision = "blocked"

    # Check 2: Usage compliance
    intended_uses = request.context.get("intended_use", [])
    geographic_scope = request.context.get("geographic_scope", [])

    is_compliant, violations = check_usage_compliance(manifest, intended_uses, geographic_scope)

    usage_check = {
        "check_id": "usage_compliance",
        "check_name": "Usage Rights Verification",
        "category": "usage_rights",
        "status": "pass" if is_compliant else "fail",
        "result": {
            "message": "All intended uses are compliant" if is_compliant else "Usage violations detected",
            "details": {"violations": violations} if violations else None,
            "severity": "high" if violations else "info"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "duration_ms": 12
    }
    checks_performed.append(usage_check)

    if violations:
        for violation in violations:
            blocking_issues.append({
                "issue_id": f"usage_violation_{len(blocking_issues)}",
                "category": "policy_violation",
                "description": violation,
                "severity": "high",
                "resolution_steps": ["Review signal usage restrictions", "Adjust intended use cases"]
            })
        decision = "blocked"
        confidence = 0.95

    # Check 3: Trust score
    trust_score = calculate_trust_score(manifest)
    trust_threshold = 0.6

    trust_check = {
        "check_id": "trust_score",
        "check_name": "Trust Score Evaluation",
        "category": "trust_score",
        "status": "pass" if trust_score >= trust_threshold else "warning",
        "result": {
            "message": f"Trust score: {trust_score:.2f} (threshold: {trust_threshold:.2f})",
            "details": {"score": trust_score, "threshold": trust_threshold},
            "severity": "medium" if trust_score < trust_threshold else "info"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "duration_ms": 8
    }
    checks_performed.append(trust_check)

    if trust_score < trust_threshold:
        warnings.append({
            "warning_id": "low_trust_score",
            "description": f"Trust score ({trust_score:.2f}) is below recommended threshold ({trust_threshold:.2f})",
            "category": "data_quality",
            "recommendation": "Review signal quality metrics and consider higher-quality alternatives",
            "impact": "medium"
        })
        if decision == "approved":
            decision = "approved_with_conditions"
            confidence = 0.85

    # Check 4: Consent requirements
    requires_consent = manifest.get("permissioning", {}).get("requires_consent", False)
    consent_available = request.context.get("consent_status", {}).get("consent_available", False)

    consent_check = {
        "check_id": "consent_verification",
        "check_name": "Consent Requirement Check",
        "category": "consent_validation",
        "status": "pass" if not requires_consent or consent_available else "fail",
        "result": {
            "message": "Consent requirements satisfied" if not requires_consent or consent_available else "Required consent not available",
            "details": {
                "requires_consent": requires_consent,
                "consent_available": consent_available
            },
            "severity": "critical" if requires_consent and not consent_available else "info"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "duration_ms": 6
    }
    checks_performed.append(consent_check)

    if requires_consent and not consent_available:
        blocking_issues.append({
            "issue_id": "missing_consent",
            "category": "missing_consent",
            "description": "Signal requires explicit user consent but consent is not available",
            "severity": "critical",
            "resolution_steps": [
                "Obtain user consent via appropriate consent framework",
                "Verify consent string includes required purposes"
            ]
        })
        decision = "blocked"

    # Build response
    response = VerifySignalResponse(
        request_id=request.request_id,
        response_id=str(uuid4()),
        timestamp=datetime.now(timezone.utc),
        signal_id=request.signal_id,
        decision=decision,
        decision_confidence=confidence,
        verification_results={
            "overall_status": "fail" if blocking_issues else ("pass_with_warnings" if warnings else "pass"),
            "checks_performed": checks_performed,
            "summary": {
                "total_checks": len(checks_performed),
                "passed": sum(1 for c in checks_performed if c["status"] == "pass"),
                "failed": sum(1 for c in checks_performed if c["status"] == "fail"),
                "warnings": sum(1 for c in checks_performed if c["status"] == "warning"),
            }
        },
        blocking_issues=blocking_issues if blocking_issues else None,
        warnings=warnings if warnings else None
    )

    logger.info(f"Verification complete for {request.signal_id}: {decision}")
    return response


@app.post("/score-signal", response_model=ScoreSignalResponse, tags=["Scoring"])
async def score_signal(request: ScoreSignalRequest):
    """
    Calculate trust score for a signal based on its quality metrics.

    Returns an overall trust score and individual dimension scores
    for coverage, freshness, precision, stability, and explainability.
    """
    logger.info(f"Calculating trust score for signal: {request.signal_id}")

    # Validate manifest
    is_valid, error_message = validator.validate_manifest(request.manifest)
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid manifest: {error_message}"
        )

    # Extract quality metrics
    quality = request.manifest.get("quality", {})

    dimension_scores = {
        "coverage": quality.get("coverage_score", 0.0),
        "freshness": quality.get("freshness_score", 0.0),
        "precision": quality.get("precision_score", 0.0),
        "stability": quality.get("stability_score", 0.0),
        "explainability": quality.get("explainability_score", 0.0),
    }

    # Calculate overall trust score
    overall_score = calculate_trust_score(request.manifest)

    # Generate assessment
    if overall_score >= 0.9:
        assessment = "excellent"
    elif overall_score >= 0.8:
        assessment = "very_good"
    elif overall_score >= 0.7:
        assessment = "good"
    elif overall_score >= 0.6:
        assessment = "acceptable"
    elif overall_score >= 0.5:
        assessment = "marginal"
    else:
        assessment = "poor"

    logger.info(f"Trust score for {request.signal_id}: {overall_score:.3f} ({assessment})")

    return ScoreSignalResponse(
        signal_id=request.signal_id,
        overall_trust_score=overall_score,
        dimension_scores=dimension_scores,
        timestamp=datetime.now(timezone.utc),
        assessment=assessment
    )


@app.post("/audit-signal-usage", response_model=AuditSignalUsageResponse, tags=["Auditing"])
async def audit_signal_usage(request: AuditSignalUsageRequest):
    """
    Log an audit event for signal usage.

    Creates a comprehensive audit trail entry for signal access, usage,
    or modification events for compliance and governance purposes.
    """
    logger.info(f"Logging audit event: {request.event_type} for signal {request.signal_id}")

    # Validate request against schema
    is_valid, error_message = validator.validate_audit_request(request.model_dump())
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid audit request: {error_message}"
        )

    # Process and store audit log
    audit_entry = request.model_dump()
    audit_logs.append(audit_entry)

    # Simulate storage and indexing
    processing_result = {
        "received": True,
        "validated": True,
        "stored": True,
        "indexed": True,
        "processing_time_ms": 45
    }

    storage_details = {
        "storage_location": f"audit-logs/2026/05/{request.audit_id}",
        "storage_tier": "hot",
        "backup_status": "completed",
        "encryption_status": "encrypted"
    }

    response = AuditSignalUsageResponse(
        audit_id=request.audit_id,
        response_id=str(uuid4()),
        timestamp=datetime.now(timezone.utc),
        status="accepted",
        processing_result=processing_result,
        storage_details=storage_details
    )

    logger.info(f"Audit log {request.audit_id} successfully stored")
    return response


@app.get("/signals", tags=["Registry"])
async def list_signals():
    """
    List all registered signals.

    Returns a summary of all signals currently registered in the system.
    This is a convenience endpoint for the reference implementation.
    """
    signals = []
    for signal_id, manifest in signal_registry.items():
        signals.append({
            "signal_id": signal_id,
            "name": manifest.get("name"),
            "type": manifest.get("signal_type"),
            "status": manifest.get("status"),
            "trust_score": calculate_trust_score(manifest)
        })

    return {
        "total": len(signals),
        "signals": signals
    }


@app.get("/audit-logs", tags=["Auditing"])
async def list_audit_logs(limit: int = 100, event_type: Optional[str] = None):
    """
    Retrieve audit logs.

    Returns recent audit log entries, optionally filtered by event type.
    This is a convenience endpoint for the reference implementation.
    """
    filtered_logs = audit_logs

    if event_type:
        filtered_logs = [log for log in filtered_logs if log.get("event_type") == event_type]

    return {
        "total": len(filtered_logs),
        "limit": limit,
        "audit_logs": filtered_logs[-limit:]
    }


if __name__ == "__main__":
    import uvicorn

    logger.info("Starting OpenSignals Protocol API server...")
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
