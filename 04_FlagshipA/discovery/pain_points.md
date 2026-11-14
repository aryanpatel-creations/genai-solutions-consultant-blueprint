# Discovery: Operational Pain-Point Register (pain_points.md)

> **Client:** Kestrel Bank  
> **Engagement:** AI Transformation Blueprint — Complaints Redressal Modernisation  
> **Prepared by:** Aryan Patel (MBA Business Analytics)  
> **Deliverable:** Flagship Step 2c — Baseline Pain-Point Register (Grounded in A1 Data & Primary Interviews)

---

## 1. Consolidated Pain-Point Register

The pain-point register synthesizes empirical evidence from our Lean Six Sigma diagnostic (Project A1: 346,481 bank complaints, 100 tagged narratives, 6 K-Means clusters) and qualitative operational findings from three frontline banking interviews:

| ID | Operational Pain Point | Empirical & Interview Evidence | Who Feels It | Operational Frequency | Business Impact | Quantitative Baseline Metric | Target Post-Transformation Metric |
|---|---|---|---|---|---|---|---|
| **P1** | **Fragmented Knowledge Retrieval:** Frontline agents spend 7–8 minutes navigating 4 disconnected systems (Core Banking, Card Base24, CRM, and intranet PDF circulars) to locate applicable bank policies and RBI master directions. | A1 narrative tagging: **38% Knowledge** root-cause; 3 of 3 interviews confirm PDF search friction. | Frontline Dispute Agents (120 users) | Every complaint (~40,000 / mo) | **High:** Drives 30% of total handling time; causes inconsistent policy explanations. | Baseline AHT: **25.0 minutes** (8.0 min spent in manual lookup). | Target AHT: **19.0 minutes** (Policy lookup cut to $<1.5$ min via RAG). |
| **P2** | **Inaccurate Initial Intake & Queue Bouncing:** Intake web portal lacks structured dispute categories, causing customers to select generic categories. Complaints bounce between Cards, Savings, and Digital teams before reaching the correct handler. | A1 narrative tagging: **27% Triage** root-cause; Interview #1 confirms **1 in 5 cases (20%)** misdirected. | Frontline Agents & Customers | ~20% of inbound volume (~8,000 cases / mo) | **Medium:** Adds 24–48 hour routing lag and wastes 5 min of agent time re-triaging misdirected tickets. | Baseline Re-Route Rate: **20.0%** of inbound complaints. | Target Re-Route Rate: **$\le 5.0\%$** via automated Haiku classification. |
| **P3** | **Manual Response Formulation Fatigue:** Agents spend 8–10 minutes drafting customized explanation letters from scratch, leading to grammatical errors, omissions of statutory rights, and agent cognitive burnout. | A1 narrative tagging: **17% Summary / 3% Draft**; Interview #3 confirms drafting consumes 8–10 min per case. | Frontline Dispute Agents | Every complaint (~40,000 / mo) | **Medium:** Drives 35% of AHT; variable tone triggers customer dissatisfaction and reopen cycles. | Baseline Drafting Time: **8.5 minutes** per complaint. | Target Drafting Time: **2.5 minutes** (Agent edits pre-drafted Claude Sonnet reply). |
| **P4** | **30-Day Statutory Resolution Drift:** Complex multi-system investigations stall across operations and fraud teams, causing cases to exceed the 30-day RB-IOS 2026 statutory window and escalate to the RBI Ombudsman. | A1 control gap analysis; Interview #2 confirms **11%–13% of cases stall past Day 25**; 3% escalate to Ombudsman. | Principal Nodal Officer, Compliance | ~12% of complaints (>25 days); 3% Ombudsman escalations | **Critical:** Triggers ₹3,500/case direct RBI conciliation fees plus regulatory compliance sanctions. | % Resolved $\le 30$ days: **88.0%**; Ombudsman rate: **3.0%** (~1,200/mo). | % Resolved $\le 30$ days: **$\ge 95.0\%$**; Ombudsman rate: **1.5%** (~600/mo). |
| **P5** | **Recurring Systemic Product & Fee Defects:** High volume of repeat complaints arising from non-transparent fees (e.g., annual maintenance, SMS charges) that lack automated root-cause feedback loops to product managers. | A1 Pareto: **10 of 20 issues drive 80% volume**; "Managing an account" represents **26.2% of volume (90,902 cases)** with an **18.2% relief rate**; Bank-wide relief rate is **24.8%** ($13.1\%$ monetary, $11.8\%$ non-monetary). | Retail Customers & Operations | Top issue drives 26.2% of volume; 15% are petty fee disputes | **High:** Causes avoidable customer churn, Brand degradation, and massive rework loops. | Customer Relief Rate: **24.8%**; Repeat Account Issues: **26.2%**. | Defect Elimination: **15% fee volume eliminated** via Lean discretionary waiver policy. |

---

## 2. Strategic Linkage to Transformation Levers

```
Pain Point          Root Cause              Lean Process Fix (Non-AI)       AI Intervention Lever
──────────────────────────────────────────────────────────────────────────────────────────────────
P1 (Search)   ───►  4 Disconnected Systems  ───► Standardized CRM Links     ───► Policy Knowledge Q&A (RAG)
P2 (Triage)   ───►  Vague Intake Categories ───► 3-Level CRM Taxonomy       ───► Auto-Triage & Routing (Haiku)
P3 (Drafting) ───►  Manual Typing           ───► Response Template Library  ───► Pre-Drafted Replies (Sonnet)
P4 (30-Day)   ───►  Queue Stalls            ───► Day-25 Amber Alert SLA     ───► Escalation Summary Assistant
P5 (Defects)  ───►  Petty Fee Policies      ───► ₹1,500 Discretionary Waiver───► Unsupervised Theme Mining
```
