# SIPOC: Kestrel Bank Retail Complaint Handling

> **Purpose:** High-level operational view mapping Suppliers, Inputs, Process Steps, Outputs, and Customers across Kestrel Bank's retail checking, savings, and credit card complaint workflows.

---

```mermaid
flowchart LR
    S["Suppliers\n• Customers\n• Branch Network\n• Contact Centre\n• RBI CMS Portal"] --> I["Inputs\n• Complaint Text & Channel\n• Core Account & Txn Data\n• Bank Product Policies\n• Regulatory Mandates"]
    I --> P["7-Step Core Process\n1. Receive & Log\n2. Acknowledge\n3. Classify & Route\n4. Investigate\n5. Decide Outcome\n6. Reply & Close\n7. Learn (DMAIC)"]
    P --> O["Outputs\n• Formal Written Response\n• Fee Reversal / Refund\n• Account Remediation\n• Regulatory Audit Trail\n• MIS Risk Reports"]
    O --> C["Customers\n• Retail Customer\n• Principal Nodal Officer\n• Compliance & Internal Audit\n• RBI Ombudsman"]
```

---

## Detailed SIPOC Breakdown

| Component | Detailed Items | Operational Notes / Observations |
|---|---|---|
| **Suppliers** | • Retail & Card Customers<br>• Branch Relationship Managers<br>• Tier-1 Call Centre Agents<br>• RBI Complaint Management System (CMS) | Inbound complaints arrive through distributed channels; web and digital forms dominate volume (~80%+). |
| **Inputs** | • Free-form consumer narrative<br>• Product & issue classification tags<br>• Customer identity & account numbers<br>• Transaction ledger & dispute history<br>• Internal policy manuals & RBI circulars | Inputs often contain unstructured, emotionally charged consumer descriptions with sensitive personal data (PII) requiring masking. |
| **Process (High Level)** | **1. Receive and Log:** Ingest from portal/branch into CRM ticket.<br>**2. Acknowledge:** Issue automated confirmation and tracking ID within 1 working day.<br>**3. Classify and Route:** Triage complaint to specialized unit (Cards, Accounts, Fraud, Escalations).<br>**4. Investigate:** Frontline agent reviews transaction logs, policies, and card network chargeback rules (AHT ~25 min).<br>**5. Decide Outcome:** Determine financial relief, non-monetary correction, or formal explanation.<br>**6. Reply and Close:** Draft regulatory-compliant closure letter and execute relief within RB-IOS 30-day limit.<br>**7. Learn:** Synthesize defect data into monthly operational risk and product engineering reviews. | Current investigation (Step 4) and drafting (Step 6) consume the vast majority of agent handling capacity. |
| **Outputs** | • Formal resolution letter / email<br>• Financial relief credit (monetary adjustment)<br>• Account unfreeze / card replacement (non-monetary)<br>• Updated CRM case history and closed ticket<br>• Regulatory compliance reporting logs | Outputs must meet strict statutory fairness and documentation standards under RB-IOS 2026. |
| **Customers** | • Aggrieved Bank Customer<br>• Principal Nodal Officer (Internal)<br>• Chief Risk Officer & Legal Counsel<br>• Reserve Bank of India (Ombudsman) | The ultimate stakeholder is both the customer (retention) and the regulator (statutory compliance and zero Ombudsman awards). |
