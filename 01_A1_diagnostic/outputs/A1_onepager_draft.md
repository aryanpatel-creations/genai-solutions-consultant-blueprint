# Kestrel Bank Complaint Process Diagnostic (A1 Executive Summary)

> **Headline:** 80% of Customer Dissatisfaction Is Concentrated in Three Core Banking Journeys; Lean Policy Fixes Can Eliminate ~18% of Volume Before Introducing GenAI

---

## 1. Problem Statement & Baseline Performance (Measure)
- **Scale & Scope:** Over the 24-month baseline window (Sept 2024 – Aug 2026), retail banking and credit cards generated substantial customer grievance volumes requiring resolution under the Reserve Bank of India (RBI) Integrated Ombudsman Scheme (RB-IOS 2026).
- **Core Baseline Metrics:**
  - **Timely Response Rate:** High compliance with intake acknowledgment (~96–97%), demonstrating that intake logging is not the primary bottleneck.
  - **Routing Lag:** Median lag of 1.0 day from customer submission to internal company assignment.
  - **Customer Relief Rate:** ~29–30% of complaints conclude with monetary adjustments or non-monetary relief—indicating that in nearly one-third of cases, the customer had a valid defect claim driven by preventable bank-side policy friction or process breakdown.

---

## 2. Root-Cause & Defect Concentration (Analyse)
- **Pareto Finding:** Customer dissatisfaction is heavily concentrated: a tight cluster of top issues accounts for 80% of all complaint volume.
- **Top Defect Drivers:**
  1. *Deposits and Withdrawals / Account Access:* Account freezes, delayed fund availability, and ATM settlement mismatches.
  2. *Billing Disputes & Unauthorized Charges:* Fraud alerts, contested credit card transactions, and interest/fee accrual disputes.
  3. *Account Closure & Maintenance:* Customers trapped in multi-hop transfer loops attempting to close dormant accounts or cancel credit lines.
- **Qualitative Root Causes (from 100 Tagged Narratives):**
  - **Policy Deficiencies (~25%):** Ambiguous fee waiver rules, rigid chargeback criteria, and punitive interest structures that frontline agents cannot adjust without multi-level managerial escalation.
  - **Process Waste (~35%):** Fragmented hand-offs between Call Center, Card Ops, and Branch personnel causing repeat contacts.
  - **System Delays (~20%):** Core banking batch update lags and slow inter-bank transaction reconciliations.
  - **Customer Misunderstanding (~15%):** Opaque statement disclosures leading to surprise billing.

---

## 3. High-Impact Non-AI Quick Wins (Improve - Zero Tech Debt)
Before investing capital in generative AI models, Kestrel Bank must implement five Lean Six Sigma operational fixes:
1. **Automated Fee Waiver Matrix:** Empower frontline Tier-1 agents with pre-approved discretionary fee reversal limits (e.g., up to ₹1,500 for first-time overdraft or late payment) without managerial sign-off, instantly eliminating dispute cycle time.
2. **Transparent Billing Alerts:** Deploy real-time SMS/push notifications 48 hours prior to recurring subscription renewals or annual fee deductions.
3. **Digital Self-Service Account Closure:** Create a single-click account/card closure journey on mobile banking compliant with RBI cancellation rules, removing branch dependency.
4. **Instant Provisional Credit:** Grant instant provisional credit on low-value (<₹2,500) disputed transactions pending fraud investigation.
5. **Standardized Dispute Intake Form:** Redesign mobile dispute intake to capture exact transaction IDs, receipts, and merchant names upfront, eliminating initial inquiry lag.

---

## 4. AI Opportunity Blueprint & Control Plan (Control)
- **Where AI Adds Distinct Value:**
  - **Intelligent Triage & Priority Routing:** Auto-detect urgent regulatory escalations (Ombudsman threats, cyber fraud) and route directly to specialized units.
  - **Contextual Knowledge & RBI Policy Retrieval (RAG):** Retrieve relevant RBI Master Directions and bank product rules to guide agent investigation.
  - **Automated Response Drafting:** Generate personalized, empathetic, regulatory-compliant response letters integrating verified account facts for human-agent sign-off.
- **Where AI Must NOT Be Used:**
  - Fully autonomous, unreviewed customer dispatch (violates RBI FREE-AI and consumer protection rules).
  - Automated dispute rejection or liability determination without human adjudication.
- **Control KPIs:**
  - Statutory 30-Day Resolution Rate: **Target ≥ 98%**
  - First-Contact Resolution (FCR): **Target ≥ 70%**
  - Agent Override Rate on AI Drafts: **Target ≤ 15%**
