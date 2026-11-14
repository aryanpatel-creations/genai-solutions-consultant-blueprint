# Kestrel Bank: AI Transformation Blueprint (Category A Portfolio)

> **"I scoped the AI opportunity like a consultant, then built the prototype like an engineer."**  
> **Author:** Aryan Patel (MBA in Business Analytics)  
> **Target Roles:** GenAI Solutions Consultant · AI Strategy Consultant · Techno-Functional Advisory  
> **Target Firms:** Big 4 Advisory (EY GDS, Deloitte USI, PwC AC, KPMG) & Strategy Consulting  
> **Environment:** Python 3.11+ · pandas · Plotly · Streamlit · Matplotlib · Microsoft Excel · PowerPoint · Draw.io

---

## 1. Executive Portfolio Overview

This repository represents the comprehensive **Category A (Management Consulting)** half of an elite GenAI Solutions Consultant portfolio. 

Working as the lead techno-functional consultant for **Kestrel Bank**—a fictional mid-sized Indian private commercial bank handling ~40,000 monthly complaints across 120 frontline agents—the engagement answers three decisive boardroom questions:
1. *"Where should Kestrel Bank deploy Artificial Intelligence across the complaint lifecycle?"*
2. *"What financial, operational, and regulatory return will it deliver?"*
3. *"How can the bank roll it out safely under RBI FREE-AI, RB-IOS 2026, and DPDP Act 2023 guidelines?"*

The work is grounded in **real empirical data** (346,481 bank complaints from the Consumer Financial Protection Bureau, enriched with 156,333 FOIA complaint narratives), primary operational interviews with Indian commercial banking professionals, multi-scenario corporate finance modeling, and automated regression testing.

---

