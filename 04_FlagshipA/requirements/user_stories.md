# Requirements: Agile User Stories & Acceptance Criteria (user_stories.md)

> **Client:** Kestrel Bank  
> **Engagement:** AI Transformation Blueprint — Complaints Redressal Modernisation  
> **Prepared by:** Aryan Patel (MBA Business Analytics)  
> **Deliverable:** Flagship Step 4 — Detailed User Stories with Empirical Evaluation Criteria  
> **Companion Document:** `04_FlagshipA/requirements/BRD.md`

---

## 1. User Story Framework

In enterprise GenAI implementations, standard software user stories are insufficient. Requirements must define **algorithmic precision**, **evaluation test sets**, **graceful degradation**, and **human-in-the-loop auditability**. Every user story below follows this rigorous format:

---

### US-01: Automated Triage & Queue Routing Suggestion
* **Story:** *As a Frontline Complaint Agent, I want the intake system to automatically suggest the correct complaint category and destination team based on the customer's grievance text, so that complaints stop bouncing between departments and reach the right specialist on Day 1.*
* **Linked Pain Point:** **P2** (Intake misdirection; 20% baseline re-route rate).
* **Target User:** Frontline Complaint Agents & Intake Routing Staff.
* **Empirical Acceptance & Evaluation Criteria:**
  1. **Algorithmic Accuracy:** The suggested team must match ground truth on **$\ge 90.0\%$** of a 200-complaint historically labeled test set across Cards, Savings, Digital, and Branch queues.
  2. **One-Click Agent Override:** The CRM interface must display the suggested queue with a one-click confirmation button and an instant dropdown to reclassify if necessary.
  3. **Audit Logging:** Every agent override must log the initial model prediction, user correction, timestamp, and agent ID to inform downstream model retraining.
  4. **Low-Confidence Safeguard:** If model classification confidence is $< 0.80$, the grievance is automatically flagged for Senior Specialist review rather than auto-routed.

---

### US-02: Policy Knowledge Retrieval with Mandatory Regulatory Citations (RAG)
* **Story:** *As a Frontline Dispute Handling Agent, I want to query our internal knowledge base using natural language and receive an immediate answer that cites the exact bank policy clause and RBI Master Direction circular, so that I stop wasting 8 minutes searching through four disconnected systems and static PDF circulars.*
* **Linked Pain Point:** **P1** (Searching 4 systems; 38% knowledge root-cause in A1).
* **Target User:** Frontline Dispute Handling Agents (120 users).
* **Empirical Acceptance & Evaluation Criteria:**
  1. **Mandatory Citation Enforcement:** 100% of generated policy answers must cite the specific document title, circular reference number, and paragraph/clause.
  2. **Refusal on Missing Source:** If no retrieved policy clause exceeds the semantic similarity cutoff ($0.75$), the system must explicitly return: *"No applicable policy clause found. Please consult your Team Lead"* rather than speculating or hallucinating.
  3. **Evaluation Benchmark:** **$\ge 85.0\%$** of answers rated completely accurate and fully grounded by two independent compliance reviewers across a 100-question golden test set.
  4. **Latency Threshold:** 95th percentile response latency (**P95 Latency**) must remain **$\le 5.0$ seconds**.

---

### US-03: AI Response Drafting Assistant
* **Story:** *As a Frontline Dispute Handling Agent, I want the system to generate an 80%-complete, professional response letter synthesizing the case facts, verified transactions, and cited regulatory rules, so that I do not have to write long letters from scratch.*
* **Linked Pain Point:** **P3** (Drafting cognitive fatigue; 8.5 min baseline drafting time).
* **Target User:** Frontline Dispute Handling Agents.
* **Empirical Acceptance & Evaluation Criteria:**
  1. **Draft Generation Speed:** Model synthesizes facts into a structured letter within **$\le 4.0$ seconds**.
  2. **Compliance Standard Language:** The draft must automatically incorporate required statutory disclosures under RB-IOS 2026, including the customer's right to escalate to the Banking Ombudsman if unsatisfied.
  3. **Editable Canvas:** The draft must appear in an editable CRM text pane allowing the agent to modify, add specific relationship notes, or regenerate specific paragraphs.
  4. **Adoption Quality Metric:** The agent acceptance rate (Accepted + Edited without major rewrite) must achieve **$\ge 80.0\%$** in live operations.

---

