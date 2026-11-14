# Deliverables Traceability Matrix (traceability.md)

This matrix maps every promised deliverable from Section 4 of the project specification to its target file, current status, and verification date.

---

## 1. Project A1: Complaint Process Diagnostic (Lean Six Sigma DMAIC)
| Promised Deliverable | Target File | Status | Verification Date | Notes |
|---|---|---|---|---|
| Problem statement & charter | `01_A1_diagnostic/outputs/A1_charter.md` | Complete | 2026-11-14 | Real baseline numbers (346,481 complaints) |
| SIPOC & CTQ table | `01_A1_diagnostic/outputs/SIPOC.md`, `CTQ.md`, `Flagship_A_templates.xlsx` | Complete | 2026-11-14 | Mapped 7 steps, CTQ metrics & targets |
| Baseline KPI table | `01_A1_diagnostic/outputs/baseline_kpis.csv` | Complete | 2026-11-14 | Measured from 24-month bank data |
| Relief rate by issue | `01_A1_diagnostic/outputs/relief_by_issue.csv` | Complete | 2026-11-14 | 20 issues with complaints & relief rates |
| Pareto chart & 80/20 finding | `01_A1_diagnostic/outputs/pareto_issues.png` | Complete | 2026-11-14 | 10 of 20 issues reach 80% cumulative |
| 100 tagged narratives sample | `01_A1_diagnostic/outputs/narrative_sample_to_tag.csv`, `Flagship_A_templates.xlsx` | Complete | 2026-11-14 | 100 sample complaints tagged & confirmed |
| Fishbone & 5 Whys (top 2 causes) | `01_A1_diagnostic/outputs/fishbone.png`, `5_whys.md` | Complete | 2026-11-14 | Grounded in 100 tagged narrative evidence |
| As-is process map (draw.io) | `01_A1_diagnostic/outputs/as_is.drawio` | Complete | 2026-11-14 | 5 swimlanes, H/R tags, timing & waste |
| Non-AI fixes, AI opps, control plan | `Flagship_A_templates.xlsx` (Fixes, Control), `ai_opportunities.md` | Complete | 2026-11-14 | 6 Lean non-AI fixes & 5 control KPIs |
| One-page A1 executive summary | `01_A1_diagnostic/outputs/A1_onepager.pdf`, `A1_onepager.png` | Complete | 2026-11-14 | Executive A4 landscape one-pager |

---

## 2. Project A2: GenAI Cost & ROI Calculator
| Promised Deliverable | Target File | Status | Verification Date | Notes |
|---|---|---|---|---|
| Aryan's custom Excel workbook | `02_A2_business_case/A2_GenAI_Cost_ROI.xlsx` | Complete | 2026-11-14 | Verified cell-by-cell formulas & named ranges |
| Scenarios (Worst/Base/Best) | `A2_GenAI_Cost_ROI.xlsx` (Inputs sheet) | Complete | 2026-11-14 | Dynamic `=CHOOSE(Scenario, ...)` switch |
| UnitCost calculation ($0.01702 check) | `A2_GenAI_Cost_ROI.xlsx` (UnitCost sheet) | Complete | 2026-11-14 | Hand-check passes: Policy Q&A = $0.01702/call |
| 3-Year CashFlow & Summary | `A2_GenAI_Cost_ROI.xlsx` (CashFlow, Summary) | Complete | 2026-11-14 | Full NPV ₹127.5L, 18m payback, 86% ROI, 8.2% tokens |
| Tornado sensitivity sheet & chart | `A2_GenAI_Cost_ROI.xlsx` (Tornado sheet), `tornado.png` | Complete | 2026-11-14 | Adoption is #1 lever (₹174.1L swing) |
| One-page executive summary | `02_A2_business_case/A2_one_pager.pdf`, `A2_one_pager.png` | Complete | 2026-11-14 | 4 executive messages & hard vs full distinction |

---

