# Kestrel Bank AI Transformation Blueprint: Client Brief

> **Notice:** Kestrel Bank is a **fictional** institution created for this portfolio project. Real public consumer complaint data from the Consumer Financial Protection Bureau (CFPB) is utilized as a stand-in for complaint patterns, product mix, and customer themes. Indian banking operational metrics, cost structures, and volumes are explicitly labelled as assumptions or sourced industry benchmarks.

---

## 1. Client Context
- **Institution:** Kestrel Bank (fictional)
- **Profile:** Mid-size Indian private-sector bank offering Retail Banking, Credit Cards, and Digital Banking products.
- **Context & Problem:** Complaint volumes have surged alongside accelerated digital banking adoption. Bank leadership faces rising operational costs, growing handling bottlenecks, and increased risk of customer escalations to the Reserve Bank of India (RBI) Integrated Ombudsman Scheme.
- **Leadership Request:** *"Tell us where AI should and should not be used in complaint handling, what it will return, and how to roll it out safely."*

---

## 2. Operating Scale & Baselines (Assumed)
- **Monthly Inflow:** ~40,000 complaints per month across four operating teams:
  - Cards & Payments
  - Savings & Current Accounts
  - Digital Banking & UPI
  - Branch & Executive Escalations
- **Agent Workforce:** ~120 full-time equivalent (FTE) agents handling intake, triage, investigation, and customer communication (accounting for shift utilization, breaks, training, and shrinkage).
- **Current Handling Time:** ~25 minutes average handle time (AHT) per complaint (baseline assumption to be validated).
- **Loaded Agent Cost:** ₹400 / hour (inclusive of salary, benefits, technology overhead, and seat cost).
- **Escalation Rate:** ~3% of unresolved/dissatisfied complaints escalate towards the RBI Ombudsman.

---

## 3. Key Constraints & Guardrails
- **Regulatory Compliance:** Full adherence to the RBI Integrated Ombudsman Scheme (RB-IOS 2026 30-day resolution timeline), Digital Personal Data Protection Act (DPDP Act 2023), and the RBI FREE-AI governance principles.
- **Data Residency & Sovereignty:** Data must remain resident in India where feasible. Customer personally identifiable information (PII) must be masked prior to any third-party or foundational model ingestion.
- **Core Banking Freeze:** No direct architectural alterations or invasive writes to core banking systems (CBS) in Year 1. Integration must rely on clean API/tool layers with human sign-off.
- **Financial Hurdle:** Any proposed AI capital and operational expenditure must achieve a net payback inside 24 months with a positive 3-year net present value (NPV).
- **Human-in-the-Loop:** Automated generation of responses without human review is strictly prohibited. AI assists, triages, and drafts; human agents make determinations and send communications.

---

## 4. Stand-in Data Disclaimer & Methodology
To conduct root-cause diagnostic and process redesign without exposing proprietary bank customer records, public data from the CFPB Consumer Complaint Database is utilized to reflect:
1. Issue distribution and Pareto frequency.
2. Company response and relief rate outcomes.
3. Customer sentiment and narrative root causes.

All financial modeling (A2), performance monitoring (A3), and strategic roadmap milestones (Flagship A) connect this empirical baseline to Kestrel Bank's operating assumptions.
