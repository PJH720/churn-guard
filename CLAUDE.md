# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

**"Churn Guard"** — a Telco customer-churn prediction + retention-strategy project built as a 2-week mini-project for a Korean data-science class (새싹반 / Sprout class). The emphasis is **traditional / classical ML** (binary classification), with model **explainability** (Feature Importance / SHAP) valued over raw accuracy, because the real deliverable is business-facing retention recommendations, not just a model.

Planning and proposal documents live in `Ref/` (Korean). The dataset is the Kaggle IBM Telco Customer Churn set: 7,043 customers × 21 columns, target column `Churn` (Yes/No), overall churn rate **26.54%**.

## Repository Layout

| Path | Role |
|---|---|
| `customer-churn-1-eda.ipynb` | **The only notebook that exists so far** — EDA + data cleaning + feature engineering. |
| `WA_Fn-UseC_-Telco-Customer-Churn.csv` | Raw dataset (repo root). |
| `telco_churn_cleaned.csv` | **Generated** by the EDA notebook's final cell — the handoff artifact for downstream notebooks (24 cols). |
| `Ref/` | Korean planning docs: project proposal, milestones, dataset metadata. |
| `.omc/`, `.remember/` | Tooling state (oh-my-claudecode / session memory). **Not project files** — ignore them. |

This is a **freshly initialized git repository** (`git init`, no commits yet) and has no `requirements.txt` / environment file. Dependencies are just `pandas`, `numpy`, `matplotlib` (no seaborn). There is no build, lint, or test setup — work happens inside Jupyter notebooks.

## Planned Architecture (4-notebook pipeline)

The project is designed as four sequential notebooks; **only #1 is built**. Each consumes the previous one's cleaned output:

1. **EDA** (`customer-churn-1-eda.ipynb`) — clean data, engineer churn features, explore patterns, emit `telco_churn_cleaned.csv`.
2. **Insights** — customer segmentation, identify high-risk groups.
3. **Modeling** — train/compare Logistic Regression → Random Forest / LightGBM.
4. **Recommendations** — interpret results, produce 3 churn risk factors + 3 retention actions.

When creating notebooks 2–4, **read `telco_churn_cleaned.csv`** (not the raw CSV) and preserve the column conventions below.

## Critical Gotcha: Data Path

The EDA notebook hardcodes a **Kaggle environment path**:
```python
file_path = "/kaggle/input/datasets/blastchar/telco-customer-churn/WA_Fn-UseC_-Telco-Customer-Churn.csv"
```
That path does **not exist locally** — the file is at the repo root (`WA_Fn-UseC_-Telco-Customer-Churn.csv`). To run the notebook locally, change `file_path` to the local CSV. Keep this in mind for any new notebook: support both, or default to the local root path.

## Established Data Conventions (load-bearing)

Downstream notebooks must respect these, set in the EDA notebook:

- **Working copy**: all cleaning happens on `df_clean = df.copy()`, never the raw `df`.
- **Target column**: `Churn_Flag` = `df_clean["Churn"].map({"Yes": 1, "No": 0})`. Use `Churn_Flag` for math; keep `Churn` for labels.
- **`TotalCharges` is dirty**: it loads as `object` (string) because 11 rows are blank — all `tenure == 0` brand-new customers. Cleaning is `pd.to_numeric(..., errors="coerce")` then `.fillna(0)`. Do not drop these rows.
- **Derived columns** already created: `Tenure_Group` (`pd.cut` bins `[-1, 12, 24, 48, 72]`), and `Risk_Factor_Count` (0–5 composite score).
- **Reusable helper**: `churn_summary(column)` returns per-category `Customer_Count` + `Churn_Rate_%`, sorted descending. Reuse it instead of re-writing groupbys.

## Modeling Direction (for the Modeling notebook)

- **Optimize Recall first**, then F1 and ROC-AUC. Do **not** rank models by Accuracy — the 26.5% churn base rate makes accuracy misleading (false negatives = missed churners cost more than retention spend).
- Sequence: **Logistic Regression** (interpretable baseline, read coefficients) → **Random Forest** / **LightGBM** (performance). Compare 2–3 models.
- Preprocessing per the plan: one-hot encode categoricals (`pd.get_dummies`), scale continuous features. Always show a **Confusion Matrix** and minimize Type II error (predicting a churner as staying).

## Reconciling the Korean Proposal vs. Reality

`Ref/플랫폼 고객 이탈 예측과 리텐션 전략 제안 (Churn Guard).md` contains **generic template language that does not match this dataset** — it references `price < 10` outlier removal and columns like `product_type`, `Quantity`, `price`. None of those exist in the Telco data (the real money columns are `MonthlyCharges` and `TotalCharges`). **Follow the actual dataset schema and the EDA notebook, not the placeholder column names in the proposal.** The proposal's strategic intent (Recall focus, LR→tree models, retention actions) is valid; its specific column names are not.

## How to Verify Work

- Run the notebook top-to-bottom in Jupyter after fixing `file_path`; confirm the final cell prints `Final shape: (7043, 24)` and writes `telco_churn_cleaned.csv`.
- Sanity checks that should hold on the cleaned data: 0 missing values, churn rate ≈ 26.54%, and churn-rate ordering Month-to-month > One year > Two year by `Contract`.
