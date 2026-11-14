# 10-Slide Executive Presentation Deck: Storyboard & Script (executive_deck_storyboard.md)

> **Client:** Kestrel Bank (Executive Committee: CEO, COO, CFO, CRO, Head of Customer Service)  
> **Engagement:** AI Transformation Blueprint — Complaints Redressal Modernisation  
> **Prepared by:** Aryan Patel (MBA Business Analytics, Techno-Functional Consultant)  
> **Deliverable:** Flagship Step 9 — 10-Slide Executive Storyboard & 8-Minute Boardroom Script  
> **Presentation Artifact:** `04_FlagshipA/deck/executive_deck.pptx`

---

## 1. Executive Deck Architecture (The "Action Title" Storyline)

In senior management consulting, executive decks follow one foundational principle: **Someone reading only the slide titles from Slide 1 to 10 must understand the complete strategic narrative without reading body text.** Every title is an active, evidence-based declarative sentence:

```
Slide 1:  AI can cut complaint handling effort by about a quarter, if we start with the process.
Slide 2:  A handful of issue types and broken cross-team workflows drive most complaints.
Slide 3:  Six operational fixes need no AI at all and should start immediately.
Slide 4:  Frontline agents lose most time navigating four systems and drafting repetitive replies.
Slide 5:  AI should assist agents at three critical points, with a human approving every reply.
Slide 6:  Two AI use cases are ready now, while autonomous replies must be strictly rejected.
Slide 7:  The investment pays back in 18 months, but only if statutory Ombudsman escalations fall.
Slide 8:  The solution design guarantees full DPDP Act, RBI FREE-AI, and RB-IOS compliance.
Slide 9:  Three evidence-based stage gates ensure Kestrel Bank scales only what is proven.
Slide 10: The AI Value Dashboard will prove whether the investment is working within 90 days.
```

---

## 2. Slide-by-Slide Storyboard, Visuals & Speaker Notes

---

### Slide 1: Executive Summary & Transformation Rationale
* **Action Title:** **AI can cut complaint handling effort by about a quarter, if we start with the process.**
* **Core Takeaway:** Kestrel Bank can achieve a 24% reduction in Average Handle Time and eliminate ₹194.4 Lakh in statutory Ombudsman escalation costs through a disciplined combination of Lean process fixes and targeted AI copilots.
* **Body Text (38 words):**  
  *We analysed 346,481 bank complaints and conducted frontline discovery across 120 agents. Deploying 6 Lean fixes alongside 3 AI copilots delivers ₹127.5 Lakh 3-year NPV and 18-month payback, while ensuring zero autonomous customer communication.*
* **Visual Structure:**
  * Card 1: **3 Core Findings** (10 issues drive 80% volume; 60% of AHT spent in manual search/typing; 15% are petty fee disputes).
  * Card 2: **1 Integrated Recommendation** (Implement 6 Lean fixes in Phase 0; pilot 3 agent copilots in Cards & Accounts; enforce 100% human sign-off).
  * Card 3: **The Ask** (Approve ₹86.0 Lakh Phase 0–1 capital allocation subject to Gate 1 privacy and operational criteria).
* **Footnote:** `MEASURED: CFPB 24-month bank subset (N=346,481) | ASSUMED: 40k monthly volume, 120 agents (AS-01 to AS-04).`
* **Speaker Script (45 seconds):**  
  *"Good morning, members of the Executive Committee. Kestrel Bank currently handles ~40,000 complaints a month across 120 dedicated agents. Our diagnostic proves that AI can reduce handle time by 24%—from 25 minutes down to 19 minutes—saving over 3,000 operational hours a quarter. However, technology alone is not the answer. By fixing broken fee waiver policies upfront and deploying three targeted copilots with mandatory human sign-off, this ₹86 Lakh investment pays back in 18 months. Today, we are seeking approval to initiate Phase 0."*

---

### Slide 2: Empirical Problem Diagnostic & Defect Concentration
* **Action Title:** **A handful of issue types and broken cross-team workflows drive most complaints.**
* **Core Takeaway:** Volume is highly concentrated: 10 of 20 issue categories account for 80% of total complaints, led by Account Management (26.2%). Furthermore, a 24.8% customer relief rate proves claims reflect genuine institutional defects.
* **Body Text (35 words):**  
  *Pareto analysis shows 80% of volume concentrates in 10 issues. Routing lag is zero days, but investigation stalls across 4 disconnected systems. 24.8% of cases end in customer relief, proving issues stem from bank policies, not customer error.*
