# Business Requirements Document (BRD)
## Project: Kestrel Bank AI-Augmented Grievance Redressal Architecture

> **Document Reference:** BRD-AI-KESTREL-2026-V1.0  
> **Prepared by:** Aryan Patel (MBA Business Analytics, Techno-Functional Consultant)  
> **Stakeholders:** Head of Customer Service (Sponsor), Principal Nodal Officer, CRO, CIO, CFO  
> **Target Release:** Phase 1 (Cards & Accounts Pilot) $\to$ Phase 2 (Enterprise Rollout)  
> **Status:** Baselined for Architecture Review

---

## 1. Objectives & Business Scope

### 1.1 Project Objectives
The objective of the Kestrel Bank AI Transformation initiative is to modernize retail banking complaint handling across 120 dedicated dispute agents handling ~40,000 monthly grievances. The transformation targets five core operational pain points identified in Project A1:

| Objective Ref | Core Transformation Objective | Addressed Pain Point | Primary Success Metric & Target | Baseline Metric (Project A1 / Interviews) |
|---|---|---|---|---|
| **OBJ-01** | Accelerate knowledge discovery and reduce cross-system manual lookup friction. | **P1** (Searching 4 systems) | Average Handle Time (AHT) reduced to **$\le 19.0$ minutes** | Baseline AHT: **25.0 minutes** (8.0 min in policy lookup) |
| **OBJ-02** | Eliminate intake misdirection and cross-departmental queue bouncing. | **P2** (Intake misrouting) | Complaint Re-Route Rate reduced to **$\le 5.0\%$** | Baseline Re-Route Rate: **20.0%** (~8,000 cases/mo) |
| **OBJ-03** | Relieve agent drafting cognitive fatigue and standardize communication tone. | **P3** (Drafting from scratch) | Response Drafting Time reduced to **$\le 2.5$ minutes** | Baseline Drafting Time: **8.5 minutes** |
| **OBJ-04** | Prevent regulatory breach and eliminate statutory Ombudsman escalation costs. | **P4** (30-day drift) | Resolved $\le 30$ days **$\ge 95.0\%$**; Ombudsman rate **$\le 1.5\%$** | $\le 30$ days: **88.0%**; Ombudsman rate: **3.0%** (~1,200/mo) |
| **OBJ-05** | Eliminate repeat disputes through frontline empowerment and root-cause feedback. | **P5** (Repeat defects) | Discretionary waiver of petty fee disputes **$\le ₹1,500$** | 15% of complaints stuck in supervisor fee waiver queues |

### 1.2 In-Scope vs. Out-of-Scope
* **In-Scope:** Internal agent-facing AI assistant copilot across 4 operational teams (Cards, Savings & Current, Digital Banking, Branch Escalations); automated triage; semantic RAG retrieval of bank policies and RBI circulars; draft reply generation; Day-25 regulatory alerts; client-side PII masking.
* **Out-of-Scope:** Fully autonomous customer-facing conversational bots; automated account debiting or ledger adjustments without human authentication; customer-facing unreviewed communications.

---

## 2. Current vs. Future State Architecture

The process redesign transitions Kestrel Bank from an unstructured, highly manual, error-prone workflow to a gated, AI-augmented architecture:

```
As-Is Baseline Architecture (11 [H] | 1 [R] | 0 [AI] | 0 [AG]):
[Customer Free Text] ──► [Manual Routing Desk] ──► [Queue Bounce 20%] ──► [Agent Toggles 4 Systems]
                            │                                                   │
                            ▼                                                   ▼
                [SLA Loss 1-3 Days]                                 [Searches PDF Circulars 8 min]
                                                                                │
                                                                                ▼
[Manual Closure Letter] ◄── [Supervisor Approval Fee <Rs 500] ◄── [Drafts Letter from Scratch 8.5 min]
```

```
To-Be AI-Augmented Architecture (7 [H] | 4 [R] | 3 [AI] | 0 [AG]):
[Structured Intake Form] ──► [PII Masking Gateway] ──► [AI Triage (Haiku 5.5)] ──► [Agent Validates 1-Click]
                                       │                                                │
                                       ▼                                                ▼
                             [Auto-Ack < 2 Hours]                           [AI Policy RAG (Sonnet 5.5)]
                                                                                        │
                                                                                        ▼
[Customer Resolution] ◄── [Agent Reviews & Signs Off] ◄── [AI Drafts Reply] ◄── [Discretionary Waiver <=1.5k]
```

* **Operational Tag Shift:** Manual human touch points decrease from **11 to 7 (-36%)**, automated deterministic rules increase from **1 to 4**, and **3 AI Copilots** perform heavy retrieval and synthesis tasks. Autonomous agents (`[AG]`) remain strictly at **0**.

---

## 3. Functional Requirements (FR)

