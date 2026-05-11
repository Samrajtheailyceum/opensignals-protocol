# THE OPENSIGNALS VISION
## The Missing Trust Layer for Agentic Advertising

**By Samraj Matharu**
**May 2026**

---

## The Problem We're Solving

The advertising industry is building the future of agentic advertising. AI agents will discover signals, plan campaigns, buy media, optimize in real-time, and report results—all autonomously.

But there's a critical gap.

**Before an agent activates a signal, how does it know that signal can be trusted?**

- Is this signal valid for my brand, category, and market?
- Is it permissioned correctly? Fresh enough? Safe for regulated categories?
- Can I explain this signal to stakeholders, regulators, and consumers?
- Does this signal require human approval before I use it?

Today, there's no standardized answer. Every platform, every DSP, every data provider handles trust differently. Agents are flying blind.

**OpenSignals Protocol is the missing trust layer.**

It doesn't replace AdCP, AAMP, OpenRTB, or any existing infrastructure. It sits on top, adding machine-readable trust metadata that makes every protocol, platform, and agent smarter, safer, and more accountable.

---

## What OpenSignals Does

OpenSignals is a standardized framework for **declaring, verifying, scoring, permissioning, and auditing** advertising signals used by AI agents.

### The Core Innovation

Every signal gets an **OpenSignal Manifest**—a machine-readable trust declaration that tells agents:

1. **Who owns this signal** (provenance and chain of custody)
2. **What it's permissioned for** (consent scope, valid use cases)
3. **How fresh it is** (last updated, refresh cadence)
4. **How good it is** (quality scores across multiple dimensions)
5. **How explainable it is** (can stakeholders understand it?)
6. **How it performs** (outcome relevance from past campaigns)
7. **How safe it is** (compliance with regulations and brand safety standards)

Agents query these manifests before activation. Governance agents verify signals against brand policy. Audit agents record usage with full context. Outcome agents feed campaign results back to improve trust scores over time.

### The Seven Core Tasks

OpenSignals defines seven protocol tasks that agents and platforms implement:

| Task | Purpose |
|------|---------|
| `get_signal_manifest` | Retrieve the full trust declaration for a signal |
| `verify_signal` | Check if a signal is valid and permissioned for a specific use case |
| `score_signal` | Score a signal against a brand objective |
| `bind_signal_policy` | Attach brand policy rules to a signal before activation |
| `audit_signal_usage` | Record how a signal was used after activation |
| `revoke_signal` | Withdraw trust from a signal |
| `submit_signal_outcome_feedback` | Feed campaign results back into trust scoring |

These tasks integrate seamlessly with existing protocols. AdCP agents can query manifests before calling `activate_signal`. AAMP agents can use OpenSignals to implement the Trust and Transparency pillar. OpenRTB platforms can surface trust scores in bid requests.

---

## Why Every Stakeholder Benefits

OpenSignals creates value for every participant in the advertising ecosystem. It's not zero-sum. The more who adopt it, the better it gets.

### For Brands

**Trust and governance before spend.**

- **Control**: Set trust thresholds, approval workflows, and compliance rules
- **Safety**: Signals are verified against your brand safety and category restrictions before activation
- **Transparency**: Full audit trails showing which signals were used, when, why, and under what policy
- **Compliance**: Automated checks for GDPR, CCPA, age restrictions, alcohol/gambling/pharma regulations
- **Performance**: Outcome feedback loops improve signal selection over time

**Example**: A premium spirits brand wants to run a campaign in the UK. The brand policy layer requires:
- No signals targeting individuals under 25
- Contextual targeting only (no individual profiling)
- Human approval for all signal activations
- Full audit trail for regulatory compliance

OpenSignals enforces these rules automatically. The buyer agent can't activate a signal without governance approval. The audit agent records every decision. The compliance team has a complete record.

### For Agencies

**Better signal selection, audit trails, and compliance.**

