# Project Charter: Kestrel Bank Complaint Process Diagnostic (A1)

> **Methodology:** Lean Six Sigma DMAIC (Define & Measure Phase)  
> **Client Context:** Kestrel Bank (fictional mid-size Indian private bank; ~40k monthly Indian operational scale)  
> **Empirical Stand-in Data:** Official CFPB Consumer Complaint Database (24-Month Window: September 1, 2024 – August 31, 2026)  
> **Last Updated:** 2026-11-14

---

## 1. Project Overview & Business Case
- **Project Title:** Kestrel Bank Complaint Process Diagnostic & Root-Cause Remediation (Project A1)
- **Business Imperative:** Under the Reserve Bank of India (RBI) Integrated Ombudsman Scheme (RB-IOS 2026), banks face a strict 30-day statutory resolution mandate with personal accountability for Principal Nodal Officers and award liabilities up to ₹30 lakh. Operating with ~120 frontline agents handling an assumed 40,000 monthly grievances at an estimated 25 minutes Average Handle Time (AHT) and ₹400/hour loaded agent cost, Kestrel Bank incurs severe operational drag (₹80+ lakh/month in grievance handling costs).
- **Core Consulting Objective:** Diagnose empirical complaint patterns to identify where resolution time and quality defects originate, determine what percentage of customer dissatisfaction can be resolved via Lean non-AI fixes (zero tech debt), and establish the verified baseline for GenAI-assisted workflows.

---

## 2. Problem Statement (Empirically Measured Baseline)
Between September 2024 and August 2026, empirical analysis of **346,481** bank complaints across retail deposit accounts and credit cards reveals:
1. **Intake Is Not the Bottleneck:** The timely response rate stands at **99.3%**, with a **median routing lag of 0.0 days** and **91.3%** submitted digitally via the web. The intake and logging mechanisms function efficiently; process delays occur during subsequent investigation and drafting.
2. **High Bank-Side Defect Rate (Relief Proxy):** **24.8%** of all complaints conclude with customer relief (**13.1%** monetary relief, **11.8%** non-monetary adjustments). In roughly 1 out of 4 cases, the customer had a valid defect claim requiring financial reimbursement or operational correction due to policy friction or bank error.
3. **Severe Pareto Defect Concentration:** Dissatisfaction is concentrated in a narrow band of root causes: **10 of 20 issue categories account for 80% of all complaint volume**. The single largest issue, *"Managing an account"*, represents **90,902 complaints (26.2%)**, followed by *"Problem with a purchase shown on statement"* (**46,653 complaints, 13.5%**).
4. **Disproportionate Friction in Dispute Investigation:** Issues related to billing and investigation demonstrate extreme relief rates: *"Problem with investigation into an existing problem"* has a **42.7% relief rate** (16,469 complaints), and *"Fees or interest"* has a **35.0% relief rate** (16,953 complaints), confirming systemic defects in customer dispute resolution.

---

## 3. Project Goal Statement
- **Goal 1 (Lean Process Optimization):** Eliminate 15–18% of avoidable dispute volume within 6 months by deploying 5 non-AI policy fixes (such as pre-approved frontline fee waiver matrices and proactive billing alerts).
- **Goal 2 (Cycle Time Compression):** Reduce frontline investigation and drafting time from 25 minutes to under 12 minutes (≥50% reduction) via intelligent retrieval and drafted compliance responses.
- **Goal 3 (Regulatory Risk Reduction):** Maintain ≥98% resolution within the RB-IOS 30-day mandate and reduce escalations to the RBI Ombudsman from 3.0% to <1.5%.

---

## 4. Scope Boundaries
| Dimension | In-Scope | Out-of-Scope |
|---|---|---|
| **Products** | Retail Checking/Savings Accounts (163,926 complaints / 47.3%)<br>Credit Cards (182,555 complaints / 52.7%) | Mortgages, student loans, commercial financing, vehicle loans |
| **Channels** | Web Portal (91.3%), Mobile App, Branch Escalations, Call Center | Core banking engine (CBS) database rewrites |
| **Process Steps** | Intake, Classification & Routing, Investigation, Decision, Response Drafting | Automated customer dispatch without human sign-off (prohibited) |

---

## 5. Team & Governance
- **Executive Sponsor:** Chief Operating Officer (COO) / Principal Nodal Officer
- **Lead Consultant:** Aryan Patel, MBA (Business Analytics)
- **Stakeholders:** Head of Retail Operations, Head of Cards, Chief Risk Officer (CRO)
- **Framework:** Lean Six Sigma DMAIC (Define, Measure, Analyse, Improve, Control)