* **Visual Structure:**
  * Chart: Embedded **Pareto Chart** (`pareto_issues.png`) highlighting the 80% cutoff and the top issue ("Managing an account", 90,902 complaints).
  * Metric Callout: **24.8% Relief Rate** (13.1% monetary refund, 11.8% non-monetary relief).
  * Root Cause Breakdown: Process (56%), Systems (25%), Policy (15%), Information (3%), People (1%).
* **Footnote:** `MEASURED: a1_step2_clean_kpis.py & a1_step3_pareto.py (2026-11-14) | SOURCED: CFPB 24m Bank Complaints.`
* **Speaker Script (45 seconds):**  
  *"Looking at our empirical data, complaint volume is not random. Just 10 issue categories drive 80% of inbound disputes. 'Managing an account' alone represents 26.2% of our entire dispute load. Importantly, 24.8% of cases result in monetary or non-monetary relief—proving that customers are highlighting valid institutional friction points. Interestingly, our intake routing lag is zero days; the operational delay occurs entirely during manual investigation and response drafting."*

---

### Slide 3: Lean Six Sigma Interventions (Non-AI Foundations)
* **Action Title:** **Six operational fixes need no AI at all and should start immediately.**
* **Core Takeaway:** 15% of complaints stem from inflexible fee policies where AI adds zero value. Deploying 6 Lean process fixes in Phase 0 removes administrative drag and reduces volume before AI deployment.
* **Body Text (36 words):**  
  *Before writing a line of AI code, Lean Six Sigma DMAIC eliminates avoidable waste. Empowering agents with a ₹1,500 discretionary fee waiver limit eliminates 15% of supervisor rework loops, while CRM taxonomy standardisation prevents intake misdirection.*
* **Visual Structure:**
  * Table of 6 Non-AI Fixes:
    1. *Discretionary Fee Waiver ($\le ₹1,500$):* Eliminates 15% petty dispute escalations (Ops Head).
    2. *Standardized 3-Level CRM Taxonomy:* Prevents 20% intake re-routing (CRM Product Lead).
    3. *Instant Auto-Acknowledgement (<2 hrs):* Satisfies RB-IOS 2026 tracking compliance (Channel Lead).
    4. *Day-25 Statutory Amber Alert:* Triggers urgent nodal intervention prior to Day 30 (PNO).
    5. *Dynamic Duplicate Ticket Filter:* Drops 4% repeat submissions within 72 hours (IT Lead).
    6. *Weekly Pareto Root-Cause Loop:* Transmits defect clusters to Product Managers (Customer Service Head).
* **Footnote:** `SOURCED: Project A1 DMAIC Diagnostic & Flagship_A_templates.xlsx (NonAI_fixes).`
* **Speaker Script (45 seconds):**  
  *"As consultants, our first recommendation is NOT to use AI where a policy fix works better. 15% of our disputes are customers upset over annual maintenance or credit card fees under ₹1,000. Today, an agent spending 20 minutes creating a supervisor escalation ticket for a ₹500 fee is pure waste. By granting frontline agents immediate discretionary waiver authority up to ₹1,500, we instantly eliminate thousands of rework loops. These six fixes launch in Phase 0."*

---

### Slide 4: Operational Pain Points & Frontline Discovery
* **Action Title:** **Frontline agents lose most time navigating four systems and drafting repetitive replies.**
* **Core Takeaway:** Frontline dispute agents spend 15 of 25 handling minutes manually querying disconnected applications and drafting customized letters from scratch, creating cognitive burnout and 30-day drift.
* **Body Text (37 words):**  
  *Discovery interviews confirm agents toggle across Finacle, Base24, CRM, and intranet PDF circulars. Searching policies takes 7–8 minutes; typing letters takes 8.5 minutes. 12% of cases stall past Day 25, risking costly RBI Ombudsman conciliations.*
* **Visual Structure:**
  * Visual Breakdown of Baseline 25-Minute AHT:
    * Policy Search (Intranet PDFs): **8.0 min (32%)** $\to$ *Target Pain Point P1*
    * Response Formulation (Manual Typing): **8.5 min (34%)** $\to$ *Target Pain Point P3*
    * Cross-System Data Query (Finacle/Base24): **6.5 min (26%)**
    * Wrap-Up & Queue Logging: **2.0 min (8%)**
  * Frontline Quote: *"Searching for the right RBI circular takes 8 minutes alone because our intranet PDF search is terrible."*
