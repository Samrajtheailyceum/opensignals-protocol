# OpenSignals Protocol - Navigation Guide

## 🚀 Quick Navigation

### I want to...

**Get started in 5 minutes** → [QUICKSTART.md](QUICKSTART.md)

**Understand the innovation** → [INNOVATION.md](INNOVATION.md)

**Download client library** → [embeddings/](embeddings/)

**See working code** → [reference-implementation/python/](reference-implementation/python/)

**Read technical spec** → [specs/opensignals-v0.1.md](specs/opensignals-v0.1.md)

**Browse examples** → [examples/SIGNAL-CATALOG.md](examples/SIGNAL-CATALOG.md)

**Test everything** → [TEST.md](TEST.md)

**Integrate with AdCP** → [integrations/adcp/README.md](integrations/adcp/README.md)

**Integrate with AAMP** → [integrations/aamp/README.md](integrations/aamp/README.md)

---

## 📁 Repository Map

```
opensignals-protocol/
│
├── 📘 START HERE
│   ├── README.md                   ← Overview & links
│   ├── QUICKSTART.md              ← 5-minute start
│   ├── INNOVATION.md              ← What's unique
│   └── NAVIGATION.md              ← This file
│
├── 🔧 IMPLEMENTATION
│   ├── embeddings/                ← CLIENT LIBRARIES
│   │   ├── javascript/           ← JS client (< 2KB)
│   │   ├── python/               ← Python client
│   │   └── examples/             ← SSP integration
│   │
│   ├── reference-implementation/  ← Python server
│   │   └── python/
│   │       ├── server.py         ← FastAPI server
│   │       └── README.md         ← API docs
│   │
│   └── TEST.md                    ← Testing guide
│
├── 📐 SPECIFICATION
│   ├── specs/
│   │   ├── opensignals-v0.1.md   ← Complete spec
│   │   ├── terminology.md
│   │   └── conformance.md
│   │
│   └── schemas/v0.1/              ← JSON schemas (7)
│
├── 📊 EXAMPLES
│   ├── examples/
│   │   ├── SIGNAL-CATALOG.md     ← Browse all
│   │   ├── alcohol-contextual-signal.json
│   │   ├── pharmaceutical-signal.json
│   │   └── ... (10 total)
│   │
│   └── EXAMPLES-BY-SCENARIO.md
│
├── 🔗 INTEGRATION
│   ├── integrations/
│   │   ├── adcp/                 ← AdCP integration
│   │   └── aamp/                 ← AAMP mapping
│   │
│   └── embeddings/examples/      ← SSP workflow
│
├── 🔬 INNOVATION
│   ├── INNOVATION.md             ← What's unique
│   ├── docs/
│   │   ├── CHAIN-OF-THOUGHT-AUTH.md  ← Core innovation
│   │   ├── gap-analysis.md
│   │   └── architecture.md
│   │
│   └── tests/                    ← Validation tests
│
└── 📄 PROJECT
    ├── CONTRIBUTING.md
    ├── CODE_OF_CONDUCT.md
    ├── LICENSE
    ├── SECURITY.md
    ├── CHANGELOG.md
    └── ROADMAP.md
```

---

## 🎯 By Role

### I'm a Publisher
1. Read [QUICKSTART.md](QUICKSTART.md) → "For Publishers" section
2. Copy template from [examples/](examples/)
3. Publish at `.well-known/opensignals/{signal_id}`

### I'm an SSP
1. Read [QUICKSTART.md](QUICKSTART.md) → "For SSPs" section
2. Download [JavaScript](embeddings/javascript/opensignals.js) or [Python](embeddings/python/opensignals_client.py) client
3. Follow [SSP integration example](embeddings/examples/ssp-integration.py)

### I'm a DSP/Platform
1. Read [integrations/adcp/README.md](integrations/adcp/README.md)
2. Add `open_signals` field to responses (optional)
3. Test with [TEST.md](TEST.md)

### I'm a Brand/Agency
1. Read [docs/brand-side-use-case.md](docs/brand-side-use-case.md)
2. Define policies using [policy-binding.schema.json](schemas/v0.1/policy-binding.schema.json)
3. Use client library to verify signals

### I'm a Developer
1. Clone repo
2. Read [reference-implementation/python/README.md](reference-implementation/python/README.md)
3. Run `python server.py`
4. Test with [TEST.md](TEST.md)

### I'm a Researcher
1. Read [INNOVATION.md](INNOVATION.md)
2. Read [docs/CHAIN-OF-THOUGHT-AUTH.md](docs/CHAIN-OF-THOUGHT-AUTH.md)
3. Read [specs/opensignals-v0.1.md](specs/opensignals-v0.1.md)

---

## 📚 Documentation Index

### Core Docs
- [README.md](README.md) - Overview
- [QUICKSTART.md](QUICKSTART.md) - 5-minute start
- [INNOVATION.md](INNOVATION.md) - What's unique
- [TEST.md](TEST.md) - Testing guide

### Technical Specs
- [opensignals-v0.1.md](specs/opensignals-v0.1.md) - Complete specification
- [terminology.md](specs/terminology.md) - Definitions
- [conformance.md](specs/conformance.md) - Requirements

### Innovation Docs
- [CHAIN-OF-THOUGHT-AUTH.md](docs/CHAIN-OF-THOUGHT-AUTH.md) - Core innovation
- [gap-analysis.md](docs/gap-analysis.md) - Why OpenSignals?
- [architecture.md](docs/architecture.md) - System design

### Integration Guides
- [AdCP Integration](integrations/adcp/README.md)
- [AAMP Mapping](integrations/aamp/README.md)
- [SSP Example](embeddings/examples/ssp-integration.py)

### Examples
- [Signal Catalog](examples/SIGNAL-CATALOG.md) - All 10 examples
- [Examples by Scenario](examples/EXAMPLES-BY-SCENARIO.md) - Find use case

### Additional
- [FAQ](docs/FAQ.md)
- [Brand Use Case](docs/brand-side-use-case.md)
- [Adoption Guide](docs/adoption-guide.md)
- [Governance](docs/governance-model.md)

---

## 🔍 Finding Things

### Want to find...

**Innovation** → [INNOVATION.md](INNOVATION.md)

**Code to copy** → [embeddings/](embeddings/)

**API reference** → [reference-implementation/python/README.md](reference-implementation/python/README.md)

**Examples** → [examples/SIGNAL-CATALOG.md](examples/SIGNAL-CATALOG.md)

**Schemas** → [schemas/v0.1/](schemas/v0.1/)

**Tests** → [TEST.md](TEST.md)

**Integration** → [integrations/](integrations/)

**FAQ** → [docs/FAQ.md](docs/FAQ.md)

---

**Lost?** Open an issue: https://github.com/Samrajtheailyceum/opensignals-protocol/issues