- **Efficiency**: Agents can assess signal trust autonomously, without manual vendor reviews
- **Risk reduction**: Signals are verified before activation, reducing compliance and brand safety exposure
- **Client trust**: Full transparency into which signals were used and why
- **Optimization**: Outcome feedback improves signal selection over time
- **Regulatory compliance**: Audit trails ready for GDPR, CCPA, and category-specific regulations

**Example**: An agency runs campaigns for 50 brands across 20 markets. Each brand has different safety requirements, category restrictions, and approval workflows. Without OpenSignals, every signal needs manual review—slowing activation and increasing risk. With OpenSignals, governance agents verify signals automatically. Buyer agents only see approved signals. Audit agents maintain compliance records. The agency moves faster, with less risk.

### For Signal Providers

**Prove quality, increase adoption.**

- **Differentiation**: Publish trust metadata that proves signal quality
- **Transparency**: Show provenance, permissioning, freshness, and outcome relevance
- **Adoption**: Agents prefer signals with OpenSignal Manifests—they're easier to verify and safer to use
- **Feedback loops**: Learn which signals perform best for which objectives
- **Trust building**: Build long-term trust through consistent quality and transparency

**Example**: A data provider has a high-quality audience signal, but buyers are hesitant—they don't know where the data comes from or how fresh it is. By publishing an OpenSignal Manifest, the provider shows:
- First-party data source with opt-in consent
- Updated daily with a 24-hour freshness guarantee
- High coverage, precision, and explainability scores
- Strong outcome relevance for similar campaigns

Agents can verify this automatically. The signal gets used more. The provider wins business.

### For Platforms (DSPs/SSPs)

**Reduce fraud, increase trust, better outcomes.**

- **Fraud reduction**: Trust scoring helps filter out low-quality or fraudulent signals
- **Trust layer**: Add a competitive differentiator by surfacing signal trust metadata
- **Better outcomes**: Campaigns perform better when signals are verified before activation
- **Compliance support**: Audit trails and permissioning help clients meet regulatory requirements
- **Network effects**: The more signals and buyers use OpenSignals, the more valuable your platform becomes

**Example**: A DSP integrates OpenSignals into its platform. When buyer agents request signals, the DSP surfaces trust scores, verification status, and policy compliance. Agents can filter for "verified only" or "trust score > 0.80". The DSP's inventory becomes more trustworthy. Buyers spend more confidently. Campaign outcomes improve. The DSP wins market share.

### For AI Agents

**Make better decisions, avoid bad signals, explain choices.**

- **Decision support**: Trust scores help agents choose the best signals for each objective
- **Risk avoidance**: Agents can filter out low-trust or non-compliant signals before activation
- **Explainability**: Agents can explain signal selection to humans ("I chose this signal because it has high provenance, freshness, and outcome relevance scores")
- **Compliance**: Agents stay within brand policy and regulatory constraints
- **Learning**: Outcome feedback improves agent performance over time

**Example**: A buyer agent is planning a campaign for a financial services brand in California. It discovers 50 potential signals. Using OpenSignals:
1. Filter out signals with trust scores below 0.75 (brand policy threshold)
2. Exclude signals without CCPA-compliant permissioning
3. Prioritize signals with high outcome relevance for similar financial services campaigns
4. Request human approval for signals in regulated categories

The agent activates only trusted, compliant signals. The campaign performs better. The brand is protected. The agent can explain every decision.

### For Regulators

**Transparency, auditability, compliance.**

- **Audit trails**: Complete records of which signals were used, when, why, and under what policy
- **Provenance tracking**: Understand where data comes from and how it was collected
- **Consent verification**: Check that signals are permissioned correctly for each use case
- **Compliance enforcement**: Verify adherence to GDPR, CCPA, age restrictions, category regulations
- **Transparency**: Machine-readable trust metadata makes the advertising supply chain more transparent

**Example**: A regulator investigates a complaint about alcohol advertising targeting minors. Using OpenSignals audit trails:
- See which signals were used in the campaign
- Verify that age-restriction policies were enforced
- Check that human approval was required and obtained
- Trace data provenance to confirm compliance with data protection laws

The regulator can answer the complaint quickly, with full transparency. The advertiser can demonstrate compliance.

### For Publishers