* **Footnote:** `SOURCED: Primary Banking Interviews INT-01 to INT-03 (2026-11-20) | ASSUMED: Baseline 25 min AHT.`
* **Speaker Script (45 seconds):**  
  *"Through operational shadowing and interviews with dispute analysts, we discovered that 66% of handling time is spent in friction. Agents toggle between four disconnected systems. They spend 8 minutes manually searching through 500-page PDF circulars to find the right fee clause, and another 8.5 minutes typing out explanation letters from scratch. This administrative drag causes 12% of complaints to drift past Day 25, creating immediate statutory exposure under the RBI Ombudsman scheme."*

---

### Slide 5: Target Process Redesign (To-Be Architecture)
* **Action Title:** **AI should assist agents at three critical points, with a human approving every reply.**
* **Core Takeaway:** The To-Be architecture reduces manual human steps by 36% (from 11 to 7) by embedding 3 targeted copilots and 4 automated rules. Crucially, autonomous agents (`[AG]`) remain strictly at zero.
* **Body Text (38 words):**  
  *The redesigned BPMN architecture embeds AI copilots at Triage, Policy Lookup, and Response Drafting. Manual steps drop from 11 to 7. Every outbound reply requires explicit agent sign-off, strictly preventing hallucinated representations under RBI FREE-AI guidelines.*
* **Visual Structure:**
  * Diagram Graphic: Thumbnail / Swimlane schematic of `to_be.drawio` across Customer, Intake Gateway, AI Copilot, Agent, and Nodal Office.
  * Step Count Comparison:
    * As-Is: **11 `[H]`, 1 `[R]`, 0 `[AI]`, 0 `[AG]`** (Total 12)
    * To-Be: **7 `[H]`, 4 `[R]`, 3 `[AI]`, 0 `[AG]`** (Total 14)
  * HITL Box: Highlight on **Mandatory Outbound Approval Gate** (Zero unreviewed text).
* **Footnote:** `SOURCED: 04_FlagshipA/diagrams/to_be.drawio & to_be_process_description.md.`
* **Speaker Script (45 seconds):**  
  *"Here is our target operational architecture. We have restructured the workflow into five gated swimlanes. Notice the step tags: manual human steps drop from 11 to 7—a 36% reduction in cognitive friction. AI intervenes at exactly three points: triage classification, policy clause retrieval via RAG, and drafting an 80%-complete response letter. Notice also that the Autonomous Agent tag is ZERO. Every outbound communication must be reviewed, edited, and approved by a licensed human agent."*

---

### Slide 6: Use-Case Prioritisation & Negative Boundaries
* **Action Title:** **Two AI use cases are ready now, while autonomous replies must be strictly rejected.**
* **Core Takeaway:** Evaluation across our 6-criterion scorecard identifies Triage (26/30) and Policy Q&A (24/30) as immediate "Do First" priorities. Autonomous customer replies (17/30) and AI compensation (14/30) are strictly rejected.
* **Body Text (37 words):**  
  *Using the AI Decision Ladder, we evaluated 9 candidate use cases. Triage and Policy Q&A deliver high value and feasibility. Conversely, autonomous customer dispatch and AI-decided compensation were rejected due to fatal regulatory liability under RB-IOS 2026.*
* **Visual Structure:**
  * Graphic: Embedded **Value-vs-Feasibility Matrix** (`value_vs_feasibility.png`).
  * Quadrant Callouts:
    * *Do First:* #1 Triage & Routing (26/30), #2 Policy Q&A (24/30).
    * *Plan Carefully:* #3 Draft Reply (22/30; requires HITL approval).
    * *Quick Wins:* #4 Escalation Summary (24/30), #6 Theme Mining (23/30), #9 Feedback Flow (23/30).
    * *Strictly Rejected:* #7 Auto-Send Replies (Risk=1), #8 AI Decides Comp (Risk=1).
