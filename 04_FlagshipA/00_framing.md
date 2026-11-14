# Engagement Framing: SCQ & Issue Tree (00_framing.md)

> **Client:** Kestrel Bank (Fictional mid-sized Indian private commercial bank)  
> **Engagement:** AI Transformation Blueprint — Complaints Redressal Modernisation  
> **Prepared by:** Aryan Patel (MBA Business Analytics, Techno-Functional Consultant)  
> **Target Audience:** Executive Committee (CEO, COO, CFO, CRO, Head of Customer Service)  
> **Date:** November 2026

---

## 1. Executive Context & Engagement Framing (SCQ)

Consulting engagements must start with the overarching business problem, not the technological tool. The **SCQ Framework** (Situation, Complication, Question) establishes the strategic rationale for the entire AI transformation engagement:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                   SITUATION                                     │
│ Kestrel Bank is a mid-sized Indian private sector bank handling ~40,000         │
│ complaints per month across 120 dedicated frontline dispute agents structured    │
│ into 4 operational teams (Cards, Savings & Current, Digital Banking, Branch      │
│ Escalations). Loaded agent cost is ₹400/hour.                                   │
└────────────────────────────────────────┬────────────────────────────────────────┘
                                         │
                                         ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                 COMPLICATION                                    │
│ Inbound dispute volume is compounding at 10-15% annually. Frontline agents spend │
│ 15 of 25 minutes per complaint manually searching fragmented core systems,     │
│ circular PDFs, and drafting repetitive responses from scratch. Under the RBI    │
│ Integrated Ombudsman Scheme (RB-IOS 2026), complaints unredressed after 30 days │
│ escalate to the Banking Ombudsman, costing ₹3,500 in direct administrative fees  │
│ plus regulatory scrutiny. Current escalation rate is ~3% (~1,200 cases/month).  │
└────────────────────────────────────────┬────────────────────────────────────────┘
                                         │
                                         ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                             CORE STRATEGIC QUESTION                             │
│ "Where should Kestrel Bank deploy Artificial Intelligence across the complaint  │
│ lifecycle, what financial and operational return will it deliver, and how can   │
│ it be rolled out safely within RBI FREE-AI and DPDP Act governance guardrails?" │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Mutually Exclusive, Collectively Exhaustive (MECE) Issue Tree

To answer the core strategic question with empirical rigor, the problem is decomposed into four mutually exclusive, collectively exhaustive sub-questions. Every project artifact and blueprint step answers one specific branch:

```
Core Strategic Question:
"Where should Kestrel Bank deploy AI in complaint handling, what will it return, and how do we roll it out safely?"
│
├── 1. Where is operational and financial value lost today?
│   │  (Answered by Project A1 Diagnostic & Flagship Steps 2–3)
│   ├── 1.1 Which complaint issues and lifecycle stages drive volume and delays?
│   │       └── Empirical Pareto analysis: 10 of 20 issues drive 80% volume; Top issue is "Managing an account" (26.2%).
│   │       └── Bottleneck: Intake routing is fast (0-day lag), but investigation & drafting consumes 60% of AHT (15 min).
│   └── 1.2 Which underlying root causes require Lean process fixes rather than technology?
│           └── 15% of complaints stem from inflexible fee waiver policies; resolved via ₹1,500 frontline discretionary limits.
│           └── 56% stem from broken cross-team workflows; resolved via standardized CRM taxonomy & auto-acknowledgement.
│
├── 2. Which AI use cases are worth pursuing?
│   │  (Answered by Flagship Step 5 & Scorecard Matrix)
│   ├── 2.1 What is the lowest rung on the AI Decision Ladder that solves each pain point?
│   │       └── Reject autonomous agents (`[AG]`); select Haiku 5.5 for Triage and Sonnet 5.5 + RAG for Policy Q&A / Drafting.
│   └── 2.2 How do candidate use cases score on multidimensional value vs. feasibility?
│           └── 6-criterion evaluation: Triage & Routing (26/30), Policy Q&A (24/30), Draft Reply (22/30) approved for rollout.
│
├── 3. What is the commercial and economic return?
│   │  (Answered by Project A2 Cost & ROI Model & Flagship Step 6)
│   ├── 3.1 What is the full Total Cost of Ownership (Capex, Opex, Cloud Hosting, Tokens)?
│   │       └── Year 0 Capex: ₹86.0 Lakh; Annual Opex: ₹40.0 Lakh fixed + ₹5.5L-₹6.6L variable token spend.
│   │       └── Token spend represents only 8.2% of 3-year TCO; engineering and change management dominate.
│   └── 3.2 What financial returns are generated under Hard-Only vs. Full-Benefit scenarios?
│           └── Hard-Only 3-Year NPV: -₹23.4 Lakh (Cashable capacity alone cannot justify platform Capex).
│           └── Full 3-Year NPV: +₹127.5 Lakh (86% ROI, 18-month payback), driven by ₹194.4 Lakh in avoided Ombudsman escalations.
│           └── Sensitivity: Frontline user adoption is the #1 financial lever (₹174.1 Lakh NPV swing).
│
└── 4. How can the transformation be governed and deployed safely?
    │  (Answered by Project A3 Dashboard & Flagship Steps 4, 7, 8)
    ├── 4.1 How do we ensure compliance with DPDP Act 2023, RBI FREE-AI, and RB-IOS 2026?
    │       └── Mandatory client-side PII tokenization/masking prior to external LLM invocation (944 pilot intercepts).
    │       └── Strict India data residency and audited 72-hour regulatory breach notification protocols.
    ├── 4.2 Where must Human-in-the-Loop (HITL) review gates be enforced?
    │       └── 100% human agent review on outgoing customer text; zero autonomous unreviewed communication.
    │       └── Mandatory supervisor escalation for low-confidence classifications (<0.80) or refunds >₹1,500.
    └── 4.3 How should rollout be phased and gated across the 12-month transformation?
            └── Phase 0 (Months 1–3): Non-AI Lean fixes, data pipelines, golden evaluation test sets.
            └── Phase 1 (Months 4–6): Internal agent copilot pilot across Cards & Accounts (Gate 1 go/no-go).
            └── Phase 2 (Months 7–9): 120-agent full operational rollout across all 4 teams (Gate 2 go/no-go).
            └── Phase 3 (Months 10–12): Continuous monitoring, classical ML migration, and executive sign-off (Gate 3).
```

---

## 3. Scope Boundaries: What Is In vs. Out of Scope

| Dimension | In Scope (Phase 1–2 Transformation) | Out of Scope / Deferred (Phase 3+) | Strategic Rationale |
|---|---|---|---|
| **Target User Group** | 120 internal frontline complaint handling agents & team leads. | External bank customers (direct chat/self-service). | Internal copilot insulates bank from hallucination risk and regulatory exposure under RBI FREE-AI. |
| **System Interaction** | Read-only policy retrieval (RAG) and draft generation in CRM. | Autonomous core banking writes (direct ledger debits). | Core transactional changes require audited human authorization; avoid operational risk. |
| **Model Architecture** | Decoupled multi-model routing (Haiku for triage, Sonnet for RAG/drafting). | Fine-tuning proprietary custom foundational LLMs. | Pre-trained models with dynamic prompt caching deliver $0.017/call economics; custom training is cost-prohibitive. |
| **Autonomous Replies** | Strictly prohibited (`[AG]` tag unused). Human approves 100% of text. | Fully automated straight-through response dispatch. | High regulatory liability under RB-IOS 2026; unreviewed AI communication violates compliance guidelines. |
