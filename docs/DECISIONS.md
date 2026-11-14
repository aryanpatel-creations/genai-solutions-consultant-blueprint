# Project Decisions & Architectural Log (DECISIONS.md)

This log records all design choices, trade-offs, scope boundaries, and technical adaptations made throughout the Kestrel Bank AI Transformation Blueprint.

---

## Log Format
- **Decision ID:** `DEC-XXX`
- **Date:** YYYY-MM-DD
- **Category:** Environment / Data / Modeling / Governance / Architecture
- **Decision:** What was decided.
- **Context & Rationale:** Why this choice was made.
- **Trade-offs / Alternatives Considered:** What was rejected or deferred.
- **Impacted Deliverables:** Affected projects/files.

---

## Decisions Record

### DEC-001: Python Runtime and Virtual Environment Baseline
- **Date:** 2026-11-14
- **Category:** Environment
- **Decision:** Adopt the host-installed Python 3.11.9 runtime in an isolated local `.venv` within the workspace root (`c:\Users\aryan\Desktop\project 1 strategy\.venv`), installing verified packages across A1, A3, and Flagship A.
- **Context & Rationale:** Aryan confirmed using the existing Python version rather than forcing an external runtime reinstallation. Python 3.11.9 is fully compatible with pandas 2.2+, scikit-learn 1.5+, Streamlit, and openpyxl.
- **Trade-offs:** Fully aligned with zero-cost and local environment stability.
- **Impacted Deliverables:** All Python scripts (`01_A1_diagnostic`, `03_A3_dashboard`, `04_FlagshipA`).

### DEC-002: Direct Download & Processing Pipeline for CFPB Complaint Data
- **Date:** 2026-11-14
- **Category:** Data
- **Decision:** Automate the direct download of the official CFPB complaint database zip archive (`complaints.csv.zip`, ~350 MB) directly into `01_A1_diagnostic/data/raw/` and extract for downstream filtering.
- **Context & Rationale:** Enables programmatic, reproducible data ingestion while maintaining the strict rule: raw data is stored unedited in `data/raw/`.
- **Trade-offs:** Requires network access and local disk space (~1.5GB uncompressed).
- **Impacted Deliverables:** `01_A1_diagnostic` (`a1_step1_load.py`, `a1_step2_clean_kpis.py`).

### DEC-003: Baseline Assumptions without Bank Specific External Citations
- **Date:** 2026-11-14
- **Category:** Modeling
- **Decision:** Adopt standard conservative mid-size Indian private bank operational assumptions (40,000 complaints/month, 120 agents, ₹400/hr loaded cost, 25 min AHT, 3% ombudsman escalation) without requiring immediate individual bank annual report citations during M0.
- **Context & Rationale:** Per Aryan's direction, focus immediately on establishing the mathematical models, templates, and analytical baseline. Specific benchmarks can be refined during stakeholder interview synthesis.
- **Trade-offs:** Numbers are clearly flagged as `ASSUMED` in the assumptions register with medium/low confidence tags until validated.
- **Impacted Deliverables:** `00_admin/assumptions_register.xlsx`, `02_A2_business_case`, `03_A3_dashboard`.

### DEC-004: Multi-Archive Narrative Ingestion & Tag Suggestion Engine
- **Date:** 2026-11-14
- **Category:** Data & Workflow
- **Decision:** Downloaded all 15 FOIA Reading Room archives (Exports 7 through 21) covering the full 24-month window (Sept 2024 – Aug 2026) to restore the `Consumer complaint narrative` field omitted from the raw live export. Enriched the 100-complaint sample (`narrative_sample_to_tag.csv` and `Flagship_A_templates.xlsx`) with `suggested_root_cause` and `suggested_ai_could_help` columns.
- **Context & Rationale:** Since August 2026, the live CFPB download excludes the narrative text column. Joining across the FOIA exports restored 156,333 real narratives (45.1% text rate), establishing the ground truth for text clustering and DMAIC root-cause analysis. Pre-generating suggested tags accelerates Aryan's human review while strictly complying with Rule 6 (Aryan confirms or changes).
- **Trade-offs:** Incurred ~450 MB of temporary zipped narrative data storage in `data/raw/narrative_zips/`.
- **Impacted Deliverables:** `bank_complaints_24m.csv`, `complaints_clean.csv`, `baseline_kpis.csv`, `narrative_sample_to_tag.csv`, `Flagship_A_templates.xlsx`.