**Work with trusted demand, better monetization.**

- **Trust layer**: Publishers can surface trust metadata for their inventory and contextual signals
- **Brand safety**: Show that your inventory meets brand safety and compliance standards
- **Premium positioning**: Publishers with high-trust signals command higher CPMs
- **Transparency**: Prove signal quality to attract premium demand
- **Long-term relationships**: Build trust with buyers through consistent quality and transparency

**Example**: A premium publisher wants to attract alcohol and pharmaceutical advertisers. By publishing OpenSignal Manifests for its contextual inventory, it can prove:
- Brand-safe content categories
- Compliance with age restrictions and category regulations
- High-quality contextual signals with strong explainability
- Fresh data with daily updates

Buyer agents can verify this automatically. The publisher attracts premium demand. CPMs increase.

---

## How OpenSignals Integrates With Everything

OpenSignals is a layer, not a competitor. It's designed to work with any protocol, any platform, any LLM, any agent framework.

### Universal Protocol Integration

OpenSignals integrates with every major advertising protocol:

#### AdCP (Ad Context Protocol)
- AdCP provides signal discovery and activation
- OpenSignals adds trust verification between discovery and activation
- Workflow: `get_signals` → `get_signal_manifest` → `verify_signal` → `activate_signal`
- AdCP agents can embed OpenSignals metadata directly in signal responses

#### AAMP (Agentic Advertising Management Protocols)
- AAMP defines three pillars: Foundations (ARTF), Protocols, and Trust and Transparency
- OpenSignals implements the Trust and Transparency pillar with practical, machine-readable trust metadata
- AAMP agents use OpenSignals tasks to verify signals before execution

#### OpenRTB
- OpenRTB handles real-time bidding auctions
- OpenSignals operates before the auction—agents verify signals, then activate them in OpenRTB workflows
- Trust scores can be surfaced in bid requests as extended fields
- Reduces fraud by filtering low-trust signals before they reach the auction

#### OpenDirect
- OpenDirect handles direct buying workflows
- OpenSignals verifies signals before direct deals are executed
- Trust metadata helps negotiators assess signal quality during deal-making

#### Custom Protocols
- OpenSignals is protocol-agnostic
- Any protocol that uses advertising signals can integrate OpenSignals manifests
- No vendor lock-in, no proprietary dependencies

### Universal Platform Integration

OpenSignals works with any advertising platform:

- **Google DV360, Campaign Manager, Ad Manager**: Integrate OpenSignals to surface trust metadata in signal selection and reporting
- **Meta Ads**: Use OpenSignals to verify custom audiences and contextual signals
- **Amazon Ads**: Add trust layer for commerce signals and audience targeting
- **The Trade Desk**: Surface OpenSignals trust scores in platform UI and APIs
- **Any DSP/SSP**: Integrate OpenSignals via APIs, extend bid requests with trust metadata
- **Any DMP/CDP**: Publish OpenSignal Manifests for audience segments and data assets

### Universal LLM Integration

OpenSignals is LLM-agnostic. Any AI agent, powered by any language model, can use OpenSignals:

- **Claude (Anthropic)**: Claude Code agents can query OpenSignals via MCP servers
- **GPT (OpenAI)**: GPT agents can call OpenSignals APIs directly or via function calling
- **Gemini (Google)**: Gemini agents can use OpenSignals for signal verification and explainability
- **Open source LLMs**: Llama, Mistral, or any other model can integrate OpenSignals tasks

### Universal Agent Framework Integration

OpenSignals works with any agent framework:

- **MCP (Model Context Protocol)**: Expose OpenSignals as MCP resources and tools
- **A2A (Agent2Agent)**: Use OpenSignals tasks as A2A skills
- **LangChain, LlamaIndex, AutoGPT**: Integrate OpenSignals via API wrappers or plugins
- **Custom agent frameworks**: Call OpenSignals APIs directly

---

## Why Standards Bodies Benefit From OpenSignals

OpenSignals is not a threat to existing standards. It's a complement that makes them more powerful.

### For AdCP and AgenticAdvertising.Org

