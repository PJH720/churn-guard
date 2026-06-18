# 🛡️ Churn Guard — Customer Churn Prediction & Retention Strategy

> Predict which Telco customers are about to leave, explain **why**, and turn that into **3 concrete retention actions**.
> 새싹반(Sprout) 2-week ML mini-project · classical ML · explainability-first.

**Links:** [Milestones](https://github.com/PJH720/churn-guard/milestones) · [Project Board](docs/PROJECT_BOARD.md) · [Roadmap](wiki/Roadmap.md) · [Architecture](wiki/Architecture.md) · [Issues](https://github.com/PJH720/churn-guard/issues)

---

## What this is

Churn Guard is a **binary-classification** project on the **Kaggle IBM Telco Customer Churn** dataset (7,043 customers × 21 columns, target `Churn`, base churn rate **26.54%**). The real deliverable is business-facing: not just a model, but **3 data-driven churn risk factors + 3 retention actions** backed by model interpretation (Feature Importance / SHAP).

The emphasis is **traditional/classical ML** and **explainability over raw accuracy** — the Demo Day audience is industry judges, and the point is an *actionable retention strategy*, not a leaderboard score.

## Schedule

| Date | Event |
|---|---|
| **6/23 – 7/8** | Project work period |
| **6/26 (Fri)** | Midterm @Day — share problem definition, EDA insights & LR baseline; collect feedback |
| **7/10 (Fri)** | **Demo Day** — final presentation + awards (industry judges) |

## Pipeline (4-notebook design)

The project is four sequential notebooks; each consumes the previous one's cleaned output. **Only #1 is built so far.**

| # | Notebook | Role | Status |
|---|---|---|---|
| 1 | `customer-churn-1-eda.ipynb` | EDA + cleaning + feature engineering → emits `telco_churn_cleaned.csv` | ✅ Built |
| 2 | Insights | Customer segmentation, high-risk group identification | ⬜ Planned |
| 3 | Modeling | Logistic Regression baseline → Random Forest / LightGBM | ⬜ Planned |
| 4 | Recommendations | Interpretation → 3 risk factors + 3 retention actions | ⬜ Planned |

## Quickstart

> ⚠️ **Gotcha:** the EDA notebook hardcodes a Kaggle path (`/kaggle/input/...`). To run locally, point `file_path` at the repo-root CSV `WA_Fn-UseC_-Telco-Customer-Churn.csv` (tracked in [#3](https://github.com/PJH720/churn-guard/issues/3)).

```bash
git clone https://github.com/PJH720/churn-guard.git
cd churn-guard
pip install pandas numpy matplotlib      # no requirements.txt yet — see issue #2
jupyter notebook customer-churn-1-eda.ipynb
```

Running notebook 1 top-to-bottom prints `Final shape: (7043, 24)` and writes **`telco_churn_cleaned.csv`** — the handoff artifact every downstream notebook reads (not the raw CSV).

## Data conventions (load-bearing)

Downstream notebooks must respect these, set in the EDA notebook:

- **Working copy:** all cleaning happens on `df_clean = df.copy()`, never the raw `df`.
- **Target:** `Churn_Flag = df_clean["Churn"].map({"Yes":1,"No":0})` — use `Churn_Flag` for math, keep `Churn` for labels.
- **`TotalCharges` is dirty:** loads as `object` (11 blanks, all `tenure==0` new customers) → `pd.to_numeric(..., errors="coerce").fillna(0)`. **Do not drop these rows.**
- **Derived columns:** `Tenure_Group` (`pd.cut` bins `[-1,12,24,48,72]`), `Risk_Factor_Count` (0–5 composite).
- **Helper:** `churn_summary(column)` → per-category `Customer_Count` + `Churn_Rate_%`, sorted descending. Reuse it.

## Modeling direction

- **Optimize Recall first**, then F1 and ROC-AUC. **Do not rank by Accuracy** — the 26.5% base rate makes it misleading (a missed churner costs more than retention spend).
- Sequence: **Logistic Regression** (interpretable baseline — read coefficients) → **Random Forest / LightGBM** (performance). Always show a **Confusion Matrix** and minimize Type-II error (predicting a churner as staying).

## Repository layout

| Path | Role |
|---|---|
| `customer-churn-1-eda.ipynb` | The only notebook built — EDA + cleaning + feature engineering |
| `WA_Fn-UseC_-Telco-Customer-Churn.csv` | Raw dataset (repo root) |
| `telco_churn_cleaned.csv` | **Generated** by notebook 1 — the downstream handoff (24 cols). Not yet on disk |
| `docs/PROJECT_BOARD.md` | Flat snapshot of all milestones + issues |
| `docs/milestones/` | Per-phase execution docs (goal, scope, Definition of Done) |
| `wiki/Roadmap.md`, `wiki/Architecture.md` | Timeline & technical-architecture docs |
| `CLAUDE.md`, `AGENTS.md` | Guidance for AI coding agents |
| `.github/` | Issue forms, PR template, label taxonomy |

## Project tracking

Work is organized into **3 milestones** mirroring the class phases — see the [Project Board](docs/PROJECT_BOARD.md) and [Roadmap](wiki/Roadmap.md):

1. [Phase 1: Data Understanding & Baseline](https://github.com/PJH720/churn-guard/milestone/1) (due 6/25)
2. [Phase 2: Advanced Modeling & Evaluation](https://github.com/PJH720/churn-guard/milestone/2) (due 7/5)
3. [Phase 3: Interpretation & Retention Strategy](https://github.com/PJH720/churn-guard/milestone/3) (due 7/8 · Demo Day 7/10)
