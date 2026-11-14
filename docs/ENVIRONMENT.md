# Technical Environment Specification (ENVIRONMENT.md)

This document records the exact runtime environment, system specifications, and package versions used across the Kestrel Bank AI Transformation Blueprint.

---

## 1. System & Hardware Baseline
- **Operating System:** Windows 11 Home Single Language (Version 10.0.26300)
- **Processor (CPU):** 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
- **Graphics (GPU):** Intel(R) Iris(R) Xe Graphics (Integrated)
- **Physical Memory (RAM):** 16 GB (~16.55 GB total visible)
- **Shell / Terminal:** Windows PowerShell
- **Project Root Path:** `C:\Users\aryan\Desktop\project 1 strategy`

---

## 2. Python Runtime & Virtual Environment
- **Python Version:** 3.11.9
- **Virtual Environment Location:** `C:\Users\aryan\Desktop\project 1 strategy\.venv`
- **Activation Script:** `.venv\Scripts\Activate.ps1`
- **Package Lockfile:** `docs/requirements.lock`

### Core Installed Packages
| Package Category | Key Libraries & Versions |
|---|---|
| **Data & EDA** | `pandas==3.1.1`, `numpy==2.4.6`, `scikit-learn==1.9.1`, `scipy==1.17.1` |
| **Visualization** | `matplotlib==3.11.2`, `seaborn==0.13.2`, `plotly==7.1.0` |
| **Application & Dashboard** | `streamlit==1.67.0`, `altair==6.3.0` |
| **Excel & Reporting** | `openpyxl==3.1.5` |
| **Testing** | `pytest==9.2.0` |

---

## 3. Tooling & External Applications
- **Spreadsheets:** Microsoft Excel (Desktop with Data Table and Scenario Manager support)
- **Process Mapping:** draw.io (diagrams.net desktop/web)
- **Roadmap / Scheduling:** ProjectLibre / MS Project / Excel Gantt export
- **Presentation Deck:** Microsoft PowerPoint (16:9 layout)

---

## 4. Test Verification Baseline
- **03_A3_dashboard test suite:**
  - Command: `pytest -q 03_A3_dashboard`
  - Result: 22 passed (1.00s) on 2026-11-14.
- **01_A1_diagnostic EDA suite:**
  - Synthetic pipeline (`a1_step1_load.py` through `a1_step4_narratives.py`): Executed cleanly on 2026-11-14.