OpenSignals fills a specific gap: **trust verification between signal discovery and activation.**

- AdCP defines how agents discover signals (`get_signals`)
- OpenSignals defines how agents verify signals before activation (`verify_signal`, `score_signal`)
- AdCP can reference OpenSignals as a recommended trust layer
- AdCP agents that use OpenSignals become safer, more compliant, and more explainable

**Benefit**: AdCP becomes the complete signal management protocol—discovery, trust, and activation in one workflow.

### For IAB Tech Lab and AAMP

OpenSignals implements the **Trust and Transparency pillar** of AAMP with practical, machine-readable trust metadata.

- AAMP defines the vision: agents need trust and transparency
- OpenSignals provides the implementation: manifests, verification tasks, audit trails, outcome feedback
- IAB Tech Lab can reference OpenSignals as a practical implementation of AAMP trust principles
- AAMP agents that use OpenSignals have standardized trust verification

**Benefit**: AAMP's Trust and Transparency pillar gets a concrete, implementable standard that complements the Foundations (ARTF) and Protocols pillars.

### For IAB Tech Lab's OpenRTB, OpenDirect, and AdCOM

OpenSignals operates **above** the execution layer, making OpenRTB and OpenDirect safer and more transparent.

- OpenRTB defines how auctions work
- OpenSignals verifies signals before they enter auctions
- Result: fewer fraudulent signals, better campaign outcomes, more buyer trust
- IAB Tech Lab can position OpenSignals as a pre-auction trust layer that improves OpenRTB quality

**Benefit**: OpenRTB and OpenDirect become more trusted, reducing fraud and improving advertiser confidence.

### For MCP and A2A

OpenSignals provides a real-world use case for agent-to-agent communication and context management.

- MCP defines how agents access context and tools
- A2A defines how agents communicate
- OpenSignals defines what signals need to be communicated and verified
- OpenSignals can be exposed as MCP resources or A2A skills

**Benefit**: MCP and A2A get a proven advertising use case, demonstrating their value in commercial contexts.

---

## The Network Effects

OpenSignals gets better the more people use it. Every adoption creates value for everyone else.

### Signal Provider Network Effects

- **More signal providers publish manifests** → Agents have more verified signals to choose from
- **More verified signals** → Buyers trust the ecosystem more, spend increases
- **More spending** → Signal providers earn more, incentivizing quality improvements
- **Higher quality** → Trust scores improve, agents prefer these signals
- **Better outcomes** → Outcome feedback improves trust scores further

### Platform Network Effects

- **More platforms integrate OpenSignals** → Agents can use trust verification everywhere
- **More agents verify signals** → Platforms differentiate by surfacing trust metadata
- **More trust metadata** → Buyers prefer platforms with OpenSignals integration
- **More buyers** → Platforms have stronger demand, publishers earn more
- **More publishers** → Platforms have better inventory, attracting more buyers

### Ecosystem Network Effects

- **More adoption** → More audit trails, improving fraud detection
- **Better fraud detection** → Ecosystem trust increases, reducing risk
- **Lower risk** → More advertisers enter agentic advertising
- **More advertisers** → More demand for verified signals
- **More demand** → More signal providers publish manifests

### Data Network Effects

- **More outcome feedback** → Trust scores become more accurate
- **More accurate scores** → Agents make better decisions
- **Better decisions** → Campaign outcomes improve
- **Better outcomes** → More feedback data
- **More feedback** → Trust scores improve further

---

## Why OpenSignals is Open Source and Free to Use

OpenSignals is released under **Apache 2.0** (code) and **CC BY 4.0** (documentation). It's free to use, free to modify, free to integrate.

### Why Open Source?

1. **Trust**: Advertising needs open standards, not proprietary vendor solutions
2. **Adoption**: Free and open means faster industry adoption
3. **Interoperability**: Anyone can implement, integrate, or extend OpenSignals
4. **Transparency**: The protocol itself must be transparent to enable signal transparency
5. **Innovation**: Open source allows the community to improve OpenSignals over time

### Why No Vendor Lock-In?