* **Footnote:** `SOURCED: 04_FlagshipA/scorecard_matrix.py & Flagship_A_templates.xlsx (Scorecard).`
* **Speaker Script (45 seconds):**  
  *"To determine where to invest, we scored 9 use cases on a 6-criterion scorecard. Triage and Policy Q&A scored highest: they operate internally, carry low risk, and solve immediate search bottlenecks. Response Drafting is slated for Phase 2 once prompt safeguards are tuned. Most importantly, we explicitly rejected autonomous customer messaging and AI-decided compensation. In banking, unreviewed communication carries binding legal enforceability. Saying 'no' to autonomy protects the bank's balance sheet."*

---

### Slide 7: Commercial Business Case & Financial Sensitivity
* **Action Title:** **The investment pays back in 18 months, but only if statutory Ombudsman escalations fall.**
* **Core Takeaway:** Hard labor savings alone yield a negative return (-₹23.4L NPV). The full business case (+₹127.5L NPV, 18m payback) is driven by avoiding ₹194.4 Lakh in statutory Ombudsman conciliation fees.
* **Body Text (38 words):**  
  *A ₹86 Lakh build pays back in 18 months with an 85.9% 3-year ROI under the full view. Token costs represent only 8.2% of spend. However, frontline adoption is our #1 financial lever, driving a ₹174.1 Lakh NPV swing.*
* **Visual Structure:**
  * Comparative Financial Summary Table (12% Discount Rate):
    * 3-Year NPV: Hard-Only **-₹23.4 Lakh** vs. Full View **+₹127.5 Lakh**
    * Payback: Hard-Only **No Payback** vs. Full View **1.50 Years (18 Months)**
    * 3-Year ROI: Hard-Only **-11.4%** vs. Full View **+85.9%**
  * Spend Reality Bar: Fixed Capex (38.3%), Cloud Hosting (53.5%), **Tokens (8.2%)**.
  * Tornado Sensitivity Snippet: Adoption Rate is #1 lever (₹174.1L swing).
* **Footnote:** `SOURCED: 02_A2_business_case/A2_GenAI_Cost_ROI.xlsx (Summary, CashFlow, Tornado).`
* **Speaker Script (50 seconds):**  
  *"Let us address the financials directly with the CFO. If we evaluate this project solely on cashable labor savings at a 50% realization factor, the Net Present Value is negative 23.4 Lakh. We do not recommend approving this project on labor savings alone. However, under our full commercial model, the project generates a positive 127.5 Lakh NPV and pays back in 18 months. What makes the difference? Avoiding 540 statutory Ombudsman escalations, saving 194.4 Lakh in direct conciliation fees and legal costs. Furthermore, our Tornado analysis shows adoption is our #1 financial lever: if adoption drops to 50%, ROI vanishes. Change management is our primary investment."*

---

### Slide 8: AI Governance, Risk Mitigation & Regulatory Compliance
* **Action Title:** **The solution design guarantees full DPDP Act, RBI FREE-AI, and RB-IOS compliance.**
* **Core Takeaway:** Compliance is engineered into the technical architecture from Day 1: client-side PII masking, Zero Data Retention contracts, 15% override tripwires, and an immutable RACI operating model.
* **Body Text (36 words):**  
  *Governance controls satisfy the DPDP Act 2023, RBI FREE-AI, and RB-IOS 2026. A client-side PII masking gateway tokenizes identifiers before API transmission, while an automated 15% override threshold provides real-time early warning against model drift.*
* **Visual Structure:**
  * 3 Regulatory Pillars:
    * *DPDP Act 2023:* Client-side tokenization (944 pilot blocks); 72-hour breach runbook; India data residency.
    * *RBI FREE-AI:* Tier-2 AI Inventory registration; mandatory citations; 100% human review.
    * *RB-IOS 2026:* Day-25 amber alert trigger; weekly QA audits; zero 30-day breaches.
  * RACI Callout: Single-point accountability across Sponsor, AI PO, IT, Compliance, and Team Leads.
* **Footnote:** `SOURCED: 04_FlagshipA/governance/governance_plan.md & Flagship_A_templates.xlsx (Control_map, RACI).`
* **Speaker Script (45 seconds):**  
  *"In banking, governance cannot be an afterthought. Our architecture satisfies three critical statutory frameworks from day one. Under the DPDP Act, all customer PII is tokenized inside our firewall before any payload reaches an LLM. Under the RBI FREE-AI framework, the copilot is registered on our institutional AI register, and citations are mandatory. Under RB-IOS, automated Day-25 alerts prevent Ombudsman conciliations. Finally, our RACI matrix establishes single-point executive accountability across every workflow."*

---

