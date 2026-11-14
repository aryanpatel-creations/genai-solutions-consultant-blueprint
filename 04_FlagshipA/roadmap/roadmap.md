# 12-Month Phased Implementation Roadmap & Stage Gates (roadmap.md)

> **Client:** Kestrel Bank  
> **Engagement:** AI Transformation Blueprint — Complaints Redressal Modernisation  
> **Prepared by:** Aryan Patel (MBA Business Analytics, Techno-Functional Consultant)  
> **Deliverable:** Flagship Step 8 — 12-Month Phased Roadmap, Stage Gates & Change Strategy  
> **Data Artifact:** `04_FlagshipA/roadmap/roadmap.csv` (ProjectLibre / MS Project Compatible)

---

## 1. Executive Phased Architecture Overview

A successful enterprise transformation does not attempt a "big-bang" deployment. Instead, the Kestrel Bank AI Transformation Roadmap is structured into **four sequential phases** punctuated by **three rigorous Stage Gates**. 

Phase 0 deploys **zero generative AI**, establishing Lean process baselines and delivering a rapid quick win. Generative AI is piloted internally with human oversight before expanding across all 120 agents:

```
  MONTH 1-2                 MONTH 3-5                 MONTH 6-9                 MONTH 10-12
┌──────────────┐          ┌──────────────┐          ┌──────────────┐          ┌──────────────┐
│   PHASE 0    │ ──[G1]─► │   PHASE 1    │ ──[G2]─► │   PHASE 2    │ ──[G3]─► │   PHASE 3    │
│ Foundations, │          │ Agent Pilot: │          │ Enterprise   │          │ Scale, ML    │
│ Lean Fixes & │          │ Cards &      │          │ Rollout &    │          │ Migration &  │
│ Quick Win #3 │          │ Accounts     │          │ Draft Reply  │          │ Agentic Spec │
└──────────────┘          └──────────────┘          └──────────────┘          └──────────────┘
   (No GenAI)               (Haiku + RAG)             (All 4 Teams)             (Category B)
```

---

## 2. Stage Gate Governance & Go / No-Go Decision Criteria

Each stage gate represents a formal executive review meeting where the Steering Committee evaluates objective evidence. **All criteria must be satisfied to achieve a "GO" decision**:

| Stage Gate | Timeline | Decision Mandate | Strict "Go" Criteria (All Must Be Met) | Evidence Source & Verification Artifact | Accountable Approver |
|---|---|---|---|---|---|
| **Gate 1** | **End of Month 2 (Week 8)** | **Start the Frontline Pilot in Cards & Accounts** | 1. All 6 Lean Six Sigma fixes deployed live in CRM (discretionary waiver $\le ₹1,500$ active).<br>2. Phase 0 Quick Win (#3 Client Feedback Flow) operational with positive sentiment routing.<br>3. DPDP Client-Side PII Masking Gateway built and verified on 50 synthetic test cases (0 leaks).<br>4. Enterprise Model Registration approved on Bank AI Inventory Register (Tier-2 risk).<br>5. Labeled evaluation test sets finalized (200 triage cases, 100 golden policy questions).<br>6. Baseline KPIs established for the 60 pilot agents. | `01_A1_diagnostic/` (Fixes), `04_FlagshipA/` (Control Map, Inventory Entry), Golden Test Sets. | **Executive Sponsor & Chief Risk Officer** |
| **Gate 2** | **End of Month 5 (Week 20)** | **Add Draft Reply Assistant & Expand to All 4 Teams** | 1. Frontline Agent Acceptance Rate $\ge \mathbf{80.0\%}$ on Triage and Policy Q&A.<br>2. Agent Override Rate $\le \mathbf{15.0\%}$ across rolling 4-week window.<br>3. Zero unmasked PII incidents reported.<br>4. $\ge \mathbf{60.0\%}$ of pilot agents active on the platform weekly.<br>5. Ombudsman escalations trending down vs. baseline ($<3.0\%$).<br>6. Financial business case re-run with actual pilot telemetry, confirming $\le 24$-month payback path. | **Project A3 Dashboard Telemetry** (All 4 audience tabs), Updated A2 Business Case Model. | **Sponsor, PNO, CRO, & CFO** |
| **Gate 3** | **End of Month 9 (Week 36)** | **Enterprise Scale & Narrow Agentic Exploration** | 1. Gate 2 operational criteria maintained consistently for 3 full months across all 120 agents.<br>2. Capital Payback proven $\le \mathbf{24 \text{ months}}$ on measured empirical run data.<br>3. Labor cash realisation audit signed off by Finance (attrition absorption / overtime drop).<br>4. Formal Model Risk Management (MRM) compliance audit passed.<br>5. Chief Compliance Officer and Legal sign-off on any prospective customer-facing automation. | Project A3 Dashboard Audit, Finance Realization Report, Annual MRM Audit Sign-off. | **Executive Committee (CEO, CFO, Sponsor, CRO)** |

---

## 3. Detailed Phase Breakdown & Milestones

### Phase 0: Foundations, Lean Six Sigma Fixes & Quick Win (Weeks 1–8 / Months 1–2)
* **Objective:** Remove operational waste, build secure infrastructure, and establish baseline evaluation sets before any GenAI tool touches customer data.
* **Core Tasks:**
  * *Task 1.1:* Operationalize the 6 Lean non-AI fixes (CRM 3-level taxonomy, instant auto-acknowledgement within 2 hours, frontline fee waiver limit up to ₹1,500).
  * *Task 1.2 (Portfolio Quick Win #3):* Deploy Client Feedback Automation using prebuilt Power Automate + AI Builder sentiment analysis. Captures post-resolution feedback and routes negative scores to team leads within 24 hours. (Zero GenAI approval required; delivers immediate sponsor value).
  * *Task 1.3:* Construct data pipelines and the client-side DPDP PII tokenization gateway.
  * *Task 1.4:* Curate and label the 200-complaint triage benchmark and 100-question golden policy evaluation dataset.
  * *Task 1.5:* Complete enterprise model registration on the Bank AI Inventory Register under RBI FREE-AI rules.
* **Milestone:** **Stage Gate 1 Review (Week 8).**

### Phase 1: Internal Agent Copilot Pilot in Cards & Accounts (Weeks 9–20 / Months 3–5)
* **Objective:** Test Triage and Policy Knowledge Q&A in live operations across 60 agents in the Cards and Savings & Current teams.
* **Core Tasks:**
  * *Task 2.1:* Execute change management: assign 1 champion per team and conduct 2-hour onboarding training.
  * *Task 2.2:* Deploy Claude Haiku 5.5 for Triage & Queue Routing ($0.0001/call).
  * *Task 2.3:* Deploy Claude Sonnet 5.5 + RAG for Policy Knowledge Q&A ($0.017/call with prompt caching).
  * *Task 2.4:* Instrument live telemetry feeding the **Project A3 AI Value Dashboard** (monitoring 16 KPIs).
  * *Task 2.5:* Conduct weekly 15-minute frontline feedback huddles to refine prompts based on agent rejections.
  * *Task 2.6:* Re-run the A2 Cost & ROI model with real pilot logs to validate financial payback.
* **Milestone:** **Stage Gate 2 Review (Week 20).**

### Phase 2: Enterprise Rollout & Response Drafting Across All 4 Teams (Weeks 21–36 / Months 6–9)
* **Objective:** Scale to all 120 agents (adding Digital Banking and Branch Escalations) and introduce AI Response Drafting.
* **Core Tasks:**
  * *Task 3.1:* Onboard the remaining 60 agents across Digital Banking and Branch Escalations.
  * *Task 3.2:* Deploy Claude Sonnet 5.5 Response Drafting Assistant, saving 6.0 minutes per complaint.
  * *Task 3.3:* Enforce the mandatory outbound human approval review gate in CRM (`[H]`).
  * *Task 3.4:* Deploy the Day-25 statutory amber alert SLA trigger and chronological case history summarizer.
  * *Task 3.5:* Implement monthly Model Risk Management (MRM) golden benchmark evaluations and monitor the 15% override tripwire.
  * *Task 3.6:* Finance audits cashable labor savings realization.
* **Milestone:** **Stage Gate 3 Review (Week 36).**

### Phase 3: Scale Optimization & Narrow Agentic Exploration (Weeks 37–52 / Months 10–12)
* **Objective:** Optimize operating unit costs and lay the architectural foundation for Category B agentic prototypes.
* **Core Tasks:**
  * *Task 4.1:* Evaluate migrating Triage & Routing from Claude Haiku to a local classical machine learning classifier (scikit-learn trained on 6 months of structured CRM labels), reducing inference costs by 95%.
  * *Task 4.2:* Complete annual regulatory compliance recertification under the DPDP Act 2023 and RBI FREE-AI guidelines.
  * *Task 4.3:* Initiate architectural design for **Category B Agentic Architecture** (autonomous internal document gathering across core banking and card engines).
  * *Task 4.4:* Final Executive Transformation Review and Year 2 capital budgeting.

---

## 4. Operational Change Management Strategy

Our Project A2 Tornado sensitivity analysis proved that frontline adoption is the **#1 financial lever (₹174.1 Lakh NPV swing)**. Change management is therefore engineered directly into the core roadmap:

1. **Frontline Champions Network:** One respected senior agent selected per team (4 champions total) to co-design prompts, test UI ergonomics, and act as peer trainers.
2. **Mandatory 2-Hour Practical Onboarding:** Conducted prior to pilot launch. Focuses on how to prompt the Policy Q&A assistant, how to verify citations, and how to execute one-click overrides.
3. **Weekly 15-Minute "Voice of the Agent" Huddles:** Held every Friday during the pilot. Team leads review top overridden responses, identify confusing prompts, and submit prompt improvement requests to the AI Product Owner.
4. **Proactive Job Security Messaging:** Clear, repeated executive communication from the Head of Customer Service emphasizing: *"The AI assistant exists to eliminate tedious PDF searches and repetitive typing so you can hit your resolution SLAs. It removes administrative drag, not jobs."*

---

## 5. Critical Path & Dependency Management

```
[Lean Fixes & Quick Win #3] ──► [PII Masking Gateway] ──► [Gate 1] ──► [Triage & Policy Q&A Pilot]
                                                                               │
                                                                               ▼
[Full 120-Agent Rollout] ◄── [Gate 2] ◄── [Pilot Telemetry & A2 Re-run] ◄─────┘
         │
         ▼
[Draft Reply Assistant] ──► [MRM Monthly Audits] ──► [Gate 3] ──► [Year 2 Scale & Category B]
```

* **Zero-GenAI Gate 1 Prerequisite:** Under no circumstances will external LLM endpoints be activated until the client-side PII masking gateway passes 100% of adversarial red-team tests and the Bank AI Inventory entry is signed by the CRO.
* **Commercial Gate 2 Tripwire:** If 90-day pilot telemetry fails to achieve an 80% acceptance rate or if Ombudsman escalations do not trend downward, Phase 2 expansion is paused for 30 days of prompt re-engineering.
