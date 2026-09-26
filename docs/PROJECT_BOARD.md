# Churn Guard — Project Board (Milestones & Issues)

> Tracking plan for the 새싹반 (AI@Sogang 2기, team 2) mini-project **"Churn Guard: Customer Churn Prediction & Retention Strategy"**.
> Mirrors the milestones/issues on [`PJH720/churn-guard`](https://github.com/PJH720/churn-guard). The plan was written in June on the 2020 Kaggle dataset; the status below records how each item ended up at **Demo Day (7/10)**.

**Legend:** ✅ done (evidence named) · ⚠️ done differently · ⬜ no record / not done. In the summary table, the row status is the overall outcome; individual items below can still be ⚠️.

**Schedule (plan)** — work period 6/23 → 7/8, Midterm @Day 6/26, **Demo Day 7/10**.
**Schedule (actual)** — team formed 6/22, topic vote 6/26, kickoff 6/28, midpoint meeting 7/1, final merge 7/8, **Demo Day 7/10**.

## Final status (after Demo Day 7/10)

| Board # | GitHub | Issue | Status | What happened · evidence |
|---|---|---|---|---|
| #1 | [#11](https://github.com/PJH720/churn-guard/issues/11) | Data Setup & EDA | ⚠️ | Switched to the IBM Telco 2025 extension (7,043 × 33, `data/2025/`); EDA done per member |
| #2 | [#12](https://github.com/PJH720/churn-guard/issues/12) | Preprocessing & Feature Engineering | ✅ | Leakage columns dropped, scaling, stratified split; income features from the Census join (`notebooks/census_income_join.ipynb`) |
| #3 | [#13](https://github.com/PJH720/churn-guard/issues/13) | Logistic Regression Baseline | ✅ | `examples/Telco_Customer_Churm2025_002 (1).ipynb` — recall 0.8717 at threshold 0.4 |
| #4 | [#14](https://github.com/PJH720/churn-guard/issues/14) | Midterm Feedback & Feature Refinement | ⚠️ | 6/26 was a topic vote, not a baseline review; imbalance handled with class weights (SMOTE tried and dropped) |
| #5 | [#15](https://github.com/PJH720/churn-guard/issues/15) | RF & LightGBM Training + Tuning | ⚠️ | RF and LightGBM trained; only LightGBM was tuned (`GridSearchCV` in `examples/ai_sogang_project_final.ipynb` and `notebooks/ensemble_segmentation_churn_analysis.ipynb`) |
| #6 | [#16](https://github.com/PJH720/churn-guard/issues/16) | Comprehensive Model Evaluation | ✅ | Confusion matrix, classification report, ROC-AUC; RF recall 0.893 at threshold 0.35 (`examples/Telco_Customer_Churm2025_003 AI_Sogang_mini.ipynb`) |
| #7 | [#17](https://github.com/PJH720/churn-guard/issues/17) | Feature Importance & Churn Drivers | ✅ | SHAP top 3: month-to-month contract, no dependents, short tenure |
| #8 | [#18](https://github.com/PJH720/churn-guard/issues/18) | Risk Groups & Retention Strategies | ✅ | 3 actions with a cost estimate (~$30K presented / ~$27K reproduced); `data/retention_action_plan.csv` |
| #9 | [#19](https://github.com/PJH720/churn-guard/issues/19) | Final PPT, Code & Rehearsal | ⚠️ | 43-slide deck presented on 7/10 (not in the repo); no rehearsal record |

Final numbers are in the [README](../README.md#results).

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
Load the Telco set, run EDA on churn drivers (contract, payment, charges, tenure), complete preprocessing, and establish an interpretable Logistic Regression baseline.

### Issue #1 — `[Phase 1] Data Setup and EDA`
- ⚠️ Load the raw CSV and fix the hardcoded Kaggle `file_path` → the team moved to the 2025 xlsx in `data/2025/`; some `examples/` notebooks still use Colab paths.
- ⚠️ Confirm shape `(7043, 21)` and target `Churn` → 2025 set is 7,043 × 33 with target `Churn Value`; churn rate **26.54%** confirmed.
- ⚠️ Use the `churn_summary()` helper → churn-rate breakdowns were done in each member's notebook without the shared helper.
- ✅ Contract ordering **Month-to-month > One year > Two year** confirmed (income × contract heatmap, `docs/figures/churn_rate_by_income_x_contract.png`).
- ⚠️ Document EDA insights for the Midterm deck → used in the Demo Day deck instead.

### Issue #2 — `[Phase 1] Data Preprocessing & Feature Engineering`
- ✅ `Total Charges` blanks (11, all at tenure 0) filled with 0, not dropped.
- ✅ Categorical encoding and `StandardScaler` for continuous features.
- ✅ Stratified train/test split on the churn target.
- ⚠️ `telco_churn_cleaned.csv` (7043×24) handoff → replaced by `data/telco_churn_with_income.csv` after the switch to the 2025 set.

### Issue #3 — `[Phase 1] Baseline Modeling using Logistic Regression`
- ✅ Logistic Regression with `class_weight="balanced"` (`examples/Telco_Customer_Churm2025_002 (1).ipynb`).
- ✅ Confusion matrix on the test set.
- ✅ Recall, F1, ROC-AUC reported; threshold tuned (recall 0.8717 at 0.4).
- ✅ Coefficients read for interpretation.

---

## 🚩 Milestone: Phase 2 — Advanced Modeling & Evaluation
**Due:** 2026-07-05
Train & tune Random Forest and LightGBM; compare all three models on Recall / F1 / ROC-AUC; select the final model by business priority (minimize missed churners).

### Issue #4 — `[Phase 2] Midterm Feedback & Feature Refinement`
- ⚠️ Document Midterm @Day (6/26) feedback → 6/26 was topic proposals, mentor feedback, and a vote.
- ✅ Class imbalance addressed with `class_weight` / `scale_pos_weight`. SMOTE was tried and dropped (recall fell to 0.66).
- ✅ Features refined: `Risk_Factor_Count`, `Tenure_Group`, income features (`Income_Charge_Ratio`), `City_Charge_Ratio`.
- ⬜ One shared train/test split for all models → each member used their own split.

### Issue #5 — `[Phase 2] Model Training & Hyperparameter Tuning (RF & LightGBM)`
- ✅ Random Forest trained.
- ✅ LightGBM trained and compared.
- ⚠️ Grid/Randomized Search + CV → `GridSearchCV` for LightGBM only; no RF tuning found.
- ⬜ Optimal params, training time, and CV results documented in one place.

### Issue #6 — `[Phase 2] Comprehensive Model Evaluation (Confusion Matrix, F1, ROC-AUC)`
- ✅ Confusion matrix per model.
- ✅ Classification report across LR / RF / LightGBM.
- ⚠️ ROC curve + AUC for all models → AUC reported for all; ROC curves plotted only in notebook 002.
- ✅ Final model selected by recall with a precision ≥ 0.45 floor: RF recall 0.893 at threshold 0.35.

---

## 🚩 Milestone: Phase 3 — Interpretation & Retention Strategy
**Due:** 2026-07-08 · **Demo Day 7/10**
Interpret the best model, derive the Top-3 churn risk factors, formulate 3 data-backed retention actions, and finalize code + deck for Demo Day.

### Issue #7 — `[Phase 3] Extract Feature Importance & Identify Churn Drivers`
- ✅ Feature importance and SHAP extracted from the tree models.
- ✅ Top churn-driving features visualized.
- ✅ Top features related to churn probability.
- ✅ **Top 3 risk factors:** month-to-month contract, no dependents, short tenure.

### Issue #8 — `[Phase 3] Define Risk Groups & Propose Retention Strategies`
- ✅ High-risk profile: low income × month-to-month (44.41% churn reproduced; 46.75% presented).
- ⚠️ The 3 actions differ from the examples planned here. Delivered: (1) price relief for the top 25% charge burden in the low-income group, (2) contract conversion with 15% off and no early-termination fee, (3) a security / device-protection add-on bundle.
- ✅ Each action tied to a finding (charge-burden t-test, income × contract, add-on count vs. churn).
- ✅ Action 1 costed: ~$30K a year presented, ~$27K recomputed from the reproduced churn rate (assumes 50% retention).

### Issue #9 — `[Phase 3] Finalize PPT, Code, and Rehearsal`
- ⚠️ Notebooks collected into `notebooks/` and `examples/`; some still use Colab paths.
- ✅ Deck built (43 slides) and presented on 7/10.
- ⬜ Review against the proposal checklist — no record.
- ⬜ Team rehearsal — no record.