### Slide 9: 12-Month Phased Implementation Roadmap & Stage Gates
* **Action Title:** **Three evidence-based stage gates ensure Kestrel Bank scales only what is proven.**
* **Core Takeaway:** A disciplined 12-month transformation structured into 4 phases. Phase 0 uses zero GenAI. Each stage gate enforces mandatory quantitative go/no-go criteria before capital expansion.
* **Body Text (38 words):**  
  *Rollout spans 4 phases across 12 months. Phase 0 executes Lean fixes and our feedback quick win. Stage Gate 1 gates the Cards pilot; Gate 2 expands to all 4 teams; Gate 3 evaluates enterprise scale and narrow agentic steps.*
* **Visual Structure:**
  * Timeline Graphic (Gantt Representation):
    * *Phase 0 (M1–M2):* Foundations, Lean Fixes, Feedback Flow (#3). $\longrightarrow$ **Gate 1 (Pilot Go/No-Go)**
    * *Phase 1 (M3–M5):* Copilot Pilot in Cards & Savings (Haiku + RAG). $\longrightarrow$ **Gate 2 (Expansion Go/No-Go)**
    * *Phase 2 (M6–M9):* Full 120-Agent Rollout & Response Drafting. $\longrightarrow$ **Gate 3 (Scale Go/No-Go)**
    * *Phase 3 (M10–M12):* Classical ML Migration & Category B Agentic Design.
  * Key Gate Criteria Box: Gate 2 requires $\ge 80\%$ acceptance, $\le 15\%$ override, zero PII leaks, and $\ge 60\%$ weekly active agents.
* **Footnote:** `SOURCED: 04_FlagshipA/roadmap/roadmap.md & roadmap.csv (2026-11-15).`
* **Speaker Script (45 seconds):**  
  *"We do not believe in big-bang deployments. Our 12-month roadmap is disciplined and gated. Phase 0 requires zero generative AI: we deploy our Lean fixes and our portfolio quick win, Client Feedback Automation. Gate 1 requires full privacy sign-off and baseline benchmarks before testing starts. Phase 1 pilots Triage and Policy Q&A across 60 agents. Only when Gate 2 proves an 80% acceptance rate and lower escalations do we expand to all 120 agents and introduce Response Drafting. The bank scales only what is empirically proven."*

---

### Slide 10: Operational Telemetry & The Investment Ask
* **Action Title:** **The AI Value Dashboard will prove whether the investment is working within 90 days.**
* **Core Takeaway:** Kestrel Bank will monitor 16 tested KPIs across CFO, COO, CRO, and Sponsor lenses via the AI Value Dashboard. We request ₹86.0 Lakh Phase 0–1 capital allocation to initiate the transformation.
* **Body Text (35 words):**  
  *Our tested 16-KPI dashboard tracks cost, velocity, risk, and adoption in real time. We request ₹86.0 Lakh capital allocation to execute Phase 0 foundations and Phase 1 pilot, delivering verified operational payback within 18 months.*
* **Visual Structure:**
  * 4 Lens KPI Summary Cards:
    * *Executive (CFO):* Cost per run **₹0.70**, Net margin **+₹6.29L**, Cumulative break-even curve.
    * *Operations (COO):* **3,370 hours saved**, **718 runs/day**, **89.7% acceptance rate**.
    * *Risk (CRO):* **10.3% override rate** (target $\le 15\%$), **944 PII blocks**, **2.89s P95 latency**.
    * *Sponsor (Head CS):* **120 active agents (100% adoption)**, **538 runs/agent**.
  * The Immediate Ask: **Approval of ₹86.0 Lakh Year 0 Capex** to launch Phase 0 foundations.
* **Footnote:** `SOURCED: 03_A3_dashboard/kpis.py & outputs/A3_AI_Value_Report.pdf (Simulated 90-Day Pilot).`
* **Speaker Script (45 seconds):**  
  *"How will executive leadership know this is working? Within 90 days of pilot launch, our AI Value Dashboard provides continuous telemetry across four stakeholder lenses. The CFO tracks cost per run and net margin; the COO tracks hours saved and acceptance; the CRO monitors our 15% override limit and PII blocks; and the Sponsor tracks agent adoption. Every metric has a named owner and an action threshold. Our ask today is approval of the ₹86 Lakh Phase 0 and Phase 1 capital allocation. Thank you, and we welcome your questions."*