### FR-01: Automated Triage & Queue Classification Assistant
* **Use Case:** Triage & Routing Copilot (`[AI]`)
* **Underlying Model:** Claude Haiku 5.5 (or lightweight local equivalent).
* **Inputs:** Customer complaint text (PII-masked), channel metadata, product category, customer relationship tenure.
* **Outputs:** Predicted complaint category (3-level taxonomy), recommended operational team (Cards, Savings, Digital, Branch), predicted urgency score (Low, Medium, High, Regulatory Risk), and confidence score ($0.00$ to $1.00$).
* **Systems Touched:** CRM Ingestion Gateway, Frontline Dispatch Routing Engine.
* **Actor:** Frontline Complaint Routing Desk / Receiving Agent.

### FR-02: Policy Knowledge Retrieval & Citation Assistant (RAG)
* **Use Case:** Policy Knowledge Q&A (`[AI]`)
* **Underlying Model:** Claude Sonnet 5.5 with Contextual Retrieval & Prompt Caching.
* **Inputs:** Grievance summary, transaction dispute code, product type, user query.
* **Outputs:** Contextual explanation of applicable bank policy clause, exact RBI Master Direction circular citation (Circular number, paragraph, date), and recommended operational resolution action.
* **Fallback Behavior:** If no relevant policy clause exceeds the semantic similarity threshold ($>0.75$), the system must explicitly state: *"No matching policy clause found. Please refer to Compliance Manual"* rather than generating a speculative response.
* **Systems Touched:** Enterprise Vector Store (Qdrant/Pinecone), Policy Document Intranet Repository.
* **Actor:** Frontline Dispute Handling Agent.

### FR-03: AI Response Drafting Assistant
* **Use Case:** Draft Reply Generator (`[AI]`)
* **Underlying Model:** Claude Sonnet 5.5.
* **Inputs:** Structured complaint facts, transaction audit records, verified policy citations (from FR-02), agent resolution decision (Relief Granted / Discretionary Waiver / Claim Declined).
* **Outputs:** Professional, empathetic, 80%-complete response letter incorporating customer reference details, explanation of decision, cited regulatory provisions, and standard RBI Ombudsman disclosure.
* **Systems Touched:** CRM Case Management Workspace, Document Generation Engine.
* **Actor:** Frontline Dispute Handling Agent.

### FR-04: Tiered Discretionary Fee Waiver Engine
* **Use Case:** Operational Policy Automation (`[H]` / `[R]`)
* **Inputs:** Customer relationship value, disputed fee amount, fee transaction date.
* **Logic:** If disputed fee $\le ₹1,500$ and customer has $\le 2$ waivers in rolling 12 months, frontline agent is empowered to execute immediate fee reversal in core banking with one click. If $> ₹1,500$, automatically routes to Supervisor Approval Queue.
* **Systems Touched:** Core Banking Integration Gateway (Finacle), CRM Case Ledger.
* **Actor:** Frontline Dispute Handling Agent.

### FR-05: Day-25 Regulatory Amber Alert & Timeline Summarizer
* **Use Case:** Regulatory Risk Prevention (`[AI]` / `[R]`)
* **Inputs:** Case age in days, multi-department case logs, pending external dependencies.
* **Logic:** At Day 25, system flags ticket as "Statutory Amber Alert", compiles an executive chronological bullet-point summary of case history, and routes to Senior Nodal Officer.
* **Systems Touched:** RB-IOS Compliance Tracking Ledger, CRM Alert Manager.
* **Actor:** Principal Nodal Officer, Escalations Team.

---

## 4. AI Quality & Evaluation Requirements

To ensure enterprise-grade reliability, all AI components must satisfy strict empirical benchmark evaluation thresholds:

| AI Module | Evaluation Metric | Quantitative Threshold | Evaluation Test Dataset | Failure Behavior / Fallback |
|---|---|---|---|---|
| **FR-01 (Triage)** | Routing Classification Accuracy | **$\ge 90.0\%$** | 200 labeled historical complaints across 4 banking teams | Divert to Senior Intake Specialist if confidence $<0.80$. |
| **FR-02 (Policy Q&A)** | Policy Citation Accuracy | **$\ge 85.0\%$** rated correct by two independent reviewers | 100 golden policy questions grounded in RBI Master Directions | Explicitly return *"Policy clause not found"* if similarity score $<0.75$. |
| **FR-02 (Policy Q&A)** | Hallucination Rate | **$\le 1.0\%$** | 100 adversarial / out-of-domain questions | Refusal to answer ungrounded queries; zero fabricated citations. |
| **FR-03 (Draft Reply)** | Agent Acceptance Rate | **$\ge 80.0\%$** of drafts accepted or edited | 90-day pilot event log (measured in Project A3) | Agent writes letter using standard manual macro template. |
| **FR-03 (Draft Reply)** | Agent Override / Rejection Rate | **$\le 15.0\%$** (2-week rolling window) | Weekly monitoring via A3 Risk Dashboard | Triggers mandatory prompt engineering review and root-cause audit. |