- **Any protocol**: Works with AdCP, AAMP, OpenRTB, OpenDirect, custom protocols
- **Any platform**: Works with Google, Meta, Amazon, The Trade Desk, any DSP/SSP
- **Any LLM**: Works with Claude, GPT, Gemini, open source models
- **Any agent framework**: Works with MCP, A2A, LangChain, custom frameworks

OpenSignals is infrastructure, not a product. It's built to last, governed by the community, and designed for universal adoption.

---

## The Path Forward

OpenSignals is a **draft RFC** (v0.1, May 2026). It's a proposal, not a finished standard. The goal is to stimulate discussion, gather feedback, and collaborate with the industry to refine the protocol.

### What Happens Next

1. **Community feedback**: Open issues, propose changes, suggest improvements
2. **Early adopters**: Signal providers, platforms, and agencies test the protocol
3. **Reference implementations**: More SDKs, integrations, and examples
4. **Real-world validation**: Pilot campaigns using OpenSignals in production
5. **Standards body engagement**: Work with AdCP, IAB Tech Lab, and AAMP to align on trust standards
6. **Protocol refinement**: Iterate based on feedback, formalize conformance requirements
7. **Industry adoption**: OpenSignals becomes the default trust layer for agentic advertising

### How to Get Involved

- **Signal Providers**: Publish OpenSignal Manifests for your signals
- **Platforms**: Integrate OpenSignals APIs into your DSP, SSP, DMP, or CDP
- **Agencies and Brands**: Test OpenSignals in pilot campaigns, provide feedback on governance workflows
- **Standards Bodies**: Reference OpenSignals as a trust implementation layer
- **Developers**: Build tools, SDKs, and integrations
- **Everyone**: Open issues, propose changes, share use cases

---

## The Vision

**OpenSignals is the missing trust layer for agentic advertising.**

It doesn't replace anything. It makes everything better.

- **AdCP becomes safer** with trust verification before activation
- **AAMP becomes practical** with machine-readable trust metadata
- **OpenRTB becomes cleaner** with fraud reduction at the signal layer
- **Platforms become more trusted** with transparency and audit trails
- **Agents become smarter** with trust-aware decision making
- **Brands become protected** with governance and compliance enforcement
- **Publishers become premium** by proving signal quality
- **Regulators gain visibility** into the advertising supply chain

The more who adopt it, the better it gets. The network effects compound. The ecosystem becomes more trusted, more transparent, and more effective.

**This is not a product. It's infrastructure.**

**This is not a competitor. It's a complement.**

**This is not proprietary. It's open.**

**This is the trust layer agentic advertising needs.**

---

## About the Creator

**Samraj Matharu** is the creator and visionary behind OpenSignals Protocol.

With a deep understanding of advertising technology, AI agent architectures, and the practical challenges of signal trust in agentic advertising, Samraj identified the critical gap: agents need standardized trust metadata before they can safely activate signals.

OpenSignals is the result of that insight—a practical, implementable protocol that complements existing standards while addressing a real-world problem.

Samraj's vision is simple: **every signal used by an advertising agent should be declared, permissioned, scored, and auditable.** OpenSignals makes that vision real.

---

## Get Started

- **Specification**: [specs/opensignals-v0.1.md](../specs/opensignals-v0.1.md)
- **Architecture**: [docs/architecture.md](architecture.md)
- **Examples**: [examples/](../examples/)
- **Reference Implementation**: [reference-implementation/python/](../reference-implementation/python/)
- **AdCP Integration**: [integrations/adcp/](../integrations/adcp/)
- **AAMP Integration**: [integrations/aamp/](../integrations/aamp/)
- **GitHub**: [github.com/Samrajtheailyceum/opensignals-protocol](https://github.com/Samrajtheailyceum/opensignals-protocol)
- **Issues**: [github.com/Samrajtheailyceum/opensignals-protocol/issues](https://github.com/Samrajtheailyceum/opensignals-protocol/issues)

---

**OpenSignals Protocol**
**The Trust Layer for Agentic Advertising**
**Created by Samraj Matharu**
**May 2026**
