# Phase 2 — Advanced Modeling & Evaluation

**Milestone:** [#2](https://github.com/PJH720/churn-guard/milestone/2) · **Due:** 2026-07-05 · **Starts after** Midterm @Day (6/26)

**Status after Demo Day (7/10):** ✅ done · ⚠️ done differently · ⬜ no record. Details and evidence: [Project Board](../PROJECT_BOARD.md#final-status-after-demo-day-710).

## Goal
Beat the baseline with tuned tree ensembles and **select a final model on business-aligned metrics** (catch churners → minimize Type-II error).

## Scope
Midterm feedback integration · Random Forest + LightGBM · Grid/Randomized Search + cross-validation · Recall/F1/ROC-AUC comparison across all three models. Maps to bootcamp **Ch05 Random Forest** & **Ch06 LightGBM**.

## Issues
- [#14 Midterm Feedback & Feature Refinement](https://github.com/PJH720/churn-guard/issues/14) — `type: data`, `priority: medium`
- [#15 Model Training & Hyperparameter Tuning (RF & LightGBM)](https://github.com/PJH720/churn-guard/issues/15) — `type: modeling`
- [#16 Comprehensive Model Evaluation](https://github.com/PJH720/churn-guard/issues/16) — `type: modeling`

## Definition of Done
- ⚠️ Midterm feedback → 6/26 was the topic vote. Imbalance strategy settled on class weights (`class_weight`, `scale_pos_weight`); SMOTE was tried and dropped (recall 0.66).
- ⚠️ RF + LightGBM trained; only LightGBM tuned (`GridSearchCV`); params not collected in one place.
- ⚠️ Confusion matrix, classification report, and AUC for LR vs RF vs LightGBM; ROC curves plotted only in notebook 002.
- ✅ Final model selected by **Recall on the churn class** (precision ≥ 0.45 floor): RF recall 0.893 at threshold 0.35.

## Dependencies / risks
- Requires Phase 1's `telco_churn_cleaned.csv` + finalized train/test split.
- Overfitting on trees — rely on CV + a held-out test set.