### DEC-005: Root-Cause Defect Taxonomy & Lean Waste Prioritization
- **Date:** 2026-11-14
- **Category:** Process & Governance
- **Decision:** Grounded the Fishbone diagram, 5 Whys, and As-Is Process map in the 100 verified complaint narrative tags (Process 56%, System 25%, Policy 15%, Information 3%, People 1%). Prioritized 6 non-AI Lean fixes (including frontline discretionary waiver limits up to ₹1,500 and CRM issue standardization) as pre-requisites to AI investment.
- **Context & Rationale:** Demonstrates management consultant maturity: 15% of complaints are pure Policy issues where AI adds zero value (`ai_could_help = None`). Solving these through delegation of authority and clear disclosure eliminates waste upfront, reducing the volume burden on subsequent AI tools.
- **Trade-offs:** Emphasizes organizational policy alignment rather than purely technical solutions.
- **Impacted Deliverables:** `01_A1_diagnostic/outputs/` (`fishbone.png`, `5_whys.md`, `as_is.drawio`, `A1_onepager.pdf`), `Flagship_A_templates.xlsx`.

### DEC-006: Financial Modeling Conventions & Prompt Caching Economics
- **Date:** 2026-11-14
- **Category:** Financial Modeling
- **Decision:** Locked token unit economics via dynamic Anthropic prompt caching (90% cache hit, 1.25x write penalty), establishing Policy Q&A cost at $0.01702/call and total token cost at ₹2.12/complaint. Modeled cash flows across Year 0 Capex (₹86L) and Years 1–3 Opex (₹40L/yr + tokens) with a 12% discount rate and 50% labor cash realization factor. Day 0 Capex is added outside `=NPV()` to avoid false discounting.
- **Context & Rationale:** Ensures financial rigour compliant with corporate finance standards. Demonstrates that while tokens are variable, they represent only 8.2% of 3-year costs, making adoption and change management the primary financial drivers.
- **Trade-offs:** Hard-only NPV is negative (-₹23.4L); full business case (+₹127.5L) requires defending soft benefits (Ombudsman escalation avoidance).
- **Impacted Deliverables:** `02_A2_business_case/` (`A2_GenAI_Cost_ROI.xlsx`, `A2_BUILD_GUIDE.md`, `A2_one_pager.pdf`, `tornado.png`).

### DEC-007: AI Value Dashboard Architecture & Functional KPI Layer
- **Date:** 2026-11-14
- **Category:** Architecture & Operational Governance
- **Decision:** Structured Project A3 as a decoupled analytics pipeline where a single pure functional Python module (`kpis.py`, 16 functions) acts as the sole source of truth for the interactive Streamlit dashboard (`dashboard.py`), static executive PDF report generator (`a3_report.py`), and automated test suite (`tests/test_kpis.py`, 22 unit tests). Locked assumptions to exact parity with A2 (₹88 FX, ₹400/hr agent cost, 50% realization, 120 agents). Partitioned governance into 4 stakeholder lenses (CFO, COO, CRO, Sponsor) with a formal 16-metric KPI Dictionary containing named business owners and action thresholds.
- **Context & Rationale:** Guarantees zero logic drift across presentations, eliminates "dashboard discrepancies" in management meetings, and enables the exact same KPI code to ingest Category B real agent event logs later without rewriting BI measures.
- **Trade-offs:** Chose Python/Streamlit over Power BI to demonstrate code-level engineering rigor and CI/CD testability, while retaining Power BI slicer dynamics.
- **Impacted Deliverables:** `03_A3_dashboard/` (`kpis.py`, `dashboard.py`, `a3_report.py`, `tests/test_kpis.py`, `README.md`, `outputs/A3_AI_Value_Report.pdf`, `outputs/A3_page*.png`), `docs/traceability.md`, `docs/interview_answers.md`.

