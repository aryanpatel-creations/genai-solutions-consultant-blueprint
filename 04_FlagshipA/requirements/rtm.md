# Requirements Traceability Matrix (RTM) (rtm.md)

> **Client:** Kestrel Bank  
> **Engagement:** AI Transformation Blueprint — Complaints Redressal Modernisation  
> **Prepared by:** Aryan Patel (MBA Business Analytics)  
> **Deliverable:** Flagship Step 4 — Requirements Traceability Matrix (RTM)  
> **Companion Document:** `04_FlagshipA/requirements/BRD.md` & `04_FlagshipA/requirements/user_stories.md`

---

## 1. Full Traceability Grid: Business Problem to Production Verification

The **Requirements Traceability Matrix (RTM)** guarantees bi-directional traceability across the entire lifecycle: connecting each empirical **Pain Point** (discovered in A1) to its **Business Objective**, **Functional / Non-Functional Requirement**, **Agile User Story**, **Architectural Design Element**, **Verification Test Method**, and **Operational Monitoring KPI** (instrumented in A3):

| Req ID | Target Pain Point | User Story Ref | System / Process Design Element | Verification & Evaluation Method | Primary Monitoring KPI (Project A3 Dashboard) | Lifecycle Status |
|---|---|---|---|---|---|---|
| **FR-01** | **P2** (Intake Misdirection; 20% re-route rate) | **US-01** | AI Triage & Queue Classifier (`[AI]`, Claude Haiku 5.5) | Benchmark against 200 labeled historical complaints; target $\ge 90\%$ accuracy. | **Acceptance Rate** ($\ge 80\%$) & **Runs per Day** | Ready for Architecture Review |
| **FR-02** | **P1** (Searching 4 systems; 8 min lookup) | **US-02** | Policy Knowledge Q&A Assistant (`[AI]`, Sonnet 5.5 + RAG) | 100-question golden test set evaluated by 2 compliance reviewers; target $\ge 85\%$. | **P95 Latency** ($\le 5.0\text{ s}$) & **Cost per Run** | Ready for Architecture Review |
| **FR-03** | **P3** (Drafting from scratch; 8.5 min fatigue) | **US-03** | AI Response Drafting Copilot (`[AI]`, Claude Sonnet 5.5) | Frontline agent usability pilot; evaluate draft completeness and tone consistency. | **Hours Saved** ($\ge 3,000\text{ hrs}$) & **Realised Value** | Ready for Architecture Review |
| **FR-04** | **P3 / P4** (Regulatory risk of bad responses) | **US-04** | Mandatory Outbound Approval HITL Review Gate (`[H]`) | Automated negative boundary test: attempt automated bypass without agent token (HTTP 403). | **Override Rate** ($\le 15\%$) & **Human Escalation Rate** | Ready for Architecture Review |
| **FR-05** | **P4** (30-day statutory resolution drift) | **US-05** | Day-25 Amber Alert & Case History Summarizer (`[R]` / `[AI]`) | Simulation on 50 past Ombudsman cases; verify Day-25 trigger and summary accuracy. | **Human Escalation Rate** ($\le 8\%$) & Ombudsman Rate | Ready for Architecture Review |
| **FR-06** | **P5** (Petty fee disputes clogging queues) | **US-06** | Frontline Discretionary Waiver Engine ($\le ₹1,500$) (`[H]` / `[R]`) | Core banking ledger reversal test; audit rolling 12-month customer waiver frequency. | **Customer Relief Rate** & **Average Handle Time** | Ready for Architecture Review |
| **NFR-01** | **P1 / Compliance** (DPDP customer privacy) | **US-07** | Client-Side DPDP PII Masking & Tokenization Gateway (`[R]`) | Adversarial benchmark on 50 synthetic high-risk PII payloads; zero leakage permitted. | **PII Blocks** (944 pilot intercepts) & **Guardrail Flags** | Ready for Architecture Review |
| **NFR-02** | **P1** (Operational responsiveness) | **US-02** | Low-Latency Policy Retrieval Architecture (<5s) | Load testing under 60 concurrent agent sessions using Apache JMeter / Locust. | **P95 Latency** ($\le 5.0\text{ s}$) | Ready for Architecture Review |
| **NFR-03** | **Commercial Viability** (Model TCO control) | **US-02 / US-03** | Anthropic Prompt Caching & Model Routing Optimization | Continuous token usage telemetry; verify cache hit rate $\ge 85\%$ on static policies. | **Cost per Run** ($\le ₹2.00$; pilot ₹0.70) & **AI Cost (INR)** | Ready for Architecture Review |
| **NFR-04** | **Change Management** (Frontline adoption) | **All** | Frontline Agent Training & Champion Incentive Program | Weekly active user tracking across all 120 pilot agents in 4 operational units. | **Active Agents** (120) & **Adoption %** ($\ge 60\%$) | Ready for Architecture Review |

---

## 2. Verification Protocol Summary

```
   Business Pain Point (A1)
             │
             ▼
   Functional Requirement (BRD)
             │
             ▼
   Agile User Story & Acceptance Criteria
             │
             ▼
   BPMN Architectural Step (Draw.io XML)
             │
             ▼
   Automated Test Suite (Golden Dataset)
             │
             ▼
   Operational Telemetry & Governance KPI (A3 Dashboard)
```
Every requirement is closed-loop: it originates in real customer complaint data, maps to an architectural container, is bounded by automated tests, and reports live status to executive leadership.
