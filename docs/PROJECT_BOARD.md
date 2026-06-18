# Churn Guard — Project Board (Milestones & Issues)

> GitHub-ready tracking plan for the 새싹반 2-week mini-project **"Churn Guard: Customer Churn Prediction & Retention Strategy"**.
> Mirrors the live milestones/issues on [`PJH720/churn-guard`](https://github.com/PJH720/churn-guard). Created from `Ref/Making Milestones input.md`, grounded in the real Telco dataset + EDA-notebook conventions.

**Schedule** — work period **6/23 → 7/8**, Midterm @Day **6/26**, **Demo Day 7/10** (industry judges).

| Milestone | Due | Focus |
|---|---|---|
| Phase 1: Data Understanding & Baseline | 2026-06-25 | EDA · preprocessing · Logistic Regression baseline |
| Phase 2: Advanced Modeling & Evaluation | 2026-07-05 | Random Forest / LightGBM · tuning · Recall/F1/ROC-AUC |
| Phase 3: Interpretation & Retention Strategy | 2026-07-08 | Feature Importance/SHAP · 3 risk factors + 3 retention actions · Demo Day prep |

**Label map** (reuses the repo's existing taxonomy — no new labels):

| Issue | Milestone | Labels |
|---|---|---|
| #1 Data Setup & EDA | Phase 1 | `phase: 1-eda` · `type: eda` · `priority: high` |
| #2 Preprocessing & Feature Engineering | Phase 1 | `phase: 1-eda` · `type: data` · `priority: high` |
| #3 Logistic Regression Baseline | Phase 1 | `phase: 1-eda` · `type: modeling` · `priority: high` |
| #4 Midterm Feedback & Feature Refinement | Phase 2 | `phase: 3-modeling` · `type: data` · `priority: medium` |
| #5 RF & LightGBM Training + Tuning | Phase 2 | `phase: 3-modeling` · `type: modeling` · `priority: high` |
| #6 Comprehensive Model Evaluation | Phase 2 | `phase: 3-modeling` · `type: modeling` · `priority: high` |
| #7 Feature Importance & Churn Drivers | Phase 3 | `phase: 4-recommendations` · `type: modeling` · `priority: high` |
| #8 Risk Groups & Retention Strategies | Phase 3 | `phase: 4-recommendations` · `type: retention` · `priority: high` |
| #9 Final PPT, Code & Rehearsal | Phase 3 | `phase: 4-recommendations` · `type: docs` · `priority: medium` |

---

## 🚩 Milestone: Phase 1 — Data Understanding & Baseline
**Due:** 2026-06-25
Load the Kaggle Telco set, run EDA on churn drivers (contract, payment, charges, tenure), complete preprocessing, and establish an interpretable Logistic Regression baseline. Feeds the Midterm @Day (6/26).

### Issue #1 — `[Phase 1] Data Setup and EDA`
Load the Telco Churn dataset and analyze churn vs. retained customer patterns.
- [ ] Load the raw CSV from the repo root (`WA_Fn-UseC_-Telco-Customer-Churn.csv`); **fix the notebook's hardcoded Kaggle `file_path`** so it runs locally.
- [ ] Confirm shape `(7043, 21)`, target `Churn` (Yes/No), base churn rate ≈ **26.54%**; create `df_clean` and `Churn_Flag = df_clean["Churn"].map({"Yes":1,"No":0})`.
- [ ] Use the existing `churn_summary(column)` helper for churn-rate breakdowns by `Contract`, `PaymentMethod`, `InternetService`, `Tenure_Group`.
- [ ] Visualize churn vs `MonthlyCharges`, `Contract`, `PaymentMethod`, `tenure`; confirm ordering **Month-to-month > One year > Two year**.
- [ ] Document key EDA insights for the Midterm deck.

### Issue #2 — `[Phase 1] Data Preprocessing & Feature Engineering`
Prepare the raw dataset for ML: clean dirty columns, encode, scale, split.
- [ ] Clean `TotalCharges` (loads as `object`; 11 blanks all at `tenure==0`): `pd.to_numeric(..., errors="coerce").fillna(0)` — **do not drop these rows**.
- [ ] One-hot encode categoricals with `pd.get_dummies()` (`Contract`, `PaymentMethod`, `InternetService`, `OnlineSecurity`, `TechSupport`, …).
- [ ] Scale continuous features (`tenure`, `MonthlyCharges`, `TotalCharges`) with StandardScaler/MinMaxScaler.
- [ ] Stratified train/test split on `Churn_Flag` (preserves the 26.5% imbalance); confirm the `telco_churn_cleaned.csv` (7043×24) handoff is the downstream input.

### Issue #3 — `[Phase 1] Baseline Modeling using Logistic Regression`
Train an interpretable baseline and set the performance benchmark.
- [ ] Train Logistic Regression on the preprocessed train set; use `class_weight="balanced"` for the imbalance.
- [ ] Predict on test; generate a Confusion Matrix.
- [ ] Evaluate on **Recall, F1, ROC-AUC** (not Accuracy — the 26.5% base rate makes it misleading).
- [ ] Read the model coefficients to see which features raise churn probability.

---

## 🚩 Milestone: Phase 2 — Advanced Modeling & Evaluation
**Due:** 2026-07-05
Integrate Midterm feedback; train & tune Random Forest and LightGBM; compare all three models on Recall / F1 / ROC-AUC (not Accuracy); select the final model by business priority (minimize missed churners).

### Issue #4 — `[Phase 2] Midterm Feedback & Feature Refinement`
Fold in Midterm @Day feedback and prepare features for tree models.
- [ ] Document feedback from the Midterm @Day (6/26).
- [ ] Address class imbalance explicitly (`class_weight` / SMOTE) and refine features (e.g. binning, `Risk_Factor_Count`).
- [ ] Re-verify the finalized train/test split and cleaned-data handoff are ready for tree models.

### Issue #5 — `[Phase 2] Model Training & Hyperparameter Tuning (RF & LightGBM)`
Train and tune ensemble tree models to beat the baseline.
- [ ] Train a Random Forest classifier (tree-model baseline).
- [ ] Train a LightGBM classifier and compare.
- [ ] Tune both with Grid/Randomized Search + cross-validation.
- [ ] Document optimal params, training time, and CV results.

### Issue #6 — `[Phase 2] Comprehensive Model Evaluation (Confusion Matrix, F1, ROC-AUC)`
Evaluate LR, RF, LightGBM head-to-head and pick the final model.
- [ ] Confusion matrix per model; analyze Type-I vs **Type-II error (missed churners — the costly one)**.
- [ ] Classification report comparing Precision/Recall/F1 across all three models.
- [ ] ROC curve + AUC for all models.
- [ ] Select the final model by business priority (maximize Recall on the churn class).

---

## 🚩 Milestone: Phase 3 — Interpretation & Retention Strategy
**Due:** 2026-07-08 · **Demo Day 7/10**
Interpret the best model (Feature Importance / SHAP), derive the Top-3 churn risk factors, formulate 3 data-backed retention actions, and finalize code + deck for Demo Day.

### Issue #7 — `[Phase 3] Extract Feature Importance & Identify Churn Drivers`
Explain *why* customers churn using the best tree model.
- [ ] Extract Feature Importance (or SHAP values) from the final tree model.
- [ ] Visualize the top churn-driving features.
- [ ] Relate top features (`Contract`, `MonthlyCharges`, `tenure`, `InternetService=Fiber optic`) to churn probability.
- [ ] Document the **Top 3 Churn Risk Factors** clearly.

### Issue #8 — `[Phase 3] Define Risk Groups & Propose Retention Strategies`
Translate model insight into 3 actionable retention plays.
- [ ] Define the high-risk customer profile from the data.
- [ ] Propose **3 retention actions** (AARRR/Retention lens), e.g.: Month-to-month → 1-yr-contract incentive (first-month discount); no `TechSupport` → 1-month free trial; high `MonthlyCharges` (Fiber optic) → targeted bundled-discount alert.
- [ ] Tie each strategy directly to a model-interpretation finding.
- [ ] Sanity-check each action is logical and practically applicable.

### Issue #9 — `[Phase 3] Finalize PPT, Code, and Rehearsal`
Polish the repo and prepare for Demo Day.
- [ ] Clean and comment the notebooks; tidy the repo.
- [ ] Build the deck in the 5-part flow: Background → EDA → Modeling/Evaluation → Feature Importance → Action Items.
- [ ] Review against the proposal checklist (logical flow, data validation, clear actions).
- [ ] Team rehearsal for **Demo Day 7/10** (industry judges).