## 2. The Four Pillar Deliverables

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 KESTREL BANK TRANSFORMATION BLUEPRINT                                  │
├────────────────────────────┬────────────────────────────┬──────────────────────────────────────────────┤
│ Project A1: Lean Diagnostic│ Project A2: ROI Calculator │ Project A3: AI Value Dashboard               │
│ • Python DMAIC pipeline    │ • Multi-scenario Excel     │ • 16 Tested KPI functions (100% test pass)   │
│ • 346,481 complaints       │ • Full NPV: +₹127.5 Lakh   │ • 4 Stakeholder views (CFO, COO, CRO, Spon)  │
│ • Pareto 80/20 & 6 Fixes   │ • Payback: 18 Months       │ • Streamlit web app + 5-page PDF report      │
│ • 5-Swimlane As-Is BPMN    │ • Token Spend: Only 8.2%   │ • Slicers, thresholds & early warnings       │
├────────────────────────────┴────────────────────────────┴──────────────────────────────────────────────┤
│ Flagship A: Full AI Transformation Blueprint                                                           │
│ • Step 1: Framing (SCQ & MECE Issue Tree)              • Step 6: Executive Business Case Slide         │
│ • Step 2: Discovery (3 Banking Interviews & P1-P5)      • Step 7: Governance Plan (DPDP, FREE-AI, RACI) │
│ • Step 3: To-Be BPMN (7 [H], 4 [R], 3 [AI], 0 [AG])    • Step 8: 12-Month Gated Roadmap (ProjectLibre) │
│ • Step 4: AI-Aware BRD, User Stories & RTM             • Step 9: 10-Slide Executive Presentation Deck  │
│ • Step 5: Prioritisation Matrix & Negative Boundaries  • Step 10: 2-Page Case Study & STAR Story       │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### Project A1: Complaint Process Diagnostic (Lean Six Sigma DMAIC)
* **Objective:** Identify operational bottlenecks, quantify defect distributions, and establish which problems require Lean process fixes rather than expensive AI.
* **Key Artifacts:**
  * [01_A1_charter.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/01_A1_diagnostic/outputs/A1_charter.md): Project charter grounded in 346,481 bank complaints.
  * [pareto_issues.png](file:///c:/Users/aryan/Desktop/project%201%20strategy/01_A1_diagnostic/outputs/pareto_issues.png): Pareto chart proving 10 of 20 issues drive 80% volume; top issue is "Managing an account" (26.2%).
  * [as_is.drawio](file:///c:/Users/aryan/Desktop/project%201%20strategy/01_A1_diagnostic/outputs/as_is.drawio): 5-swimlane As-Is process map (11 `[H]`, 1 `[R]`, 0 `[AI]`, 0 `[AG]`).
  * [A1_onepager.pdf](file:///c:/Users/aryan/Desktop/project%201%20strategy/01_A1_diagnostic/outputs/A1_onepager.pdf): Executive A4 landscape diagnostic summary.
* **Key Consultant Takeaway:** 15% of complaints stem from inflexible fee waiver policies. Recommending a ₹1,500 frontline discretionary waiver eliminates rework before applying AI.

---

### Project A2: GenAI Cost & ROI Calculator (Excel Financial Model)
* **Objective:** Model the 3-year Total Cost of Ownership (Capex, Opex, Tokens), evaluate Base/Worst/Best scenarios, and analyze financial sensitivities.
* **Key Artifacts:**
  * [A2_GenAI_Cost_ROI.xlsx](file:///c:/Users/aryan/Desktop/project%201%20strategy/02_A2_business_case/A2_GenAI_Cost_ROI.xlsx): Fully dynamic workbook with named ranges and `=CHOOSE()` scenario switches.
  * [A2_BUILD_GUIDE.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/02_A2_business_case/A2_BUILD_GUIDE.md): Cell-by-cell architectural defense guide.
  * [tornado.png](file:///c:/Users/aryan/Desktop/project%201%20strategy/02_A2_business_case/outputs/tornado.png): Tornado sensitivity chart proving Frontline Adoption is the #1 financial lever (₹174.1L NPV swing).
  * [A2_one_pager.pdf](file:///c:/Users/aryan/Desktop/project%201%20strategy/02_A2_business_case/A2_one_pager.pdf): Boardroom financial summary.
* **Key Financial Truths:**
  * **Full 3-Year NPV:** **+₹127.5 Lakh** | **Payback:** **18 Months** | **ROI:** **85.9%**
  * **Hard-Only NPV:** **-₹23.4 Lakh** (Cashable labor alone cannot justify Capex; avoided Ombudsman fees of ₹194.4L defend the build).
  * **Token Spend Reality:** Model tokens represent just **8.2% of total spend** (₹18.3L / ₹224.3L), costing only **₹2.12 ($0.0241) per complaint**.

---

### Project A3: AI Value Dashboard (Streamlit · Plotly · Python)
* **Objective:** Instrument real-time operational governance across four executive audiences to answer: *"Is the AI working?"*
* **Key Artifacts:**
  * [kpis.py](file:///c:/Users/aryan/Desktop/project%201%20strategy/03_A3_dashboard/kpis.py): Decoupled pure functional KPI engine (16 tested functions; identical parameters to A2).
  * [dashboard.py](file:///c:/Users/aryan/Desktop/project%201%20strategy/03_A3_dashboard/dashboard.py): Interactive Streamlit app with CFO, COO, CRO, Sponsor, and KPI Dictionary tabs.
  * [A3_AI_Value_Report.pdf](file:///c:/Users/aryan/Desktop/project%201%20strategy/03_A3_dashboard/outputs/A3_AI_Value_Report.pdf): 5-page static executive PDF report.
  * [test_kpis.py](file:///c:/Users/aryan/Desktop/project%201%20strategy/03_A3_dashboard/tests/test_kpis.py): Automated unit test suite (**22/22 tests passing**).
* **Key Consultant Takeaway:** Built in Python so the exact same KPI code ingests simulated pilot data today and connects directly to Category B live agent logs tomorrow without rewriting BI measures.

---

### Flagship A: AI Transformation Blueprint
* **Objective:** Comprehensive institutional blueprint from discovery to board presentation.
* **Deliverable Directory:**
  * **Framing:** [00_framing.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/00_framing.md) (SCQ & MECE Issue Tree).
  * **Discovery:** [stakeholder_map.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/discovery/stakeholder_map.md) · [interview_notes.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/discovery/interview_notes.md) (3 banking interviews) · [pain_points.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/discovery/pain_points.md) (Grounded P1–P5).
  * **Process Redesign:** [to_be.drawio](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/diagrams/to_be.drawio) (7 `[H]`, 4 `[R]`, 3 `[AI]`, 0 `[AG]`) · [to_be_process_description.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/diagrams/to_be_process_description.md) (5 HITL rules).
  * **Requirements:** [BRD.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/requirements/BRD.md) · [user_stories.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/requirements/user_stories.md) · [rtm.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/requirements/rtm.md).
  * **Prioritisation:** [use_case_prioritisation.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/prioritisation/use_case_prioritisation.md) · [value_vs_feasibility.png](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/outputs/value_vs_feasibility.png) (9 use cases, Decision Ladder, what NOT to automate).
  * **Commercial Case:** [business_case_slide.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/business_case/business_case_slide.md) (Hard vs. full NPV walk, 4 CFO messages).
  * **Governance Plan:** [governance_plan.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/governance/governance_plan.md) (Control map, 6 risks, RACI, 15% override tripwire).
  * **Roadmap:** [roadmap.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/roadmap/roadmap.md) · [roadmap.csv](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/roadmap/roadmap.csv) (12 months, 4 phases, 3 stage gates).
  * **Executive Deck:** [executive_deck.pptx](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/deck/executive_deck.pptx) (10 action-title slides) · [executive_deck_storyboard.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/deck/executive_deck_storyboard.md).
  * **Case Study:** [case_study.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/04_FlagshipA/case_study.md) (2-page standard executive case study).

---

## 3. How to Run & Verify the Code

### 1. Run Unit Tests on the KPI Analytics Engine
```powershell
# Run from repository root
.\.venv\Scripts\pytest -q 03_A3_dashboard
# Output: 22 passed in 0.83s
```

### 2. Launch the Interactive Streamlit AI Value Dashboard
```powershell
cd 03_A3_dashboard
..\.venv\Scripts\streamlit run dashboard.py
# Access dashboard at http://localhost:8501
```

### 3. Generate the 5-Page Static PDF Executive Report
```powershell
cd 03_A3_dashboard
..\.venv\Scripts\python a3_report.py
# Output saved to outputs/A3_AI_Value_Report.pdf
```

### 4. Regenerate the Value-vs-Feasibility Scatter Matrix
```powershell
cd 04_FlagshipA
..\.venv\Scripts\python scorecard_matrix.py
# Output saved to matrix.png
```

---

## 4. Governance & Traceability Audit

* **[docs/traceability.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/docs/traceability.md):** 100% of promised deliverables verified and mapped to physical files.
* **[docs/interview_answers.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/docs/interview_answers.md):** 10 core interview defense questions answered with empirical data.
* **[docs/DECISIONS.md](file:///c:/Users/aryan/Desktop/project%201%20strategy/docs/DECISIONS.md):** Complete architectural log covering DEC-001 through DEC-009.
* **[00_admin/assumptions_register.xlsx](file:///c:/Users/aryan/Desktop/project%201%20strategy/00_admin/assumptions_register.xlsx):** Synchronized assumptions register (AS-01 to AS-05).

---

## 5. Non-Negotiable Consultant Principles Upheld
1. **Zero Fabrication:** CFPB data limitation acknowledged upfront (CFPB has NO resolution dates; handling times and resolution costs are labeled as ASSUMED or INTERVIEW-VALIDATED).
2. **Honest Framing:** Hard-only and full commercial returns presented together on every slide and report.
3. **Technological Frugality:** Began with 6 Lean non-AI fixes; explicitly rejected autonomous agents (`[AG] = 0`) due to RBI FREE-AI liability.
4. **Change Leadership:** Quantified that adoption rate creates a ₹174.1 Lakh NPV swing, making human training the primary investment.
