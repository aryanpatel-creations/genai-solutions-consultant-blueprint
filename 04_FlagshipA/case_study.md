# Case Study: AI Transformation Blueprint for Kestrel Bank

> **Project Title:** Complaints Redressal Modernisation: From Lean Process Diagnostic to AI-Augmented Architecture  
> **Author:** Aryan Patel (MBA in Business Analytics)  
> **Role:** Lead Techno-Functional Solutions Consultant  
> **Target Institutions:** Top Consulting & Big 4 Advisory Firms (EY GDS, Deloitte USI, PwC AC, KPMG)  
> **Date:** November 2026

---

## 1. Context (60 Words)
Kestrel Bank is a fictional mid-sized Indian private commercial bank handling ~40,000 retail complaints monthly across 120 dedicated dispute agents. The institution operates under the Reserve Bank of India’s Integrated Ombudsman Scheme (RB-IOS 2026). Public Consumer Financial Protection Bureau (CFPB) data served as an empirical proxy for banking defect patterns, while Indian operational baselines were validated through primary industry interviews.

---

## 2. Problem Statement (60 Words)
Dispute volumes were compounding at 12% annually, straining frontline capacity. Average handle time reached 25 minutes, with agents losing 60% of their time manually querying disconnected core banking applications and drafting letters from scratch. Crucially, 12% of complaints drifted past Day 25, threatening statutory 30-day RB-IOS breach thresholds and incurring direct ₹3,500 Ombudsman conciliation fees plus severe regulatory penalties.

---

## 3. Approach & Methodology (150 Words)
We executed an end-to-end management consulting engagement structured across seven sequential phases:
1. **Diagnostic:** Applied Lean Six Sigma DMAIC in Python, analyzing 346,481 bank complaints, deriving baseline KPIs, Pareto distributions, and clustering 156,333 narratives via TF-IDF and K-Means.
2. **Discovery:** Conducted operational interviews across operations managers, nodal grievance officers, and frontline agents; mapped stakeholders on a Power-Interest grid; and baselined five critical pain points (P1–P5).
3. **Process Redesign:** Formulated a 5-swimlane To-Be BPMN architecture in Draw.io, categorizing all 14 steps into standard operational tags (`[H]`, `[R]`, `[AI]`, `[AG]`).
4. **Requirements:** Authored an AI-aware BRD, 7 Agile user stories with testable evaluation criteria, and a bi-directional RTM.
5. **Prioritisation:** Evaluated 9 candidate use cases using the AI Decision Ladder and a 6-criterion scorecard.
6. **Commercial Modeling:** Built a multi-scenario financial model in Excel calculating NPV, payback, and Tornado sensitivities.
7. **Governance & Telemetry:** Engineered a DPDP/FREE-AI control map and an interactive 16-KPI Streamlit dashboard.

---

## 4. Empirical Findings (150 Words)
Our diagnostic uncovered three pivotal operational and financial realities:
* **Defect Concentration [MEASURED]:** Pareto analysis revealed that 10 of 20 issue categories generate 80% of total complaint volume. "Managing an account" alone drove 26.2% (90,902 complaints). A 24.8% customer relief rate confirmed that grievances reflect legitimate bank-side policy and system defects rather than customer misunderstandings.
* **Administrative Drag [SOURCED / ASSUMED]:** Intake routing lag was 0.0 days (99.3% timely response). The bottleneck existed entirely within investigation: agents toggled four disconnected systems, spending 8.0 minutes searching static PDF circulars and 8.5 minutes typing repetitive responses.
* **Policy Inflexibility [MEASURED / ASSUMED]:** 15% of complaints were petty fee disputes (<₹1,000) trapped in 48-hour supervisor approval loops because frontline staff lacked discretionary waiver authority.

---

## 5. Recommended Solution (150 Words)
The recommended transformation pairs non-AI Lean foundations with targeted generative AI copilots:
* **Six Lean Process Fixes (Phase 0):** Implemented immediately without AI cost: frontline discretionary fee waiver authority up to ₹1,500 (eliminating 15% of supervisor rework loops); mandatory 3-level CRM intake taxonomy; instant 2-hour auto-acknowledgements; and Day-25 regulatory amber alerts.
* **Three Targeted AI Copilots:**
  1. *Triage & Queue Routing (Claude Haiku 5.5, $0.0001/call):* Directs inbound complaints with $\ge 90\%$ accuracy, cutting a 20% misrouting rate.
  2. *Policy Knowledge Q&A (Claude Sonnet 5.5 + RAG, $0.017/call):* Retrieves verified policy clauses and mandatory RBI citations in $<2.9$ seconds, cutting search time from 8.0 to 1.5 minutes.
  3. *Response Drafting Assistant (Claude Sonnet 5.5):* Pre-drafts 80%-complete personalized letters, saving 6.0 minutes of drafting time.
* **Human-in-the-Loop Oversight:** Five strict governance rules enforce mandatory human sign-off on 100% of outgoing communications; autonomous agents (`[AG]`) remain deliberately at zero.

---

## 6. Financial Results & Business Case (120 Words)
Under Base Case assumptions (12.0% discount rate, 50% labor cash realization), the transformation delivers:
* **Full Commercial View:** **+₹127.5 Lakh 3-Year Net Present Value**, **1.50-Year (18-Month) Capital Payback**, and an **85.9% ROI** on an initial ₹86.0 Lakh Capex.
* **The Hard vs. Soft Reality:** Hard labor savings alone produce a **-₹23.4 Lakh NPV** (no payback). The commercial business case is defended by avoiding **540 statutory Ombudsman conciliations (+₹194.4 Lakh saved)**.
* **Token Unit Economics:** Variable LLM tokens represent just **8.2% of total spend** (₹18.3L / ₹224.3L), costing only **₹2.12 ($0.0241) per complaint**.
* **Sensitivity:** Frontline adoption is the primary financial swing factor (**₹174.1 Lakh NPV swing**).

---

## 7. Governance, Risk & Regulatory Compliance (100 Words)
The architecture strictly enforces Indian regulatory frameworks:
* **DPDP Act 2023:** Client-side regex/NER gateway tokenizes Aadhaar, PAN, and account numbers prior to API dispatch (intercepting 944 PII occurrences during the pilot). Contracts enforce Zero Data Retention and Mumbai data residency.
* **RBI FREE-AI Framework:** Solutions are cataloged on the Bank AI Inventory (Tier-2 risk). RAG outputs mandate verifiable clause citations; speculative answers are blocked.
* **Model Risk Management:** Telemetry monitors weekly agent overrides. An override rate exceeding 15% for two weeks triggers an automated prompt freeze and compliance audit.

---

## 8. Strategic Reflections & Consultant Learnings (100 Words)
This engagement demonstrated that the most effective AI strategy often begins by eliminating unnecessary AI. 15% of complaints were resolved through a simple policy delegation (the ₹1,500 waiver limit) before writing a single prompt. Furthermore, financial modeling proved that organizational change management—not model selection—drives economic success: a 30% drop in agent adoption destroys ₹174 Lakh in value, dwarfing any token pricing optimization. The role of the solutions consultant is not to automate every workflow, but to design the risk-adjusted human-AI collaboration that protects both the customer and the balance sheet.
