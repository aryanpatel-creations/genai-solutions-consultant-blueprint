# AI Governance Plan: Statutory Control Map, Risk Register & RACI (governance_plan.md)

> **Client:** Kestrel Bank  
> **Engagement:** AI Transformation Blueprint — Complaints Redressal Modernisation  
> **Prepared by:** Aryan Patel (MBA Business Analytics, Techno-Functional Consultant)  
> **Deliverable:** Flagship Step 7 — Institutional AI Governance, Regulatory Controls & Operating Model  
> **Statutory Frameworks:** DPDP Act 2023 · RBI FREE-AI Guidelines · RBI Integrated Ombudsman Scheme (RB-IOS 2026) · Model Risk Management (MRM)

---

## 1. Executive Governance Mandate

In the Indian financial sector, deploying Artificial Intelligence in customer dispute resolution is fundamentally a **regulatory and governance challenge**, not merely a technical implementation.

Under the Reserve Bank of India's **FREE-AI Framework** (*Fairness, Reliability, Ethics, and Explainability in AI*) and the **Digital Personal Data Protection (DPDP) Act 2023**, Kestrel Bank must maintain strict algorithmic transparency, enforceable data privacy, and uncompromised human accountability. The architecture enforces two foundational operating doctrines:
1. **Human Agency & Ultimate Accountability:** AI acts solely as an operational accelerator (Copilot). Final decision-making authority on customer communication, fee adjustments, and case closures remains 100% human.
2. **Zero Trust Data Ingestion:** Customer financial and demographic identifiers are tokenized inside the bank's secure perimeter prior to external model inference.

---

## 2. Statutory & Regulatory Control Map (Step 7a)

The control map operationalizes statutory banking laws into enforceable technical and process safeguards:

| Statutory Authority / Source | Regulatory Requirement | Design & Architectural Meaning | Enforced Governance Control | Accountable Business Owner | Verification Evidence & Telemetry (Project A3) |
|---|---|---|---|---|---|
| **DPDP Act 2023 (Sec 6 & 8)** | **Purpose Limitation & Data Minimisation:** Regulated entities may only process customer personal data strictly necessary for grievance redressal. | External LLM endpoints must never ingest customer names, Aadhaar numbers, PAN identifiers, or raw account numbers. | **Client-Side Masking Gateway:** Regex and NER pipeline tokenizes sensitive identifiers inside bank perimeter before API transmission. Masking logs persisted. | **Chief Information Security Officer (CISO)** | **PII Blocks Metric** (944 pilot intercepts); 50-item adversarial red-team test set. |
| **DPDP Act 2023 (Sec 8)** | **Security Safeguards & 72-Hour Breach Reporting:** Data fiduciaries must implement reasonable security safeguards and report data breaches within 72 hours. | Prompt logs, retrieved documents, and drafted replies contain sensitive financial context requiring cryptographic isolation. | **Cryptographic Security & Incident Runbook:** AES-256 at rest, TLS 1.3 in transit; strict 90-day log retention ceiling; automated 72-hour breach escalation runbook. | **Data Protection Officer (DPO)** | Annual Third-Party Penetration Test; Signed Incident Response Runbook; Access Control Review. |
| **DPDP Act 2023 (Sec 11)** | **Data Processor Obligations:** Fiduciaries remain liable for processor actions; cloud vendors must provide contractual compliance. | Third-party foundational model providers process bank grievance context on the bank's behalf. | **Enterprise Data Processing Addendum (DPA):** Zero Data Retention (ZDR) clause prohibiting model training; India Data Residency (AWS/Azure Mumbai regions). | **Head of Procurement & Legal** | Fully Executed Enterprise Master Services Agreement & DPA. |
| **RBI FREE-AI Framework** | **Institutional AI Policy & AI Inventory Register:** Regulated banks must maintain a central inventory of all AI/ML models with defined risk tiers. | Kestrel Bank's complaint assistant cannot operate as "shadow IT"; it must be registered on the bank's enterprise model inventory. | **Enterprise Model Registration:** Cataloged on Bank AI Register with Tier-2 (Medium-High) risk rating, designated AI Product Owner, model lineage, and evaluation benchmarks. | **Chief Risk Officer (CRO)** | Formal AI Inventory Entry & Model Risk Review Committee Sign-Off. |
| **RBI FREE-AI Framework** | **Consumer Disclosure & Explainability:** Banking customers have the right not to be misled by synthetic content. | Customers must never receive unreviewed, hallucinated, or deceptive machine-generated representations. | **Mandatory Human-in-the-Loop Sign-Off:** Frontline agent reviews and approves 100% of outbound text; standard disclosure text approved by Compliance. | **Head of Compliance & Legal** | Outbound Communication Audit Logs (`HTTP 403` negative bypass tests). |
| **RB-IOS 2026 (Sec 16)** | **Statutory 30-Day Resolution Timeline:** Grievances must be resolved within 30 days or face automatic Banking Ombudsman conciliation. | Accelerated handling must not compromise investigation depth or generate premature rejections. | **Day-25 Amber Alert & Weekly QA Audits:** Automated SLA alert triggers Nodal review on Day 25; random weekly QA audit of 5% of AI-assisted resolutions. | **Principal Nodal Officer (PNO)** | % Resolved $\le 30$ Days ($\ge 95\%$ target); Ombudsman Escalation Rate ($\le 1.5\%$). |
| **Model Risk Management (SR 11-7 Best Practice)** | **Model Drift & Semantic Degradation:** LLM inference quality degrades over time due to policy updates, prompt drift, or vendor model updates. | The model might generate inaccurate policy interpretations as circulars evolve. | **Continuous Benchmarking & Override Monitoring:** Re-run 100-question golden evaluation test set monthly; trigger mandatory root-cause audit if override rate exceeds 15%. | **AI Product Owner** | **Override Rate Trend** (Project A3 Risk Lens; tolerance $\le 15.0\%$). |

