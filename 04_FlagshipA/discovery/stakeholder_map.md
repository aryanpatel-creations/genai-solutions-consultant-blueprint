# Discovery: Stakeholder Map & Influence Grid (stakeholder_map.md)

> **Client:** Kestrel Bank  
> **Engagement:** AI Transformation Blueprint — Complaints Redressal Modernisation  
> **Prepared by:** Aryan Patel (MBA Business Analytics)  
> **Deliverable:** Flagship Step 2a — Stakeholder Analysis

---

## 1. Stakeholder Analysis Matrix

Organizational change management is the #1 sensitivity driver of financial return in GenAI implementations (as proven by our Project A2 Tornado analysis, where adoption drives a ₹174.1 Lakh NPV swing). The stakeholder matrix identifies all key decision-makers, their institutional motivations, influence levels, and specific engagement mechanisms:

| Stakeholder Persona | Organizational Role | Decision Mandate | Influence / Interest | Core Motivations & Anxieties ("What They Care About") | Engagement Mechanism & Governance Rhythm | Status / Interviewed? |
|---|---|---|---|---|---|---|
| **Head of Customer Service** | Executive Sponsor | Owns budget, operations, and final vendor/solution sign-off. | **High / High** | Reducing resolution cycle time, mitigating customer churn, driving agent productivity, staying within operational budget. | Fortnightly Steering Committee chair; Business case and ROI review. | **Validated (Sponsor Brief)** |
| **Principal Nodal Officer (PNO)** | Grievance Custodian | Legally accountable to Reserve Bank of India (RBI) under RB-IOS 2026. | **High / High** | 30-day statutory resolution compliance, eliminating ₹3,500 Ombudsman escalation fees, audit defensibility. | Dedicated 1-on-1 interview; Co-designer of Escalation Triggers and Governance Control Map. | **Interviewed (Interview #2)** |
| **Chief Risk & Compliance Officer (CRO)** | Regulatory Gatekeeper | Can veto or halt deployment based on compliance or security risks. | **High / Medium** | DPDP Act 2023 compliance, RBI FREE-AI adherence, hallucination risk, data leak prevention, algorithmic bias. | Bi-weekly Governance Gate reviews; Sign-off on Model Risk Policy and PII Masking Architecture. | **Consulted (Compliance Gate)** |
| **Chief Information Officer (CIO) / Enterprise Arch** | Technical Delivery Lead | Responsible for infrastructure, hosting, API integration, and security. | **High / Medium** | Core banking security, latency SLOs (<5s P95), uptime (99.9%), prompt caching efficiency, minimal API maintenance. | Weekly Technical Architecture Working Group; NFR definition workshops. | **Consulted (IT Architecture)** |
| **Complaint Team Leads (Cards, Accounts, Digital)** | Frontline Supervisors | Manage daily roster, workflow distribution, and first-line QA. | **Medium / High** | Queue backlogs, shift burnout, QA review burden, training overhead for new tools, SLA breach management. | Operational deep-dive interviews; Co-designers of Pilot Stage 1 feedback loops and QA rubrics. | **Interviewed (Interview #1)** |
| **Frontline Complaint Handling Agents** | Daily Platform Users (120 agents) | Execute daily triage, investigation, and customer draft formulation. | **Low / High** | Fragmented core systems (navigating 4 UIs), anxiety regarding job replacement, time spent drafting repetitive text. | Frontline shadowing and workflow interviews; Design partner champions; Pilot training workshops. | **Interviewed (Interview #3)** |
| **Chief Financial Officer (CFO)** | Investment Approver | Signs off capital allocation (₹86 Lakh Capex, ₹40 Lakh/yr Opex). | **High / Low** | Hard cashable savings vs. soft cost avoidance, payback period ($\le 18$ months), 3-year NPV hurdle rate. | Milestone business case presentation; Hard vs. Full NPV walk slide; Stage gate financial reviews. | **Consulted (A2 Sign-off)** |

---

## 2. Power vs. Interest Grid

```
                  HIGH INFLUENCE
                       │
       [MEET THEIR NEEDS]   │   [KEY PLAYERS / MANAGE CLOSELY]
                            │
  • CFO / Finance           │  • Head of Customer Service (Sponsor)
  • Chief Risk Officer (CRO)│  • Principal Nodal Officer (PNO)
  • CIO / Enterprise Arch   │
────────────────────────────┼────────────────────────────
                            │
       [MONITOR - MIN EFFORT]│   [KEEP ADEQUATELY INFORMED]
                            │
  • Branch Operations Leads │  • Complaint Team Leads
                            │  • Frontline Dispute Agents (120 users)
                       │
                   LOW INFLUENCE
  LOW INTEREST ───────────────────────────── HIGH INTEREST
```

### Strategic Change Management Implications:
1. **Manage Closely (High Power / High Interest):** The Head of Customer Service and Principal Nodal Officer hold existential authority. The business case must continuously align with the PNO's compliance mandate (eliminating the ₹194.4L Ombudsman escalation cost) while satisfying the Sponsor's efficiency targets.
2. **Meet Their Needs (High Power / Moderate Interest):** The CFO and CRO are defensive gatekeepers. If the CRO identifies a single unmasked PII data leak or if the CFO views savings as non-cashable "paper savings," the initiative will be blocked. Our A2 hard-vs-full financial model and A3 automated PII blocking tripwires directly mitigate their objections.
3. **Keep Informed & Empower (Low Power / High Interest):** Frontline agents cannot veto the purchase, but their collective refusal or hesitation to adopt the assistant will collapse project ROI (Tornado sensitivity #1). Addressing agent anxiety early—positioning the assistant as an administrative copilot that eliminates manual searches rather than an autonomous replacement—is mandatory for change success.