### US-04: Mandatory Human Outbound Review & Approval Gate
* **Story:** *As a Compliance Officer and Customer Service Supervisor, I want every customer-facing letter drafted by the AI assistant to require explicit agent review and sign-off before dispatch, so that no unreviewed, inaccurate, or hallucinated text can ever reach a bank customer.*
* **Linked Pain Point:** **P3 / P4** (Regulatory liability and quality control).
* **Target User:** Team Leads, Supervisors, Compliance Officers.
* **Empirical Acceptance & Evaluation Criteria:**
  1. **Technical Blocking Gate:** The CRM messaging gateway API must reject any outbound message payload that lacks a cryptographic verification token signed by an authenticated agent session.
  2. **Negative Boundary Test:** Automated security unit tests must attempt to bypass agent sign-off; 100% of automated bypass attempts must fail with an `HTTP 403 Forbidden` error.
  3. **Edit Logging:** The system must record the original AI draft, the finalized sent text, and calculate the Levenshtein edit distance to measure agent modification intensity.

---

### US-05: Day-25 Statutory Amber Alert & Case History Summarizer
* **Story:** *As a Principal Nodal Officer, I want complaints reaching Day 25 of the 30-day statutory clock to trigger an urgent amber alert accompanied by an AI-generated chronological case summary, so that our team can intervene and settle complex cases before they breach Day 30 and escalate to the RBI Ombudsman.*
* **Linked Pain Point:** **P4** (30-day drift; 3.0% baseline Ombudsman escalation rate).
* **Target User:** Principal Nodal Officer, Senior Grievance Redressal Managers.
* **Empirical Acceptance & Evaluation Criteria:**
  1. **Automated Trigger:** The CRM SLA engine must automatically flag cases on Day 25 at 08:00 IST and transfer ownership to the Senior Nodal Officer queue.
  2. **Chronological Case Summary:** The AI summarizer must ingest all case notes across operations, fraud, and branch systems, outputting a bulleted timeline: (1) Core customer claim, (2) Root cause defect, (3) Current investigative bottleneck, and (4) Proposed resolution.
  3. **Evaluation:** Tested against 50 historical complex cases; summary must capture 100% of major financial transactions and blockages without omitting key dates.

---

### US-06: Frontline Discretionary Fee Waiver Engine ($\le ₹1,500$)
* **Story:** *As a Frontline Complaint Agent, I want the authority to execute an immediate discretionary waiver for disputed fees up to ₹1,500 directly in CRM, so that I can resolve petty fee complaints on first contact without waiting 48 hours for supervisor approval.*
* **Linked Pain Point:** **P5** (Repeat fee defects; 15% of complaints stuck in supervisor queues).
* **Target User:** Frontline Dispute Handling Agents (120 users).
* **Empirical Acceptance & Evaluation Criteria:**
  1. **One-Click Execution:** Authorized agents can click "Apply Discretionary Waiver" for eligible fee codes $\le ₹1,500$; the transaction posts directly to the Core Banking Finacle ledger.
  2. **Eligibility Rules:** CRM verifies that the customer has not received $>2$ discretionary waivers in the preceding rolling 12-month period.
  3. **Automatic Routing for Over-Limit:** Any waiver request $> ₹1,500$ automatically routes to the Supervisor Approval Queue with a justification prompt.

---

### US-07: Client-Side DPDP PII Masking & Data Tokenization Gateway
* **Story:** *As a Chief Information Security Officer (CISO) and Data Protection Officer, I want all sensitive customer PII (Aadhaar, PAN, Card Numbers, Mobile Numbers) masked on the bank's internal network before any prompt payload is transmitted to an LLM API, so that Kestrel Bank complies fully with the Digital Personal Data Protection Act 2023.*
* **Linked Pain Point:** **Compliance / NFR** (Data privacy and regulatory protection).
* **Target User:** CISO, Compliance Officers, Enterprise Security Architects.
* **Empirical Acceptance & Evaluation Criteria:**
  1. **Tokenization Coverage:** 100% of 12-digit Aadhaar numbers, 10-character PAN identifiers, and 16-digit Primary Account Numbers (PAN/Credit Card) must be redacted or tokenized prior to API dispatch.
  2. **Adversarial Validation:** Validated against a benchmark suite of 50 synthetic adversarial complaint narratives containing nested, formatted, and obfuscated PII; zero leakage permitted.
  3. **Telemetry:** Masking events are tracked via the A3 Risk Dashboard (`pii_blocks` metric; baseline 944 working intercepts).
