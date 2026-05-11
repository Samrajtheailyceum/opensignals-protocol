# OpenSignals Examples by Scenario

**Version**: 0.1
**Last Updated**: 2026-05-11
**Status**: Active

This guide organizes all OpenSignals example manifests by practical use scenarios, making it easy to find the right signal for your specific needs.

---

## Table of Contents

1. [By Industry](#by-industry)
2. [By Trust Level](#by-trust-level)
3. [By Governance Needs](#by-governance-needs)
4. [By Signal Type](#by-signal-type)
5. [By Compliance Category](#by-compliance-category)
6. [By Use Case](#by-use-case)
7. [By CPM Range](#by-cpm-range)
8. [Decision Tree Guide](#decision-tree-guide)

---

## By Industry

### Retail & E-Commerce

**Signals to Use**:
- **Home Decor Purchase Intent** (`retail-commerce-signal.json`)
  - Trust Score: 0.91
  - CPM: $8-$18
  - Best for: Home goods, furniture, interior design
  - Conversion: 3.1-4.2%, ROAS: 4.8x

- **Carbon-Neutral Consumer** (`carbon-neutral-signal.json`)
  - Trust Score: 0.81
  - CPM: $14-$32
  - Best for: Sustainable products, eco-friendly retail
  - Conversion: 2.2-3.8%, ROAS: 4.5-7.8x

**When to Use**: Direct response campaigns, conversion optimization, seasonal promotions, new product launches.

---

### Financial Services

**Signals to Use**:
- **High-Value Financial Customer** (`financial-services-signal.json`)
  - Trust Score: 0.89
  - CPM: $25-$60
  - Best for: Wealth management, private banking, premium financial products
  - Lead Quality: 4.2x standard, High transaction values

**When to Use**: HNWI acquisition, wealth management campaigns, premium credit cards, investment advisory.

**Critical**: Requires human approval, GLBA/FCRA compliance, strict prohibited use enforcement.

---

### Luxury Goods

**Signals to Use**:
- **Luxury Purchase Intent** (`luxury-intent-signal.json`)
  - Trust Score: 0.93
  - CPM: $35-$85
  - Best for: High-end fashion, jewelry, watches, automotive ($5K+)
  - Conversion: 0.6-1.8%, ROAS: 18-45x, AOV: $45K-$180K

- **High-Value Financial Customer** (`financial-services-signal.json`)
  - Trust Score: 0.89
  - CPM: $25-$60
  - Best for: Ultra-luxury goods, requires financial qualification

**When to Use**: Ultra-premium products, VIP programs, exclusive events, high-value acquisitions.

---

### Healthcare & Pharmaceutical

**Signals to Use**:
- **Health Condition Management** (`pharmaceutical-signal.json`)
  - Trust Score: 0.76
  - CPM: $12-$28
  - Best for: Disease awareness, patient education (NOT direct drug promotion)
  - Education Focus: 12-18% resource downloads, 5-8% HCP discussion tools

**When to Use**: Disease awareness campaigns, patient education, treatment information (educational only).

**Critical**: HIPAA compliance, FDA/EMA regulations, cohort-level only (minimum 1,000 individuals), human approval required.

---

### Alcohol & Spirits

**Signals to Use**:
- **Premium Cocktail Contexts** (`alcohol-contextual-signal.json`)
  - Trust Score: 0.88
  - CPM: $4.50-$12
  - Best for: Spirits, wine, beer, premium alcohol brands
  - Brand Lift: 8-14%, CTR: 0.45-0.72%

**When to Use**: Age-restricted alcohol advertising, premium spirits campaigns, contextual brand safety.

**Critical**: Age verification mandatory, human approval required, strict market restrictions.

---

### Travel & Hospitality

**Signals to Use**:
- **Luxury Purchase Intent** (`luxury-intent-signal.json`)
  - Trust Score: 0.93
  - CPM: $35-$85
  - Best for: Ultra-premium travel, private aviation, luxury resorts

- **Carbon-Neutral Consumer** (`carbon-neutral-signal.json`)
  - Trust Score: 0.81
  - CPM: $14-$32
  - Best for: Eco-tourism, carbon-neutral travel packages

**When to Use**: Premium travel packages, luxury hospitality, adventure travel, eco-tourism.

---

### Family & Entertainment

**Signals to Use**:
- **COPPA-Compliant Family Content** (`children-safe-signal.json`)
  - Trust Score: 0.82
  - CPM: $8-$18
  - Best for: Toys, games, family entertainment, children's products
  - Safety Score: 99.8%, Parent Satisfaction: 4.7/5

**When to Use**: Products for children under 13, family entertainment, educational products.

**Critical**: Zero behavioral tracking, age-gating mandatory, COPPA compliance, human approval required.

---

### Political & Advocacy

**Signals to Use**:
- **Voter Engagement Political** (`political-signal.json`)
  - Trust Score: 0.73
  - CPM: $6-$22 (spikes near election day)
  - Best for: Political campaigns, ballot initiatives, civic engagement
  - Turnout Lift: 3-8%, Persuasion: 5-12%

**When to Use**: Legitimate political campaigns, voter mobilization, ballot initiatives.

**Critical**: Election law compliance, disclosure requirements, record retention, human approval required.

---

### Automotive

**Signals to Use**:
- **Luxury Purchase Intent** (`luxury-intent-signal.json`)
  - Trust Score: 0.93
  - CPM: $35-$85
  - Best for: Luxury/exotic vehicles ($100K+)
  - Conversion: 0.6-1.8%, High-value transactions

- **Carbon-Neutral Consumer** (`carbon-neutral-signal.json`)
  - Trust Score: 0.81
  - CPM: $14-$32
  - Best for: Electric vehicles, hybrids, sustainable automotive

**When to Use**: Luxury automotive, EV launches, high-consideration vehicle purchases.

---

### Media & Publishing

**Signals to Use**:
- **Verified Attention Quality** (`attention-signal.json`)
  - Trust Score: 0.94
  - CPM: $0.50-$2.00 (measurement fee)
  - Best for: Inventory optimization, quality measurement
  - Brand Lift Correlation: 0.89

**When to Use**: Inventory packaging, premium placement justification, media quality optimization.

---

### Sustainable & ESG Brands

**Signals to Use**:
- **Carbon-Neutral Consumer** (`carbon-neutral-signal.json`)
  - Trust Score: 0.81
  - CPM: $14-$32
  - Best for: Sustainable products with verified credentials
  - Premium Pricing Acceptance: +18%, Loyalty: 32% higher repeat rate

- **Verified Sustainable Inventory** (`sustainability-signal.json`)
  - Trust Score: 0.79
  - CPM: $3-$7.50
  - Best for: Carbon-neutral media campaigns, ESG reporting
  - Carbon Offset: 0.8g CO2/impression

**When to Use**: Sustainability commitments, ESG reporting, carbon-neutral campaigns, climate action.

**Critical**: Third-party verification required, greenwashing prevention mandatory.

---

## By Trust Level

### Very High Trust (0.90-1.00)

**Signals**:
1. **Verified Attention Quality** - 0.94
   - Measurement signal with MRC accreditation
   - Real-time, transparent methodology, third-party validated
   - Use for: Media optimization, brand campaigns

2. **Luxury Purchase Intent** - 0.93
   - First-party luxury retail data with verified transactions
   - Performance-validated with documented outcomes
   - Use for: Ultra-premium products ($5K+)

**Characteristics**: Exceptional provenance, third-party validation, strong performance history, high compliance.

**Governance**: Can operate autonomously after initial approval (if policy allows).

---

### High Trust (0.75-0.89)

**Signals**:
1. **Home Decor Purchase Intent** - 0.91
   - First-party commerce data with explicit consent
   - Strong conversion performance
   - Use for: Retail, home goods, furniture

2. **High-Value Financial Customer** - 0.89
   - Banking relationship data with strict compliance
   - Verified financial capacity
   - Use for: Financial services, luxury goods

3. **Premium Cocktail Contexts** - 0.88
   - Contextual signal with compliance verification
   - Regulated category with governance controls
   - Use for: Alcohol advertising

4. **COPPA-Compliant Family Content** - 0.82
   - Contextual-only, zero tracking, child safety verified
   - Strong safety protections
   - Use for: Family/children's products

5. **Carbon-Neutral Consumer** - 0.81
   - Verified sustainability actions, third-party certified
   - Greenwashing prevention
   - Use for: Sustainable products

**Characteristics**: Good provenance, clear methodology, strong compliance, standard governance checks.

**Governance**: Use with standard governance checks, some require human approval.

---

### Limited Trust (0.60-0.74)

**Signals**:
1. **Health Condition Management** - 0.76
   - Privacy-first design limits precision
   - Cohort-level only for privacy protection
   - Use for: Disease awareness, patient education

2. **Voter Engagement Political** - 0.73
   - Complex regulatory environment
   - Public records plus engagement data
   - Use for: Political campaigns

**Characteristics**: Emerging markets, privacy-first constraints, complex regulations, moderate performance.

**Governance**: Human review required per activation, enhanced monitoring.

---

## By Governance Needs

### Autonomous (After Initial Approval)

**Signals**:
- **Verified Attention Quality** - No human approval required
  - Low risk measurement signal
  - Monthly audits sufficient

- **Home Decor Purchase Intent** - No human approval required
  - First-party with consent, quarterly audits

- **Verified Sustainable Inventory** - No human approval required
  - Environmental signal, monthly audits

**When to Use**: Operational efficiency, frequent activations, low-risk campaigns.

---

### Human Approval Required (First Activation Only)

**Signals**:
- **Luxury Purchase Intent** - First activation approval
  - Brand alignment verification
  - Creative quality review
  - Subsequent activations autonomous

**When to Use**: Premium brand partnerships, quality control needed, high-value products.

---

### Human Approval Required (Every Activation)

**Regulated Categories**:
- **Premium Cocktail Contexts** - Alcohol (every activation)
  - Legal and compliance review mandatory
  - Age verification, market restrictions
  - Per-activation audit

- **High-Value Financial Customer** - Financial services (every activation)
  - Legal, compliance, privacy, risk review
  - GLBA/FCRA compliance verification
  - Per-activation + monthly audit

- **Carbon-Neutral Consumer** - Sustainability (every activation)
  - Greenwashing prevention review
  - Environmental claims verification
  - Quarterly + annual ESG audit

- **Voter Engagement Political** - Political (every activation)
  - Election law compliance
  - Disclosure requirements
  - Per-activation + ongoing + post-election audit

**Restricted Categories**:
- **Health Condition Management** - Healthcare (every activation)
  - Medical, legal, privacy, ethics review
  - FDA/EMA compliance, HIPAA
  - Per-activation + quarterly audit

- **COPPA-Compliant Family Content** - Children's privacy (every activation)
  - Child safety, legal, compliance, creative review
  - COPPA compliance, age-gating verification
  - Per-activation + weekly monitoring

**When to Use**: Only when strict compliance is mandatory, legal requirements dictate, reputational risk is high.

---

## By Signal Type

### Contextual

**Page-Level Content Targeting (No User Data)**:

1. **Premium Cocktail Contexts** - 0.88 trust
   - Food, drink, lifestyle content
   - Age-restricted, compliance-heavy
   - CPM: $4.50-$12

2. **COPPA-Compliant Family Content** - 0.82 trust
   - Family-friendly, child-safe content
   - Zero tracking, age-gated
   - CPM: $8-$18

**When to Use**:
- Cookieless targeting strategies
- Brand safety critical
- Privacy-first approach
- Regulatory compliance required (alcohol, children)

**Advantages**: No consent needed, privacy-compliant, brand-safe.
**Limitations**: No behavioral optimization, moderate performance vs. audience signals.

---

### Audience

**User-Level Targeting (With Consent)**:

1. **Home Decor Purchase Intent** - 0.91 trust
   - First-party commerce intent
   - CPM: $8-$18, ROAS: 4.8x

2. **High-Value Financial Customer** - 0.89 trust
   - Banking relationship data
   - CPM: $25-$60, Lead quality: 4.2x

3. **Health Condition Management** - 0.76 trust
   - Cohort-level (1,000+ min), education focus
   - CPM: $12-$28

4. **Voter Engagement Political** - 0.73 trust
   - Public records + engagement
   - CPM: $6-$22

5. **Carbon-Neutral Consumer** - 0.81 trust
   - Verified sustainability actions
   - CPM: $14-$32, ROAS: 4.5-7.8x

**When to Use**:
- High-value customer acquisition
- Precision targeting needed
- Strong ROI focus
- Have consent infrastructure

**Advantages**: High precision, strong performance, targetable intent.
**Limitations**: Consent required, privacy obligations, smaller reach vs. contextual.

---

### Commerce

**Purchase Intent & Transaction Data**:

1. **Home Decor Purchase Intent** - 0.91 trust
   - Retail commerce intent
   - CPM: $8-$18, Conversion: 3.1-4.2%

2. **Luxury Purchase Intent** - 0.93 trust
   - Ultra-premium intent ($5K+)
   - CPM: $35-$85, ROAS: 18-45x

**When to Use**:
- Direct response campaigns
- Conversion optimization
- High-value product sales
- Full-funnel commerce

**Advantages**: Verified intent, strong conversion, high ROAS.
**Limitations**: Premium pricing, smaller reach, conversion focus only.

---

### Attention/Measurement

**Media Quality Signals**:

1. **Verified Attention Quality** - 0.94 trust
   - Eye-tracking calibrated measurement
   - CPM: $0.50-$2.00 (measurement fee)
   - Brand Lift Correlation: 0.89

**When to Use**:
- Brand awareness campaigns
- Media optimization
- Proving campaign effectiveness
- Premium inventory justification

**Advantages**: Objective quality metrics, transparent methodology, MRC accredited.
**Limitations**: Adds cost, no targeting (measurement only), requires SDK integration.

---

### Environmental

**Sustainability Signals**:

1. **Verified Sustainable Inventory** - 0.79 trust
   - Carbon-neutral media delivery
   - CPM: $3-$7.50 (includes offset)
   - Carbon: 0.8g CO2/impression offset

2. **Carbon-Neutral Consumer** - 0.81 trust
   - Verified sustainability actions (audience)
   - CPM: $14-$32

**When to Use**:
- ESG compliance campaigns
- Sustainability reporting
- Carbon-neutral goals
- Climate-conscious brand alignment

**Advantages**: ESG reporting value, verified environmental benefits, brand alignment.
**Limitations**: Limited scale, premium pricing, emerging standards.

---

## By Compliance Category

### General (Standard Compliance)

**Signals**:
- **Verified Attention Quality** - 0.94 trust
  - GDPR, CCPA, IAB, MRC standards
  - Autonomous operation, monthly audits

- **Home Decor Purchase Intent** - 0.91 trust
  - GDPR, CCPA, IAB GPP
  - Autonomous operation, quarterly audits

**Characteristics**: Standard privacy laws, broad use cases, low regulatory risk.

---

### Regulated (Industry-Specific Compliance)

**Signals**:
- **Premium Cocktail Contexts** - 0.88 trust
  - UK CAP, US DISCUS, EU AVMS
  - Age restrictions, human approval required

- **High-Value Financial Customer** - 0.89 trust
  - GLBA, FCRA, SOX, GDPR Article 9
  - Financial data protections, human approval required

- **Voter Engagement Political** - 0.73 trust
  - FECA, FEC, state election laws
  - Disclosure requirements, human approval required

- **Carbon-Neutral Consumer** - 0.81 trust
  - FTC Green Guides, EU Green Claims
  - Greenwashing prevention, human approval required

- **Luxury Purchase Intent** - 0.93 trust
  - GDPR, CCPA, brand standards
  - First activation approval only

**Characteristics**: Industry regulations, compliance verification, moderate-to-high risk.

---

### Restricted (Special Category Data)

**Signals**:
- **Health Condition Management** - 0.76 trust
  - HIPAA, FDA, EMA, GDPR Article 9
  - Cohort-level only, human approval every activation

- **COPPA-Compliant Family Content** - 0.82 trust
  - COPPA, GDPR-K, AADC
  - Zero tracking, human approval every activation

**Characteristics**: Protected classes (health, children), strict privacy laws, high risk, zero tolerance.

---

## By Use Case

### Brand Awareness

**Best Signals**:
1. **Verified Attention Quality** - 0.94 trust
   - Optimize for quality over quantity
   - Brand lift correlation: 0.89

2. **Premium Cocktail Contexts** - 0.88 trust (alcohol only)
   - Premium context adjacency
   - Brand lift: 8-14%

3. **COPPA-Compliant Family Content** - 0.82 trust (family brands)
   - Family brand awareness
   - High parent engagement

**Strategy**: Layer attention measurement with contextual targeting for brand-safe, high-quality placements.

---

### Direct Response / Conversion

**Best Signals**:
1. **Luxury Purchase Intent** - 0.93 trust
   - ROAS: 18-45x for ultra-premium
   - Conversion: 0.6-1.8%

2. **Home Decor Purchase Intent** - 0.91 trust
   - ROAS: 4.8x
   - Conversion: 3.1-4.2%

3. **Carbon-Neutral Consumer** - 0.81 trust
   - ROAS: 4.5-7.8x
   - Conversion: 2.2-3.8%

**Strategy**: Use high-intent commerce signals with strong conversion history. Optimize for ROAS, not reach.

---

### Lead Generation

**Best Signals**:
1. **High-Value Financial Customer** - 0.89 trust
   - Lead quality: 4.2x standard
   - High-value B2B/B2C leads

2. **Luxury Purchase Intent** - 0.93 trust
   - Qualified leads for premium products
   - Long sales cycles, high LTV

**Strategy**: Focus on lead quality over quantity. Long attribution windows (60-90 days).

---

### Education & Awareness (Non-Commercial)

**Best Signals**:
1. **Health Condition Management** - 0.76 trust
   - Patient education, disease awareness
   - Education downloads: 12-18%

2. **Voter Engagement Political** - 0.73 trust
   - Civic engagement, voter mobilization
   - Turnout lift: 3-8%

**Strategy**: Measure education engagement, not clicks. Long attribution, indirect ROI.

---

### ESG & Sustainability

**Best Signals**:
1. **Verified Sustainable Inventory** - 0.79 trust
   - Carbon-neutral delivery
   - ESG reporting value

2. **Carbon-Neutral Consumer** - 0.81 trust
   - Target verified climate-conscious consumers
   - 18% premium pricing acceptance

**Strategy**: Combine sustainable inventory with carbon-conscious audience for full sustainability alignment.

---

### Seasonal Campaigns

**Best Signals by Season**:

**Q4 Holiday**:
- **Home Decor Purchase Intent** - Peak gifting season
- **Luxury Purchase Intent** - Holiday luxury spending
- **COPPA-Compliant Family Content** - Toy season (Nov-Dec)
- **Carbon-Neutral Consumer** - Sustainable gifting

**Q1 New Year**:
- **Health Condition Management** - Wellness resolutions
- **Carbon-Neutral Consumer** - Sustainability resolutions

**Q2 Spring**:
- **Home Decor Purchase Intent** - Spring refresh
- **Luxury Purchase Intent** - Spring fashion

**Q3 Back-to-School**:
- **COPPA-Compliant Family Content** - Peak (Aug-Sep)
- **Health Condition Management** - Fall wellness

**Election Years**:
- **Voter Engagement Political** - Spikes near election day

---

## By CPM Range

### Budget-Friendly ($0.50-$12)

**Signals**:
1. **Verified Attention Quality** - $0.50-$2.00
   - Measurement fee (added to base CPM)
   - Very high trust (0.94)

2. **Verified Sustainable Inventory** - $3.00-$7.50
   - Includes carbon offset
   - High trust (0.79)

3. **Premium Cocktail Contexts** - $4.50-$12.00
   - Regulated but accessible
   - High trust (0.88)

4. **Voter Engagement Political** - $6.00-$22.00
   - Variable by election cycle
   - Limited trust (0.73)

**Best For**: Large reach campaigns, testing, early-stage brands, contextual strategies.

---

### Mid-Range ($8-$32)

**Signals**:
1. **Home Decor Purchase Intent** - $8.00-$18.00
   - Strong ROAS (4.8x)
   - Very high trust (0.91)

2. **COPPA-Compliant Family Content** - $8.00-$18.00
   - High safety, compliance included
   - High trust (0.82)

3. **Health Condition Management** - $12.00-$28.00
   - Education focus, compliance heavy
   - Limited trust (0.76)

4. **Carbon-Neutral Consumer** - $14.00-$32.00
   - Verified actions, niche
   - High trust (0.81)

**Best For**: Balanced reach/precision, standard commerce, regulated categories.

---

### Premium ($25-$85)

**Signals**:
1. **High-Value Financial Customer** - $25.00-$60.00
   - Lead quality: 4.2x
   - High trust (0.89)

2. **Luxury Purchase Intent** - $35.00-$85.00
   - ROAS: 18-45x
   - Very high trust (0.93)

**Best For**: High-value products, luxury brands, qualified lead generation, ultra-premium targeting.

**ROI Justification**: Transaction values ($45K-$180K) justify premium CPMs.

---

## Decision Tree Guide

### Start Here: What's Your Primary Objective?

#### 1. Brand Awareness
- **Q**: Need regulated category compliance?
  - **YES** → Alcohol? → **Premium Cocktail Contexts**
  - **YES** → Children/Family? → **COPPA-Compliant Family Content**
  - **NO** → Want quality measurement? → **Verified Attention Quality**

#### 2. Direct Response / Conversion
- **Q**: What's your average order value?
  - **$5K+** → **Luxury Purchase Intent**
  - **$200-$5K** → **Home Decor Purchase Intent** (or similar commerce)
  - **Sustainable Product?** → **Carbon-Neutral Consumer**

#### 3. Lead Generation
- **Q**: What's your target customer value?
  - **High-Value ($50K+)** → **High-Value Financial Customer**
  - **Luxury Products** → **Luxury Purchase Intent**
  - **Standard B2B/B2C** → **Home Decor Purchase Intent** (adapt)

#### 4. Education / Awareness (Non-Commercial)
- **Q**: What's your focus?
  - **Healthcare/Patient Education** → **Health Condition Management**
  - **Political/Civic** → **Voter Engagement Political**

#### 5. ESG / Sustainability
- **Q**: What's your priority?
  - **Carbon-Neutral Campaign** → **Verified Sustainable Inventory**
  - **Target Eco-Conscious** → **Carbon-Neutral Consumer**
  - **Both** → Use both signals together

---

### Filter by Constraints:

#### Budget Constraint?
- **Tight Budget** → **Verified Attention Quality**, **Premium Cocktail Contexts**, **Voter Engagement Political**
- **Moderate Budget** → **Home Decor Purchase Intent**, **COPPA-Compliant Family Content**, **Carbon-Neutral Consumer**
- **Premium Budget** → **High-Value Financial Customer**, **Luxury Purchase Intent**

#### Compliance Requirements?
- **Healthcare** → **Health Condition Management** (HIPAA)
- **Financial** → **High-Value Financial Customer** (GLBA/FCRA)
- **Alcohol** → **Premium Cocktail Contexts** (Age restrictions)
- **Children** → **COPPA-Compliant Family Content** (COPPA)
- **Political** → **Voter Engagement Political** (Election law)
- **Environmental Claims** → **Carbon-Neutral Consumer** (FTC Green Guides)

#### Privacy/Consent Preference?
- **Privacy-First (No User Data)** → **Premium Cocktail Contexts**, **COPPA-Compliant Family Content**, **Verified Attention Quality**
- **First-Party with Consent** → **Home Decor Purchase Intent**, **Luxury Purchase Intent**, **High-Value Financial Customer**
- **Aggregated Only** → **Health Condition Management**, **Verified Sustainable Inventory**

#### Governance Tolerance?
- **Autonomous Operation** → **Verified Attention Quality**, **Home Decor Purchase Intent**, **Verified Sustainable Inventory**
- **First Activation Approval** → **Luxury Purchase Intent**
- **Every Activation Approval** → All Regulated/Restricted signals

---

## Quick Reference Matrix

| Signal | Trust | CPM | Approval | Audit | Best For |
|--------|-------|-----|----------|-------|----------|
| Verified Attention Quality | 0.94 | $0.50-$2 | No | Monthly | Media optimization |
| Luxury Purchase Intent | 0.93 | $35-$85 | First only | Quarterly | Ultra-premium ($5K+) |
| Home Decor Purchase Intent | 0.91 | $8-$18 | No | Quarterly | Retail commerce |
| High-Value Financial Customer | 0.89 | $25-$60 | Every | Per + Monthly | Financial, luxury |
| Premium Cocktail Contexts | 0.88 | $4.50-$12 | Every | Per activation | Alcohol advertising |
| COPPA-Compliant Family | 0.82 | $8-$18 | Every | Per + Weekly | Children's products |
| Carbon-Neutral Consumer | 0.81 | $14-$32 | Every | Quarterly + Annual | Sustainable products |
| Verified Sustainable Inventory | 0.79 | $3-$7.50 | No | Monthly | ESG campaigns |
| Health Condition Management | 0.76 | $12-$28 | Every | Per + Quarterly | Patient education |
| Voter Engagement Political | 0.73 | $6-$22 | Every | Per + Ongoing + Post | Political campaigns |

---

## Additional Resources

### Documentation
- [Signal Catalog](SIGNAL-CATALOG.md) - Detailed signal descriptions
- [Examples README](README.md) - Technical overview
- [Protocol Specification](../specs/opensignals-v0.1.md)

### Integration
- [API Documentation](../docs/api-integration.md)
- [Governance Integration](../docs/governance-integration.md)

### Support
- **GitHub Issues**: https://github.com/Samrajtheailyceum/opensignals-protocol/issues
- **Discussions**: https://github.com/Samrajtheailyceum/opensignals-protocol/discussions

---

**Document Version**: 1.0
**Last Updated**: 2026-05-11
**Maintained By**: OpenSignals Protocol Working Group
