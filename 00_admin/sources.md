# Sources & Citations Register

This register documents all primary data sources, regulatory benchmarks, and industry references utilized across the Kestrel Bank AI Transformation Blueprint.

---

## 1. Primary Empirical Data
| Source ID | Source Name | Publisher / Institution | Access / Reference Date | Link / Citation |
|---|---|---|---|---|
| **SRC-01** | Consumer Complaint Database | Consumer Financial Protection Bureau (CFPB) | Nov 2026 | [CFPB Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/) |
| **SRC-02** | FOIA Consumer Complaint Narratives Archive | Consumer Financial Protection Bureau (CFPB) | Nov 2026 | [CFPB Narratives Archive](https://www.consumerfinance.gov/foia-requests/foia-electronic-reading-room/cfpb-consumer-complaint-database-narratives-archive/) |
| **SRC-03** | CFPB Complaint Database Field Reference | CFPB GitHub API Docs | Nov 2026 | [Field Reference](https://cfpb.github.io/api/ccdb/fields.html) |

### Empirical Stand-in Data Limitations (Consulting Note)
1. **No Resolution Timestamp:** CFPB complaint records record intake date (`Date received`) and transmission date (`Date sent to company`), but lack case closure / resolution dates. Handling time (AHT) and total resolution cycles cannot be empirically derived from this data; they are explicitly treated as operational assumptions to be validated through process mapping and stakeholder interviews.
2. **Jurisdictional Transfer:** US retail banking data serves as a proxy for complaint topology, issue distributions, and root-cause taxonomies. Total volumes, cost figures, and legal timelines reflect Indian banking standards.
3. **Consumer-Reported & Redacted Text:** Unstructured complaint narratives represent consumer-asserted statements with personal identifiable information (PII) pre-masked as `XXXX`.

---

## 2. Regulatory & Governance Frameworks
| Source ID | Framework / Policy | Issuing Authority | Effective Date | Key Mandates Applied |
|---|---|---|---|---|
| **REG-01** | Reserve Bank – Integrated Ombudsman Scheme (RB-IOS 2026) | Reserve Bank of India (RBI) | 1 July 2026 | 30-day resolution timeline; escalation pathways; ₹30 lakh award ceiling |
| **REG-02** | FREE-AI Committee Recommendations | Reserve Bank of India (RBI) | Aug 2025 | AI governance, fairness, accountability, transparency, ethics |
| **REG-03** | Digital Personal Data Protection Act (DPDP Act) | Government of India | 2023 / Rules 2025-26 | Purpose limitation, customer consent, mandatory PII masking, data breach reporting |
| **REG-04** | Master Direction on Credit Card and Debit Card Issuance | Reserve Bank of India (RBI) | Updated 2024-26 | Unsolicited card issuance rules, billing dispute closure timelines |

---

## 3. Technology & Cost Benchmarks
| Source ID | Component | Vendor / Source | Date | Benchmark Price |
|---|---|---|---|---|
| **TECH-01** | Claude 3.5 Sonnet / 3.7 Sonnet API Pricing | Anthropic Pricing Page | Nov 2026 | $3.00 / 1M input tokens, $15.00 / 1M output tokens (standard tier) |
| **TECH-02** | Embedding Models (`nomic-embed-text`) | Ollama / Open Source | Nov 2026 | $0.00 (Self-hosted on premise) |
| **TECH-03** | Loaded Operations Agent Cost | Indian Banking Industry Average | Nov 2026 | ₹400 / hour (Salary, EPF, seat cost, IT licensing) |
