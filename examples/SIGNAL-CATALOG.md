# OpenSignals Protocol - Signal Catalog

**Version**: 0.1
**Last Updated**: 2026-05-11
**Status**: Active

This catalog provides comprehensive documentation for all OpenSignals example manifests, explaining what each signal represents, who uses it, trust scoring rationale, governance requirements, and real-world applications.

---

## Table of Contents

1. [Existing Signals](#existing-signals)
   - [Premium Cocktail & Spirits Content Contexts](#1-premium-cocktail--spirits-content-contexts)
   - [Verified Attention Quality Measurement](#2-verified-attention-quality-measurement)
   - [Home Decor Purchase Intent Audience](#3-home-decor-purchase-intent-audience)
   - [Verified Sustainable Advertising Inventory](#4-verified-sustainable-advertising-inventory)

2. [Advanced Signals](#advanced-signals)
   - [High-Value Financial Services Customer Signal](#5-high-value-financial-services-customer-signal)
   - [Health Condition Management Signal](#6-health-condition-management-signal)
   - [COPPA-Compliant Family Content Signal](#7-coppa-compliant-family-content-signal)
   - [Voter Engagement Political Signal](#8-voter-engagement-political-signal)
   - [Luxury Purchase Intent Signal](#9-luxury-purchase-intent-signal)
   - [Carbon-Neutral Consumer Signal](#10-carbon-neutral-consumer-signal)

3. [Trust Score Methodology](#trust-score-methodology)
4. [Governance Framework](#governance-framework)
5. [Compliance Matrix](#compliance-matrix)
6. [Performance Benchmarks](#performance-benchmarks)

---

## Existing Signals

### 1. Premium Cocktail & Spirits Content Contexts

**File**: `alcohol-contextual-signal.json`
**Signal ID**: `premium-cocktail-contexts`
**Signal Type**: Contextual

#### What It Represents
A page-level contextual signal that identifies premium content environments suitable for spirits and cocktail advertising. Uses semantic analysis to classify editorial content about food, drink, lifestyle, and premium entertainment.

#### Who Uses It
- **Primary Users**: Premium spirits brands (whisky, vodka, gin, craft cocktails)
- **Secondary Users**: Wine brands, beer brands, hospitality advertisers
- **Industries**: Alcohol beverage, luxury lifestyle, travel & hospitality

#### Target Audience Profile
- Age: 25-65 (age-gated by market requirements)
- Interests: Premium dining, cocktail culture, entertaining, luxury lifestyle
- Content Context: Food & drink editorial, recipe sites, lifestyle magazines, entertainment venues

#### Trust Score Breakdown: 0.88

**Why This Score?**

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Coverage | 0.85 | Large reach (45M) but limited to premium content categories |
| Freshness | 0.95 | Hourly updates ensure current content classification |
| Precision | 0.87 | High accuracy in identifying suitable contexts, minimal false positives |
| Explainability | 0.92 | Clear NLP methodology, transparent taxonomy mapping |
| Compliance Safety | 0.94 | Strong compliance with UK CAP Code and US DISCUS standards |
| Outcome Relevance | 0.78 | Good performance but contextual signals show moderate lift vs. behavioral |

**Overall**: 0.88 - Highly trusted but requires governance due to regulated category.

#### Governance Requirements

**Category**: Regulated - Alcohol
**Human Approval Required**: YES
**Why**: Alcohol advertising is strictly regulated in most markets with age restrictions, content adjacency rules, and appeal restrictions.

**Approval Workflow**:
1. Brand legal team review
2. Compliance officer sign-off
3. Market-specific regulatory check
4. Content adjacency verification
5. Age-gating verification

**Audit Frequency**: Per activation (every campaign)
**Risk Level**: Medium-High

**Market Restrictions**:
- **Prohibited**: Saudi Arabia (SA), United Arab Emirates (AE), Iraq (IQ)
- **Age-Restricted**: US (21+), GB (18+), FR (18+), DE (18+), AU (18+), CA (19+), JP (20+)

#### Compliance Frameworks
- UK CAP Code (Committee of Advertising Practice)
- US DISCUS Code of Responsible Practices
- EU Audiovisual Media Services Directive
- Portman Group Code of Practice

#### Real-World Use Cases

**Use Case 1: Premium Whisky Brand - UK Launch**
- **Scenario**: Scottish single malt launching limited edition
- **Target**: Premium food & drink editorial, lifestyle content
- **Outcome**: 3.2x higher engagement vs. run-of-network, zero compliance issues
- **Why This Signal**: Contextual targeting avoids behavioral tracking while maintaining brand safety

**Use Case 2: Craft Cocktail Bar - Local Campaign**
- **Scenario**: High-end cocktail bar promoting mixology classes
- **Target**: Recipe sites, entertaining content, local food blogs
- **Outcome**: 42% conversion rate for event registrations
- **Why This Signal**: Reaches engaged audience in relevant mindset

**Use Case 3: Global Spirits Brand - Responsible Marketing**
- **Scenario**: Premium vodka brand with strict internal policies
- **Target**: Only premium contexts, no youth-adjacent content
- **Outcome**: Full compliance, premium placement quality
- **Why This Signal**: Built-in brand safety categories prevent risky placements

#### When to Use vs. Alternatives

**Use This Signal When**:
- Advertising in regulated alcohol category
- Need brand safety and compliance guarantees
- Targeting premium, context-relevant environments
- Cookie-less/privacy-first approach required
- Operating in multiple international markets

**Use Alternatives When**:
- Need behavioral/audience targeting (use first-party data signals)
- Want broader reach beyond premium content (use broader contextual)
- Targeting specific demographics (use demographic signals with age verification)
- Need real-time bidding optimization (use attention signals)

**Complementary Signals**:
- Combine with attention measurement for premium inventory quality
- Layer with first-party CRM for existing customer suppression
- Use with geographic signals for local market targeting

#### Expected Performance Outcomes

**Typical Performance Metrics**:
- **CTR**: 0.45-0.72% (2.1x industry average for alcohol)
- **Brand Lift**: 8-14% aided awareness
- **Completion Rate** (video): 78-85%
- **Viewability**: 82-89%
- **Brand Safety**: 99.7% suitable content

**ROI Profile**: Medium-High
- Higher CPMs ($4.50-$12.00) but strong engagement
- Lower frequency needed due to contextual relevance
- Premium placement quality justifies cost

**Optimization Tips**:
- Layer with time-of-day targeting (evening/weekend performs better)
- Combine with seasonal content (holidays, entertaining seasons)
- Test creative messaging in premium vs. casual contexts

#### Technical Integration

**Activation Method**: API endpoint with HTTP Message Signatures
**Rate Limits**: 100 req/min, 10,000 req/day
**Latency**: < 200ms
**Match Rate**: N/A (contextual, page-level)

---

### 2. Verified Attention Quality Measurement

**File**: `attention-signal.json`
**Signal ID**: `verified-attention-quality`
**Signal Type**: Attention

#### What It Represents
A measurement signal that predicts and tracks human attention quality across display and video inventory. Uses eye-tracking-calibrated models to score each ad placement based on active engagement time, viewability, interaction depth, and attention quality.

#### Who Uses It
- **Primary Users**: Media buying agencies, trading desks, DSPs
- **Secondary Users**: Publishers (for inventory quality assessment), Advertisers (for campaign optimization)
- **Industries**: All verticals using digital advertising

#### Target Use Cases
- Campaign optimization and real-time bidding
- Media quality assessment and inventory selection
- Performance reporting and attribution modeling
- Publisher inventory quality benchmarking

#### Trust Score Breakdown: 0.94

**Why This Score?**

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Coverage | 0.89 | Very large reach (125M) across 850+ publishers, 16 markets |
| Freshness | 0.98 | Real-time measurement with <150ms latency |
| Precision | 0.93 | 96% measurement accuracy validated against eye-tracking |
| Explainability | 0.95 | Transparent methodology, published research, clear model weights |
| Compliance Safety | 0.97 | Privacy-preserving, no PII, explicit opt-in, MRC accredited |
| Outcome Relevance | 0.91 | Strong correlation with brand lift (0.89 correlation coefficient) |

**Overall**: 0.94 - Very high trust due to third-party validation and transparent methodology.

#### Governance Requirements

**Category**: Measurement - Attention Quality
**Human Approval Required**: NO
**Why**: Measurement signals with explicit consent and privacy-preserving methods can operate autonomously.

**Audit Frequency**: Monthly
**Risk Level**: Low

**No Market Restrictions**: Operates globally with privacy compliance

#### Compliance Frameworks
- MRC Invalid Traffic Detection Standards
- MRC Attention Measurement Standards
- IAB Measurement Guidelines
- GDPR (EU privacy regulation)
- CCPA (California privacy law)

#### Real-World Use Cases

**Use Case 1: Auto Brand - Premium Video Campaign**
- **Scenario**: Luxury car brand prioritizing quality over reach
- **Target**: High-attention video inventory only (>0.75 attention score)
- **Outcome**: 18% brand lift vs. 7% on standard inventory, 2.4x efficiency
- **Why This Signal**: Pay premium for guaranteed attention quality

**Use Case 2: Performance Advertiser - Display Optimization**
- **Scenario**: E-commerce advertiser optimizing for conversions
- **Target**: Real-time bid adjustment based on attention prediction
- **Outcome**: 31% conversion rate improvement, 15% lower CPA
- **Why This Signal**: Real-time signal allows dynamic bidding optimization

**Use Case 3: Publisher - Inventory Packaging**
- **Scenario**: Premium publisher creating attention-verified packages
- **Target**: Package top-performing placements by attention metrics
- **Outcome**: 40% CPM premium for verified high-attention inventory
- **Why This Signal**: Differentiate inventory with objective quality metrics

**Use Case 4: Agency - Campaign Reporting**
- **Scenario**: Agency proving campaign effectiveness beyond clicks
- **Target**: Report attention time as proxy for brand impact
- **Outcome**: Client renewal rate +22%, upsell to premium inventory
- **Why This Signal**: Demonstrate value with attention-based metrics

#### When to Use vs. Alternatives

**Use This Signal When**:
- Optimizing for brand awareness and consideration
- Need objective media quality measurement
- Justifying premium inventory investment
- Moving beyond click-based optimization
- Proving campaign effectiveness to stakeholders

**Use Alternatives When**:
- Only need basic viewability (use MRC viewability standard)
- Cost is primary constraint (attention measurement adds CPM fee)
- Direct response campaigns focused solely on conversions
- Testing phase with limited budget

**Complementary Signals**:
- Layer with contextual signals for brand-safe + high-attention inventory
- Combine with commerce intent signals for full-funnel optimization
- Use with brand lift studies for validation

#### Expected Performance Outcomes

**Typical Performance Metrics**:
- **Average Attention Time**: 8.7 seconds (industry benchmark: 5.2 seconds)
- **Attention Quality Score**: 0.82 average
- **Brand Lift Correlation**: 0.89 (high predictive value)
- **Viewability**: 92% (higher than standard inventory)

**ROI Profile**: High
- Adds $0.50-$2.00 CPM measurement fee
- Delivers 2-3x better brand lift per dollar
- Reduces wasted impressions by 35-45%

**Optimization Tips**:
- Set attention score thresholds by campaign objective (0.6 for reach, 0.8 for branding)
- Use attention-weighted frequency capping
- Optimize creative for high-attention placements
- Report attention time instead of impressions to stakeholders

#### Technical Integration

**Activation Method**: SDK integration + API reporting
**Rate Limits**: 500 req/min, 100,000 req/day
**Latency SLA**: 150ms
**SDK Versions**: JavaScript 3.2.1, iOS 2.8.0, Android 2.7.5

**Measurement Methodology**:
- **40%** Active visible time
- **30%** Interaction depth (scroll, hover, click)
- **20%** Viewability quality
- **10%** Content completion

---

### 3. Home Decor Purchase Intent Audience

**File**: `retail-commerce-signal.json`
**Signal ID**: `home-decor-purchase-intent`
**Signal Type**: Commerce

#### What It Represents
First-party audience signal identifying authenticated users with demonstrated purchase intent for home decor and furnishings. Built from browsing behavior, cart activity, wishlist engagement, and transaction history across a premium home goods retailer network.

#### Who Uses It
- **Primary Users**: Home goods brands, furniture retailers, interior design services
- **Secondary Users**: Home improvement retailers, moving services, real estate advertisers
- **Industries**: Retail, home furnishings, interior design, home services

#### Target Audience Profile
- **Demographics**: 28-65 years old, 78% homeowners, household income index 125
- **Intent Signals**: Product views, cart adds, wishlists, reviews, past purchases
- **Segment Size**: 850,000 average (refreshed daily)
- **Lookback Period**: 30 days

#### Trust Score Breakdown: 0.91

**Why This Score?**

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Coverage | 0.78 | Medium reach (8.5M) focused on quality over quantity |
| Freshness | 0.93 | Daily updates capture recent intent signals |
| Precision | 0.94 | Very high accuracy from first-party transaction data |
| Explainability | 0.90 | Clear intent indicators, transparent methodology |
| Compliance Safety | 0.96 | Explicit opt-in, GDPR/CCPA compliant, user transparency portal |
| Outcome Relevance | 0.88 | Strong conversion performance (4.8x ROAS average) |

**Overall**: 0.91 - Highly trusted first-party signal with explicit consent and strong performance.

#### Governance Requirements

**Category**: Commerce - Purchase Intent
**Human Approval Required**: NO
**Why**: First-party data with explicit consent and clear usage terms can operate autonomously.

**Audit Frequency**: Quarterly
**Risk Level**: Low-Medium

**Geographic Restrictions**: GDPR-compliant processing for EU users

#### Compliance Frameworks
- GDPR (General Data Protection Regulation)
- CCPA (California Consumer Privacy Act)
- IAB GPP (Global Privacy Platform)
- ePrivacy Directive (EU cookie law)

#### Real-World Use Cases

**Use Case 1: Furniture Brand - New Product Launch**
- **Scenario**: Mid-century modern furniture line targeting active shoppers
- **Target**: High-intent segment (cart adds, wishlists in past 14 days)
- **Outcome**: 6.2% conversion rate, $425 average order value, 5.8x ROAS
- **Why This Signal**: Recent, verified purchase intent drives high conversion

**Use Case 2: Interior Design Service - Lead Generation**
- **Scenario**: Design consultation service targeting room renovation projects
- **Target**: Medium-intent segment (multiple room category views)
- **Outcome**: 8.3% lead capture rate, 42% consultation booking rate
- **Why This Signal**: Multi-category browsing indicates larger project intent

**Use Case 3: Home Decor Retailer - Competitive Conquest**
- **Scenario**: Retailer targeting competitor's browsing customers
- **Target**: Browsing-intent segment from competitor network sites
- **Outcome**: 12% consideration lift, 3.4% new customer acquisition
- **Why This Signal**: Capture in-market shoppers before purchase decision

**Use Case 4: Moving Services - Lifecycle Targeting**
- **Scenario**: Moving company targeting new homeowners furnishing homes
- **Target**: High-intent segment with large basket values
- **Outcome**: 2.1% conversion rate for moving service bookings
- **Why This Signal**: Furniture purchase intent indicates moving/relocation

#### When to Use vs. Alternatives

**Use This Signal When**:
- Need high-quality commerce intent with strong conversion rates
- Have sufficient budget for premium CPMs ($8-$18)
- Want first-party data with transparent provenance
- Targeting full-funnel conversion campaigns
- Need privacy-compliant audience targeting

**Use Alternatives When**:
- Need broader reach (use contextual signals)
- Budget-constrained (use lower-cost behavioral signals)
- Early awareness stage (use interest-based audiences)
- Geographic targeting outside covered markets

**Complementary Signals**:
- Layer with contextual home/lifestyle content
- Combine with attention signals for premium inventory quality
- Use for lookalike modeling to expand reach
- Suppress existing customers with CRM matching

#### Expected Performance Outcomes

**Typical Performance Metrics**:
- **CTR**: 1.2-2.8% (2.4x industry average for home goods)
- **Conversion Rate**: 3.1-4.2%
- **Average Order Value**: $285
- **ROAS**: 4.8x average
- **Conversion Uplift vs. Benchmark**: 2.8x

**ROI Profile**: Very High
- Premium CPMs justified by conversion performance
- High average order values
- Strong repeat purchase behavior

**Optimization Tips**:
- Target high-intent tier for conversion campaigns ($18 CPM)
- Use medium-intent for consideration/nurture ($12 CPM)
- Suppress recent purchasers (0-30 days)
- Retarget cart abandoners with dynamic product ads
- Test seasonal patterns (spring/fall higher intent)

#### Technical Integration

**Activation Method**: OAuth2 API with segment IDs or audience lists
**Rate Limits**: 60 req/min, 5,000 req/day
**Match Rate**: 72% average
**Supported ID Types**: Hashed email (SHA256), mobile ad ID, first-party cookie ID
**Delivery Format**: Segment ID or audience list export

---

### 4. Verified Sustainable Advertising Inventory

**File**: `sustainability-signal.json`
**Signal ID**: `verified-sustainable-inventory`
**Signal Type**: Environmental

#### What It Represents
Environmental impact signal identifying advertising inventory with verified carbon-neutral delivery. Includes publisher carbon footprint assessment, renewable energy verification, and supply chain emissions tracking. Enables brands to align advertising with sustainability commitments and ESG goals.

#### Who Uses It
- **Primary Users**: Brands with net-zero commitments, sustainability-focused companies
- **Secondary Users**: Agencies managing ESG portfolios, publishers demonstrating green credentials
- **Industries**: Consumer goods, technology, automotive, financial services (any with ESG commitments)

#### Target Use Cases
- Carbon-neutral media campaigns
- ESG reporting and sustainability documentation
- Brand alignment with environmental values
- Supply chain emissions reduction (Scope 3)

#### Trust Score Breakdown: 0.79

**Why This Score?**

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Coverage | 0.62 | Limited reach (18M) as emerging standard, 145 certified publishers |
| Freshness | 0.85 | Monthly updates balance verification rigor with currency |
| Precision | 0.81 | Third-party audited but carbon measurement has inherent uncertainty |
| Explainability | 0.88 | Clear methodology following GHG Protocol standards |
| Compliance Safety | 0.91 | Strong adherence to ISO 14064 and carbon neutrality standards |
| Outcome Relevance | 0.74 | Delivers on sustainability promise but emerging performance data |

**Overall**: 0.79 - Trusted with governance checks. Lower score reflects emerging nature of carbon measurement standards, limited scale, and ongoing methodology refinement.

#### Governance Requirements

**Category**: Environmental - Carbon Neutral Inventory
**Human Approval Required**: NO
**Why**: Environmental signals with third-party verification can operate autonomously.

**Audit Frequency**: Monthly (carbon audits)
**Risk Level**: Low

**No Geographic Restrictions**: Global application

#### Compliance Frameworks
- GHG Protocol Scope 3 (emissions measurement)
- Science Based Targets Initiative (SBTi)
- ISO 14064 (greenhouse gas accounting)
- PAS 2060 (carbon neutrality)
- Ad Net Zero (industry initiative)

#### Real-World Use Cases

**Use Case 1: Consumer Electronics - Net Zero Campaign**
- **Scenario**: Tech company with 2030 net-zero commitment
- **Target**: 100% verified sustainable inventory for product launch
- **Outcome**: Carbon-neutral campaign, ESG report inclusion, 8% brand favorability lift
- **Why This Signal**: Enables credible sustainability claims with third-party verification

**Use Case 2: Automotive - EV Launch Campaign**
- **Scenario**: Electric vehicle manufacturer emphasizing environmental credentials
- **Target**: Sustainable inventory aligned with product positioning
- **Outcome**: Message resonance +14%, reduced Scope 3 emissions by 2,400kg CO2
- **Why This Signal**: Walk the talk - advertise sustainably for sustainable products

**Use Case 3: Financial Services - ESG Portfolio**
- **Scenario**: Investment firm marketing sustainable investment funds
- **Target**: Carbon-neutral inventory for brand integrity
- **Outcome**: Inclusion in annual ESG report, investor confidence boost
- **Why This Signal**: Demonstrate commitment across all business activities

**Use Case 4: Retail Brand - Sustainability Report**
- **Scenario**: Fashion retailer with detailed carbon accounting requirements
- **Target**: All digital advertising through sustainable inventory
- **Outcome**: 12,500kg CO2 offset documented for annual report
- **Why This Signal**: Quantifiable, audited emissions data for Scope 3 reporting

#### When to Use vs. Alternatives

**Use This Signal When**:
- Have net-zero or carbon-neutral commitments
- Need Scope 3 emissions reporting for advertising
- Want third-party verified environmental claims
- Targeting sustainability-conscious consumers
- ESG reporting requirements apply

**Use Alternatives When**:
- Cost is primary constraint (adds $0.50-$2.00 CPM premium)
- Maximum reach is priority (limited publisher scale)
- No sustainability reporting requirements
- Early testing phase (small budget)

**Complementary Signals**:
- Combine with sustainability-focused audience signals
- Layer with contextual environmental content targeting
- Use for brand campaigns (awareness/consideration)

#### Expected Performance Outcomes

**Typical Performance Metrics**:
- **CTR**: Comparable to standard inventory (no significant lift/drop)
- **Viewability**: 85-90% (high-quality publishers)
- **Brand Favorability**: +5-8% lift among sustainability-conscious consumers
- **Carbon Offset**: Average 0.8g CO2 per impression

**ROI Profile**: Medium
- Premium CPMs ($3-$7.50) for carbon offset inclusion
- Brand value and ESG compliance justify cost
- Growing publisher adoption expanding scale

**ESG Reporting Value**:
- **Carbon Footprint**: Detailed impression-level tracking
- **Renewable Energy**: Publisher-level percentage reporting
- **Offsets**: Verified through Gold Standard credits
- **Third-Party Audit**: Monthly Carbon Trust reports

#### Technical Integration

**Activation Method**: API key authentication
**Rate Limits**: 50 req/min, 5,000 req/day
**Carbon Reporting**: Real-time and monthly aggregated
**ESG Export**: Formatted reports for sustainability disclosures

---

## Advanced Signals

### 5. High-Value Financial Services Customer Signal

**File**: `financial-services-signal.json`
**Signal ID**: `high-value-financial-customer`
**Signal Type**: Audience

#### What It Represents
Premium audience signal identifying authenticated banking customers with indicators of wealth, investment activity, and financial product interest. Built from first-party banking relationship data, transaction patterns (aggregated/anonymized), and financial product engagement. Strict privacy controls and compliance oversight.

#### Who Uses It
- **Primary Users**: Financial institutions (banks, wealth management, investment firms)
- **Secondary Users**: Luxury brands, premium insurance, high-end automotive
- **Industries**: Financial services, luxury goods, premium travel, private education

#### Target Audience Profile
- **Wealth Indicators**: High account balances, investment portfolios, premium banking tier
- **Financial Behaviors**: Active trading, mortgage/loan products, wealth management engagement
- **Demographics**: 35-70 years old, high-net-worth individuals (HNWIs)
- **Segment Size**: 450,000 (highly selective)

#### Trust Score Breakdown: 0.89

**Why This Score?**

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Coverage | 0.71 | Limited reach by design (HNWIs only), high selectivity |
| Freshness | 0.92 | Weekly updates balance currency with privacy/compliance review |
| Precision | 0.95 | Very high accuracy from verified financial relationship data |
| Explainability | 0.87 | Clear indicators but some aggregation for privacy protection |
| Compliance Safety | 0.98 | Exceptional compliance: SOX, GLBA, FCRA, KYC, human approval required |
| Outcome Relevance | 0.86 | Strong performance but limited historical data due to strict controls |

**Overall**: 0.89 - Highly trusted but requires significant governance due to financial data sensitivity.

#### Governance Requirements

**Category**: Regulated - Financial Services
**Human Approval Required**: YES (MANDATORY)
**Why**: Financial data is highly sensitive with strict regulatory requirements. Every activation requires compliance officer approval.

**Approval Workflow**:
1. Legal team review of use case
2. Compliance officer verification of permitted use
3. Privacy team assessment of data handling
4. Risk management sign-off
5. Senior executive approval for first-time use cases

**Audit Frequency**: Per activation + monthly comprehensive audit
**Risk Level**: High

**Market-Specific Requirements**:
- **US**: GLBA compliance, FCRA adherence (no credit decisioning)
- **EU**: GDPR Article 9 special category data protections
- **GB**: FCA financial promotion rules
- **Global**: AML/KYC considerations, prohibition on discriminatory use

#### Compliance Frameworks
- GLBA (Gramm-Leach-Bliley Act) - US financial privacy
- FCRA (Fair Credit Reporting Act) - US credit data protections
- SOX (Sarbanes-Oxley) - Financial data integrity
- GDPR Article 9 - Special category data
- FCA Handbook - UK financial advertising
- PCI DSS - Payment data security

#### Real-World Use Cases

**Use Case 1: Wealth Management Firm - HNWI Acquisition**
- **Scenario**: Investment advisory firm targeting affluent investors
- **Target**: High-net-worth segment with active investment behavior
- **Outcome**: 2.1% consultation booking rate, $2.4M AUM from 47 new clients, 11:1 ROI
- **Why This Signal**: Verified financial capacity ensures qualified lead quality

**Use Case 2: Luxury Automotive - Private Banking Partnership**
- **Scenario**: Ultra-luxury car brand (>$200K vehicles) targeting qualified buyers
- **Target**: Top-tier banking customers with documented purchasing power
- **Outcome**: 8.4% dealership visit rate, 0.7% conversion to purchase, $850K revenue
- **Why This Signal**: Financial verification eliminates unqualified leads

**Use Case 3: Premium Travel - First-Class Targeting**
- **Scenario**: Airline promoting first-class and business-class long-haul routes
- **Target**: Affluent segment with international transaction patterns
- **Outcome**: 3.2% booking rate, $8,500 average booking value, 6.2x ROAS
- **Why This Signal**: Financial indicators correlate with premium travel propensity

**Use Case 4: Private Education - Executive MBA Program**
- **Scenario**: Business school targeting self-funded executive education
- **Target**: High-income professionals with career investment indicators
- **Outcome**: 12% information request rate, 1.8% enrollment rate, 4.1x ROAS
- **Why This Signal**: Financial capacity indicates ability to self-fund $150K program

#### When to Use vs. Alternatives

**Use This Signal When**:
- Selling high-value products/services ($50K+)
- Need verified financial qualification
- Can meet strict compliance requirements
- Have legal/compliance team support
- Targeting legitimate financial services or luxury products

**NEVER Use This Signal For**:
- Credit decisioning or lending (FCRA violation)
- Employment screening (FCRA violation)
- Insurance underwriting (discriminatory)
- Predatory targeting of vulnerable populations
- Any prohibited use cases under GLBA/FCRA

**Use Alternatives When**:
- Broader reach needed (use interest-based audiences)
- Cannot meet compliance requirements
- Lower-value products
- Budget constraints (premium CPMs $25-$60)

**Complementary Signals**:
- Layer with attention signals for high-value placements
- Combine with luxury lifestyle contextual targeting
- Use geographic signals for wealth-concentrated areas

#### Expected Performance Outcomes

**Typical Performance Metrics**:
- **CTR**: 0.8-1.4% (quality over quantity)
- **Lead Quality**: 4.2x higher than standard audiences
- **Conversion Rate**: 2-4% for high-consideration purchases
- **Average Transaction Value**: $45,000-$180,000
- **Customer Lifetime Value**: 5.8x standard customer

**ROI Profile**: Very High (for appropriate use cases)
- Premium CPMs ($25-$60) justified by transaction values
- Long sales cycles but high conversion values
- Strong customer lifetime value

**Optimization Tips**:
- Use for high-value products only (justify CPM cost)
- Long attribution windows (60-90 days) for considered purchases
- Frequency cap at 2-3 impressions (affluent audiences resist oversaturation)
- Premium creative and messaging required (audience sophistication)
- Test seasonal patterns (Q4 higher financial activity, Q1 tax planning)

#### Technical Integration

**Activation Method**: OAuth2 + Multi-factor authentication
**Rate Limits**: 20 req/min, 1,000 req/day (intentionally restricted)
**Match Rate**: 65% average (privacy protections limit matching)
**Supported ID Types**: Hashed email (SHA256 only), secure customer ID
**Security**: TLS 1.3, encrypted data transfer, audit logging

**Special Requirements**:
- Signed Data Processing Agreement required
- Annual compliance audit mandatory
- Quarterly usage review meetings
- Real-time anomaly detection and alerts

---

### 6. Health Condition Management Signal

**File**: `pharmaceutical-signal.json`
**Signal ID**: `health-condition-management`
**Signal Type**: Audience

#### What It Represents
Privacy-preserving signal identifying individuals with interest in managing specific health conditions. Built from aggregated, de-identified health content engagement, pharmacy loyalty programs (opt-in), and wellness app data. Designed for disease awareness and treatment education advertising, NOT individual targeting.

#### Who Uses It
- **Primary Users**: Pharmaceutical manufacturers (disease awareness campaigns)
- **Secondary Users**: Healthcare providers, medical device manufacturers, health insurance
- **Industries**: Pharmaceuticals, healthcare, wellness, medical devices

#### Target Audience Profile
- **Health Interests**: Chronic condition management (diabetes, hypertension, arthritis, etc.)
- **Engagement**: Health content consumption, symptom checkers, wellness apps
- **Aggregation**: Cohort-level only (minimum 1,000 individuals per segment)
- **No Individual Profiling**: Privacy-preserving aggregation prevents individual targeting

#### Trust Score Breakdown: 0.76

**Why This Score?**

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Coverage | 0.68 | Moderate reach (12M) with strict privacy aggregation requirements |
| Freshness | 0.81 | Bi-weekly updates balance currency with privacy review |
| Precision | 0.79 | Moderate accuracy due to required aggregation and privacy protections |
| Explainability | 0.84 | Clear methodology but some opacity for privacy compliance |
| Compliance Safety | 0.95 | Exceptional HIPAA, GDPR health data protections, ethics review |
| Outcome Relevance | 0.68 | Good for awareness/education, limited direct response (by design) |

**Overall**: 0.76 - Trusted with governance checks. Lower score reflects privacy-first design that prioritizes compliance over precision, and emerging nature of health data advertising.

#### Governance Requirements

**Category**: Regulated - Healthcare/Pharmaceutical
**Human Approval Required**: YES (MANDATORY)
**Why**: Health data is protected under HIPAA (US), GDPR Article 9 (EU), and other regulations. Medical advertising has strict FDA/EMA rules. Ethics oversight required.

**Approval Workflow**:
1. Medical/scientific review of campaign claims
2. Legal review for FDA/EMA compliance
3. Privacy officer review of data handling
4. Ethics committee review (internal or external)
5. Compliance officer final approval

**Audit Frequency**: Per activation + quarterly comprehensive review
**Risk Level**: High

**Market-Specific Requirements**:
- **US**: HIPAA compliance, FDA advertising regulations, no individual PHI
- **EU**: GDPR Article 9 special category data, no individual health profiling
- **Global**: No targeting of minors, no discrimination, educational messaging only

#### Compliance Frameworks
- HIPAA (Health Insurance Portability and Accountability Act) - US
- FDA Regulations on Prescription Drug Advertising - US
- EMA Guidelines on Advertising of Medicinal Products - EU
- GDPR Article 9 (Special Category Data) - EU
- PhRMA Code on Interactions with Healthcare Professionals
- EFPIA Code of Practice - EU

#### Real-World Use Cases

**Use Case 1: Diabetes Management - Disease Awareness**
- **Scenario**: Pharmaceutical company promoting diabetes education, not specific drug
- **Target**: Cohort interested in diabetes management content (10,000+ individuals)
- **Outcome**: 42% website visit rate for educational resources, 8% HCP discussion tool downloads
- **Why This Signal**: HIPAA-compliant awareness campaign without individual profiling

**Use Case 2: Arthritis Treatment - Undiagnosed Patient Education**
- **Scenario**: Pharma manufacturer educating about arthritis symptoms and treatment options
- **Target**: Aggregate audience engaging with joint pain content
- **Outcome**: 18% symptom checker usage, 6% physician finder tool usage
- **Why This Signal**: Educational messaging to potentially undiagnosed patients (ethical)

**Use Case 3: Heart Health - Preventive Care Campaign**
- **Scenario**: Cardiology device manufacturer promoting heart health awareness
- **Target**: Cohort interested in cardiovascular health management
- **Outcome**: 24% healthy lifestyle guide downloads, 5% cardiac screening locator usage
- **Why This Signal**: Public health benefit with privacy protections

**Use Case 4: Mental Health - Treatment Awareness**
- **Scenario**: Antidepressant manufacturer promoting treatment options (FDA-approved messaging)
- **Target**: Aggregate audience engaging with mental health support content
- **Outcome**: 15% mental health screening tool usage, 8% treatment discussion guide requests
- **Why This Signal**: Reduces stigma, promotes treatment-seeking (ethical outcome)

#### When to Use vs. Alternatives

**Use This Signal When**:
- Running disease awareness or educational campaigns
- Can meet HIPAA/GDPR health data requirements
- Have medical/legal review capabilities
- Messaging is educational, not promotional
- Targeting cohorts, not individuals

**NEVER Use This Signal For**:
- Targeting specific individuals with health conditions (HIPAA violation)
- Discriminatory practices (insurance, employment)
- Non-educational commercial purposes
- Targeting minors with health conditions
- Any use case without human approval

**Use Alternatives When**:
- Cannot meet healthcare compliance requirements
- Need individual-level targeting (use condition-agnostic signals)
- Promotional (not educational) campaigns
- Broad wellness campaigns (use general wellness signals)

**Complementary Signals**:
- Combine with healthcare professional contextual targeting
- Layer with attention signals for high-quality placements
- Use geographic signals for HCP density areas

#### Expected Performance Outcomes

**Typical Performance Metrics**:
- **CTR**: 0.6-1.1% (educational content, not direct response)
- **Educational Resource Download**: 12-18%
- **HCP Discussion Tool Usage**: 5-8%
- **Physician Finder Usage**: 4-7%
- **Attribution**: Long, indirect path (education → HCP visit → prescription)

**ROI Profile**: Low Direct, High Indirect
- Premium CPMs ($12-$28) for compliance and privacy costs
- ROI measured in awareness, not direct sales
- Long-term brand equity and patient education value

**Optimization Tips**:
- Focus on educational value, not product promotion
- Use FDA-approved messaging and disclosures
- Long attribution windows (90-180 days)
- Measure education engagement, not just clicks
- Partner with patient advocacy groups for credibility
- Test messaging with focus groups (ethics)

#### Technical Integration

**Activation Method**: OAuth2 + Compliance portal access
**Rate Limits**: 30 req/min, 2,000 req/day
**Match Rate**: N/A (cohort-level targeting only)
**Minimum Segment Size**: 1,000 individuals (privacy protection)
**De-identification**: HIPAA Safe Harbor method

**Special Requirements**:
- Signed Business Associate Agreement (HIPAA)
- Annual privacy and security training for users
- Campaign pre-approval process (2-week lead time)
- Real-time monitoring for off-label promotion

---

### 7. COPPA-Compliant Family Content Signal

**File**: `children-safe-signal.json`
**Signal ID**: `coppa-compliant-family-content`
**Signal Type**: Contextual

#### What It Represents
Strictly contextual signal identifying family-friendly content environments that are COPPA-compliant and safe for child audiences. Zero behavioral tracking, no profiling, age-gated verification, and strict content safety standards. Enables brands to reach family audiences without collecting data on children under 13.

#### Who Uses It
- **Primary Users**: Family-oriented brands (toys, games, education, food)
- **Secondary Users**: Entertainment companies, streaming services, restaurants
- **Industries**: Consumer goods, entertainment, education, quick-service restaurants

#### Target Content Environments
- **Content Types**: G-rated entertainment, educational content, parenting resources
- **Platforms**: Family streaming services, educational websites, parenting blogs
- **Context**: Kids' content, family activities, child development, parenting advice
- **Strict Safety**: No violence, no mature themes, age-appropriate only

#### Trust Score Breakdown: 0.82

**Why This Score?**

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Coverage | 0.74 | Good reach (22M) but limited to verified family-safe publishers |
| Freshness | 0.88 | Daily content verification with real-time safety checks |
| Precision | 0.86 | High accuracy in content classification with human review |
| Explainability | 0.91 | Transparent methodology, clear content standards |
| Compliance Safety | 0.98 | Exceptional COPPA, GDPR-K, child safety protections |
| Outcome Relevance | 0.72 | Good engagement but contextual-only limits optimization |

**Overall**: 0.82 - Trusted with governance checks. Score reflects necessary trade-offs for child safety (limited data, contextual-only, conservative approach).

#### Governance Requirements

**Category**: Regulated - Children's Privacy
**Human Approval Required**: YES (MANDATORY)
**Why**: Children under 13 are protected class under COPPA. Zero tolerance for violations. Every campaign must be child-safe reviewed.

**Approval Workflow**:
1. Child safety officer review of creative and messaging
2. Legal review for COPPA compliance
3. Content suitability verification
4. Age-gating verification for all placements
5. Ongoing monitoring for policy violations

**Audit Frequency**: Per activation + weekly monitoring
**Risk Level**: High (regulatory and reputational)

**Absolute Prohibitions**:
- NO behavioral tracking of users under 13
- NO collection of personal information without verifiable parental consent
- NO persistent identifiers (cookies) for users under 13
- NO age misrepresentation or circumvention
- NO inappropriate content adjacency

#### Compliance Frameworks
- COPPA (Children's Online Privacy Protection Act) - US
- GDPR-K (GDPR protections for children) - EU
- AADC (Age Appropriate Design Code) - UK
- CCPA provisions for minors - California
- YouTube Kids Guidelines
- ESRB Advertising Guidelines (gaming)

#### Real-World Use Cases

**Use Case 1: Toy Manufacturer - Holiday Campaign**
- **Scenario**: Major toy brand promoting new product line for ages 6-12
- **Target**: Family content, parenting sites, kids' entertainment (contextual only)
- **Outcome**: 2.8% CTR, strong brand awareness, zero compliance issues
- **Why This Signal**: COPPA-compliant reach to family audiences during peak season

**Use Case 2: Educational Game - Back-to-School**
- **Scenario**: Learning app promoting summer learning retention
- **Target**: Educational content, parenting blogs, family activity sites
- **Outcome**: 42,000 app downloads, 18% conversion to paid subscription
- **Why This Signal**: Contextual targeting reaches parents in educational mindset

**Use Case 3: Family Restaurant - Kids Meal Promotion**
- **Scenario**: QSR promoting new kids' menu with collectible toys
- **Target**: Family entertainment content, children's movie sites
- **Outcome**: 15% coupon redemption rate, 8% new family customer acquisition
- **Why This Signal**: Brand-safe family context without tracking children

**Use Case 4: Streaming Service - Family Content Launch**
- **Scenario**: Streaming platform promoting new kids' original series
- **Target**: Parenting content, family lifestyle blogs, children's book sites
- **Outcome**: 380,000 new family subscriptions, 12% from campaign attribution
- **Why This Signal**: Contextual targeting of parents making subscription decisions

#### When to Use vs. Alternatives

**Use This Signal When**:
- Advertising products for children under 13
- Need COPPA-compliant family reach
- Brand safety in children's content is critical
- Can accept contextual-only (no behavioral) targeting
- Want to avoid reputational risk with children's data

**NEVER Use This Signal For**:
- Products not appropriate for children
- Targeting children directly (must target parents/guardians)
- Collecting personal information from children
- Behavioral profiling of family members
- Any use case requiring tracking users under 13

**Use Alternatives When**:
- Targeting adults only (use age-gated audience signals)
- Need behavioral optimization (use adult signals only)
- Broad brand awareness (use general contextual)
- Budget constraints (premium CPMs for compliance)

**Complementary Signals**:
- Cannot layer with behavioral/audience signals (privacy violation)
- Can combine with other contextual signals (age-appropriate only)
- Can use attention measurement (if privacy-preserving and COPPA-compliant)

#### Expected Performance Outcomes

**Typical Performance Metrics**:
- **CTR**: 0.7-1.2% (engaging family content)
- **Brand Awareness**: Strong lift in target demographic (families with children)
- **Purchase Intent**: Moderate (indirect - parents make decisions)
- **Safety Score**: 99.8% brand-safe content

**ROI Profile**: Medium-High
- Premium CPMs ($8-$18) for compliance and safety verification
- Strong seasonal performance (holidays, back-to-school)
- High parent engagement but longer purchase consideration

**Optimization Tips**:
- Focus on educational and entertainment value
- Seasonal strategies (holidays, summer, back-to-school)
- Test creative with child development experts
- Parent-focused messaging (decision-makers)
- Frequency cap conservatively (avoid oversaturation)
- Monitor social media for parent sentiment

#### Technical Integration

**Activation Method**: API with COPPA attestation required
**Rate Limits**: 80 req/min, 8,000 req/day
**Age Gating**: Mandatory for all placements
**Content Verification**: Real-time + human review

**Special Requirements**:
- Signed COPPA compliance agreement
- Child safety training for all campaign managers
- Weekly content safety audits
- Real-time monitoring for policy violations
- Incident response plan required

---

### 8. Voter Engagement Political Signal

**File**: `political-signal.json`
**Signal ID**: `voter-engagement-political`
**Signal Type**: Audience

#### What It Represents
Highly regulated signal for political advertising, identifying registered voters with indicators of civic engagement. Built from voter registration data (public records), civic participation patterns, and political content engagement. Subject to strict election laws, transparency requirements, and disclosure mandates.

#### Who Uses It
- **Primary Users**: Political campaigns, PACs, ballot initiative committees
- **Secondary Users**: Civic engagement organizations, voter registration drives
- **Industries**: Political campaigns, advocacy, non-profit civic engagement

#### Target Audience Profile
- **Voter Status**: Registered voters with verified addresses
- **Engagement**: Voting history (public record), civic content engagement
- **Demographics**: Voting-age adults (18+) in target districts/states
- **Restrictions**: No targeting based on race, religion, or other protected characteristics

#### Trust Score Breakdown: 0.73

**Why This Score?**

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Coverage | 0.81 | Good reach (28M registered voters) with geographic specificity |
| Freshness | 0.79 | Monthly updates align with voter registration cycles |
| Precision | 0.76 | Moderate accuracy due to self-reported data and changing voter behavior |
| Explainability | 0.88 | Transparent sources (public records) with clear methodology |
| Compliance Safety | 0.92 | Strong adherence to election laws, disclosure requirements |
| Outcome Relevance | 0.58 | Moderate performance due to political advertising skepticism |

**Overall**: 0.73 - Limited trust requiring governance. Score reflects controversial nature of political advertising, regulatory complexity, rapid changes in election law, and moderate performance.

#### Governance Requirements

**Category**: Regulated - Political Advertising
**Human Approval Required**: YES (MANDATORY)
**Why**: Political advertising is heavily regulated with disclosure, transparency, and fairness requirements. Federal and state election laws apply.

**Approval Workflow**:
1. Legal review for election law compliance (federal + state)
2. Disclosure and transparency verification
3. Content review for false/misleading claims
4. Fairness review (no discriminatory targeting)
5. Documentation for public inspection (legally required)

**Audit Frequency**: Per activation + ongoing monitoring + post-election audit
**Risk Level**: High

**Market-Specific Requirements**:
- **US Federal**: FEC disclosure rules, "paid for by" disclaimers, record retention (3 years)
- **US State**: Varies by state (California CCPA + political microtargeting restrictions, etc.)
- **EU**: Political advertising transparency regulations (varies by country)

#### Compliance Frameworks
- Federal Election Campaign Act (FECA) - US
- FEC Regulations on Internet Communications - US
- State Election Laws (varies by state)
- EU Political Advertising Transparency Regulations
- Platform-specific policies (Meta, Google, etc. political ad rules)

#### Real-World Use Cases

**Use Case 1: Senate Campaign - Voter Mobilization**
- **Scenario**: Statewide Senate race mobilizing likely supporters
- **Target**: Registered voters in target districts with civic engagement indicators
- **Outcome**: 12% voter turnout increase in target precincts, 2.1% margin of victory
- **Why This Signal**: Efficient targeting of persuadable voters in key districts

**Use Case 2: Ballot Initiative - Issue Advocacy**
- **Scenario**: Education funding ballot measure campaign
- **Target**: Registered voters with children, homeowners (tax impact messaging)
- **Outcome**: 58% approval rate, strong turnout among target voters
- **Why This Signal**: Targeted messaging to voters most affected by issue

**Use Case 3: Voter Registration Drive - Civic Engagement**
- **Scenario**: Non-partisan organization registering young voters
- **Target**: Voting-age adults not yet registered, civic content engagement
- **Outcome**: 47,000 new registrations, 62% turnout rate in first election
- **Why This Signal**: Identify and mobilize underrepresented voters

**Use Case 4: Local Election - Get Out The Vote**
- **Scenario**: Mayoral campaign with limited budget
- **Target**: High-propensity voters in key neighborhoods
- **Outcome**: 8% higher turnout in target areas, election decided by 1,200 votes
- **Why This Signal**: Efficient resource allocation in competitive race

#### When to Use vs. Alternatives

**Use This Signal When**:
- Running legitimate political campaigns
- Can meet election law disclosure requirements
- Have legal team familiar with election law
- Need verified voter targeting
- Operating in regulated political advertising environment

**NEVER Use This Signal For**:
- Voter suppression tactics
- Misleading or false political claims
- Discriminatory targeting (race, religion, etc.)
- Foreign interference in elections
- Circumventing campaign finance laws

**Use Alternatives When**:
- Broad civic engagement (use general audience signals)
- Issue advocacy not related to specific election (use issue-interest signals)
- Cannot meet disclosure requirements
- Operating in high-risk regulatory environment

**Complementary Signals**:
- Layer with geographic signals for district-specific targeting
- Combine with contextual political content targeting
- Use attention signals for video ad effectiveness

#### Expected Performance Outcomes

**Typical Performance Metrics**:
- **CTR**: 0.4-0.9% (political advertising fatigue)
- **Voter Turnout Lift**: 3-8% in target precincts
- **Persuasion**: 5-12% shift in favorability (among persuadables)
- **Volunteer Recruitment**: 2-4% conversion rate

**ROI Profile**: Variable (campaign-dependent)
- Competitive CPMs ($6-$22, spikes near election day)
- ROI measured in votes, not revenue
- Winner-take-all stakes justify investment

**Optimization Tips**:
- Start early (avoid late-campaign saturation)
- Test messaging with focus groups (polarization risk)
- Frequency cap conservatively (political ad fatigue)
- Use negative targeting to avoid opposition voters
- Geographic precision (district boundaries matter)
- Comply with disclosure rules (credibility and legal requirement)

#### Technical Integration

**Activation Method**: OAuth2 + Political advertiser verification
**Rate Limits**: 50 req/min, 5,000 req/day
**Match Rate**: 74% average (voter registration data)
**Supported ID Types**: Hashed email (SHA256), hashed address

**Special Requirements**:
- Political advertiser verification (identity + legitimacy)
- Disclosure of funding sources (legally required)
- Record retention for public inspection (3 years)
- Real-time monitoring for policy violations
- Rapid response for complaints/challenges

---

### 9. Luxury Purchase Intent Signal

**File**: `luxury-intent-signal.json`
**Signal ID**: `luxury-purchase-intent`
**Signal Type**: Commerce

#### What It Represents
Premium commerce signal identifying high-net-worth individuals with verified intent to purchase luxury goods and services. Built from first-party data from luxury retail networks, concierge services, premium travel bookings, and high-end lifestyle engagement. Focuses on ultra-premium market ($5K+ transaction values).

#### Who Uses It
- **Primary Users**: Luxury brands (fashion, jewelry, watches, automotive)
- **Secondary Users**: Premium travel, fine dining, luxury real estate, art galleries
- **Industries**: Luxury retail, premium automotive, high-end hospitality, private aviation

#### Target Audience Profile
- **Wealth Indicators**: Ultra-high transaction values, luxury brand engagement, premium service usage
- **Purchase Intent**: Recent luxury brand interactions, concierge service requests, high-end product research
- **Demographics**: HNWIs and Ultra-HNWIs, typically 35-70 years old
- **Segment Size**: 125,000 (highly exclusive)

#### Trust Score Breakdown: 0.93

**Why This Score?**

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Coverage | 0.79 | Limited reach by design (ultra-luxury market is small) |
| Freshness | 0.96 | Real-time updates capture immediate purchase intent |
| Precision | 0.97 | Exceptionally high accuracy from verified luxury purchase data |
| Explainability | 0.91 | Clear intent indicators from first-party luxury interactions |
| Compliance Safety | 0.95 | Strong privacy protections, explicit opt-in, GDPR/CCPA compliant |
| Outcome Relevance | 0.94 | Very strong performance with documented luxury purchase outcomes |

**Overall**: 0.93 - Very high trust due to first-party data, verified intent, strong performance, and appropriate governance.

#### Governance Requirements

**Category**: Commerce - Luxury/High-Value
**Human Approval Required**: YES (for first-time luxury brand partnerships)
**Why**: High transaction values and exclusive brand partnerships require quality control and brand alignment verification.

**Approval Workflow** (first activation):
1. Brand partnership verification (ensure brand alignment)
2. Creative quality review (luxury brand standards)
3. Placement quality verification (premium inventory only)
4. Privacy review (HNWI data handling)
5. Account manager approval

**Subsequent activations**: Autonomous (after first approval)

**Audit Frequency**: Quarterly
**Risk Level**: Medium

#### Compliance Frameworks
- GDPR (General Data Protection Regulation) - EU
- CCPA (California Consumer Privacy Act) - US
- Luxury brand partnership agreements
- Premium publisher quality standards

#### Real-World Use Cases

**Use Case 1: Swiss Watchmaker - New Timepiece Launch**
- **Scenario**: Luxury watch brand launching $45K limited-edition timepiece
- **Target**: Ultra-luxury segment with watch collecting indicators
- **Outcome**: 4.2% boutique visit rate, 0.8% conversion, $1.8M revenue from 40 sales
- **Why This Signal**: Verified purchasing power ensures qualified interest

**Use Case 2: Luxury Automotive - Ultra-Premium Model**
- **Scenario**: Supercar manufacturer promoting $850K limited production model
- **Target**: High-intent luxury automotive segment (previous luxury auto purchases)
- **Outcome**: 18 test drive requests, 7 pre-orders, $5.95M revenue, 42:1 ROAS
- **Why This Signal**: Documented luxury auto intent indicates genuine purchase consideration

**Use Case 3: High-End Jewelry - Private Sale Event**
- **Scenario**: Fine jewelry house hosting VIP private sale
- **Target**: Luxury jewelry purchase intent segment (recent engagement, high AOV)
- **Outcome**: 22% RSVP rate, $2.4M event sales, 14 new high-value customers
- **Why This Signal**: First-party luxury data identifies ideal VIP event attendees

**Use Case 4: Luxury Resort - Exclusive Package**
- **Scenario**: Ultra-luxury resort promoting $25K/night private villa package
- **Target**: Premium travel segment with verified luxury spending patterns
- **Outcome**: 32 inquiries, 11 bookings, $2.75M revenue, ongoing guest relationships
- **Why This Signal**: Verified luxury travel behavior predicts ultra-premium booking propensity

#### When to Use vs. Alternatives

**Use This Signal When**:
- Selling ultra-premium products ($5K+)
- Need verified luxury purchase intent
- Can justify premium CPMs ($35-$85)
- Operating in luxury brand space
- Want qualified leads over volume

**Use Alternatives When**:
- Mid-market or accessible luxury products (use standard commerce intent)
- Broad awareness campaigns (use interest-based audiences)
- Budget constraints (use lower-cost signals)
- Testing new products (use broader signals first)

**Complementary Signals**:
- Layer with attention signals for premium placement quality
- Combine with luxury lifestyle contextual targeting
- Use geographic signals for luxury retail concentration areas
- Suppress existing top clients (privacy and exclusivity)

#### Expected Performance Outcomes

**Typical Performance Metrics**:
- **CTR**: 1.4-2.8% (high engagement from qualified audience)
- **Conversion Rate**: 0.6-1.8% (considered purchases)
- **Average Transaction Value**: $45,000-$180,000
- **ROAS**: 18-45x (high transaction values justify costs)
- **Customer Lifetime Value**: Exceptional (luxury customers are repeat buyers)

**ROI Profile**: Exceptional (for appropriate use cases)
- Premium CPMs ($35-$85) justified by transaction values
- Small reach but very high conversion values
- Strong repeat purchase and lifetime value

**Optimization Tips**:
- Premium creative quality mandatory (luxury brand standards)
- Long attribution windows (90-180 days for considered purchases)
- Minimal frequency (1-2 impressions, exclusivity matters)
- Premium placement only (inventory quality reflects brand)
- Personal service integration (concierge, private shopping)
- Seasonal strategies (holidays, gifting occasions)

#### Technical Integration

**Activation Method**: OAuth2 + Brand partnership verification
**Rate Limits**: 30 req/min, 2,000 req/day
**Match Rate**: 68% average (privacy protections)
**Supported ID Types**: Hashed email (SHA256), secure customer ID
**Minimum Campaign Budget**: $50,000 (ensures appropriate use)

**Special Requirements**:
- Brand partnership agreement
- Creative quality approval process
- Premium publisher whitelist
- Quarterly business reviews
- VIP customer service integration

---

### 10. Carbon-Neutral Consumer Signal

**File**: `carbon-neutral-signal.json`
**Signal ID**: `carbon-conscious-consumers`
**Signal Type**: Audience

#### What It Represents
Audience signal identifying consumers with verified commitment to climate action and sustainable living. Built from third-party certified sustainability behaviors (carbon offset purchases, renewable energy adoption, sustainable product purchases), environmental content engagement, and sustainability program participation. Third-party verified and ESG-compliant.

#### Who Uses It
- **Primary Users**: Sustainability-focused consumer brands, green energy companies
- **Secondary Users**: ESG-committed corporations, impact investment marketers, eco-tourism
- **Industries**: Sustainable consumer goods, renewable energy, eco-friendly services, green technology

#### Target Audience Profile
- **Sustainability Actions**: Carbon offset purchases, renewable energy subscriptions, sustainable product buying patterns
- **Engagement**: Climate action content, sustainability apps, environmental advocacy
- **Verification**: Third-party verified actions (not just claimed interest)
- **Segment Size**: 2.8M (verified actions, not just interest)

#### Trust Score Breakdown: 0.81

**Why This Score?**

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Coverage | 0.72 | Moderate reach (2.8M) limited to verified sustainable behaviors |
| Freshness | 0.87 | Weekly updates capture evolving sustainability actions |
| Precision | 0.84 | Good accuracy from verified actions, but evolving consumer behavior |
| Explainability | 0.89 | Clear methodology based on observable, verified actions |
| Compliance Safety | 0.93 | Strong GDPR/CCPA compliance, third-party verification, no greenwashing |
| Outcome Relevance | 0.82 | Strong performance for sustainability-focused products |

**Overall**: 0.81 - Trusted with governance checks. Score reflects emerging market, verification requirements, and need to prevent greenwashing.

#### Governance Requirements

**Category**: Audience - Sustainability/Environmental
**Human Approval Required**: YES
**Why**: Prevent greenwashing and ensure authentic sustainability claims. Reputational risk if misused for non-sustainable products.

**Approval Workflow**:
1. Sustainability officer review of product/campaign claims
2. Third-party verification of environmental claims (if product claims made)
3. Marketing review for greenwashing risk
4. Legal review of environmental claims compliance
5. ESG team approval

**Audit Frequency**: Quarterly + annual ESG reporting
**Risk Level**: Medium

**Prohibited Uses**:
- Greenwashing (false/misleading environmental claims)
- Targeting for non-sustainable products
- Misleading "eco-friendly" claims without substantiation

#### Compliance Frameworks
- FTC Green Guides (environmental marketing claims) - US
- EU Green Claims Directive
- ISO 14021 (environmental labels and declarations)
- Science Based Targets Initiative (SBTi)
- B Corp Certification standards
- Carbon offset verification standards (Gold Standard, Verified Carbon Standard)

#### Real-World Use Cases

**Use Case 1: Electric Vehicle - Climate Conscious Buyers**
- **Scenario**: EV manufacturer targeting verified climate-conscious consumers
- **Target**: Carbon-conscious segment with renewable energy subscriptions
- **Outcome**: 8.2% test drive booking rate, 1.4% conversion, $42M revenue, strong brand alignment
- **Why This Signal**: Verified climate commitment predicts EV consideration

**Use Case 2: Renewable Energy - Solar Installation**
- **Scenario**: Solar panel company targeting homeowners committed to sustainability
- **Target**: Homeowners with carbon offset purchases and sustainability engagement
- **Outcome**: 12% consultation request rate, 3.1% conversion, $8.4M revenue
- **Why This Signal**: Verified willingness to invest in sustainability

**Use Case 3: Sustainable Fashion - Clothing Line Launch**
- **Scenario**: Carbon-neutral fashion brand launching new collection
- **Target**: Verified sustainable product purchasers
- **Outcome**: 2.8% purchase rate, $185 average order value, 4.2x ROAS, strong repeat purchase
- **Why This Signal**: Past sustainable purchases predict future behavior

**Use Case 4: Eco-Tourism - Carbon-Neutral Travel**
- **Scenario**: Travel company promoting carbon-offset vacation packages
- **Target**: Travelers with verified carbon offset history
- **Outcome**: 6.4% booking inquiry rate, $4,200 average package value, 7.1x ROAS
- **Why This Signal**: Carbon offset behavior extends to travel decisions

#### When to Use vs. Alternatives

**Use This Signal When**:
- Selling genuinely sustainable products/services
- Have verified environmental credentials
- Can justify sustainability claims (third-party certified)
- Target audience values verified actions over claims
- ESG reporting and authenticity matter

**NEVER Use This Signal For**:
- Greenwashing campaigns (false environmental claims)
- Products with negative environmental impact
- Misleading "eco-friendly" positioning
- Any campaign without substantiated sustainability claims

**Use Alternatives When**:
- Broad environmental interest (use interest-based signals)
- Budget constraints (premium CPMs for verification)
- Early-stage sustainability testing
- Products with mixed sustainability profile

**Complementary Signals**:
- Layer with sustainable inventory signal (full alignment)
- Combine with premium attention for quality placements
- Use contextual environmental content targeting

#### Expected Performance Outcomes

**Typical Performance Metrics**:
- **CTR**: 1.1-1.9% (high engagement from committed audience)
- **Conversion Rate**: 2.2-3.8% (strong intent-to-action alignment)
- **Average Order Value**: 15-20% premium (willingness to pay for sustainability)
- **ROAS**: 4.5-7.8x
- **Customer Loyalty**: 32% higher repeat purchase rate vs. standard customers

**ROI Profile**: High
- Premium CPMs ($14-$32) for verification and niche targeting
- Strong conversion and loyalty justify costs
- Premium pricing acceptance in target segment

**Optimization Tips**:
- Substantiate all environmental claims (FTC Green Guides)
- Third-party certifications boost credibility (B Corp, Carbon Neutral, etc.)
- Transparency about sustainability trade-offs (honest communication)
- Long attribution windows (researched purchases)
- Educational content performs well (not just sales messaging)
- Show impact metrics (carbon saved, trees planted, etc.)

#### Technical Integration

**Activation Method**: API key + Sustainability verification
**Rate Limits**: 60 req/min, 6,000 req/day
**Match Rate**: 71% average
**Supported ID Types**: Hashed email (SHA256), sustainable loyalty program IDs
**Third-Party Verification**: Quarterly sustainability action audits

**Special Requirements**:
- Sustainability claims verification document
- ESG reporting access (for participating brands)
- Quarterly impact reporting
- Greenwashing prevention training
- Annual third-party audit

---

## Trust Score Methodology

### Overview

OpenSignals uses a multi-dimensional trust scoring framework to evaluate signal quality, reliability, and risk. Each signal receives an overall trust score (0.0-1.0) calculated from seven weighted dimensions.

### Trust Score Dimensions

| Dimension | Weight | What It Measures |
|-----------|--------|------------------|
| **Coverage** | 20% | Reach, scale, representativeness, and audience size |
| **Freshness** | 15% | How recently data was updated, update frequency |
| **Precision** | 20% | Accuracy, false positive rate, consistency |
| **Explainability** | 10% | Methodology transparency, auditability |
| **Compliance Safety** | 15% | Regulatory adherence, privacy protections |
| **Outcome Relevance** | 20% | Historical performance, business impact |

**Total**: 100%

### Score Ranges and Interpretation

| Overall Score | Trust Level | Recommended Action | Use Cases |
|---------------|-------------|-------------------|-----------|
| 0.90 - 1.00 | Very High Trust | Autonomous activation (if policy allows) | Mission-critical campaigns, high-value products |
| 0.75 - 0.89 | High Trust | Use with standard governance checks | Most commercial applications |
| 0.60 - 0.74 | Limited Trust | Require human review per activation | Experimental signals, emerging data sources |
| 0.40 - 0.59 | Low Trust | Senior approval required, limit spend | Test-only, low-risk applications |
| 0.00 - 0.39 | Untrusted | Do not activate | Block usage |

### Dimension Deep Dive

#### Coverage Score (20%)

**What It Evaluates**:
- Reach and scale (impressions, audience size)
- Geographic coverage
- Device and platform coverage
- Representativeness of target market

**Scoring Examples**:
- 0.90+: Large scale (100M+ reach), broad coverage, representative
- 0.70-0.89: Medium scale (10M-100M), good coverage
- 0.50-0.69: Smaller scale (<10M) or limited geography
- <0.50: Very limited reach or unrepresentative

**Impact on Overall Trust**: High coverage increases confidence in signal utility but doesn't guarantee quality.

#### Freshness Score (15%)

**What It Evaluates**:
- Last update timestamp
- Update frequency relative to signal type
- Data staleness impact on accuracy

**Scoring Examples**:
- 0.95+: Real-time or hourly updates
- 0.85-0.94: Daily updates
- 0.70-0.84: Weekly updates
- 0.50-0.69: Monthly updates
- <0.50: Quarterly or stale data

**Impact on Overall Trust**: Freshness matters more for intent signals than contextual signals.

#### Precision Score (20%)

**What It Evaluates**:
- Accuracy and false positive rate
- Consistency across activations
- Measurement error and variance
- Third-party validation results

**Scoring Examples**:
- 0.95+: Validated accuracy >95%, minimal false positives
- 0.85-0.94: Good accuracy (85-95%), low error rate
- 0.70-0.84: Moderate accuracy (70-85%)
- 0.50-0.69: Lower accuracy (50-70%), noisy signal
- <0.50: Poor accuracy, unreliable

**Impact on Overall Trust**: Precision is critical for performance and trust.

#### Explainability Score (10%)

**What It Evaluates**:
- Methodology transparency
- Data source documentation
- Ability to audit and verify
- User understanding

**Scoring Examples**:
- 0.90+: Fully transparent, published methodology, auditable
- 0.75-0.89: Clear methodology, some proprietary elements
- 0.60-0.74: Limited transparency, black box elements
- <0.60: Opaque, cannot explain

**Impact on Overall Trust**: Explainability builds confidence and enables governance.

#### Compliance Safety Score (15%)

**What It Evaluates**:
- Regulatory compliance (GDPR, CCPA, etc.)
- Privacy protections
- Consent mechanisms
- Sensitive category handling
- Third-party certifications

**Scoring Examples**:
- 0.95+: Exceptional compliance, third-party certified
- 0.85-0.94: Strong compliance, clear privacy protections
- 0.70-0.84: Basic compliance, some gaps
- 0.50-0.69: Compliance concerns, limited protections
- <0.50: Non-compliant, high risk

**Impact on Overall Trust**: Compliance is non-negotiable for regulated categories.

#### Outcome Relevance Score (20%)

**What It Evaluates**:
- Historical campaign performance
- Business outcome correlation
- ROI and efficiency
- Validated effectiveness

**Scoring Examples**:
- 0.90+: Exceptional performance, validated outcomes
- 0.75-0.89: Strong performance, good ROI
- 0.60-0.74: Moderate performance
- 0.40-0.59: Unclear or mixed performance
- <0.40: Poor performance

**Impact on Overall Trust**: Outcome relevance justifies investment and builds confidence.

### Governance and Trust Scores

Trust scores inform but don't dictate governance decisions. Additional factors include:

**Regulatory Requirements**: Some categories (alcohol, pharma, financial) require human approval regardless of trust score.

**Brand Policy**: Brands may set higher thresholds than default recommendations.

**Risk Tolerance**: Conservative brands may require approval for scores <0.85, while others accept 0.70+.

**Use Case**: High-value campaigns may require higher trust scores than experimental tests.

---

## Governance Framework

### Governance Categories

OpenSignals defines three governance categories that determine approval requirements:

#### 1. General (Low Risk)

**Characteristics**:
- Non-sensitive content targeting
- Low regulatory requirements
- Standard privacy protections
- Broad use cases

**Examples**:
- Contextual signals (general content)
- Attention measurement
- General interest audiences
- Geographic signals

**Approval Requirements**:
- Trust Score >0.75: Autonomous
- Trust Score 0.60-0.74: Standard review
- Trust Score <0.60: Do not use

**Audit Frequency**: Quarterly or annual

---

#### 2. Regulated (Medium-High Risk)

**Characteristics**:
- Industry-specific regulations
- Compliance requirements
- Sensitive use cases
- Age restrictions or content rules

**Examples**:
- Alcohol advertising (age-gated)
- Financial services (GLBA, FCRA)
- Political advertising (election laws)
- Luxury/high-value (brand alignment)

**Approval Requirements**:
- Human approval required for first activation (regardless of trust score)
- Legal/compliance review mandatory
- Ongoing monitoring required
- Trust Score >0.80 recommended

**Audit Frequency**: Per activation or monthly

---

#### 3. Restricted (High Risk)

**Characteristics**:
- Protected classes (children, health)
- Strict privacy laws (HIPAA, COPPA)
- High reputational risk
- Special category data

**Examples**:
- Healthcare/pharmaceutical (HIPAA, health data)
- Children's privacy (COPPA, GDPR-K)
- Some political advertising (voter suppression risk)
- Sensitive financial (credit, insurance underwriting)

**Approval Requirements**:
- Mandatory human approval for every activation
- Multi-stakeholder review (legal, compliance, ethics, privacy)
- Trust Score >0.85 required
- Ongoing monitoring and audits

**Audit Frequency**: Per activation + weekly monitoring

---

### Human Approval Workflows

#### Standard Approval Workflow (Regulated Category)

1. **Requestor** submits campaign with signal details
2. **Legal Team** reviews regulatory compliance
3. **Compliance Officer** verifies signal usage aligns with policies
4. **Privacy Team** assesses data handling (if applicable)
5. **Approval/Rejection** with documented rationale

**Timeline**: 2-5 business days

---

#### Enhanced Approval Workflow (Restricted Category)

1. **Requestor** submits detailed campaign brief with signal details
2. **Legal Team** comprehensive review (federal + state/local laws)
3. **Compliance Officer** detailed signal audit
4. **Privacy Officer** data handling and consent verification
5. **Ethics Committee** (for healthcare, children, political)
6. **Senior Executive** final sign-off
7. **Approval/Rejection** with conditions and monitoring plan

**Timeline**: 5-15 business days

---

### Risk Levels

| Risk Level | Description | Typical Categories | Monitoring |
|------------|-------------|-------------------|------------|
| **Low** | Minimal regulatory or reputational risk | General contextual, measurement | Quarterly audit |
| **Low-Medium** | Some governance needs, standard protections | First-party commerce, general audiences | Quarterly audit |
| **Medium** | Moderate compliance needs, some restrictions | Sustainability, luxury, some geographic | Monthly audit |
| **Medium-High** | Significant regulations, age restrictions | Alcohol, some financial, political | Per activation audit |
| **High** | Strict regulations, protected classes, high reputational risk | Healthcare, children's privacy, sensitive financial | Per activation + ongoing monitoring |

---

### Audit Requirements

#### Quarterly Audits

**Scope**:
- Signal quality metrics review
- Compliance spot checks
- Performance validation
- User feedback review

**Participants**: Internal audit team

---

#### Monthly Audits

**Scope**:
- Detailed compliance verification
- Campaign review for policy adherence
- Third-party verification (if applicable)
- Incident review

**Participants**: Compliance team + third-party auditor (if required)

---

#### Per-Activation Audits

**Scope**:
- Pre-activation compliance verification
- Campaign-specific risk assessment
- Creative and messaging review
- Ongoing monitoring during campaign

**Participants**: Full governance team (legal, compliance, privacy, etc.)

---

## Compliance Matrix

### By Signal

| Signal | Primary Compliance | Geographic Restrictions | Approval Required | Audit Frequency |
|--------|-------------------|------------------------|------------------|----------------|
| Premium Cocktail Contexts | UK CAP, US DISCUS, EU AVMS | Prohibited: SA, AE, IQ; Age-restricted: US, GB, FR, DE, AU, CA, JP | Yes | Per activation |
| Verified Attention Quality | MRC, IAB, GDPR, CCPA | None | No | Monthly |
| Home Decor Purchase Intent | GDPR, CCPA, IAB GPP | GDPR for EU | No | Quarterly |
| Verified Sustainable Inventory | GHG Protocol, ISO 14064, SBTi | None | No | Monthly |
| Financial Services Customer | GLBA, FCRA, SOX, GDPR Article 9 | US: GLBA/FCRA; EU: GDPR; GB: FCA | Yes | Per activation + monthly |
| Health Condition Management | HIPAA, FDA, EMA, GDPR Article 9 | US: HIPAA/FDA; EU: GDPR + EMA | Yes | Per activation + quarterly |
| COPPA-Compliant Family Content | COPPA, GDPR-K, AADC, CCPA minors | Global child privacy protections | Yes | Per activation + weekly |
| Voter Engagement Political | FECA, FEC, State election laws | US: Federal + state; EU: varies by country | Yes | Per activation + post-election |
| Luxury Purchase Intent | GDPR, CCPA | GDPR for EU | Yes (first time) | Quarterly |
| Carbon-Neutral Consumer | FTC Green Guides, EU Green Claims | None | Yes | Quarterly + annual ESG |

---

### By Compliance Framework

#### GDPR (General Data Protection Regulation) - EU

**Applies To**:
- All signals processing EU citizen data
- Special provisions for Article 9 (special category data: health, political)

**Signals Most Affected**:
- Health Condition Management (Article 9)
- Financial Services Customer (Article 9)
- Voter Engagement Political (Article 9)
- All first-party audience signals

**Key Requirements**:
- Lawful basis for processing
- Data minimization
- Consent or legitimate interest
- Right to access, deletion, portability
- Data protection by design

---

#### CCPA (California Consumer Privacy Act) - US California

**Applies To**:
- Signals processing California resident data
- Additional provisions for minors (<16)

**Signals Most Affected**:
- All first-party audience signals
- COPPA-Compliant Family Content (minors)

**Key Requirements**:
- Right to know data collected
- Right to deletion
- Right to opt-out of sale
- Specific protections for minors

---

#### COPPA (Children's Online Privacy Protection Act) - US

**Applies To**:
- Any signal targeting children <13
- Collection of personal information from children

**Signals Most Affected**:
- COPPA-Compliant Family Content (primary)

**Key Requirements**:
- Verifiable parental consent for data collection
- No behavioral tracking of children
- No persistent identifiers for children
- Clear privacy policies

---

#### HIPAA (Health Insurance Portability and Accountability Act) - US

**Applies To**:
- Health condition data
- Protected Health Information (PHI)

**Signals Most Affected**:
- Health Condition Management (primary)

**Key Requirements**:
- No individual PHI without authorization
- Business Associate Agreements
- Security safeguards
- Patient rights (access, amendment)

---

#### FTC Green Guides - US

**Applies To**:
- Environmental marketing claims
- Sustainability positioning

**Signals Most Affected**:
- Carbon-Neutral Consumer (primary)
- Verified Sustainable Inventory

**Key Requirements**:
- Substantiation of environmental claims
- Clear, prominent disclosures
- Avoid deceptive green marketing
- Third-party certification recommended

---

## Performance Benchmarks

### By Signal Type

#### Contextual Signals

| Metric | Premium Cocktail Contexts | COPPA-Compliant Family Content | Benchmark (Industry Avg) |
|--------|--------------------------|------------------------------|-------------------------|
| CTR | 0.45-0.72% | 0.7-1.2% | 0.35% |
| Viewability | 82-89% | 85-92% | 70% |
| Brand Safety | 99.7% | 99.8% | 95% |
| Brand Lift | 8-14% | Strong (qualitative) | 6% |

**Use Cases**: Brand safety, regulatory compliance, cookieless targeting

---

#### Attention/Measurement Signals

| Metric | Verified Attention Quality | Benchmark (Standard Inventory) |
|--------|---------------------------|------------------------------|
| Avg Attention Time | 8.7 seconds | 5.2 seconds |
| Attention Quality Score | 0.82 | 0.68 |
| Brand Lift Correlation | 0.89 | 0.52 |
| Viewability | 92% | 70% |

**Use Cases**: Media quality optimization, brand campaigns, performance reporting

---

#### Commerce/Intent Signals

| Signal | CTR | Conversion Rate | ROAS | Avg Order Value |
|--------|-----|----------------|------|----------------|
| Home Decor Purchase Intent | 1.2-2.8% | 3.1-4.2% | 4.8x | $285 |
| Financial Services Customer | 0.8-1.4% | 2.0-4.0% | 11x+ | $45K-$180K |
| Luxury Purchase Intent | 1.4-2.8% | 0.6-1.8% | 18-45x | $45K-$180K |
| Industry Benchmark | 0.5% | 1.5% | 2.5x | $150 |

**Use Cases**: Direct response, conversion campaigns, high-value products

---

#### Audience Signals

| Signal | CTR | Conversion | ROAS | Brand Lift |
|--------|-----|-----------|------|-----------|
| Health Condition Management | 0.6-1.1% | N/A (education) | Indirect | Education-focused |
| Voter Engagement Political | 0.4-0.9% | 3-8% turnout lift | N/A | 5-12% favorability shift |
| Carbon-Neutral Consumer | 1.1-1.9% | 2.2-3.8% | 4.5-7.8x | Strong alignment |
| Industry Benchmark | 0.5% | 1.5% | 2.5x | 6% |

**Use Cases**: Awareness, consideration, specialized targeting

---

#### Environmental Signals

| Signal | CTR | Carbon Impact | Brand Favorability | CPM Premium |
|--------|-----|--------------|-------------------|-------------|
| Verified Sustainable Inventory | Comparable | 0.8g CO2/impression offset | +5-8% (sustainability-conscious) | $0.50-$2.00 |
| Standard Inventory | Baseline | ~5g CO2/impression | Baseline | Baseline |

**Use Cases**: ESG compliance, sustainability reporting, brand alignment

---

### CPM Ranges by Signal

| Signal | CPM Range (USD) | Rationale |
|--------|----------------|-----------|
| Premium Cocktail Contexts | $4.50 - $12.00 | Regulated category, premium content, compliance costs |
| Verified Attention Quality | $0.50 - $2.00 | Measurement fee (added to base CPM) |
| Home Decor Purchase Intent | $8.00 - $18.00 | First-party intent, tiered by intent strength |
| Verified Sustainable Inventory | $3.00 - $7.50 | Carbon offset included, limited publisher scale |
| Financial Services Customer | $25.00 - $60.00 | High-value audience, strict compliance, exclusivity |
| Health Condition Management | $12.00 - $28.00 | Compliance costs, privacy protections, ethics oversight |
| COPPA-Compliant Family Content | $8.00 - $18.00 | Safety verification, compliance, limited inventory |
| Voter Engagement Political | $6.00 - $22.00 | Variable (spikes near election), disclosure costs |
| Luxury Purchase Intent | $35.00 - $85.00 | Ultra-high-value audience, exclusivity, verified intent |
| Carbon-Neutral Consumer | $14.00 - $32.00 | Verified sustainability actions, niche targeting |

---

### ROI Profiles

| Signal | ROI Profile | Best For | When to Use |
|--------|------------|----------|-------------|
| Premium Cocktail Contexts | Medium-High | Brand awareness, regulated alcohol | Premium spirits, luxury brands |
| Verified Attention Quality | High | Media optimization, brand campaigns | Proving effectiveness, premium inventory |
| Home Decor Purchase Intent | Very High | Direct response, conversions | Full-funnel commerce campaigns |
| Verified Sustainable Inventory | Medium | ESG compliance, brand alignment | Sustainability commitments, reporting |
| Financial Services Customer | Very High | High-value acquisition | Wealth management, luxury goods |
| Health Condition Management | Indirect | Patient education, awareness | Disease awareness, not direct sales |
| COPPA-Compliant Family Content | Medium-High | Family brands, seasonal | Toys, games, family entertainment |
| Voter Engagement Political | Variable | Votes, not revenue | Political campaigns, ballot initiatives |
| Luxury Purchase Intent | Exceptional | Ultra-premium products | Luxury goods ($5K+ transaction values) |
| Carbon-Neutral Consumer | High | Sustainable products, ESG | Verified green products, climate action |

---

## Usage Recommendations

### By Industry

**Financial Services**: Financial Services Customer, Luxury Purchase Intent, Attention Quality
**Healthcare/Pharma**: Health Condition Management, Contextual Health Content
**Luxury Retail**: Luxury Purchase Intent, Financial Services Customer, Attention Quality
**Consumer Goods**: Home Decor Purchase Intent, Carbon-Neutral Consumer, Contextual
**Alcohol/Spirits**: Premium Cocktail Contexts
**Family/Entertainment**: COPPA-Compliant Family Content
**Political Campaigns**: Voter Engagement Political
**Sustainable Brands**: Carbon-Neutral Consumer, Verified Sustainable Inventory

### By Campaign Objective

**Brand Awareness**: Attention Quality, Contextual signals
**Consideration**: Commerce intent, Audience signals
**Conversion**: Commerce intent, Luxury intent
**Education**: Health Condition, Contextual
**Compliance**: All regulated signals with appropriate governance
**ESG Reporting**: Sustainable Inventory, Carbon-Neutral Consumer

---

**Document Version**: 1.0
**Last Updated**: 2026-05-11
**Maintained By**: OpenSignals Protocol Working Group

For questions or contributions: [GitHub Issues](https://github.com/Samrajtheailyceum/opensignals-protocol/issues)
