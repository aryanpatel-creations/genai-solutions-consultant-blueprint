# AI Opportunity Mapping & Scope Boundaries (A1 Step 11)

> **Core Philosophy:** "AI should assist human judgment where unstructured data creates friction; AI must never replace human accountability in regulatory decisions."

---

## 1. High-Value AI Opportunity Shortlist

| As-Is Process Step | Operational Pain Point & Waste | Proposed AI Intervention | Empirical Evidence & Tag Grounding | Feasibility & Risk Rating |
|---|---|---|---|---|
| **Classify & Route** | Queue misrouting (~20% tickets); customer narrative text contains emotional noise obscuring true product issue. | **Intelligent Semantic Triage:** Multiclass NLP classifier predicting product category and routing destination with confidence scores. | **27% of tagged sample** (`ai_could_help = Triage`); Pareto shows 80% volume concentrated in 10 issues. | **High Feasibility / Low Risk** (Internal routing only; human can re-route). |
| **Investigate: Policy & Regulations** | Agents spend 8–10 minutes searching across 4 siloed PDF repositories for RBI Master Directions and internal bank rules. | **Regulatory & Policy RAG Engine:** Retrieval-Augmented Generation with strict vector search across RBI circulars and product manuals, returning grounded answers with exact section citations. | **38% of tagged sample** (`ai_could_help = Knowledge`); 56% Process root causes. | **High Feasibility / Medium Risk** (Requires strict anti-hallucination guardrails and citations). |
| **Investigate: Account Facts & Chronology** | Agents manually alt-tab between core banking (Finacle) and dispute management ledgers to assemble multi-month transaction timelines. | **Chronology & Dispute History Summarizer:** MCP-enabled read-only account fact extraction generating structured bulleted case timelines. | **17% of tagged sample** (`ai_could_help = Summary`); prominent in multi-month dispute narratives. | **High Feasibility / Low Risk** (Summarizes internal system logs for agent review). |
| **Reply & Close: Response Drafting** | Writing closure letters from scratch (7–8 min/ticket); inconsistent empathy; risk of ombudsman non-compliance. | **Compliance-Grounded Response Drafter:** Drafts personalized, empathetic closure letters synthesizing customer grievance and investigation findings, with an automated compliance checklist. | Standardizes drafting across 120 agents; saves 5–7 mins per ticket. | **Medium Feasibility / Medium Risk** (Mandatory human-in-the-loop sign-off prior to dispatch). |

---

## 2. Strict Negative Scope: Where AI Must NOT Be Used

A senior consultant demonstrates maturity by establishing clear boundaries where AI should be rejected:

| Excluded Use Case | Rationale & Regulatory Constraint | Better Lean Alternative |
|---|---|---|
| **Autonomous Customer Dispatch** | Generative AI models must **never** send unreviewed emails or letters directly to aggrieved bank customers. Hallucinated commitments or tone missteps create severe reputational damage and statutory liability under RB-IOS 2026. | **Human-in-the-Loop (HITL):** Frontline agent reviews, edits, and explicitly signs off on every AI-drafted communication. |
| **Automated Dispute Rejection** | Automatically denying fee waivers or transaction fraud claims based on probabilistic model scoring violates RBI FREE-AI fairness principles and natural justice requirements. | **Human Adjudication:** Rejections must be made by authorized bank officers with clear, documented factual grounds. |
| **Fixing Broken Bank Policies** | 15% of complaint narratives represent pure **Policy Defects** (e.g., hidden fees, unfair dormant account freezes). Building AI to explain bad policies is wasteful and creates customer cynicism. | **Non-AI Policy Fix:** Change the product policy directly (e.g., frontline fee waiver limits, transparent pre-debit alerts). `ai_could_help = None`. |
| **Direct Core Banking System (CBS) Writes** | Allowing AI agents direct write-access to CBS ledger accounts (such as initiating automated refunds without approval tokens) introduces catastrophic operational risk. | **Approval Token Gating:** Refunds must require a server-issued cryptographic approval token verified by an authorized supervisor (demonstrated in Category B). |
