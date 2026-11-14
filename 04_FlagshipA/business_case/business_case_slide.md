# Executive Business Case: Investment Decision & Financial Walk (business_case_slide.md)

> **Client:** Kestrel Bank  
> **Engagement:** AI Transformation Blueprint — Complaints Redressal Modernisation  
> **Prepared by:** Aryan Patel (MBA Business Analytics, Techno-Functional Consultant)  
> **Deliverable:** Flagship Step 6 — Executive Business Case Slide & CFO Defense  
> **Source Model:** `02_A2_business_case/A2_GenAI_Cost_ROI.xlsx`

---

## 1. Executive Summary & Action Headline

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              EXECUTIVE DECISION HEADLINE                               │
│ "A ₹86 Lakh initial investment achieves capital payback in 18 months and generates     │
│ a +₹127.5 Lakh 3-year Net Present Value (86% ROI) — but ONLY if Kestrel Bank defends   │
│ avoided Ombudsman escalations and enforces frontline adoption. Releasing agent hours   │
│ alone yields a negative hard return (-₹23.4 Lakh NPV) and cannot justify the spend."   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Comparative Financial Analysis: Hard-Only vs. Full Commercial View

Corporate finance committees scrutinize whether claimed benefits represent hard cash savings (e.g., headcount reduction or avoided regulatory fines) or soft efficiency gains (saved hours absorbed by other tasks). We explicitly model both perspectives across Base, Worst, and Best operating scenarios:

### Three-Year Financial Summary Table (12.0% Discount Rate)

| Financial Metric | Hard-Only View (Saved Hours Cashable @ 50%) | Full Commercial View (Hard Savings + Ombudsman Escalations Avoided) | Methodological Distinction / Strategic Implication |
|---|---|---|---|
| **3-Year Net Present Value (Base Case)** | **-₹23.4 Lakh** *(Unviable alone)* | **+₹127.5 Lakh** *(Highly attractive)* | Hard savings alone produce an immediate **-₹23.4L deficit**; project viability relies entirely on avoiding statutory Ombudsman fees (+₹194.4L). |
| **Capital Payback Period (Base Case)** | **No Payback** *(> 3.0 Years)* | **1.50 Years (18.0 Months)** | Capital outlay (₹86L Capex) is fully recovered midway through Year 2 under the full commercial model. |
| **3-Year Return on Investment (ROI)** | **-11.4%** | **+85.9% (~86.0%)** | Full view delivers an 85.9% net return over total discounted 3-year expenditures (₹148.4L PV costs). |
| **Scenario Sensitivity Range (NPV)** | **-₹123.3 Lakh to +₹75.6 Lakh** | **-₹68.0 Lakh to +₹324.6 Lakh** | Worst case fails to break even (-₹68.0L); Best case delivers a massive +₹324.6L return on scale. |
| **Primary Financial Sensitivity Levers** | Frontline Adoption (80%) & Labor Cash Realisation (50%) | Frontline Adoption (80%) & Cost per Ombudsman Escalation (₹3,500) | Frontline user adoption is the single largest financial swing factor across both perspectives. |

---

## 3. Total Cost of Ownership (TCO) & Token Spend Reality

A common misconception among non-technical executives is that AI token inference costs dominate ongoing expenditure. Our A2 cost modeling exposes the true economics of generative AI:

```
Three-Year Spend Breakdown (₹224.3 Lakh Total Undiscounted Expenditure):
┌───────────────────────────────────────────────────────────────────────────────────────┐
│ [████████████████████████████████] Fixed Platform Engineering & Capex: ₹86.0L (38.3%) │
│ [████████████████████████████████████████████] Fixed Cloud Hosting & Support: ₹120.0L (53.5%)│
│ [███] Variable LLM Model Token Inference: ₹18.3L (8.2%)                              │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

* **Token Inference Spend is Negligible:** Across all 3 years, variable model token costs represent just **8.2% of total expenditure** (₹18.3 Lakh out of ₹224.3 Lakh).
* **Inference Unit Cost:** Operating cost per complaint is just **₹2.12 ($0.0241 USD)**:
  * Triage & Routing (Claude Haiku 5.5): **$0.0001 / complaint**
  * Policy Knowledge Q&A (Claude Sonnet 5.5 + Prompt Caching): **$0.01702 / complaint**
  * Draft Reply Assistant (Claude Sonnet 5.5): **$0.00700 / complaint**
* **Strategic Takeaway:** Negotiating a 10% token discount from model providers saves only ₹1.8 Lakh over 3 years; driving agent adoption by 10% increases 3-year return by **₹58.0 Lakh**.

---

## 4. Sensitivity Analysis Walk: The Tornado Chart

Our Tornado sensitivity analysis evaluated the relative NPV impact of swing factors spanning $\pm 20\%$ to $\pm 30\%$ variation around Base Case inputs:

```
                              TORNADO SENSITIVITY: 3-YEAR FULL NPV SWING (₹ LAKH)
                                                 [Base: ₹127.5L]
──────────────────────────────────────────────────────────────────────────────────────────────────────────
#1 Frontline Adoption Rate (50% to 95%)        │████████████████████████████████████████│  ₹174.1L Swing
#2 Ombudsman Fee Reduction (0.3% to 0.7%)      │██████████████████████                  │  ₹97.2L Swing
#3 Realisation Factor (30% to 70%)             │███████████████                         │  ₹67.0L Swing
#4 Agent Hourly Loaded Cost (₹320 to ₹480)     │█████████████                           │  ₹55.8L Swing
#5 Annual Core Cloud Hosting (₹30L to ₹50L)    │██████                                  │  ₹26.2L Swing
#6 Token Pricing / FX Fluctuation (₹75 to ₹100)│████                                    │  ₹17.8L Swing
──────────────────────────────────────────────────────────────────────────────────────────────────────────
```

* **Adoption is the #1 Lever:** A drop in frontline agent adoption from 80% to 50% reduces 3-year NPV from **+₹127.5L to +₹11.4L**, completely eliminating capital payback. If adoption drops to 40%, NPV turns negative (-₹27.0L).
* **Token Cost Volatility is #6:** Token pricing and FX swings produce less than a 10% movement in NPV, proving that technical infrastructure cost is not the project risk.

---

## 5. The Four Executive Messages for the Chief Financial Officer (CFO)

When presenting this business case to the Chief Financial Officer and Investment Committee, deliver these four structured arguments:

### Message 1: "Hard labor savings alone will not pay for this platform."
> *"If Kestrel Bank evaluates this investment purely on cashable agent headcount reduction, the project yields a negative Net Present Value of **-₹23.4 Lakh** and fails to break even. Frontline agents do not instantly get laid off when they save 6 minutes; time savings are absorbed into queue backlogs and quality investigations. Do not approve this business case on labor savings alone."*

### Message 2: "The investment is fully justified by statutory risk mitigation."
> *"The project becomes highly lucrative (+₹127.5 Lakh NPV, 18-month payback, 86% ROI) once we account for the elimination of statutory penalties under the RBI Integrated Ombudsman Scheme. By resolving disputes within 30 days and cutting Ombudsman escalations from 3.0% to 2.55%, the bank avoids **₹194.4 Lakh in direct conciliation fees and executive legal overhead** over 3 years."*

### Message 3: "Change management is our primary financial risk, not model pricing."
> *"Our Tornado sensitivity analysis proves that frontline adoption is the single largest financial driver (a ₹174.1 Lakh swing). If frontline agents resist the tool, ROI collapses. Consequently, our Phase 0 allocation dedicates ₹15 Lakh to operational change management, frontline champions, and UX workflow integration."*

### Message 4: "Token inference costs are economically negligible (8.2% of TCO)."
> *"Thanks to semantic model routing (using Claude Haiku for triage) and prompt caching (cutting policy Q&A costs by 60%), our variable model cost is just **₹2.12 per complaint**. Model tokens represent only 8.2% of our 3-year spend, meaning future API price fluctuations pose zero threat to financial viability."*