## 3. Project A3: AI Value Dashboard
| Promised Deliverable | Target File | Status | Verification Date | Notes |
|---|---|---|---|---|
| KPI calculation engine (16 KPIs) | `03_A3_dashboard/kpis.py` | Complete | 2026-11-14 | 16 KPI functions matching A2 financial parameters |
| KPI test suite (22 unit tests) | `03_A3_dashboard/tests/test_kpis.py` | Complete | 2026-11-14 | 22/22 tests passing via pytest in 0.83s |
| Interactive Streamlit dashboard | `03_A3_dashboard/dashboard.py` | Complete | 2026-11-14 | 4 audience tabs, dynamic slicers & KPI dictionary |
| PDF executive value report | `03_A3_dashboard/a3_report.py` | Complete | 2026-11-14 | 5-page A4 landscape PDF + 5 PNG slide exports |
| Folder README with screenshots | `03_A3_dashboard/README.md` | Complete | 2026-11-14 | Metrics dictionary, decisions supported, interview defense |

---

## 4. Flagship A: AI Transformation Blueprint
| Step | Deliverable | Target File | Status | Verification Date | Notes |
|---|---|---|---|---|---|
| **Step 1** | Discovery: SCQ & issue tree | `04_FlagshipA/00_framing.md`, `discovery/00_framing.md` | Complete | 2026-11-14 | MECE issue tree mapping all 4 engagement questions |
| **Step 2** | Stakeholder map, interview guide, notes, pain points | `Flagship_A_templates.xlsx` (Stakeholders, Interviews, Pain_points), `discovery/` | Complete | 2026-11-14 | 3 banking interviews, 7 stakeholders, P1-P5 grounded in A1 data |
| **Step 3** | As-is & to-be BPMN (draw.io XML) | `04_FlagshipA/diagrams/to_be.drawio`, `to_be_process_description.md` | Complete | 2026-11-14 | 7 [H], 4 [R], 3 [AI], 0 [AG]; 5 HITL rules; 6 Lean fixes |
| **Step 4** | AI-aware BRD, user stories, RTM | `04_FlagshipA/requirements/BRD.md`, `user_stories.md`, `rtm.md`, `Flagship_A_templates.xlsx` | Complete | 2026-11-14 | 8-section BRD, 7 agile stories, bi-directional RTM |
| **Step 5** | Use-case scorecard, 6 criteria, matrix | `04_FlagshipA/scorecard_matrix.py`, `prioritisation/use_case_prioritisation.md`, `Flagship_A_templates.xlsx` | Complete | 2026-11-14 | 9 use cases, Decision Ladder, matrix plot, negative boundaries |
| **Step 6** | Business case slide (hard vs full) | `04_FlagshipA/business_case/business_case_slide.md` | Complete | 2026-11-14 | Hard vs full NPV walk, 18m payback, CFO talk-track, Tornado walk |
| **Step 7** | Governance: control map, risk register, RACI | `04_FlagshipA/governance/governance_plan.md`, `Flagship_A_templates.xlsx` | Complete | 2026-11-14 | DPDP, FREE-AI, RB-IOS 2026 control map, 6 risks, RACI matrix |
| **Step 8** | 12-month roadmap (3 stage gates) | `04_FlagshipA/roadmap/roadmap.md`, `roadmap.csv`, `Flagship_A_templates.xlsx` | Complete | 2026-11-15 | 4 phases, 3 stage gates, quick win #3, change strategy |
| **Step 9** | 10-slide executive deck | `04_FlagshipA/deck/executive_deck.pptx`, `executive_deck_storyboard.md`, `Flagship_A_templates.xlsx` | Complete | 2026-11-15 | 10 action titles, 8-minute pitch, python-pptx generated |
| **Step 10** | Case study, README, LinkedIn, STAR story | `04_FlagshipA/case_study.md`, `README.md`, `docs/linkedin_post.md`, `docs/star_interview_story.md` | Complete | 2026-11-15 | 2-page case study, root README, LinkedIn post, STAR story |
 
---

## 5. Global Portfolio Governance
| Deliverable | Target File | Status | Notes |
|---|---|---|---|
| Client Brief | `00_admin/client_brief.md` | Complete | Baseline fictional bank setup |
| Sources Register | `00_admin/sources.md` | Complete | CFPB, RBI, and Tech pricing sources |
| Assumptions Register | `00_admin/assumptions_register.xlsx` | Complete | AS-01 through AS-05 verified |
| Architectural Decision Log | `docs/DECISIONS.md` | Complete | Logged DEC-001 through DEC-010 |
| Technical Environment Log | `docs/ENVIRONMENT.md` | Complete | System specifications and pip freeze |
| Interview Preparation Document | `docs/interview_answers.md` | Complete | Mapped all 10 interview questions to empirical results |