---

## 3. Enterprise AI Risk Register & Early Warning Telemetry (Step 7b)

The risk register defines the six primary operational, technological, and organizational failure modes, pairing each with mitigation protocols and real-time leading indicators instrumented in Project A3:

| Risk ID | Risk Description | Pre-Mitigation Likelihood | Pre-Mitigation Impact | Inherent Risk Severity | Risk Mitigation Protocol | Project A3 Early Warning Indicator | Action Threshold | Accountable Risk Owner |
|---|---|---|---|---|---|---|---|---|
| **RSK-01** | **Flawed Policy Citation Leading to Misleading Reply:** RAG system retrieves an outdated circular or hallucinates an incorrect settlement clause. | Medium | High | **High** | Mandatory clause citation enforcement; prompt engineered refusal on missing source ($<0.75$ similarity); human agent review of every draft; monthly 100-question golden set benchmarking. | **Agent Override Rate** (monitored weekly) | **$> 15.0\%$ for 2 consecutive weeks** | **AI Product Owner** |
| **RSK-02** | **Customer PII Transmitted to Public LLM Endpoint:** Sensitive Aadhaar, PAN, or account numbers leak to an external foundation model provider. | Low | High | **High** | Client-side regex and NER tokenization filter; Zero Data Retention contractual clauses; synthetic adversarial red-teaming test set (50 edge cases). | **PII Blocks Metric** (Project A3 Risk lens) | **Sudden drop to 0 or spike $> 500/\text{wk}$** | **CISO / IT Security** |
| **RSK-03** | **Frontline Change Resistance & Low Adoption:** Frontline dispute agents avoid using the copilot due to workflow friction or fear of job replacement. | Medium | High | **High** | Dedicated change champions per team; mandatory 2-hour onboarding training; 15-minute weekly user feedback huddles; clear executive messaging that AI eliminates administrative typing, not jobs. | **Active Agents & Adoption %** (Project A3 Sponsor lens) | **Active Agents $< 60\%$ of pilot cohort** | **Head of Customer Service (Sponsor)** |
| **RSK-04** | **Saved Capacity Fails to Convert to Monetary Value:** Agent time saved (6 min/case) is absorbed into non-productive slack rather than cashable financial return. | Medium | Medium | **Medium** | Finance agreement on natural attrition absorption, reallocation of dispute capacity to complex fraud investigations, and overtime reduction. | **Realised Value vs. Target** (Project A3 Executive lens) | **Realised Value $< 80\%$ of plan** | **Chief Financial Officer (CFO)** |
| **RSK-05** | **Token Cost Overrun on Model Inference:** Excessive prompt context, lack of caching, or query runaway causes API inference costs to exceed budget. | Low | Low | **Low** | Strict output token caps (max 450 tokens); semantic model routing (Haiku for triage); 90% prompt caching on static policies; automated monthly cost ceiling threshold alerts. | **Cost per Run (INR)** (Project A3 Executive lens) | **Cost per Run $> ₹2.00$** | **AI Product Owner** |
| **RSK-06** | **Vendor API Deprecation or Model Quality Shock:** Cloud vendor updates model weights or deprecates API, degrading response accuracy. | Medium | Medium | **Medium** | Pin exact model version snapshots (`claude-sonnet-5.5-20261022`); run automated 200-item regression test suite prior to deploying any model update. | **Agent Acceptance Rate** (Project A3 Operations lens) | **Acceptance Rate $< 80.0\%$** | **IT Enterprise Architecture** |

