# 🛡️ Churn Guard — Customer Churn Prediction & Retention Strategy

> Predict which Telco customers are about to leave, explain **why**, and turn that into **3 concrete retention actions**.
> 새싹반(Sprout) 2-week ML mini-project · classical ML · explainability-first.

**Links:** [Milestones](https://github.com/PJH720/churn-guard/milestones) · [Project Board](docs/PROJECT_BOARD.md) · [Roadmap](wiki/Roadmap.md) · [Architecture](wiki/Architecture.md) · [Issues](https://github.com/PJH720/churn-guard/issues)

---

## What this is

Churn Guard is a **binary-classification** project on the **Kaggle IBM Telco Customer Churn** dataset (7,043 customers × 21 columns, target `Churn`, base churn rate **26.54%**). The real deliverable is business-facing: not just a model, but **3 data-driven churn risk factors + 3 retention actions** backed by model interpretation (Feature Importance / SHAP).

The emphasis is **traditional/classical ML** and **explainability over raw accuracy** — the Demo Day audience is industry judges, and the point is an *actionable retention strategy*, not a leaderboard score.

## Final results (Demo Day · 2026-07-10)

The project is complete. Headline finding: **the Zip Code column — normally dropped for high cardinality (1,652 unique values) — becomes the strongest business lever once it is joined to public income data.**

| Step | What was done | Result |
|---|---|---|
| **1. Enrich** | Joined US Census Bureau ACS 2024 (S1901) household income onto the Telco data by ZCTA | **99.94%** join rate (1,651 / 1,652 zip codes; 1 missing imputed with the median) |
| **2. Engineer** | Built `Income_Charge_Ratio` = monthly charge ÷ area median household income — the customer's *felt* telecom cost burden | New continuous feature, no dimensionality blow-up |
| **3. Test** | Independent two-sample t-test on churned vs retained customers | Churned **1.08%** vs retained **0.87%** · **p = 4.76e-31**, t = **11.72** |
| **4. Segment** | K-Means clustering + SHAP attribution across income segment × contract type | **Low-income + month-to-month churns at 46.75%** — ~2× the 26.5% base rate |
| **5. Act** | Costed a retention promotion against defended revenue | **≈ $30K net profit defended per year** |

**The retention action, costed out**

- Target: bottom-income customers in the top 25% of cost burden — **405 customers**
- Offer: 20% discount for 3 months → marketing cost **405 × $64.6 × 20% × 3 = $15,697**
- Conservative assumption: of the 121 expected churners, only **50% (60 customers)** are retained for a year → **60 × $64.6 × 12 = $46,512** revenue defended
- **Net: $46,512 − $15,697 ≈ $30K/year**
- Moving those customers to a 2-year contract drops churn from **46.75% → 7.89%** (**−38.86%p**)

Final model: LightGBM, **ROC-AUC 0.8356** — tuned toward recall, because a missed churner costs more than a wasted discount.

*Caveat: the $30K figure rests on an assumed 50% retention rate. Measuring the real rate with an A/B test is the natural next step.*

## Notebooks

Run in this order — each consumes the previous one's output.

| # | Notebook | Role |
|---|---|---|
| 1 | `examples/customer-churn-1-eda.ipynb` | EDA, cleaning, feature engineering |
| 2 | `notebooks/census_income_join.ipynb` | ACS income join by ZCTA → `data/telco_churn_with_income.csv` |
| 3 | `notebooks/income_segmentation_churn_analysis.ipynb` | `Income_Charge_Ratio` design + t-test |
| 4 | `notebooks/ensemble_segmentation_churn_analysis.ipynb` | K-Means segmentation, churn rate by segment × contract |
| 5 | `notebooks/customer_retention_strategy.ipynb` · `notebooks/(logic only) shap_retention_strategy.ipynb` | SHAP interpretation → retention actions → `data/retention_action_plan.csv` |
| — | `examples/ai_sogang_project_final.ipynb` | Demo Day presentation notebook (end-to-end) |

## Schedule

| Date | Event |
|---|---|
| **6/23 – 7/8** | Project work period |
| **6/26 (Fri)** | Midterm @Day — share problem definition, EDA insights & LR baseline; collect feedback |
| **7/10 (Fri)** | **Demo Day** — final presentation + awards (industry judges) |

## Pipeline (4-notebook design)

The original 4-notebook plan below is kept for context; the notebooks actually delivered are listed in **Notebooks** above.

| # | Notebook | Role | Status |
|---|---|---|---|
| 1 | `customer-churn-1-eda.ipynb` | EDA + cleaning + feature engineering → emits `telco_churn_cleaned.csv` | ✅ Built |
| 2 | Insights | Customer segmentation, high-risk group identification | ✅ Built |
| 3 | Modeling | Logistic Regression baseline → Random Forest / LightGBM | ✅ Built |
| 4 | Recommendations | Interpretation → 3 risk factors + 3 retention actions | ✅ Built |

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
