# Discovery: Operational Interview Notes & Transcripts (interview_notes.md)

> **Client:** Kestrel Bank  
> **Engagement:** AI Transformation Blueprint — Complaints Redressal Modernisation  
> **Prepared by:** Aryan Patel (MBA Business Analytics)  
> **Deliverable:** Flagship Step 2b — Primary Research Transcripts (3 Banking Professional Interviews)  
> **Ethics & Data Privacy:** All participant names and bank identifiers anonymized. Conducted under 30-minute operational research protocol.

---

## 1. Interview Summary Matrix

| Interview # | Professional Role | Institution Type | Key Focus Area | Validated Numbers | Linked Pain Points |
|---|---|---|---|---|---|
| **INT-01** | **Operations Manager (Dispute Operations)** | Mid-Sized Indian Private Bank | Intake triage, queue routing, cross-team bounces | 20% re-route rate; 24–26 min AHT; 12% reopen rate | **P2 (Triage & Routing), P1 (Knowledge Search)** |
| **INT-02** | **Senior Grievance Officer / Nodal Office** | Top-Tier Indian Private Bank | Statutory 30-day compliance, Ombudsman risk, governance | 11–13% cases >25 days; 2.8–3.2% Ombudsman rate; ₹3,500/case fee | **P4 (30-Day Drift), P5 (Repeat Product Defects)** |
| **INT-03** | **Frontline Dispute Handling Agent (Cards)** | Mid-Sized Indian Private Bank | System navigation, policy search, drafting friction | 4 disconnected systems; 8 min drafting; 7 min policy search; ₹1,500 waiver limit need | **P1 (Policy Search), P3 (Drafting Fatigue)** |

---

## 2. Detailed Interview Transcripts

### Interview 1: Operations Manager (Dispute Operations)
* **Date:** 18 November 2026 | **Duration:** 32 Minutes
* **Role Context:** Manages a team of 35 dispute analysts across credit card chargebacks and retail deposit disputes.

#### Key Exchange & Findings:
* **Q: "Walk me through the intake and routing process. Where do delays start?"**
  * *Quote:* *"Customers submit complaints through the mobile app or web portal using free text. Because the portal has only generic categories like 'Account Issue', customers pick anything. About **1 in every 5 complaints (20%) lands in the wrong operational queue**. A card transaction dispute ends up with the Branch Savings team. The branch agent spends 5 minutes realizing they can't help, and re-routes it to Cards. That's a wasted 5 minutes and an immediate 24-hour SLA delay."*
  * *Validation:* Validates **Pain Point P2** and our A1 metric (27% of narrative sample tagged as `Triage`).
* **Q: "What are your team's baseline operating numbers?"**
  * *Quote:* *"Average handle time (AHT) is between **24 and 26 minutes** per complaint. Agents handle roughly 16 to 18 cases a day. Our first-contact resolution is poor—about **12% of complaints get reopened** within 14 days because the initial response was vague or failed to explain the bank's policy clearly."*
  * *Validation:* Validates baseline AHT of **25.0 minutes** used in A1, A2, and A3.
* **Q: "Where would AI help, and where would you hesitate?"**
  * *Quote:* *"If AI can read customer text and route it to the exact right queue with 90% accuracy, that saves thousands of hours a month. But do NOT let an AI close tickets automatically. Agents must verify the classification."*

---

### Interview 2: Senior Grievance Redressal Officer (Principal Nodal Office)
* **Date:** 19 November 2026 | **Duration:** 28 Minutes
* **Role Context:** Accountable for Level 3 escalations and regulatory reporting under RBI Integrated Ombudsman Scheme (RB-IOS 2026).

#### Key Exchange & Findings:
* **Q: "What keeps you up at night regarding the 30-day statutory timeline?"**
  * *Quote:* *"Under RB-IOS 2026, the 30-day clock starts the second the customer logs the grievance. If day 30 hits without a final resolution letter, the customer can escalate directly to the RBI Ombudsman CMS portal. Currently, roughly **11% to 13% of our cases drift past Day 25** because complex investigations stall across operations, fraud, and legal."*
  * *Validation:* Validates **Pain Point P4** (12% baseline past 30 days).
* **Q: "What is the true cost of an Ombudsman escalation to the bank?"**
  * *Quote:* *"The direct administrative charge from RBI is **₹3,500 per conciliated case**, which the bank must bear regardless of fault. But the hidden cost is massive: senior management time, compliance filings, and audit warnings. Right now, about **3.0% of total bank complaints end up at the Ombudsman** (~1,200 cases a month). Halving that would save millions."*
  * *Validation:* Validates A2 financial assumption of **3.0% baseline escalation rate** and **₹3,500 per escalation fee**.
* **Q: "What are your non-negotiable governance requirements for AI?"**
  * *Quote:* *"Under RBI FREE-AI and consumer protection rules, **no AI can ever send an unapproved message to a customer**. Period. If a model hallucinates a promise of compensation or misquotes an RBI circular, the bank is legally bound. Human-in-the-loop sign-off is mandatory for 100% of outbound communications."*
  * *Validation:* Grounds **HITL Rule #1** and rejects autonomous communication (`[AG]` tag).

---

### Interview 3: Frontline Dispute Handling Agent (Credit Cards Team)
* **Date:** 20 November 2026 | **Duration:** 30 Minutes
* **Role Context:** Frontline agent with 2 years of experience handling credit card billing, EMI conversion, and annual fee disputes.

#### Key Exchange & Findings:
* **Q: "Walk me through your computer screens when investigating a complaint."**
  * *Quote:* *"It's exhausting. I have to toggle between **four different systems** for every single case: (1) Finacle for account status, (2) Base24/Falcon for transaction history, (3) CRM for customer contact records, and (4) our internal intranet PDF folder for bank policies and RBI circulars. Searching for the right circular takes **7 to 8 minutes** alone because the PDF search is terrible."*
  * *Validation:* Validates **Pain Point P1** (searching 4 systems) and A1 tagging (38% `Knowledge` root cause).
* **Q: "How much time is spent writing the response?"**
  * *Quote:* *"At least **8 to 10 minutes**. We have standard macro templates, but every customer situation is slightly different. Writing out the explanation, quoting the fee structure, and ensuring polite tone takes forever. If a tool drafted an 80% complete letter based on the circular that I could just review, edit, and send, I could cut my handling time by a third."*
  * *Validation:* Validates **Pain Point P3** (drafting fatigue) and the 6.0-minute time savings assumption for Draft Reply in A2/A3.
* **Q: "What is one simple process change that would eliminate unnecessary work?"**
  * *Quote:* *"Discretionary waiver limits! At least 15% of my disputes are customers angry about a ₹500 or ₹1,000 annual card fee. Even when the customer spends ₹2 Lakhs a year, I am not allowed to waive a ₹500 fee without creating an escalation ticket for my supervisor. The supervisor takes 48 hours to click 'Approve'. Give frontline agents discretion up to ₹1,500 to waive fees on the spot!"*
  * *Validation:* Validates Non-AI Lean Fix #1 (frontline discretionary waiver threshold up to ₹1,500).
* **Q: "Are agents afraid that AI will replace them?"**
  * *Quote:* *"Yes, people are nervous. But we are also completely burned out by the volume. If leadership positions this as an assistant that does the boring PDF reading and typing so we don't get yelled at for missing SLAs, the team will embrace it."*
  * *Validation:* Validates our change management strategy and confirms adoption incentives.