### DEC-008: Process Redesign Governance, HITL Rules & Autonomous Agent Deliberate Omission
- **Date:** 2026-11-14
- **Category:** Process Architecture & AI Governance
- **Decision:** In Flagship Step 3 To-Be process redesign (`to_be.drawio`), deliberately restricted autonomous agent execution (`[AG] = 0`), structuring all AI capabilities as frontline copilots (`[AI] = 3`) governed by 5 strict Human-in-the-Loop (HITL) rules: mandatory human sign-off on 100% of outbound communications, algorithmic routing divert for confidence $<0.80$, tiered frontline fee waiver limits up to ₹1,500, Day-25 regulatory amber alert triggers, and client-side PII masking. Replaced unstructured manual friction with deterministic rules, reducing human steps from 11 to 7 (-36%).
- **Context & Rationale:** Demonstrates senior management consultant judgment. In retail banking under RBI FREE-AI and RB-IOS 2026, unmonitored autonomous text dispatch carries severe regulatory, legal, and brand risk. Frontline copilots capture 80% of drafting and retrieval speed advantages while insulating the institution from hallucination liability.
- **Trade-offs:** Maintains human agent touch on every case rather than attempting straight-through automated resolution.
- **Impacted Deliverables:** `04_FlagshipA/` (`00_framing.md`, `discovery/`, `diagrams/to_be.drawio`, `diagrams/to_be_process_description.md`, `requirements/BRD.md`, `requirements/user_stories.md`, `requirements/rtm.md`, `Flagship_A_templates.xlsx`), `docs/traceability.md`.

### DEC-009: Use-Case Prioritization Matrix, Commercial Framing & Statutory Governance
- **Date:** 2026-11-14
- **Category:** Prioritization, Commercial Strategy & Statutory Governance
- **Decision:** Evaluated 9 candidate use cases across the AI Decision Ladder and 6-Criterion Scorecard. Approved Triage (26/30) and Policy Q&A (24/30) for Phase 1 ("Do First"), Draft Reply (22/30) for Phase 2 ("Plan Carefully"), and Quick Wins (Escalation Summary 24/30, Theme Mining 23/30, Feedback Sentiment 23/30). Formally rejected Auto-Send Replies (17/30) and AI Compensation (14/30) due to fatal Risk = 1 scores. Framed the executive business case around avoided Ombudsman escalations (+₹127.5L Full NPV vs. -₹23.4L Hard NPV), establishing that labor capacity alone cannot fund platform Capex. Institutionalized AI governance across DPDP Act 2023, RBI FREE-AI, RB-IOS 2026, and Model Risk Management with an immutable RACI matrix.
- **Context & Rationale:** Provides the executive committee with an unassailable commercial and regulatory rationale. Demonstrates that risk controls and change management (the #1 sensitivity lever) take precedence over model selection.
- **Trade-offs:** Rejected autonomous customer dispatch and automated ledger compensation to eliminate regulatory risk.
- **Impacted Deliverables:** `04_FlagshipA/` (`scorecard_matrix.py`, `matrix.png`, `prioritisation/`, `business_case/`, `governance/`, `Flagship_A_templates.xlsx`), `docs/traceability.md`, `docs/interview_answers.md`.

### DEC-010: Implementation Roadmap, Executive Presentation & Final Portfolio Packaging
- **Date:** 2026-11-15
- **Category:** Delivery Strategy & Executive Packaging
- **Decision:** Structured the 12-month transformation roadmap (`roadmap.csv`, `roadmap.md`) across 4 disciplined phases with 3 evidence-based stage gates (Gate 1 Month 2, Gate 2 Month 5, Gate 3 Month 9). Deployed portfolio project #3 (Client Feedback Automation) as a Phase 0 quick win using prebuilt AI. Formatted executive presentation into a 10-slide action-title storyboard and generated `04_FlagshipA/deck/executive_deck.pptx` using python-pptx with 16:9 widescreen layout and clear measured/assumed labeling. Packaged the engagement with a 2-page case study (`case_study.md`), master portfolio `README.md`, LinkedIn post draft, and 90-second STAR interview story.
- **Context & Rationale:** Completes the consultant storyline ("scoped like a consultant, built like an engineer"). Guarantees that every deliverable promised in Section 4 of the specification is fully verified and reproducible, equipping Aryan to defend every finding, number, and recommendation in Big 4 and consulting interviews.
- **Trade-offs:** Kept Phase 0 free of generative AI costs to establish operational baselines and privacy sign-offs before technical pilot launch.
- **Impacted Deliverables:** `04_FlagshipA/roadmap/`, `04_FlagshipA/deck/`, `04_FlagshipA/case_study.md`, `README.md`, `docs/linkedin_post.md`, `docs/star_interview_story.md`, `docs/traceability.md`, `Flagship_A_templates.xlsx`.

---

## "Later" List (Scope Control)
- Integration with live core banking simulators (deferred to Category B / Year 2).
- Advanced automated speech-to-text for inbound call centre recordings (deferred to roadmap Phase 2).