---

## 5. Human-in-the-Loop (HITL) Oversight & Control

The solution strictly enforces Human-in-the-Loop oversight at every critical operational inflection point:

1. **HITL Review Gate 1 (Triage Validation):** The agent confirms or reclassifies the suggested dispute category with one click. Reclassifications are logged to measure model accuracy.
2. **HITL Review Gate 2 (Mandatory Outbound Approval):** No text drafted by the AI assistant can be dispatched to a customer without explicit human agent sign-off. The CRM UI blocks the "Send Communication" button until the agent checks a verification box.
3. **HITL Review Gate 3 (Financial Delegation):** Any financial compensation or waiver exceeding ₹1,500 requires secondary supervisor approval.
4. **Audit Logging:** 100% of human overrides, agent edits, and prompt inputs/outputs are persisted in an immutable audit ledger with user ID, timestamp, and duration for 7 years under RBI record-keeping guidelines.

---

## 6. Data Architecture & Regulatory Privacy (DPDP Act 2023)

### 6.1 Data Sources
* Core Banking System (Finacle): Transaction records, account status, relationship tenure.
* Card Management Platform (Base24/Falcon): Dispute chargeback status, authorization codes.
* Knowledge Base Repository: Bank retail service policies, product circulars, RBI Master Directions on Customer Service.

### 6.2 Data Privacy & Masking (DPDP Act 2023)
* **Client-Side Masking Gateway:** Prior to transmission to any external model inference endpoint, all raw complaint text must pass through a regex and NER tokenization filter.
* **Target Sensitive Identifiers:**
  * 12-digit Aadhaar Numbers $\to$ `[REDACTED_AADHAAR]`
  * 10-character Permanent Account Numbers (PAN) $\to$ `[REDACTED_PAN]`
  * 16-digit Primary Account / Credit Card Numbers $\to$ `[REDACTED_CARD]`
  * Indian Mobile Numbers (+91 / 10 digits) $\to$ `[REDACTED_PHONE]`
  * Customer Email Addresses $\to$ `[REDACTED_EMAIL]`
* **Data Residency:** All model inference pipelines must execute within the Sovereign Territory of India (AWS/Azure/GCP Mumbai or Hyderabad regions).
* **Zero Model Retention:** Contracts with cloud LLM providers must legally enforce zero data retention (ZDR) for foundation model training.

---

## 7. Non-Functional Requirements (NFR)

| Ref ID | Category | Requirement Specification | Measurement & Target |
|---|---|---|---|
| **NFR-01** | **Latency (P95)** | The Policy Knowledge Q&A and Draft Reply assistants must deliver answers within interactive agent tolerance. | **P95 Latency $\le 5.0$ seconds** (Measured via A3 Risk lens). |
| **NFR-02** | **Availability & Uptime** | The AI assistant layer and vector search services must maintain high availability during banking hours. | **$\ge 99.9\%$ operational uptime** during 08:00–20:00 IST. |
| **NFR-03** | **Cost per Complaint Ceiling** | Variable model inference token consumption must remain economically viable and within A2 business case parameters. | **$\le ₹2.00$ per complaint** (Actual pilot baseline: ₹0.70/run). |
| **NFR-04** | **Prompt Caching Efficiency** | Static policy documents and system prompts must leverage API prompt caching to minimize latency and token expenditure. | **$\ge 85.0\%$ prompt cache hit rate** for Policy Q&A calls. |
| **NFR-05** | **Security & Encryption** | All customer grievance payloads in transit and at rest must be cryptographically protected. | **TLS 1.3 in transit; AES-256 at rest.** |
| **NFR-06** | **Concurrent User Concurrency** | System must support peak concurrent load across 120 frontline agents without degradation. | **$\ge 60$ concurrent active agent sessions.** |

---

## 8. Monitoring, Acceptance & Governance Sign-Off

* **Acceptance Test Sets:**
  * Test Set 1: 200 labeled historical complaints (Cards, Accounts, Digital, Branch) for Triage evaluation.
  * Test Set 2: 100 verified policy questions for RAG precision and citation evaluation.
  * Test Set 3: 50 synthetic high-risk PII payloads for data leak validation.
* **Operational Monitoring Layer:** Fully instrumented via **Project A3 AI Value Dashboard** tracking 16 tested KPIs across CFO, COO, CRO, and Sponsor lenses.
* **Governance Sign-Off Owners:**
  * Business Requirements: Head of Customer Service (Sponsor).
  * Compliance & Regulatory Controls: Principal Nodal Officer & Chief Compliance Officer.
  * Technical & Security Architecture: Chief Information Officer & CISO.