---

## 4. Governance Operating Model: RACI Matrix (Step 7c)

Accountability across the transformation lifecycle is governed by an enterprise **RACI Matrix** (*Responsible, Accountable, Consulted, Informed*). In strict adherence to governance principles, **exactly one Accountable role (`A`)** is assigned per activity:

* **Legend:**
  * **`R` (Responsible):** The role that executes the activity or build.
  * **`A` (Accountable):** The single individual with ultimate decision, veto, and sign-off authority.
  * **`C` (Consulted):** Subject matter experts who must provide input prior to execution.
  * **`I` (Informed):** Stakeholders kept updated on progress, outcomes, and status.

### Enterprise RACI Assignment Table

| Transformation Governance Activity | Executive Sponsor (Head of Customer Service) | AI Product Owner | IT & Enterprise Architecture | Compliance & Risk (CRO / PNO) | Frontline Complaint Team Leads |
|---|---|---|---|---|---|
| **1. Approve AI Use Cases & Capital Allocation** | **Accountable (`A`)** | Responsible (`R`) | Consulted (`C`) | Consulted (`C`) | Informed (`I`) |
| **2. Solution Engineering, RAG Build & Testing** | Informed (`I`) | **Accountable (`A`)** | Responsible (`R`) | Consulted (`C`) | Consulted (`C`) |
| **3. Stage Gate Go/No-Go Approval (Gates 1, 2, 3)** | **Accountable (`A`)** | Responsible (`R`) | Consulted (`C`) | Responsible / Veto (`R`) | Consulted (`C`) |
| **4. Operational Monitoring & KPI Review (A3)** | Informed (`I`) | **Accountable (`A`)** | Responsible (`R`) | Consulted (`C`) | Responsible (`R`) |
| **5. Data Incident & Privacy Breach Management** | Informed (`I`) | Responsible (`R`) | Responsible (`R`) | **Accountable (`A`)** | Informed (`I`) |

---

## 5. Model Risk Management (MRM) & Continuous Drift Control

To satisfy Model Risk Management guidelines (analogous to US Fed SR 11-7 adopted by Indian commercial banks), Kestrel Bank establishes an ongoing drift verification cadence:

```
                                 CONTINUOUS MRM CADENCE
                                            │
        ┌───────────────────────────────────┼───────────────────────────────────┐
        ▼                                   ▼                                   ▼
[WEEKLY TELEMETRY AUDIT]           [MONTHLY GOLDEN BENCHMARK]           [QUARTERLY POLICY RETEST]
Review A3 Risk Dashboard:         Execute 100-Question Test Set:       Ingest newly issued RBI Circulars;
• Override Rate vs 15% limit       • Citation accuracy >= 85%           update RAG vector indices;
• PII Blocks intercept count       • Zero hallucination check           run regression suite before live.
• P95 Latency under 5.0 s          • Re-evaluate prompt templates
```

* **The 15% Override Review Tripwire:** If the frontline agent override rate exceeds 15.0% for two consecutive weeks, new prompt changes are frozen immediately. The AI Product Owner and Lead Compliance Officer must inspect the 50 most recent rejected cases, update few-shot prompt examples, and re-certify the model before releasing the freeze.
