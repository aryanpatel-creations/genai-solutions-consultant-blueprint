# 5 Whys Root-Cause Analysis: Kestrel Bank

> **Methodology:** Lean Six Sigma Root-Cause Analysis grounded in the 100 tagged complaint narratives, empirical baseline KPIs, and operational observations.

---

## Root Cause 1: Process Inefficiency & Knowledge Retrieval Latency (56% of Defects)

| Level | Question | Answer | Evidence / Source |
|---|---|---|---|
| **Why 1** | Why are complex complaints slow to investigate (AHT ~25 minutes)? | Agents spend excessive time searching for relevant bank policies, product terms, and RBI circulars. | 38% of tagged narratives identified `ai_could_help = Knowledge` |
| **Why 2** | Why does finding the applicable policy or circular take so long? | Policies, circulars, and dispute precedents sit across four disconnected repositories with no unified search interface. | Process interviews & IT landscape |
| **Why 3** | Why are there four separate document repositories? | Each product team (Cards, Savings/Current, Digital/UPI, Fraud Ops) manages its own documentation independently. | Operational silo structure |
| **Why 4** | Why does nobody maintain a unified complaint knowledge base? | Frontline complaint teams are measured strictly on ticket closure volume and speed, not on knowledge curation or defect prevention. | Performance KPI structure |
| **Root Cause (Why 5)** | **Lack of centralized knowledge ownership and unified semantic search tools across product verticals.** |
| **Actionable Fix** | **Non-AI Fix:** Appoint a single Knowledge Custodian under the Principal Nodal Officer with mandatory monthly policy updates.<br>**AI Intervention:** Implement an internal Policy & Regulatory RAG assistant with verified citations to reduce search time from ~10 mins to <1 min. |

---

## Root Cause 2: Multi-Hop Routing & Rigid Approval Thresholds (15% Policy + 25% System Defects)

| Level | Question | Answer | Evidence / Source |
|---|---|---|---|
| **Why 1** | Why do low-value fee and transaction disputes bounce between multiple agents and supervisors? | Frontline Tier-1 agents lack authorization to reverse fees or issue provisional dispute credits directly upon first contact. | 27% of tagged narratives identified `ai_could_help = Triage`; 15% were pure `Policy` defects |
| **Why 2** | Why do Tier-1 agents lack reversal authority? | The bank's delegation of financial powers requires dual supervisory sign-off for any ledger credit, regardless of amount. | Kestrel Bank operational policy manual |
| **Why 3** | Why was the approval threshold set so strictly? | Historical fear of operational leakage and fraud without auditing mechanisms for discretionary agent overrides. | Internal audit & risk policy |
| **Why 4** | Why has leadership not re-evaluated this policy? | The bank never quantified the loaded handling cost (₹400/hr = ~₹167 per 25-minute ticket) against small dispute amounts (e.g., ₹250–₹500 fee waiver). | Operations vs Finance disconnect |
| **Root Cause (Why 5)** | **Misalignment between financial approval controls and transactional handling cost, creating artificial operational bottlenecks.** |
| **Actionable Fix** | **Non-AI Fix:** Institute a tiered frontline discretionary fee waiver matrix (up to ₹1,500 for eligible first-time disputes) with automated monthly audit sampling.<br>**AI Intervention:** Automated account fact retrieval and compliance checklist generator to ensure waiver conditions are strictly met before human approval. |
