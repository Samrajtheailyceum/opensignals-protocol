# Chain-of-Thought Authentication for OpenSignals

**Version**: 0.1
**Status**: Revolutionary Security Innovation
**Last Updated**: May 2026
**Authors**: OpenSignals Protocol Community

---

## Executive Summary

Chain-of-Thought Authentication (CoTA) is a revolutionary cryptographic framework that makes AI agent decisions **provably explainable, tamper-evident, and auditable**. Unlike traditional authentication that signs only the final decision, CoTA signs the entire reasoning process, making it mathematically impossible to approve signals without showing your work.

This document specifies how OpenSignals implements CoTA to prevent signal spoofing, trust score manipulation, compliance bypassing, unauthorized activation, and fraud in agentic advertising systems.

**The innovation**: You can't fake a decision you can explain. Every verification must show its reasoning, every step must be cryptographically signed, and every decision forms an immutable chain of custody that auditors can follow from input to output.

---

## Table of Contents

1. [The Problem: Why Traditional Auth Fails for Agents](#1-the-problem-why-traditional-auth-fails-for-agents)
2. [The Solution: Chain-of-Thought Authentication](#2-the-solution-chain-of-thought-authentication)
3. [Core Concepts](#3-core-concepts)
4. [Architecture](#4-architecture)
5. [JSON Schema for CoTA](#5-json-schema-for-cota)
6. [Example: Signed Verification with Reasoning](#6-example-signed-verification-with-reasoning)
7. [Python Implementation](#7-python-implementation)
8. [Integration with verify_signal](#8-integration-with-verify_signal)
9. [Multi-Party Verification](#9-multi-party-verification)
10. [Attack Resistance](#10-attack-resistance)
11. [Compliance and Audit Benefits](#11-compliance-and-audit-benefits)
12. [Implementation Guidelines](#12-implementation-guidelines)
13. [Security Considerations](#13-security-considerations)
14. [Future Enhancements](#14-future-enhancements)

---

## 1. The Problem: Why Traditional Auth Fails for Agents

### 1.1 The Attack Surface

Traditional authentication systems sign decisions but not reasoning:

```json
{
  "signal_id": "premium-cocktails",
  "decision": "approved",
  "trust_score": 0.92,
  "signature": "3045022100..."
}
```

**Problem**: This signature proves the agent made a decision, but:
- **Can't prove WHY** the decision was made
- **Can't detect** if trust scores were manipulated before signing
- **Can't verify** that compliance checks actually ran
- **Can't audit** the reasoning process that led to approval
- **Can't prevent** agents from rubber-stamping approvals

### 1.2 Real-World Attack Scenarios

**Scenario 1: Trust Score Inflation**
```
Attacker: Submits signal with fake trust_score: 0.95
Traditional System: Signs the high score ✓
Result: Low-quality signal approved
```

**Scenario 2: Compliance Bypass**
```
Attacker: Marks regulated signal as "approved" without checks
Traditional System: Signs the decision ✓
Result: Alcohol signal activated in prohibited market
```

**Scenario 3: Reasoning Spoofing**
```
Attacker: Claims "GDPR compliant" but never checked
Traditional System: No way to verify the claim
Result: Privacy violation undetected
```

**Scenario 4: Retroactive Forgery**
```
Attacker: After incident, claims different reasoning
Traditional System: Can't prove what was originally reasoned
Result: No accountability for bad decisions
```

### 1.3 Why This Matters for Agentic Advertising

AI agents in advertising operate at scale:
- **Thousands of signals** evaluated per day
- **Millions of dollars** allocated autonomously
- **Regulated categories** (alcohol, pharma, finance) requiring strict compliance
- **Cross-border operations** with complex legal requirements
- **High fraud incentive** due to money at stake

Without provable reasoning, a single compromised agent could:
- Approve prohibited signals
- Bypass human review requirements
- Fake compliance attestations
- Manipulate trust scores
- Create liability for brands

---

## 2. The Solution: Chain-of-Thought Authentication

### 2.1 Core Principle

**Every verification must show its work, and every step must be cryptographically signed.**

Instead of signing just the final decision, CoTA signs:
1. **Input signal data** (what was evaluated)
2. **Reasoning steps** (how the evaluation happened)
3. **Evidence checked** (what data sources were consulted)
4. **Logic applied** (which rules and policies were tested)
5. **Intermediate conclusions** (partial results along the way)
6. **Final decision** (approve/block/review)
7. **Confidence assessment** (how certain is the agent)

Each step links cryptographically to the previous step, forming a chain of custody from input to output.

### 2.2 Key Properties

**Explainability**: Every decision includes human-readable reasoning
**Tamper-Evidence**: Any change to reasoning breaks the cryptographic chain
**Verifiability**: Anyone can verify the signature and reasoning independently
**Auditability**: Full reasoning trail available for compliance review
**Non-Repudiation**: Agent cannot deny what it reasoned
**Multi-Party**: Multiple agents can co-sign complex decisions

### 2.3 What Makes This Revolutionary

1. **Reasoning as First-Class Artifact**: The thought process becomes a verifiable data structure
2. **Math Proves Logic**: Cryptography guarantees the reasoning happened as claimed
3. **Agent Accountability**: AI must explain itself or the decision is invalid
4. **Compliance by Design**: Regulators can audit the exact logic used
5. **Fraud Prevention**: Can't fake a decision you can explain in detail

---

## 3. Core Concepts

### 3.1 Chain-of-Thought Structure

A CoTA reasoning chain consists of:

```
Input Hash → Reasoning Step 1 → Reasoning Step 2 → ... → Final Decision
     ↓              ↓                  ↓                        ↓
  [signed]      [signed]           [signed]                 [signed]
```

Each step includes:
- **Step ID**: Unique identifier in the chain
- **Step Type**: Type of reasoning (check_compliance, evaluate_trust, etc.)
- **Input**: Data consumed by this step
- **Logic**: Rule or algorithm applied
- **Output**: Result or conclusion
- **Evidence**: External data sources consulted
- **Confidence**: Certainty level (0-1)
- **Timestamp**: When this step was executed
- **Previous Hash**: Link to prior step in chain
- **Signature**: Cryptographic signature of this step

### 3.2 Signature Hierarchy

Three levels of signatures:

1. **Step Signatures**: Each reasoning step signed individually
2. **Chain Signature**: Overall reasoning chain signed by primary verifier
3. **Co-Signatures**: Additional agents can co-sign to attest agreement

### 3.3 Reasoning Transparency Levels

CoTA supports different transparency levels:

- **Full Transparency**: All reasoning steps publicly visible
- **Auditor Access**: Reasoning available to authorized auditors only
- **Zero-Knowledge**: Proof that reasoning happened without revealing details
- **Selective Disclosure**: Some steps public, sensitive steps private

---

## 4. Architecture

### 4.1 System Components

```
┌─────────────────────────────────────────────────────────────────┐
│                    Verification Agent                            │
│                                                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │           Chain-of-Thought Engine                          │  │
│  │  • Orchestrates reasoning steps                            │  │
│  │  • Maintains chain integrity                               │  │
│  │  • Signs each step                                         │  │
│  └───────────────────────────────────────────────────────────┘  │
│                            ▲                                      │
│                            │                                      │
│  ┌────────────┬────────────┴──────┬──────────────────────────┐  │
│  │            │                   │                          │  │
│  │  Compliance  Trust Score   Provenance    Policy          │  │
│  │  Checker     Validator     Tracer        Enforcer        │  │
│  │                                                           │  │
│  └───────────────────────────────────────────────────────────┘  │
│                            │                                      │
└────────────────────────────┼──────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│               Reasoning Chain Storage (Tamper-Evident)           │
│  • Content-addressed storage                                     │
│  • Blockchain or Merkle tree                                     │
│  • Distributed ledger (optional)                                 │
└─────────────────────────────────────────────────────────────────┘
                             ▲
                             │
┌────────────────────────────┴──────────────────────────────────┐
│                    Audit & Verification Tools                   │
│  • Chain validator                                              │
│  • Reasoning analyzer                                           │
│  • Compliance reporting                                         │
│  • Fraud detection                                              │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Data Flow

```
1. Signal Verification Request
         ↓
2. CoTA Engine Initializes Chain
   - Hashes input signal data
   - Signs initial state
         ↓
3. Execute Reasoning Steps (parallelizable where independent)
   - Check geographic restrictions → Sign step
   - Validate trust score → Sign step
   - Verify consent permissions → Sign step
   - Assess compliance rules → Sign step
   - Evaluate provenance chain → Sign step
         ↓
4. Synthesize Final Decision
   - Aggregate step conclusions
   - Apply decision logic
   - Calculate confidence
   - Sign final decision
         ↓
5. Package Reasoning Chain
   - Bundle all signed steps
   - Create chain signature
   - Store in tamper-evident storage
         ↓
6. Return Verification Response
   - Decision (approve/block/review)
   - Trust score
   - Reasoning chain reference
   - Signature for full package
```

### 4.3 Chain Storage Options

**Option 1: Centralized Append-Only Log**
- PostgreSQL with append-only table
- Each step gets sequential ID
- Cryptographic hash chain links steps
- Fast, simple, auditable

**Option 2: Distributed Ledger**
- Blockchain (Ethereum, Polygon, Hyperledger)
- Each reasoning chain = smart contract
- Immutable, decentralized, trustless
- Higher latency, more complex

**Option 3: Content-Addressed Storage**
- IPFS or similar
- Each step = content-addressed object
- Reasoning chains reference step CIDs
- Distributed, censorship-resistant

**Recommendation**: Start with Option 1 (centralized), migrate to Option 3 (IPFS) for scale.

---

## 5. JSON Schema for CoTA

### 5.1 Reasoning Step Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://opensignals.org/schemas/v0.1/cota-reasoning-step.schema.json",
  "title": "Chain-of-Thought Reasoning Step",
  "description": "A single reasoning step in a Chain-of-Thought authentication process",
  "type": "object",
  "required": [
    "step_id",
    "step_type",
    "step_index",
    "timestamp",
    "input",
    "logic",
    "output",
    "confidence",
    "previous_hash",
    "signature"
  ],
  "properties": {
    "step_id": {
      "type": "string",
      "format": "uuid",
      "description": "Unique identifier for this reasoning step"
    },
    "step_type": {
      "type": "string",
      "enum": [
        "input_validation",
        "geographic_check",
        "category_compliance",
        "trust_score_validation",
        "consent_verification",
        "provenance_check",
        "policy_enforcement",
        "risk_assessment",
        "decision_synthesis",
        "custom"
      ],
      "description": "Type of reasoning performed in this step"
    },
    "step_index": {
      "type": "integer",
      "minimum": 0,
      "description": "Sequential index of this step in the chain (0-based)"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp when this reasoning step was executed"
    },
    "input": {
      "type": "object",
      "description": "Input data consumed by this reasoning step",
      "properties": {
        "data": {
          "type": "object",
          "description": "The actual input data"
        },
        "data_hash": {
          "type": "string",
          "pattern": "^[a-fA-F0-9]{64}$",
          "description": "SHA-256 hash of input data for integrity verification"
        },
        "sources": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Data sources consulted (URLs, database queries, API calls)"
        }
      },
      "required": ["data_hash"]
    },
    "logic": {
      "type": "object",
      "description": "The reasoning logic applied in this step",
      "properties": {
        "rule_id": {
          "type": "string",
          "description": "Identifier of the rule or policy applied"
        },
        "rule_description": {
          "type": "string",
          "description": "Human-readable description of the logic"
        },
        "algorithm": {
          "type": "string",
          "description": "Algorithm or method used (e.g., 'regex_match', 'threshold_comparison', 'ml_classifier')"
        },
        "parameters": {
          "type": "object",
          "description": "Parameters used in the logic execution"
        },
        "explanation": {
          "type": "string",
          "minLength": 10,
          "description": "Natural language explanation of what this step checks and why"
        }
      },
      "required": ["explanation"]
    },
    "output": {
      "type": "object",
      "description": "Result or conclusion of this reasoning step",
      "properties": {
        "result": {
          "type": "string",
          "enum": ["pass", "fail", "warning", "info", "conditional"],
          "description": "Outcome of this reasoning step"
        },
        "value": {
          "description": "Computed value (boolean, number, string, object)"
        },
        "message": {
          "type": "string",
          "description": "Human-readable message explaining the result"
        },
        "evidence": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "source": {
                "type": "string",
                "description": "Source of evidence (URL, database, API endpoint)"
              },
              "data": {
                "description": "Evidence data (can be redacted for privacy)"
              },
              "timestamp": {
                "type": "string",
                "format": "date-time",
                "description": "When evidence was collected"
              }
            }
          },
          "description": "Evidence supporting this reasoning step's conclusion"
        },
        "recommendations": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Recommendations based on this step's findings"
        }
      },
      "required": ["result", "message"]
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "description": "Confidence level in this step's conclusion (0-1)"
    },
    "dependencies": {
      "type": "array",
      "items": {
        "type": "string",
        "format": "uuid"
      },
      "description": "Step IDs that this step depends on"
    },
    "previous_hash": {
      "type": "string",
      "pattern": "^[a-fA-F0-9]{64}$",
      "description": "SHA-256 hash of the previous step in the chain (or input hash for step 0)"
    },
    "step_hash": {
      "type": "string",
      "pattern": "^[a-fA-F0-9]{64}$",
      "description": "SHA-256 hash of this step's content (before signature)"
    },
    "signature": {
      "type": "object",
      "description": "Cryptographic signature of this reasoning step",
      "properties": {
        "algorithm": {
          "type": "string",
          "enum": ["ECDSA-SHA256", "RSA-SHA256", "EdDSA"],
          "description": "Signature algorithm used"
        },
        "value": {
          "type": "string",
          "description": "Base64-encoded signature value"
        },
        "public_key": {
          "type": "string",
          "description": "Public key used for signature verification"
        },
        "signer_id": {
          "type": "string",
          "description": "Identifier of the agent or system that signed this step"
        },
        "signer_role": {
          "type": "string",
          "enum": ["governance_agent", "compliance_checker", "trust_scorer", "human_reviewer", "co_signer"],
          "description": "Role of the signing entity"
        }
      },
      "required": ["algorithm", "value", "public_key", "signer_id"]
    },
    "metadata": {
      "type": "object",
      "description": "Additional metadata for this step",
      "properties": {
        "execution_time_ms": {
          "type": "integer",
          "minimum": 0,
          "description": "Time taken to execute this step in milliseconds"
        },
        "parallel_group": {
          "type": "string",
          "description": "Identifier for parallel execution group (if step ran in parallel)"
        },
        "retry_count": {
          "type": "integer",
          "minimum": 0,
          "description": "Number of retries for this step"
        },
        "tags": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Tags for categorization and search"
        }
      }
    }
  },
  "additionalProperties": false
}
```

### 5.2 Reasoning Chain Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://opensignals.org/schemas/v0.1/cota-reasoning-chain.schema.json",
  "title": "Chain-of-Thought Reasoning Chain",
  "description": "Complete chain of reasoning steps for a signal verification decision",
  "type": "object",
  "required": [
    "chain_id",
    "signal_id",
    "verification_request_id",
    "timestamp_start",
    "timestamp_end",
    "input_hash",
    "steps",
    "final_decision",
    "chain_signature"
  ],
  "properties": {
    "chain_id": {
      "type": "string",
      "format": "uuid",
      "description": "Unique identifier for this reasoning chain"
    },
    "signal_id": {
      "type": "string",
      "description": "Identifier of the signal being verified"
    },
    "verification_request_id": {
      "type": "string",
      "format": "uuid",
      "description": "ID of the original verify_signal request"
    },
    "timestamp_start": {
      "type": "string",
      "format": "date-time",
      "description": "When reasoning chain execution started"
    },
    "timestamp_end": {
      "type": "string",
      "format": "date-time",
      "description": "When reasoning chain execution completed"
    },
    "input_hash": {
      "type": "string",
      "pattern": "^[a-fA-F0-9]{64}$",
      "description": "SHA-256 hash of the verification request input"
    },
    "input_data": {
      "type": "object",
      "description": "The original verification request data (optional, can be stored separately)"
    },
    "steps": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "https://opensignals.org/schemas/v0.1/cota-reasoning-step.schema.json"
      },
      "description": "Ordered array of reasoning steps in this chain"
    },
    "final_decision": {
      "type": "object",
      "description": "The final verification decision synthesized from reasoning steps",
      "properties": {
        "decision": {
          "type": "string",
          "enum": ["approved", "approved_with_conditions", "blocked", "requires_review", "error"],
          "description": "Overall verification decision"
        },
        "decision_confidence": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "description": "Confidence in the final decision (0-1)"
        },
        "trust_score": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "description": "Computed trust score for the signal"
        },
        "conditions": {
          "type": "array",
          "items": {
            "type": "object"
          },
          "description": "Conditions attached to approved_with_conditions decision"
        },
        "blocking_issues": {
          "type": "array",
          "items": {
            "type": "object"
          },
          "description": "Issues that led to blocked decision"
        },
        "synthesis_explanation": {
          "type": "string",
          "minLength": 20,
          "description": "Natural language explanation of how final decision was reached from reasoning steps"
        }
      },
      "required": ["decision", "decision_confidence", "synthesis_explanation"]
    },
    "chain_signature": {
      "type": "object",
      "description": "Signature of the complete reasoning chain",
      "properties": {
        "algorithm": {
          "type": "string",
          "enum": ["ECDSA-SHA256", "RSA-SHA256", "EdDSA"],
          "description": "Signature algorithm"
        },
        "value": {
          "type": "string",
          "description": "Base64-encoded signature of chain hash"
        },
        "chain_hash": {
          "type": "string",
          "pattern": "^[a-fA-F0-9]{64}$",
          "description": "SHA-256 hash of the complete reasoning chain (Merkle root of all step hashes)"
        },
        "public_key": {
          "type": "string",
          "description": "Public key for signature verification"
        },
        "signer_id": {
          "type": "string",
          "description": "Primary verifier agent ID"
        },
        "signer_role": {
          "type": "string",
          "description": "Role of primary signer"
        }
      },
      "required": ["algorithm", "value", "chain_hash", "public_key", "signer_id"]
    },
    "co_signatures": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "signer_id": {
            "type": "string",
            "description": "ID of co-signing agent"
          },
          "signer_role": {
            "type": "string",
            "description": "Role of co-signer"
          },
          "signature": {
            "type": "string",
            "description": "Co-signature value"
          },
          "public_key": {
            "type": "string",
            "description": "Co-signer's public key"
          },
          "attestation": {
            "type": "string",
            "description": "What the co-signer is attesting to"
          },
          "timestamp": {
            "type": "string",
            "format": "date-time",
            "description": "When co-signature was created"
          }
        },
        "required": ["signer_id", "signature", "public_key", "attestation"]
      },
      "description": "Additional co-signatures from other verifiers"
    },
    "transparency_level": {
      "type": "string",
      "enum": ["full_transparency", "auditor_access", "zero_knowledge", "selective_disclosure"],
      "description": "Transparency level for this reasoning chain"
    },
    "storage_reference": {
      "type": "object",
      "description": "Reference to where full chain is stored",
      "properties": {
        "storage_type": {
          "type": "string",
          "enum": ["centralized_db", "ipfs", "blockchain", "other"],
          "description": "Type of storage backend"
        },
        "reference": {
          "type": "string",
          "description": "Storage reference (URL, CID, transaction hash, etc.)"
        },
        "retrieval_endpoint": {
          "type": "string",
          "format": "uri",
          "description": "API endpoint to retrieve full chain"
        }
      }
    },
    "audit_metadata": {
      "type": "object",
      "description": "Metadata for audit and compliance purposes",
      "properties": {
        "compliance_frameworks": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Compliance frameworks this chain satisfies (GDPR, CCPA, etc.)"
        },
        "retention_until": {
          "type": "string",
          "format": "date-time",
          "description": "When this chain can be deleted per retention policy"
        },
        "jurisdiction": {
          "type": "array",
          "items": {
            "type": "string",
            "pattern": "^[A-Z]{2}$"
          },
          "description": "Legal jurisdictions this decision applies to"
        },
        "human_reviewers": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "reviewer_id": {
                "type": "string"
              },
              "reviewer_role": {
                "type": "string"
              },
              "review_timestamp": {
                "type": "string",
                "format": "date-time"
              },
              "review_outcome": {
                "type": "string",
                "enum": ["approved", "rejected", "flagged"]
              },
              "review_notes": {
                "type": "string"
              }
            }
          },
          "description": "Human reviewers who examined this reasoning chain"
        }
      }
    },
    "metadata": {
      "type": "object",
      "description": "Additional metadata",
      "properties": {
        "protocol_version": {
          "type": "string",
          "description": "OpenSignals Protocol version"
        },
        "cota_version": {
          "type": "string",
          "description": "Chain-of-Thought Auth version"
        },
        "total_execution_time_ms": {
          "type": "integer",
          "minimum": 0,
          "description": "Total execution time for reasoning chain"
        },
        "step_count": {
          "type": "integer",
          "minimum": 0,
          "description": "Total number of steps in chain"
        },
        "parallel_steps": {
          "type": "integer",
          "minimum": 0,
          "description": "Number of steps executed in parallel"
        }
      }
    }
  },
  "additionalProperties": false
}
```

---

## 6. Example: Signed Verification with Reasoning

### 6.1 Complete Example: Alcohol Signal Verification

```json
{
  "chain_id": "550e8400-e29b-41d4-a716-446655440000",
  "signal_id": "premium-cocktail-contexts",
  "verification_request_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
  "timestamp_start": "2026-05-11T14:30:00.000Z",
  "timestamp_end": "2026-05-11T14:30:02.847Z",
  "input_hash": "a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a",
  "input_data": {
    "signal_id": "premium-cocktail-contexts",
    "requestor": {
      "organization_id": "premium-spirits-co",
      "user_id": "media-buyer-bot-v2"
    },
    "verification_type": "pre_activation",
    "context": {
      "intended_use": ["targeting"],
      "geographic_scope": ["GB"],
      "campaign_details": {
        "policy_sensitive_categories": ["alcohol"]
      }
    }
  },
  "steps": [
    {
      "step_id": "step-00000000-0000-0000-0000-000000000001",
      "step_type": "input_validation",
      "step_index": 0,
      "timestamp": "2026-05-11T14:30:00.123Z",
      "input": {
        "data_hash": "a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a",
        "sources": ["verification_request"]
      },
      "logic": {
        "rule_id": "input_validation_v1",
        "rule_description": "Validate that verification request contains all required fields and follows schema",
        "algorithm": "json_schema_validation",
        "parameters": {
          "schema_version": "0.1"
        },
        "explanation": "I am validating that the verification request is well-formed and contains all mandatory fields (signal_id, requestor, verification_type, context). This ensures downstream reasoning steps have valid input data to work with."
      },
      "output": {
        "result": "pass",
        "value": true,
        "message": "Verification request is valid and complete. All required fields present.",
        "evidence": [
          {
            "source": "json_schema_validator",
            "data": {
              "schema_valid": true,
              "missing_fields": []
            },
            "timestamp": "2026-05-11T14:30:00.120Z"
          }
        ]
      },
      "confidence": 1.0,
      "dependencies": [],
      "previous_hash": "a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a",
      "step_hash": "b8aad2c7c0fe87d7ab8afe1c24e46a98d1c19ae28d7fc3e9c53e62c7b2e8e564",
      "signature": {
        "algorithm": "ECDSA-SHA256",
        "value": "MEUCIQDxKx4JBZz3h9...",
        "public_key": "04a7b8c9d0e1f2...",
        "signer_id": "governance-agent-001",
        "signer_role": "governance_agent"
      },
      "metadata": {
        "execution_time_ms": 23,
        "parallel_group": "init"
      }
    },
    {
      "step_id": "step-00000000-0000-0000-0000-000000000002",
      "step_type": "geographic_check",
      "step_index": 1,
      "timestamp": "2026-05-11T14:30:00.456Z",
      "input": {
        "data": {
          "geographic_scope": ["GB"],
          "category": "alcohol"
        },
        "data_hash": "c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2",
        "sources": [
          "verification_request",
          "https://compliance-api.opensignals.org/geographic-restrictions"
        ]
      },
      "logic": {
        "rule_id": "alcohol_geographic_restriction_v2",
        "rule_description": "Check if alcohol advertising is permitted in requested geography",
        "algorithm": "geographic_policy_lookup",
        "parameters": {
          "category": "alcohol",
          "markets": ["GB"]
        },
        "explanation": "I am checking whether alcohol advertising is legally permitted in Great Britain (GB). I consulted the OpenSignals compliance API which maintains current advertising regulations by market and category. For GB, alcohol advertising is permitted for adults 18+ under UK Advertising Code (CAP Code)."
      },
      "output": {
        "result": "pass",
        "value": {
          "permitted": true,
          "age_restriction": 18,
          "additional_requirements": [
            "no_youth_appeal",
            "responsible_messaging",
            "no_under_18_targeting"
          ]
        },
        "message": "Alcohol advertising is permitted in GB for adults 18+. Must comply with UK CAP Code restrictions on youth appeal and responsible messaging.",
        "evidence": [
          {
            "source": "https://compliance-api.opensignals.org/geographic-restrictions",
            "data": {
              "market": "GB",
              "category": "alcohol",
              "permitted": true,
              "age_restriction": 18,
              "regulation_reference": "UK CAP Code Section 18"
            },
            "timestamp": "2026-05-11T14:30:00.450Z"
          }
        ],
        "recommendations": [
          "Enforce age targeting >= 18 years",
          "Apply CAP Code content restrictions"
        ]
      },
      "confidence": 0.98,
      "dependencies": ["step-00000000-0000-0000-0000-000000000001"],
      "previous_hash": "b8aad2c7c0fe87d7ab8afe1c24e46a98d1c19ae28d7fc3e9c53e62c7b2e8e564",
      "step_hash": "d9bbc2d8d1ff98e8bc9bff2d35f57ba9e2d2aabf3e8ed4faed64f73d3f9f9675",
      "signature": {
        "algorithm": "ECDSA-SHA256",
        "value": "MEQCIG8Ly5KCZa4k...",
        "public_key": "04a7b8c9d0e1f2...",
        "signer_id": "governance-agent-001",
        "signer_role": "compliance_checker"
      },
      "metadata": {
        "execution_time_ms": 187,
        "parallel_group": "checks"
      }
    },
    {
      "step_id": "step-00000000-0000-0000-0000-000000000003",
      "step_type": "trust_score_validation",
      "step_index": 2,
      "timestamp": "2026-05-11T14:30:00.498Z",
      "input": {
        "data": {
          "signal_id": "premium-cocktail-contexts",
          "claimed_trust_score": 0.88
        },
        "data_hash": "e4ddc3e53fc0a7e79d19d80f5c3b8d9e0a1fbb3c5da2e40d15e7f8a9b0c1d2e3",
        "sources": [
          "https://signals-api.opensignals.org/manifests/premium-cocktail-contexts",
          "https://trust-scorer.opensignals.org/scores"
        ]
      },
      "logic": {
        "rule_id": "trust_score_independent_validation_v1",
        "rule_description": "Independently recompute trust score and compare to claimed score",
        "algorithm": "trust_score_calculation_v0.1",
        "parameters": {
          "weights": {
            "coverage": 0.15,
            "freshness": 0.15,
            "precision": 0.25,
            "stability": 0.15,
            "explainability": 0.15,
            "compliance": 0.15
          }
        },
        "explanation": "I am independently verifying the trust score claimed in the signal manifest. I retrieved the signal manifest, extracted the trust dimension scores, and recomputed the overall score using OpenSignals v0.1 weighted average formula. This prevents trust score inflation attacks where a signal provider falsifies their score."
      },
      "output": {
        "result": "pass",
        "value": {
          "claimed_score": 0.88,
          "computed_score": 0.87,
          "delta": 0.01,
          "within_tolerance": true
        },
        "message": "Trust score validated. Computed score (0.87) matches claimed score (0.88) within acceptable tolerance (±0.02). Signal trust dimensions: coverage 0.89, freshness 0.95, precision 0.85, stability 0.91, explainability 0.82, compliance 0.80.",
        "evidence": [
          {
            "source": "https://signals-api.opensignals.org/manifests/premium-cocktail-contexts",
            "data": {
              "signal_id": "premium-cocktail-contexts",
              "trust_scores": {
                "coverage": 0.89,
                "freshness": 0.95,
                "precision": 0.85,
                "stability": 0.91,
                "explainability": 0.82,
                "compliance": 0.80,
                "overall": 0.88
              }
            },
            "timestamp": "2026-05-11T14:30:00.470Z"
          }
        ]
      },
      "confidence": 0.95,
      "dependencies": ["step-00000000-0000-0000-0000-000000000001"],
      "previous_hash": "b8aad2c7c0fe87d7ab8afe1c24e46a98d1c19ae28d7fc3e9c53e62c7b2e8e564",
      "step_hash": "f5eed4f54gg10f9fd0cbgg3e46g68cb0f3e3bbcg4f9fe5gfef75g84e4g0g0786",
      "signature": {
        "algorithm": "ECDSA-SHA256",
        "value": "MEUCIQDM9Nz6NCb5...",
        "public_key": "04a7b8c9d0e1f2...",
        "signer_id": "governance-agent-001",
        "signer_role": "trust_scorer"
      },
      "metadata": {
        "execution_time_ms": 312,
        "parallel_group": "checks"
      }
    },
    {
      "step_id": "step-00000000-0000-0000-0000-000000000004",
      "step_type": "category_compliance",
      "step_index": 3,
      "timestamp": "2026-05-11T14:30:00.623Z",
      "input": {
        "data": {
          "category": "alcohol",
          "signal_type": "contextual",
          "use_case": "targeting"
        },
        "data_hash": "a1bbc2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1",
        "sources": [
          "brand_policy_db",
          "https://signals-api.opensignals.org/manifests/premium-cocktail-contexts"
        ]
      },
      "logic": {
        "rule_id": "regulated_category_policy_v1",
        "rule_description": "Verify that regulated category (alcohol) complies with brand policy and requires appropriate approvals",
        "algorithm": "policy_compliance_check",
        "parameters": {
          "category": "alcohol",
          "required_approvals": ["human_review"],
          "prohibited_use_cases": ["individual_profiling", "sensitive_category_targeting"]
        },
        "explanation": "I am checking that this alcohol signal complies with OpenSignals policy for regulated categories. Alcohol is a sensitive category that requires human approval before activation. I verified the signal uses contextual targeting (not individual profiling), which is permitted. However, human review is mandatory regardless of trust score."
      },
      "output": {
        "result": "conditional",
        "value": {
          "compliant": true,
          "human_approval_required": true,
          "prohibited_use_cases_detected": false
        },
        "message": "Signal complies with regulated category policy. Uses contextual targeting (permitted). Human approval REQUIRED before activation due to alcohol category.",
        "evidence": [
          {
            "source": "brand_policy_db",
            "data": {
              "policy_id": "alcohol_targeting_policy_v2",
              "requires_human_approval": true,
              "permitted_signal_types": ["contextual", "geographic", "temporal"],
              "prohibited_signal_types": ["behavioral_profiling", "sensitive_attribute"]
            },
            "timestamp": "2026-05-11T14:30:00.610Z"
          }
        ],
        "recommendations": [
          "Route to human approval workflow",
          "Require compliance officer sign-off"
        ]
      },
      "confidence": 1.0,
      "dependencies": ["step-00000000-0000-0000-0000-000000000001"],
      "previous_hash": "b8aad2c7c0fe87d7ab8afe1c24e46a98d1c19ae28d7fc3e9c53e62c7b2e8e564",
      "step_hash": "b2ccd3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
      "signature": {
        "algorithm": "ECDSA-SHA256",
        "value": "MEQCIFjP0A7OCc8...",
        "public_key": "04a7b8c9d0e1f2...",
        "signer_id": "governance-agent-001",
        "signer_role": "compliance_checker"
      },
      "metadata": {
        "execution_time_ms": 145,
        "parallel_group": "checks"
      }
    },
    {
      "step_id": "step-00000000-0000-0000-0000-000000000005",
      "step_type": "provenance_check",
      "step_index": 4,
      "timestamp": "2026-05-11T14:30:00.789Z",
      "input": {
        "data": {
          "signal_id": "premium-cocktail-contexts",
          "provider_id": "contextual-signals-inc"
        },
        "data_hash": "c3dde4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3",
        "sources": [
          "https://signals-api.opensignals.org/manifests/premium-cocktail-contexts",
          "https://provenance-registry.opensignals.org/chains"
        ]
      },
      "logic": {
        "rule_id": "provenance_chain_verification_v1",
        "rule_description": "Verify data provenance chain and ensure data sources are legitimate",
        "algorithm": "chain_of_custody_validation",
        "parameters": {
          "max_chain_length": 5,
          "require_source_certification": true
        },
        "explanation": "I am verifying the provenance chain for this signal. I traced the data lineage from the signal back to its original data sources. The signal is derived from NLP analysis of premium food and beverage content. The data source (premium publisher content) is certified and the chain of custody is documented. No red flags detected."
      },
      "output": {
        "result": "pass",
        "value": {
          "provenance_verified": true,
          "chain_length": 2,
          "data_sources": ["premium_publisher_content"],
          "collection_method": "nlp_contextual_analysis",
          "certifications": ["TAG_Certified_Against_Fraud"]
        },
        "message": "Provenance verified. Signal derived from certified premium publisher content via NLP analysis. Chain of custody documented and validated.",
        "evidence": [
          {
            "source": "https://provenance-registry.opensignals.org/chains/premium-cocktail-contexts",
            "data": {
              "chain": [
                {
                  "stage": "data_collection",
                  "source": "premium_publishers",
                  "method": "content_ingestion",
                  "timestamp": "2026-05-10T00:00:00Z"
                },
                {
                  "stage": "signal_generation",
                  "processor": "nlp_engine_v3",
                  "method": "contextual_classification",
                  "timestamp": "2026-05-10T12:00:00Z"
                }
              ],
              "certifications": ["TAG_Certified_Against_Fraud"]
            },
            "timestamp": "2026-05-11T14:30:00.780Z"
          }
        ]
      },
      "confidence": 0.92,
      "dependencies": ["step-00000000-0000-0000-0000-000000000001"],
      "previous_hash": "b8aad2c7c0fe87d7ab8afe1c24e46a98d1c19ae28d7fc3e9c53e62c7b2e8e564",
      "step_hash": "d4ffe5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4",
      "signature": {
        "algorithm": "ECDSA-SHA256",
        "value": "MEUCIQCkR1B8PDf...",
        "public_key": "04a7b8c9d0e1f2...",
        "signer_id": "governance-agent-001",
        "signer_role": "governance_agent"
      },
      "metadata": {
        "execution_time_ms": 278,
        "parallel_group": "checks"
      }
    },
    {
      "step_id": "step-00000000-0000-0000-0000-000000000006",
      "step_type": "decision_synthesis",
      "step_index": 5,
      "timestamp": "2026-05-11T14:30:02.847Z",
      "input": {
        "data": {
          "previous_steps": [
            "step-00000000-0000-0000-0000-000000000001",
            "step-00000000-0000-0000-0000-000000000002",
            "step-00000000-0000-0000-0000-000000000003",
            "step-00000000-0000-0000-0000-000000000004",
            "step-00000000-0000-0000-0000-000000000005"
          ]
        },
        "data_hash": "e5aaf6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5",
        "sources": ["reasoning_steps_1_through_5"]
      },
      "logic": {
        "rule_id": "final_decision_synthesis_v1",
        "rule_description": "Synthesize final verification decision based on all reasoning steps",
        "algorithm": "decision_aggregation",
        "parameters": {
          "blocking_failures": 0,
          "conditional_results": 1,
          "warnings": 0
        },
        "explanation": "I am synthesizing the final verification decision by aggregating results from all reasoning steps. All critical checks passed: geographic restrictions OK, trust score validated, provenance verified. However, step 4 (category compliance) requires human approval because this is a regulated alcohol category. Therefore, my final decision is 'approved_with_conditions' where the condition is mandatory human review before activation."
      },
      "output": {
        "result": "conditional",
        "value": {
          "decision": "approved_with_conditions",
          "conditions": [
            {
              "condition_id": "human_approval_required",
              "description": "Human approval required due to alcohol regulated category",
              "type": "human_review",
              "severity": "mandatory"
            }
          ],
          "trust_score": 0.87,
          "all_checks_passed": false,
          "blocking_issues": 0,
          "conditional_issues": 1
        },
        "message": "Signal APPROVED WITH CONDITIONS. All technical and compliance checks passed. Trust score validated at 0.87 (Trusted tier). However, mandatory human approval required due to alcohol category per OpenSignals regulated category policy. Route to compliance officer for final sign-off.",
        "evidence": [
          {
            "source": "reasoning_chain_aggregation",
            "data": {
              "step_results": {
                "input_validation": "pass",
                "geographic_check": "pass",
                "trust_score_validation": "pass",
                "category_compliance": "conditional",
                "provenance_check": "pass"
              },
              "blocking_count": 0,
              "conditional_count": 1
            },
            "timestamp": "2026-05-11T14:30:02.845Z"
          }
        ],
        "recommendations": [
          "Send to human approval workflow",
          "Include full reasoning chain for reviewer context",
          "Require compliance officer or legal counsel approval"
        ]
      },
      "confidence": 0.94,
      "dependencies": [
        "step-00000000-0000-0000-0000-000000000001",
        "step-00000000-0000-0000-0000-000000000002",
        "step-00000000-0000-0000-0000-000000000003",
        "step-00000000-0000-0000-0000-000000000004",
        "step-00000000-0000-0000-0000-000000000005"
      ],
      "previous_hash": "d4ffe5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4",
      "step_hash": "f6bb07b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6",
      "signature": {
        "algorithm": "ECDSA-SHA256",
        "value": "MEYCIQD3Tp2FRHh...",
        "public_key": "04a7b8c9d0e1f2...",
        "signer_id": "governance-agent-001",
        "signer_role": "governance_agent"
      },
      "metadata": {
        "execution_time_ms": 95,
        "parallel_group": "synthesis"
      }
    }
  ],
  "final_decision": {
    "decision": "approved_with_conditions",
    "decision_confidence": 0.94,
    "trust_score": 0.87,
    "conditions": [
      {
        "condition_id": "human_approval_alcohol_category",
        "description": "Human approval required: Signal targets alcohol category in GB market. Requires compliance officer or legal counsel sign-off per regulated category policy.",
        "type": "human_review",
        "severity": "mandatory",
        "enforcement": "manual"
      }
    ],
    "synthesis_explanation": "After executing 6 reasoning steps with cryptographic signing, I have determined this signal should be APPROVED WITH CONDITIONS. Here's my chain of reasoning:\n\n1. INPUT VALIDATION: The verification request was well-formed and complete (confidence: 1.0)\n2. GEOGRAPHIC CHECK: Alcohol advertising is permitted in GB for adults 18+ under UK CAP Code (confidence: 0.98)\n3. TRUST SCORE: Independently validated trust score of 0.87 matches manifest claim within tolerance (confidence: 0.95)\n4. CATEGORY COMPLIANCE: Signal uses contextual targeting (permitted), but requires mandatory human approval due to alcohol category (confidence: 1.0)\n5. PROVENANCE: Data lineage verified from certified premium publisher content (confidence: 0.92)\n6. DECISION SYNTHESIS: All technical checks passed, one mandatory condition imposed (confidence: 0.94)\n\nThe signal meets all technical and compliance criteria for activation. However, OpenSignals policy requires human review for all alcohol category signals regardless of trust score. This decision cannot be made autonomously. The signal should be routed to a compliance officer or legal counsel for final approval before activation."
  },
  "chain_signature": {
    "algorithm": "ECDSA-SHA256",
    "value": "MEUCIQD8UsZ3QIf9k7L...",
    "chain_hash": "a8bb18c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7",
    "public_key": "04a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7",
    "signer_id": "governance-agent-001",
    "signer_role": "primary_verifier"
  },
  "co_signatures": [],
  "transparency_level": "full_transparency",
  "storage_reference": {
    "storage_type": "centralized_db",
    "reference": "reasoning_chains/550e8400-e29b-41d4-a716-446655440000",
    "retrieval_endpoint": "https://audit.opensignals.org/api/v1/chains/550e8400-e29b-41d4-a716-446655440000"
  },
  "audit_metadata": {
    "compliance_frameworks": ["OpenSignals_v0.1", "UK_CAP_Code", "GDPR"],
    "retention_until": "2027-05-11T14:30:02.847Z",
    "jurisdiction": ["GB"],
    "human_reviewers": []
  },
  "metadata": {
    "protocol_version": "0.1",
    "cota_version": "0.1",
    "total_execution_time_ms": 2847,
    "step_count": 6,
    "parallel_steps": 4
  }
}
```

### 6.2 Human Approval Step (Co-Signature)

After human review, a co-signature is added:

```json
{
  "co_signatures": [
    {
      "signer_id": "jane.smith@premium-spirits-co.com",
      "signer_role": "compliance_officer",
      "signature": "MEUCIQCvN4R9SKg...",
      "public_key": "04b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8",
      "attestation": "I have reviewed the reasoning chain for signal 'premium-cocktail-contexts' and approve its activation for the GB market campaign. The signal meets UK CAP Code requirements for alcohol advertising. Approved for contextual targeting only with age 18+ restriction.",
      "timestamp": "2026-05-11T15:15:00.000Z",
      "approval_decision": "approved",
      "approval_notes": "Signal is compliant with UK alcohol advertising regulations. Verified contextual targeting methodology does not involve individual profiling. Recommend proceeding with activation."
    }
  ]
}
```

---

## 7. Python Implementation

### 7.1 Core CoTA Engine

```python
"""
Chain-of-Thought Authentication Engine for OpenSignals
Implements cryptographically signed reasoning chains for signal verification
"""

import hashlib
import json
import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature
import base64


class StepType(Enum):
    """Types of reasoning steps in a CoTA chain"""
    INPUT_VALIDATION = "input_validation"
    GEOGRAPHIC_CHECK = "geographic_check"
    CATEGORY_COMPLIANCE = "category_compliance"
    TRUST_SCORE_VALIDATION = "trust_score_validation"
    CONSENT_VERIFICATION = "consent_verification"
    PROVENANCE_CHECK = "provenance_check"
    POLICY_ENFORCEMENT = "policy_enforcement"
    RISK_ASSESSMENT = "risk_assessment"
    DECISION_SYNTHESIS = "decision_synthesis"
    CUSTOM = "custom"


class StepResult(Enum):
    """Possible outcomes of a reasoning step"""
    PASS = "pass"
    FAIL = "fail"
    WARNING = "warning"
    INFO = "info"
    CONDITIONAL = "conditional"


class Decision(Enum):
    """Final verification decisions"""
    APPROVED = "approved"
    APPROVED_WITH_CONDITIONS = "approved_with_conditions"
    BLOCKED = "blocked"
    REQUIRES_REVIEW = "requires_review"
    ERROR = "error"


@dataclass
class ReasoningStep:
    """A single step in a chain-of-thought reasoning process"""
    step_id: str
    step_type: StepType
    step_index: int
    timestamp: str
    input_data: Dict[str, Any]
    input_data_hash: str
    logic_rule_id: str
    logic_explanation: str
    logic_algorithm: str
    output_result: StepResult
    output_message: str
    output_value: Any
    confidence: float
    previous_hash: str
    step_hash: str = ""
    signature: Optional[Dict[str, Any]] = None
    evidence: List[Dict[str, Any]] = None
    dependencies: List[str] = None
    metadata: Dict[str, Any] = None

    def __post_init__(self):
        if self.evidence is None:
            self.evidence = []
        if self.dependencies is None:
            self.dependencies = []
        if self.metadata is None:
            self.metadata = {}

    def to_dict(self) -> Dict[str, Any]:
        """Convert step to dictionary for serialization"""
        step_dict = {
            "step_id": self.step_id,
            "step_type": self.step_type.value,
            "step_index": self.step_index,
            "timestamp": self.timestamp,
            "input": {
                "data_hash": self.input_data_hash,
                "sources": self.input_data.get("sources", [])
            },
            "logic": {
                "rule_id": self.logic_rule_id,
                "explanation": self.logic_explanation,
                "algorithm": self.logic_algorithm
            },
            "output": {
                "result": self.output_result.value,
                "message": self.output_message,
                "value": self.output_value,
                "evidence": self.evidence
            },
            "confidence": self.confidence,
            "dependencies": self.dependencies,
            "previous_hash": self.previous_hash,
            "step_hash": self.step_hash,
            "metadata": self.metadata
        }

        if self.signature:
            step_dict["signature"] = self.signature

        return step_dict

    def compute_hash(self) -> str:
        """Compute SHA-256 hash of step content (excluding signature)"""
        step_dict = self.to_dict()
        step_dict.pop("signature", None)  # Exclude signature from hash
        step_dict.pop("step_hash", None)  # Exclude self-hash

        # Canonical JSON representation
        canonical_json = json.dumps(step_dict, sort_keys=True, separators=(',', ':'))
        return hashlib.sha256(canonical_json.encode()).hexdigest()


@dataclass
class ReasoningChain:
    """Complete chain of reasoning steps for a verification decision"""
    chain_id: str
    signal_id: str
    verification_request_id: str
    timestamp_start: str
    timestamp_end: str
    input_hash: str
    steps: List[ReasoningStep]
    final_decision: Decision
    final_decision_explanation: str
    decision_confidence: float
    trust_score: float
    conditions: List[Dict[str, Any]]
    chain_signature: Optional[Dict[str, Any]] = None
    co_signatures: List[Dict[str, Any]] = None
    transparency_level: str = "full_transparency"
    metadata: Dict[str, Any] = None

    def __post_init__(self):
        if self.co_signatures is None:
            self.co_signatures = []
        if self.metadata is None:
            self.metadata = {}

    def to_dict(self) -> Dict[str, Any]:
        """Convert chain to dictionary for serialization"""
        return {
            "chain_id": self.chain_id,
            "signal_id": self.signal_id,
            "verification_request_id": self.verification_request_id,
            "timestamp_start": self.timestamp_start,
            "timestamp_end": self.timestamp_end,
            "input_hash": self.input_hash,
            "steps": [step.to_dict() for step in self.steps],
            "final_decision": {
                "decision": self.final_decision.value,
                "decision_confidence": self.decision_confidence,
                "trust_score": self.trust_score,
                "conditions": self.conditions,
                "synthesis_explanation": self.final_decision_explanation
            },
            "chain_signature": self.chain_signature,
            "co_signatures": self.co_signatures,
            "transparency_level": self.transparency_level,
            "metadata": self.metadata
        }

    def compute_chain_hash(self) -> str:
        """Compute Merkle root of all step hashes"""
        step_hashes = [step.step_hash for step in self.steps]

        # Build Merkle tree
        while len(step_hashes) > 1:
            if len(step_hashes) % 2 == 1:
                step_hashes.append(step_hashes[-1])  # Duplicate last if odd

            next_level = []
            for i in range(0, len(step_hashes), 2):
                combined = step_hashes[i] + step_hashes[i + 1]
                next_level.append(hashlib.sha256(combined.encode()).hexdigest())
            step_hashes = next_level

        return step_hashes[0] if step_hashes else ""


class CotaEngine:
    """Chain-of-Thought Authentication Engine"""

    def __init__(self, signer_id: str, private_key_pem: Optional[bytes] = None):
        """
        Initialize CoTA engine

        Args:
            signer_id: Identifier of the agent/system doing verification
            private_key_pem: PEM-encoded ECDSA private key (generates new if None)
        """
        self.signer_id = signer_id

        if private_key_pem:
            self.private_key = serialization.load_pem_private_key(
                private_key_pem, password=None
            )
        else:
            # Generate new ECDSA key pair
            self.private_key = ec.generate_private_key(ec.SECP256R1())

        self.public_key = self.private_key.public_key()
        self.public_key_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode()

    def compute_input_hash(self, input_data: Dict[str, Any]) -> str:
        """Compute SHA-256 hash of input data"""
        canonical_json = json.dumps(input_data, sort_keys=True, separators=(',', ':'))
        return hashlib.sha256(canonical_json.encode()).hexdigest()

    def sign_data(self, data: str) -> str:
        """Sign data with ECDSA private key"""
        signature_bytes = self.private_key.sign(
            data.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        return base64.b64encode(signature_bytes).decode()

    def verify_signature(self, data: str, signature: str, public_key_pem: str) -> bool:
        """Verify ECDSA signature"""
        try:
            public_key = serialization.load_pem_public_key(public_key_pem.encode())
            signature_bytes = base64.b64decode(signature)
            public_key.verify(
                signature_bytes,
                data.encode(),
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except (InvalidSignature, Exception):
            return False

    def create_reasoning_chain(
        self,
        signal_id: str,
        verification_request_id: str,
        input_data: Dict[str, Any]
    ) -> ReasoningChain:
        """Initialize a new reasoning chain"""
        chain_id = str(uuid.uuid4())
        timestamp_start = datetime.now(timezone.utc).isoformat()
        input_hash = self.compute_input_hash(input_data)

        return ReasoningChain(
            chain_id=chain_id,
            signal_id=signal_id,
            verification_request_id=verification_request_id,
            timestamp_start=timestamp_start,
            timestamp_end="",
            input_hash=input_hash,
            steps=[],
            final_decision=Decision.APPROVED,  # Placeholder
            final_decision_explanation="",
            decision_confidence=0.0,
            trust_score=0.0,
            conditions=[],
            metadata={
                "protocol_version": "0.1",
                "cota_version": "0.1",
                "signer_id": self.signer_id
            }
        )

    def add_reasoning_step(
        self,
        chain: ReasoningChain,
        step_type: StepType,
        input_data: Dict[str, Any],
        logic_rule_id: str,
        logic_explanation: str,
        logic_algorithm: str,
        output_result: StepResult,
        output_message: str,
        output_value: Any,
        confidence: float,
        evidence: Optional[List[Dict[str, Any]]] = None,
        dependencies: Optional[List[str]] = None
    ) -> ReasoningStep:
        """
        Add a reasoning step to the chain and sign it

        Args:
            chain: The reasoning chain to add to
            step_type: Type of reasoning step
            input_data: Input data for this step
            logic_rule_id: ID of rule/policy applied
            logic_explanation: Human-readable explanation of reasoning
            logic_algorithm: Algorithm/method used
            output_result: Result of step (pass/fail/etc)
            output_message: Human-readable result message
            output_value: Computed value
            confidence: Confidence in result (0-1)
            evidence: Supporting evidence
            dependencies: IDs of steps this depends on

        Returns:
            The signed reasoning step
        """
        step_id = str(uuid.uuid4())
        step_index = len(chain.steps)
        timestamp = datetime.now(timezone.utc).isoformat()
        input_data_hash = self.compute_input_hash(input_data)

        # Previous hash is either the last step's hash or the input hash
        if step_index == 0:
            previous_hash = chain.input_hash
        else:
            previous_hash = chain.steps[-1].step_hash

        step = ReasoningStep(
            step_id=step_id,
            step_type=step_type,
            step_index=step_index,
            timestamp=timestamp,
            input_data=input_data,
            input_data_hash=input_data_hash,
            logic_rule_id=logic_rule_id,
            logic_explanation=logic_explanation,
            logic_algorithm=logic_algorithm,
            output_result=output_result,
            output_message=output_message,
            output_value=output_value,
            confidence=confidence,
            previous_hash=previous_hash,
            evidence=evidence or [],
            dependencies=dependencies or []
        )

        # Compute step hash
        step.step_hash = step.compute_hash()

        # Sign the step hash
        signature_value = self.sign_data(step.step_hash)
        step.signature = {
            "algorithm": "ECDSA-SHA256",
            "value": signature_value,
            "public_key": self.public_key_pem,
            "signer_id": self.signer_id,
            "signer_role": "governance_agent"
        }

        # Add to chain
        chain.steps.append(step)

        return step

    def finalize_chain(
        self,
        chain: ReasoningChain,
        final_decision: Decision,
        decision_explanation: str,
        decision_confidence: float,
        trust_score: float,
        conditions: Optional[List[Dict[str, Any]]] = None
    ) -> ReasoningChain:
        """
        Finalize reasoning chain with decision and sign the complete chain

        Args:
            chain: The chain to finalize
            final_decision: Final verification decision
            decision_explanation: Explanation of how decision was reached
            decision_confidence: Confidence in decision
            trust_score: Computed trust score
            conditions: Conditions attached to decision

        Returns:
            The finalized and signed chain
        """
        chain.timestamp_end = datetime.now(timezone.utc).isoformat()
        chain.final_decision = final_decision
        chain.final_decision_explanation = decision_explanation
        chain.decision_confidence = decision_confidence
        chain.trust_score = trust_score
        chain.conditions = conditions or []

        # Compute execution time
        start = datetime.fromisoformat(chain.timestamp_start.replace('Z', '+00:00'))
        end = datetime.fromisoformat(chain.timestamp_end.replace('Z', '+00:00'))
        execution_time_ms = int((end - start).total_seconds() * 1000)

        chain.metadata.update({
            "total_execution_time_ms": execution_time_ms,
            "step_count": len(chain.steps)
        })

        # Compute chain hash (Merkle root of all steps)
        chain_hash = chain.compute_chain_hash()

        # Sign the chain hash
        chain_signature_value = self.sign_data(chain_hash)
        chain.chain_signature = {
            "algorithm": "ECDSA-SHA256",
            "value": chain_signature_value,
            "chain_hash": chain_hash,
            "public_key": self.public_key_pem,
            "signer_id": self.signer_id,
            "signer_role": "primary_verifier"
        }

        return chain

    def verify_chain(self, chain: ReasoningChain) -> Tuple[bool, List[str]]:
        """
        Verify integrity of a reasoning chain

        Args:
            chain: The chain to verify

        Returns:
            Tuple of (is_valid, list of errors)
        """
        errors = []

        # Verify each step
        for i, step in enumerate(chain.steps):
            # Verify step hash
            computed_hash = step.compute_hash()
            if computed_hash != step.step_hash:
                errors.append(f"Step {i} hash mismatch")

            # Verify step signature
            if step.signature:
                is_valid = self.verify_signature(
                    step.step_hash,
                    step.signature["value"],
                    step.signature["public_key"]
                )
                if not is_valid:
                    errors.append(f"Step {i} signature invalid")
            else:
                errors.append(f"Step {i} missing signature")

            # Verify chain linkage
            if i == 0:
                if step.previous_hash != chain.input_hash:
                    errors.append(f"Step 0 previous_hash doesn't match input_hash")
            else:
                if step.previous_hash != chain.steps[i-1].step_hash:
                    errors.append(f"Step {i} previous_hash doesn't link to step {i-1}")

        # Verify chain signature
        if chain.chain_signature:
            computed_chain_hash = chain.compute_chain_hash()
            if computed_chain_hash != chain.chain_signature["chain_hash"]:
                errors.append("Chain hash mismatch")

            is_valid = self.verify_signature(
                chain.chain_signature["chain_hash"],
                chain.chain_signature["value"],
                chain.chain_signature["public_key"]
            )
            if not is_valid:
                errors.append("Chain signature invalid")
        else:
            errors.append("Chain signature missing")

        return (len(errors) == 0, errors)

    def add_co_signature(
        self,
        chain: ReasoningChain,
        co_signer_id: str,
        co_signer_role: str,
        attestation: str,
        private_key_pem: bytes
    ) -> Dict[str, Any]:
        """
        Add a co-signature from another verifier (e.g., human approver)

        Args:
            chain: The chain to co-sign
            co_signer_id: ID of co-signer
            co_signer_role: Role of co-signer
            attestation: What the co-signer is attesting to
            private_key_pem: Co-signer's private key

        Returns:
            The co-signature object
        """
        # Load co-signer's key
        private_key = serialization.load_pem_private_key(private_key_pem, password=None)
        public_key = private_key.public_key()
        public_key_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode()

        # Sign the chain hash
        chain_hash = chain.chain_signature["chain_hash"]
        signature_bytes = private_key.sign(
            chain_hash.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        signature_value = base64.b64encode(signature_bytes).decode()

        co_signature = {
            "signer_id": co_signer_id,
            "signer_role": co_signer_role,
            "signature": signature_value,
            "public_key": public_key_pem,
            "attestation": attestation,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        chain.co_signatures.append(co_signature)

        return co_signature


# Example usage
if __name__ == "__main__":
    # Initialize CoTA engine
    engine = CotaEngine(signer_id="governance-agent-001")

    # Create reasoning chain
    input_data = {
        "signal_id": "premium-cocktail-contexts",
        "requestor": {"organization_id": "premium-spirits-co"},
        "context": {"geographic_scope": ["GB"], "category": "alcohol"}
    }

    chain = engine.create_reasoning_chain(
        signal_id="premium-cocktail-contexts",
        verification_request_id=str(uuid.uuid4()),
        input_data=input_data
    )

    # Add reasoning steps
    engine.add_reasoning_step(
        chain=chain,
        step_type=StepType.GEOGRAPHIC_CHECK,
        input_data={"geographic_scope": ["GB"], "category": "alcohol"},
        logic_rule_id="alcohol_geographic_restriction_v2",
        logic_explanation="Checking if alcohol advertising is permitted in GB",
        logic_algorithm="geographic_policy_lookup",
        output_result=StepResult.PASS,
        output_message="Alcohol permitted in GB for 18+",
        output_value={"permitted": True, "age_restriction": 18},
        confidence=0.98
    )

    # Finalize chain
    engine.finalize_chain(
        chain=chain,
        final_decision=Decision.APPROVED_WITH_CONDITIONS,
        decision_explanation="Signal approved pending human review",
        decision_confidence=0.94,
        trust_score=0.87,
        conditions=[{"condition_id": "human_approval_required"}]
    )

    # Verify chain
    is_valid, errors = engine.verify_chain(chain)
    print(f"Chain valid: {is_valid}")
    if errors:
        print(f"Errors: {errors}")

    # Export chain
    chain_json = json.dumps(chain.to_dict(), indent=2)
    print(f"Chain: {chain_json[:500]}...")
```

### 7.2 Integration Helper Functions

```python
"""
Helper functions for integrating CoTA with OpenSignals verify_signal task
"""

from typing import Dict, Any, Optional
import asyncio


class CotaVerificationEngine:
    """High-level verification engine using CoTA"""

    def __init__(self, cota_engine: CotaEngine):
        self.cota = cota_engine
        self.compliance_api = ComplianceAPI()  # Placeholder
        self.trust_scorer = TrustScorer()  # Placeholder

    async def verify_signal_with_cota(
        self,
        verification_request: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Execute full signal verification with chain-of-thought authentication

        Args:
            verification_request: The verify_signal request payload

        Returns:
            Verification response with embedded reasoning chain
        """
        # Initialize chain
        chain = self.cota.create_reasoning_chain(
            signal_id=verification_request["signal_id"],
            verification_request_id=verification_request["request_id"],
            input_data=verification_request
        )

        # Step 1: Input validation
        self.cota.add_reasoning_step(
            chain=chain,
            step_type=StepType.INPUT_VALIDATION,
            input_data={"request": verification_request},
            logic_rule_id="input_validation_v1",
            logic_explanation="Validating that verification request is well-formed",
            logic_algorithm="json_schema_validation",
            output_result=StepResult.PASS,
            output_message="Request valid",
            output_value=True,
            confidence=1.0
        )

        # Execute parallel checks
        geographic_task = self._check_geographic_restrictions(chain, verification_request)
        trust_task = self._validate_trust_score(chain, verification_request)
        provenance_task = self._verify_provenance(chain, verification_request)
        compliance_task = self._check_category_compliance(chain, verification_request)

        await asyncio.gather(
            geographic_task,
            trust_task,
            provenance_task,
            compliance_task
        )

        # Synthesize decision
        final_decision, explanation, confidence, conditions = self._synthesize_decision(chain)

        # Finalize chain
        trust_score = self._extract_trust_score(chain)
        self.cota.finalize_chain(
            chain=chain,
            final_decision=final_decision,
            decision_explanation=explanation,
            decision_confidence=confidence,
            trust_score=trust_score,
            conditions=conditions
        )

        # Build response
        return self._build_verification_response(chain)

    async def _check_geographic_restrictions(
        self,
        chain: ReasoningChain,
        request: Dict[str, Any]
    ):
        """Execute geographic restrictions check"""
        geographic_scope = request["context"]["geographic_scope"]
        category = request["context"]["campaign_details"].get("policy_sensitive_categories", ["none"])[0]

        # Query compliance API (mock)
        result = await self.compliance_api.check_geographic_permission(
            markets=geographic_scope,
            category=category
        )

        self.cota.add_reasoning_step(
            chain=chain,
            step_type=StepType.GEOGRAPHIC_CHECK,
            input_data={"markets": geographic_scope, "category": category},
            logic_rule_id=f"{category}_geographic_restriction_v2",
            logic_explanation=f"Checking if {category} advertising is permitted in {geographic_scope}",
            logic_algorithm="geographic_policy_lookup",
            output_result=StepResult.PASS if result["permitted"] else StepResult.FAIL,
            output_message=result["message"],
            output_value=result,
            confidence=0.98,
            evidence=[{
                "source": "compliance_api",
                "data": result,
                "timestamp": datetime.now(timezone.utc).isoformat()
            }]
        )

    async def _validate_trust_score(
        self,
        chain: ReasoningChain,
        request: Dict[str, Any]
    ):
        """Independently validate trust score"""
        signal_id = request["signal_id"]

        # Fetch manifest and recompute score
        manifest = await self.trust_scorer.fetch_manifest(signal_id)
        computed_score = await self.trust_scorer.compute_trust_score(manifest)
        claimed_score = manifest["quality"]["overall_trust_score"]

        delta = abs(computed_score - claimed_score)
        within_tolerance = delta <= 0.02

        self.cota.add_reasoning_step(
            chain=chain,
            step_type=StepType.TRUST_SCORE_VALIDATION,
            input_data={"signal_id": signal_id, "claimed_score": claimed_score},
            logic_rule_id="trust_score_independent_validation_v1",
            logic_explanation="Independently recomputing trust score to prevent manipulation",
            logic_algorithm="trust_score_calculation_v0.1",
            output_result=StepResult.PASS if within_tolerance else StepResult.FAIL,
            output_message=f"Score {'validated' if within_tolerance else 'mismatch'}: claimed {claimed_score}, computed {computed_score}",
            output_value={
                "claimed_score": claimed_score,
                "computed_score": computed_score,
                "delta": delta,
                "within_tolerance": within_tolerance
            },
            confidence=0.95
        )

    async def _verify_provenance(
        self,
        chain: ReasoningChain,
        request: Dict[str, Any]
    ):
        """Verify data provenance chain"""
        # Implementation similar to above
        pass

    async def _check_category_compliance(
        self,
        chain: ReasoningChain,
        request: Dict[str, Any]
    ):
        """Check regulated category compliance"""
        # Implementation similar to above
        pass

    def _synthesize_decision(
        self,
        chain: ReasoningChain
    ) -> Tuple[Decision, str, float, List[Dict]]:
        """Synthesize final decision from all reasoning steps"""
        # Count pass/fail/conditional results
        results = [step.output_result for step in chain.steps]

        fail_count = results.count(StepResult.FAIL)
        conditional_count = results.count(StepResult.CONDITIONAL)

        if fail_count > 0:
            decision = Decision.BLOCKED
            explanation = "One or more critical checks failed"
            confidence = 0.99
            conditions = []
        elif conditional_count > 0:
            decision = Decision.APPROVED_WITH_CONDITIONS
            explanation = "All checks passed but conditions apply"
            confidence = 0.94
            conditions = [{"condition_id": "human_approval_required"}]
        else:
            decision = Decision.APPROVED
            explanation = "All checks passed"
            confidence = 0.99
            conditions = []

        return decision, explanation, confidence, conditions

    def _extract_trust_score(self, chain: ReasoningChain) -> float:
        """Extract trust score from trust validation step"""
        for step in chain.steps:
            if step.step_type == StepType.TRUST_SCORE_VALIDATION:
                return step.output_value.get("computed_score", 0.0)
        return 0.0

    def _build_verification_response(
        self,
        chain: ReasoningChain
    ) -> Dict[str, Any]:
        """Build standard verify_signal response with embedded CoTA chain"""
        return {
            "request_id": chain.verification_request_id,
            "response_id": str(uuid.uuid4()),
            "timestamp": chain.timestamp_end,
            "signal_id": chain.signal_id,
            "decision": chain.final_decision.value,
            "decision_confidence": chain.decision_confidence,
            "trust_score": chain.trust_score,
            "conditions": chain.conditions,
            "cota_reasoning_chain": {
                "chain_id": chain.chain_id,
                "chain_hash": chain.chain_signature["chain_hash"],
                "chain_signature": chain.chain_signature,
                "storage_reference": {
                    "storage_type": "centralized_db",
                    "retrieval_endpoint": f"https://audit.opensignals.org/api/v1/chains/{chain.chain_id}"
                },
                "step_count": len(chain.steps),
                "transparency_level": chain.transparency_level
            },
            "reasoning_summary": chain.final_decision_explanation
        }


# Placeholder classes
class ComplianceAPI:
    async def check_geographic_permission(self, markets, category):
        return {"permitted": True, "message": "Allowed"}

class TrustScorer:
    async def fetch_manifest(self, signal_id):
        return {"quality": {"overall_trust_score": 0.87}}

    async def compute_trust_score(self, manifest):
        return 0.87
```

---

## 8. Integration with verify_signal

### 8.1 Modified verify_signal Task

The existing `verify_signal` task is enhanced to return a CoTA reasoning chain:

**Before (traditional)**:
```json
{
  "request_id": "...",
  "signal_id": "...",
  "decision": "approved",
  "trust_score": 0.87,
  "signature": "..."
}
```

**After (with CoTA)**:
```json
{
  "request_id": "...",
  "signal_id": "...",
  "decision": "approved_with_conditions",
  "trust_score": 0.87,
  "decision_confidence": 0.94,
  "conditions": [...],
  "cota_reasoning_chain": {
    "chain_id": "550e8400-e29b-41d4-a716-446655440000",
    "chain_hash": "a8bb18c9d0e1f2...",
    "chain_signature": {
      "algorithm": "ECDSA-SHA256",
      "value": "MEUCIQD8UsZ3QIf...",
      "public_key": "04a7b8c9d0e1f2...",
      "signer_id": "governance-agent-001"
    },
    "storage_reference": {
      "storage_type": "centralized_db",
      "retrieval_endpoint": "https://audit.opensignals.org/api/v1/chains/550e8400-..."
    },
    "step_count": 6,
    "transparency_level": "full_transparency"
  },
  "reasoning_summary": "After executing 6 reasoning steps with cryptographic signing, I have determined this signal should be APPROVED WITH CONDITIONS. Here's my chain of reasoning: ..."
}
```

### 8.2 Retrieving Full Reasoning Chain

Clients can retrieve the full reasoning chain for audit:

```python
import requests

# Get verification response
verify_response = opensignals_client.verify_signal(request)

# Extract chain reference
chain_id = verify_response["cota_reasoning_chain"]["chain_id"]
retrieval_url = verify_response["cota_reasoning_chain"]["storage_reference"]["retrieval_endpoint"]

# Fetch full chain
full_chain = requests.get(
    retrieval_url,
    headers={"Authorization": f"Bearer {audit_token}"}
).json()

# Verify chain integrity
cota_engine = CotaEngine(signer_id="auditor")
is_valid, errors = cota_engine.verify_chain(ReasoningChain(**full_chain))

if is_valid:
    print("Chain is cryptographically valid")
    # Examine reasoning
    for step in full_chain["steps"]:
        print(f"Step {step['step_index']}: {step['logic']['explanation']}")
        print(f"Result: {step['output']['message']}")
else:
    print(f"Chain invalid: {errors}")
```

---

## 9. Multi-Party Verification

### 9.1 Concept

Multiple independent agents can co-sign a verification decision, providing stronger attestation:

```
Primary Verifier (Governance Agent)
    ↓ [signs reasoning chain]
Co-Signer 1 (Trust Scoring Service)
    ↓ [signs chain hash]
Co-Signer 2 (Human Compliance Officer)
    ↓ [signs chain hash]
Co-Signer 3 (Independent Auditor)
    ↓ [signs chain hash]

→ Multi-party attested decision
```

### 9.2 Use Cases

**Use Case 1: High-Value Campaigns**
- Primary: Governance agent verifies signal
- Co-Signer 1: Human compliance officer approves
- Co-Signer 2: Brand legal counsel approves
- Threshold: Requires 2/3 co-signatures for activation

**Use Case 2: Regulated Categories**
- Primary: Governance agent verifies signal
- Co-Signer 1: Category specialist (alcohol compliance expert)
- Co-Signer 2: Market-specific regulator representative
- Threshold: Requires all co-signatures

**Use Case 3: Cross-Organization Collaboration**
- Primary: Advertiser's governance agent
- Co-Signer 1: Agency's governance agent
- Co-Signer 2: Publisher's trust & safety team
- Threshold: All parties must agree

### 9.3 Implementation

```python
# Primary verification
chain = verification_engine.verify_signal_with_cota(request)

# Co-signature 1: Human approver
human_signature = cota_engine.add_co_signature(
    chain=chain,
    co_signer_id="jane.smith@brand.com",
    co_signer_role="compliance_officer",
    attestation="I approve this signal for activation per brand policy",
    private_key_pem=load_human_private_key()
)

# Co-signature 2: Independent auditor
auditor_signature = cota_engine.add_co_signature(
    chain=chain,
    co_signer_id="auditor-service-001",
    co_signer_role="independent_auditor",
    attestation="I have reviewed the reasoning and attest it follows proper procedure",
    private_key_pem=load_auditor_private_key()
)

# Verification requires 2/2 co-signatures
required_co_signatures = 2
if len(chain.co_signatures) >= required_co_signatures:
    # Activate signal
    activate_signal(chain)
else:
    # Wait for additional co-signatures
    queue_for_additional_approval(chain)
```

---

## 10. Attack Resistance

### 10.1 Attack Vectors and Defenses

| Attack | Traditional Auth | CoTA Defense |
|--------|------------------|--------------|
| **Trust Score Inflation** | Attacker falsifies trust score before signing | CoTA independently recomputes score in signed step. Any manipulation breaks chain. |
| **Reasoning Spoofing** | Attacker claims "GDPR compliant" without checking | CoTA requires explicit reasoning step showing GDPR check. Missing step = invalid chain. |
| **Retroactive Forgery** | Attacker changes reasoning after incident | CoTA reasoning is signed and stored immutably. Timestamped blockchain prevents backdating. |
| **Compliance Bypass** | Attacker skips human approval | CoTA encodes human approval as mandatory step. Missing co-signature = blocked. |
| **Step Injection** | Attacker inserts fake reasoning step | Each step links cryptographically to previous. Injection breaks hash chain. |
| **Signature Replay** | Attacker reuses old signature | Each signature includes timestamp and chain-specific input hash. Replay detected. |
| **Partial Chain Disclosure** | Attacker hides unfavorable reasoning | Merkle tree ensures any missing step breaks chain verification. |
| **Signer Impersonation** | Attacker uses stolen private key | Key rotation and certificate pinning limit exposure. Multi-party reduces single point of failure. |

### 10.2 Example: Preventing Trust Score Manipulation

**Attack Scenario**:
```
Attacker: Submits signal with trust_score: 0.95 (fake)
Traditional System:
  1. Checks if score > 0.8 ✓
  2. Signs decision ✓
  3. Approves signal ✓
  RESULT: Low-quality signal activated
```

**CoTA Defense**:
```
Attacker: Submits signal with trust_score: 0.95 (fake)
CoTA System:
  1. Receives request
  2. STEP 1: Input validation [signed]
  3. STEP 2: Fetch signal manifest from provider API
  4. STEP 3: Independently recompute trust score
     - Actual score: 0.62 (not 0.95)
     - Delta: 0.33 (exceeds tolerance)
     - Result: FAIL
     - Message: "Trust score mismatch. Claimed 0.95, computed 0.62. Possible manipulation."
     - [This step is cryptographically signed]
  5. STEP 4: Decision synthesis
     - Blocking issue detected
     - Decision: BLOCKED
     - [This step is signed]
  6. Finalize chain with BLOCKED decision [chain signed]

  RESULT: Signal blocked, full reasoning trail proves why
```

The attacker cannot:
- Skip step 3 (hash chain would break)
- Modify step 3 result (signature would be invalid)
- Fake step 3 signature (requires private key)
- Remove step 3 from audit trail (Merkle tree would break)

### 10.3 Example: Preventing Compliance Bypass

**Attack Scenario**:
```
Attacker: Submits alcohol signal, claims "approved without human review"
Traditional System:
  1. Checks trust score ✓
  2. Checks geographic permission ✓
  3. Signs decision ✓
  RESULT: Regulated signal activated without required approval
```

**CoTA Defense**:
```
Attacker: Submits alcohol signal
CoTA System:
  1. STEP 1: Geographic check [signed]
     - Result: PASS (alcohol permitted in GB)
  2. STEP 2: Category compliance check [signed]
     - Category: alcohol (regulated)
     - Result: CONDITIONAL
     - Condition: human_approval_required
     - Explanation: "Per OpenSignals policy, all alcohol signals require human approval regardless of trust score"
  3. STEP 3: Decision synthesis [signed]
     - Decision: APPROVED_WITH_CONDITIONS
     - Conditions: [human_approval_required]
  4. Finalize chain [signed]
  5. Wait for human co-signature
     - Required co-signer role: compliance_officer
     - Status: PENDING

  → Signal CANNOT be activated until human co-signs

  IF attacker tries to activate anyway:
    - Activation system checks for co-signature
    - co_signatures array is empty
    - Activation BLOCKED
    - Incident logged: "Attempted activation without required approval"
```

---

## 11. Compliance and Audit Benefits

### 11.1 Regulatory Audit Scenarios

**Scenario 1: GDPR Right to Explanation**

User: "Why was I targeted with this ad?"

With CoTA:
```
1. Retrieve reasoning chain for campaign activation
2. Show decision synthesis step:
   "Signal 'premium-cocktail-contexts' was approved because:
   - Geographic check: User in GB where alcohol ads permitted (18+)
   - Trust score: 0.87 (Trusted tier)
   - Signal type: Contextual (no individual profiling)
   - Consent: Not required (contextual targeting)
   - Human approval: Obtained from compliance officer"
3. Provide full chain to user or regulator
4. User can verify signatures independently
```

**Scenario 2: Post-Campaign Compliance Audit**

Regulator: "Show us how you ensured GDPR compliance for this campaign"

With CoTA:
```
1. Query all reasoning chains for campaign
2. Filter to GDPR-related steps
3. Generate audit report:
   - 1,247 signals evaluated
   - 1,203 approved (97%)
   - 44 blocked for GDPR violations (3%)
   - All approvals include consent verification step
   - All steps cryptographically signed
   - No evidence of tampering
4. Provide Merkle proofs for any specific signal
5. Regulator can independently verify signatures
```

**Scenario 3: Incident Investigation**

Brand: "A prohibited signal was activated. How did this happen?"

With CoTA:
```
1. Retrieve reasoning chain for incident signal
2. Trace decision path:
   STEP 1: Geographic check - PASS
   STEP 2: Category check - CONDITIONAL
   STEP 3: Trust score - PASS
   STEP 4: Human approval - SKIPPED ← ROOT CAUSE
   STEP 5: Decision - APPROVED (incorrect)
3. Verify signatures:
   - Steps 1-3 signatures valid
   - Step 4 missing
   - Step 5 signature valid but incorrect logic
4. Identify responsible agent: governance-agent-002
5. Review agent code: Bug in decision synthesis
6. Root cause: Logic error allowed approval without step 4
7. Remediation: Fix agent, re-verify all pending approvals
```

### 11.2 Audit Trail Permanence

CoTA reasoning chains provide permanent, tamper-evident audit trails:

**Storage Options**:

1. **Centralized Database with Append-Only Log**
   - PostgreSQL with event sourcing pattern
   - Each chain = append-only record
   - Database triggers prevent updates/deletes
   - Periodic merkle root checkpoints to blockchain
   - Retention: 7 years (GDPR compliance)

2. **Content-Addressed Storage (IPFS)**
   - Each chain stored as IPFS object
   - CID = cryptographic hash of content
   - Cannot modify without changing CID
   - Distributed copies ensure availability
   - Retrieval via IPFS gateway

3. **Blockchain Storage**
   - Full chain or merkle root stored on-chain
   - Immutable by design
   - Public verifiability
   - High cost, lower throughput
   - Use for high-value or regulated signals only

**Recommended Architecture**:
```
Real-time: PostgreSQL append-only → CID stored
Daily: Batch export to IPFS → IPFS CIDs stored
Weekly: Merkle root checkpoint → Ethereum or Polygon
Query: Check PostgreSQL → Fallback to IPFS → Ultimate fallback to blockchain
```

### 11.3 Compliance Reporting

CoTA enables automated compliance reporting:

```python
class ComplianceReporter:
    """Generate compliance reports from CoTA reasoning chains"""

    def generate_gdpr_report(self, campaign_id: str, date_range: tuple) -> Dict:
        """Generate GDPR compliance report for a campaign"""
        # Query all reasoning chains for campaign
        chains = self.query_chains(campaign_id, date_range)

        report = {
            "campaign_id": campaign_id,
            "date_range": date_range,
            "total_signals_evaluated": len(chains),
            "gdpr_checks": {
                "consent_verified": 0,
                "legitimate_interest_claimed": 0,
                "data_minimization_checked": 0,
                "right_to_deletion_supported": 0
            },
            "violations": [],
            "high_risk_processing": []
        }

        for chain in chains:
            # Analyze GDPR-related steps
            for step in chain.steps:
                if step.step_type == StepType.CONSENT_VERIFICATION:
                    if step.output_result == StepResult.PASS:
                        report["gdpr_checks"]["consent_verified"] += 1
                    else:
                        report["violations"].append({
                            "chain_id": chain.chain_id,
                            "signal_id": chain.signal_id,
                            "issue": "Consent not obtained",
                            "step": step.to_dict()
                        })

        return report

    def generate_category_compliance_report(
        self,
        category: str,
        date_range: tuple
    ) -> Dict:
        """Generate compliance report for regulated category (alcohol, pharma, etc.)"""
        chains = self.query_chains_by_category(category, date_range)

        report = {
            "category": category,
            "date_range": date_range,
            "total_signals": len(chains),
            "human_approval_rate": 0.0,
            "average_approval_time_hours": 0.0,
            "compliance_checks": {
                "geographic_restrictions_checked": 0,
                "age_restrictions_checked": 0,
                "content_restrictions_checked": 0
            },
            "approvals": [],
            "denials": []
        }

        # Analyze each chain
        for chain in chains:
            if chain.final_decision == Decision.APPROVED_WITH_CONDITIONS:
                # Check if human approval was obtained
                if len(chain.co_signatures) > 0:
                    report["human_approval_rate"] += 1

                    # Calculate approval time
                    chain_end = datetime.fromisoformat(chain.timestamp_end)
                    for co_sig in chain.co_signatures:
                        approval_time = datetime.fromisoformat(co_sig["timestamp"])
                        hours = (approval_time - chain_end).total_seconds() / 3600
                        report["average_approval_time_hours"] += hours

        # Compute averages
        report["human_approval_rate"] /= len(chains) if chains else 1
        report["average_approval_time_hours"] /= len(chains) if chains else 1

        return report
```

---

## 12. Implementation Guidelines

### 12.1 Deployment Checklist

**Phase 1: Development (Weeks 1-4)**
- [ ] Implement CotaEngine class
- [ ] Create reasoning step schema validation
- [ ] Set up key management (generate/store ECDSA keys)
- [ ] Build chain storage (PostgreSQL append-only table)
- [ ] Implement chain verification logic
- [ ] Write unit tests for cryptographic functions
- [ ] Create integration tests with mock verify_signal

**Phase 2: Integration (Weeks 5-8)**
- [ ] Modify verify_signal task to use CoTA
- [ ] Add reasoning chain retrieval endpoint
- [ ] Implement chain verification API
- [ ] Build audit query interface
- [ ] Create compliance reporting tools
- [ ] Set up monitoring and alerting
- [ ] Performance testing (target: <3s for 10-step chain)

**Phase 3: Pilot (Weeks 9-12)**
- [ ] Deploy to staging environment
- [ ] Run pilot with non-regulated signals
- [ ] Test with sample compliance audits
- [ ] Gather feedback from governance agents
- [ ] Optimize step execution (parallelize where possible)
- [ ] Harden security (pen testing)
- [ ] Document operator runbooks

**Phase 4: Production (Week 13+)**
- [ ] Deploy to production
- [ ] Enable for regulated categories first
- [ ] Monitor chain verification performance
- [ ] Scale storage infrastructure
- [ ] Onboard human approvers
- [ ] Regular security audits
- [ ] Compliance reporting automation

### 12.2 Performance Considerations

**Optimization Strategies**:

1. **Parallel Step Execution**
   - Independence analysis: Identify steps with no dependencies
   - Execute parallel groups concurrently
   - Example: Geographic check + Trust score validation + Provenance check
   - Speedup: 3x for 4-core system

2. **Lazy Signature Verification**
   - Only verify signatures when chain is queried for audit
   - During execution, trust the agent's signatures
   - Verification happens post-hoc
   - Trade-off: Faster execution, detect tampering later

3. **Signature Batching**
   - Sign multiple steps in batch (BLS signatures)
   - Single aggregate signature for all steps
   - Reduces signature size and verification time
   - Requires BLS cryptography support

4. **Storage Optimization**
   - Store full chains in blob storage (S3/IPFS)
   - Store only chain hash and metadata in DB
   - Retrieve full chain on-demand
   - Reduces DB size, slightly slower retrieval

**Target Performance**:
- Chain initialization: <50ms
- Single step execution + signing: <100ms
- 6-step chain execution: <2s (with 4 parallel)
- Chain finalization: <100ms
- Total: <2.5s for typical verification

### 12.3 Key Management

**Key Hierarchy**:

```
Root CA Key (offline, HSM-protected)
    ↓
Organization Key (rotate yearly)
    ↓
Agent Key (rotate monthly)
        ↓
    Per-chain ephemeral keys (optional)
```

**Best Practices**:
- Store private keys in Hardware Security Module (HSM)
- Use key rotation policy (monthly for agent keys)
- Implement key revocation list
- Log all key operations
- Use separate keys for different agent roles
- Human approvers use personal keys (smart cards)
- Never log or transmit private keys

**Key Storage**:
```python
# Use cloud KMS or HSM
from google.cloud import kms_v1

def load_private_key_from_kms(key_name: str) -> bytes:
    """Load private key from Google Cloud KMS"""
    client = kms_v1.KeyManagementServiceClient()

    # Get key from KMS
    crypto_key = client.get_crypto_key(name=key_name)

    # Decrypt private key material
    plaintext = client.decrypt(
        request={"name": crypto_key.name, "ciphertext": encrypted_key}
    ).plaintext

    return plaintext
```

### 12.4 Error Handling

**Failure Modes**:

1. **Step Execution Failure**
   ```python
   try:
       result = execute_compliance_check(signal)
   except Exception as e:
       # Log error
       logger.error(f"Step failed: {e}")

       # Add error step to chain
       cota.add_reasoning_step(
           chain=chain,
           step_type=StepType.CUSTOM,
           output_result=StepResult.FAIL,
           output_message=f"Step failed due to error: {str(e)}",
           confidence=0.0
       )

       # Fail-safe: Block signal on error
       final_decision = Decision.BLOCKED
   ```

2. **Signature Failure**
   ```python
   try:
       signature = cota.sign_data(step_hash)
   except CryptoError as e:
       # Critical: Cannot proceed without signature
       logger.critical(f"Signature failed: {e}")

       # Emergency: Use backup key
       signature = cota_backup.sign_data(step_hash)

       # Alert ops team
       send_alert("Signature failure, using backup key")
   ```

3. **Chain Verification Failure**
   ```python
   is_valid, errors = cota.verify_chain(chain)

   if not is_valid:
       # Tamper detected
       logger.critical(f"Chain tampered: {errors}")

       # Block activation
       raise TamperDetectedError(errors)

       # Trigger investigation
       security_team.investigate(chain_id, errors)
   ```

---

## 13. Security Considerations

### 13.1 Threat Model

**Threat Actors**:
1. **External Attacker**: Tries to bypass verification via API manipulation
2. **Compromised Agent**: Malicious agent tries to approve prohibited signals
3. **Insider Threat**: Human approver colludes to approve fraudulent signals
4. **Signal Provider**: Falsifies trust scores or manifests

**Attack Surfaces**:
1. API endpoints (verify_signal, retrieve_chain)
2. Key storage and management
3. Chain storage and retrieval
4. Signature verification logic
5. Human approval workflow

**Security Controls**:

| Threat | Attack | Control |
|--------|--------|---------|
| External Attacker | API manipulation | Input validation, rate limiting, authentication |
| Compromised Agent | Fake reasoning steps | Cryptographic signing, multi-party verification |
| Insider Threat | Colluding approver | Multi-party approval, audit logging |
| Signal Provider | Trust score inflation | Independent recomputation, signed manifests |

### 13.2 Cryptographic Security

**Signature Algorithm Choice**:
- **ECDSA (secp256r1)**: Recommended for general use
  - Pros: Fast, compact signatures, widely supported
  - Cons: Malleability (use deterministic k)
- **EdDSA (Ed25519)**: Alternative, slightly better security
  - Pros: No malleability, faster verification
  - Cons: Less widely supported
- **RSA (2048-bit)**: Legacy compatibility
  - Pros: Most compatible
  - Cons: Large signatures, slower

**Recommendation**: Use ECDSA with deterministic nonce (RFC 6979) for compatibility and security.

**Hash Algorithm**:
- **SHA-256**: Required for all hashing
- Do NOT use: MD5, SHA-1 (broken)

**Key Length**:
- ECDSA: 256-bit curve (secp256r1 / P-256)
- RSA: Minimum 2048-bit, prefer 4096-bit
- Symmetric: AES-256 for key encryption

### 13.3 Storage Security

**Chain Storage**:
- Encrypt at rest (AES-256)
- Append-only (no updates/deletes)
- Access control (role-based)
- Audit logging (all reads/writes)
- Backup and disaster recovery

**Key Storage**:
- Hardware Security Module (HSM) for root keys
- Cloud KMS (AWS KMS, Google Cloud KMS) for agent keys
- Never store plaintext keys in code or config
- Rotate keys regularly
- Implement key revocation

**Access Control**:
```
Roles:
- governance_agent: Can create chains, sign steps
- human_approver: Can add co-signatures
- auditor: Can read chains (read-only)
- admin: Can manage keys, view logs
- public: Can verify signatures (no PII access)
```

---

## 14. Future Enhancements

### 14.1 Zero-Knowledge Proofs

Enable privacy-preserving reasoning verification:

**Problem**: Some reasoning steps may contain sensitive data (PII, trade secrets)

**Solution**: Use ZK-SNARKs to prove reasoning happened without revealing details

```
Example:
STEP 3: Consent verification
  - Input: User consent string (sensitive)
  - Logic: Check if purpose 1 is consented
  - Output: Consent granted (public)

ZK Proof: "I verified consent was granted for purpose 1, but I won't reveal the consent string or user ID"

Verifier can check:
1. Proof is valid
2. Conclusion is "consent granted"
3. BUT cannot see user's consent string

This enables:
- Full auditability (proof exists)
- Privacy protection (PII not revealed)
- Regulatory compliance (GDPR right to be forgotten)
```

**Implementation**: Use zk-SNARKs library (e.g., libsnark, arkworks)

### 14.2 AI-Generated Explanations

Enhance reasoning explanations with LLM-generated summaries:

**Current**: Explanations are template-based
```
"I am checking whether alcohol advertising is permitted in GB."
```

**Future**: LLM generates natural explanations
```
"I consulted the UK Advertising Practise Code (CAP Code) section 18, which governs alcohol advertising in Great Britain. The code permits alcohol advertising to adults aged 18 and over, provided the content does not appeal to minors and promotes responsible drinking. Since this signal uses contextual targeting of premium cocktail content without individual profiling, it complies with CAP Code requirements. However, human approval is still required as a safeguard for this regulated category."
```

**Benefits**:
- More accessible to non-technical reviewers
- Better GDPR "right to explanation" responses
- Improved human-AI trust

**Implementation**:
```python
def generate_explanation(step: ReasoningStep) -> str:
    """Use LLM to generate natural language explanation"""
    prompt = f"""
    You are explaining an AI verification decision to a compliance officer.

    Step type: {step.step_type}
    Rule applied: {step.logic_rule_id}
    Input: {step.input_data}
    Result: {step.output_result}

    Write a clear 2-3 sentence explanation of:
    1. What was checked
    2. Why it was checked
    3. What the result means

    Be specific, cite regulations if applicable, use professional tone.
    """

    explanation = llm_api.generate(prompt, max_tokens=200)
    return explanation
```

### 14.3 Decentralized Verification Network

Create a decentralized network of independent verifiers:

**Architecture**:
```
Signal Provider publishes manifest
    ↓
Multiple independent verifiers execute CoTA reasoning
    ↓
Consensus: 3/5 verifiers must agree
    ↓
Aggregate signatures into multi-sig approval
    ↓
Signal approved only if consensus reached
```

**Benefits**:
- No single point of failure
- Resistance to compromised verifiers
- Increased trust through decentralization
- Regulatory-friendly (distributed oversight)

**Implementation**: Use blockchain smart contracts or distributed ledger

### 14.4 Reasoning Chain Compression

Reduce storage and bandwidth for reasoning chains:

**Current**: Full JSON chains are verbose (10-50 KB each)

**Future**: Merkle-compressed representation
```
Full chain: 50 KB
Compressed:
- Step hashes: 32 bytes × 6 steps = 192 bytes
- Merkle root: 32 bytes
- Metadata: ~200 bytes
- Total: ~400 bytes (125x compression)

On-demand expansion:
- Query full chain from IPFS when needed
- Verify compressed version matches
```

**Benefits**:
- Lower storage costs
- Faster transmission
- Still fully verifiable

---

## Conclusion

Chain-of-Thought Authentication represents a paradigm shift in AI agent security for advertising. By making reasoning provably explainable and tamper-evident, CoTA solves critical trust problems that traditional authentication cannot address.

**Key Innovations**:
1. **Reasoning as Data**: The thought process becomes a first-class, verifiable artifact
2. **Cryptographic Proofs**: Math proves logic, not just identity
3. **Tamper-Evidence**: Any manipulation breaks the chain
4. **Multi-Party Trust**: Multiple agents can attest to correctness
5. **Audit-First Design**: Compliance built into the protocol

**Impact on OpenSignals**:
- **Fraud Prevention**: Cannot fake decisions or manipulate trust scores
- **Compliance**: Full audit trails for regulators (GDPR, CCPA, etc.)
- **Accountability**: Every decision traceable to specific agent and reasoning
- **Trust**: Brands can confidently delegate to agents with verification
- **Transparency**: Human-readable explanations for all decisions

**Next Steps**:
1. Implement CoTA engine and integrate with verify_signal
2. Deploy to staging with sample signals
3. Run compliance audits to validate effectiveness
4. Scale to production for regulated categories
5. Expand to all signal types
6. Explore zero-knowledge and decentralized enhancements

Chain-of-Thought Authentication makes OpenSignals **impossible to game** and **easy to trust**—exactly what agentic advertising needs.

---

**Document Version**: 0.1
**Last Updated**: May 2026
**Authors**: OpenSignals Protocol Community
**License**: Apache 2.0 (code), CC BY 4.0 (documentation)
**Feedback**: https://github.com/opensignals-protocol/discussions
