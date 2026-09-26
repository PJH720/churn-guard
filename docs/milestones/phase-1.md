# Phase 1 — Data Understanding & Baseline

**Milestone:** [#1](https://github.com/PJH720/churn-guard/milestone/1) · **Due:** 2026-06-25 · **Feeds:** Midterm @Day (6/26)

**Status after Demo Day (7/10):** ✅ done · ⚠️ done differently · ⬜ no record. Details and evidence: [Project Board](../PROJECT_BOARD.md#final-status-after-demo-day-710).

## Goal
Load the Kaggle Telco set, understand who churns, complete preprocessing, and stand up an **interpretable Logistic Regression baseline** to benchmark against.

## Scope
EDA on churn drivers (contract, payment, charges, tenure) · `TotalCharges` cleaning · one-hot encoding · scaling · stratified split · LR baseline. Maps to bootcamp **Ch04 Logistic Regression**.

## Issues
- [#11 Data Setup and EDA](https://github.com/PJH720/churn-guard/issues/11) — `type: eda`
- [#12 Data Preprocessing & Feature Engineering](https://github.com/PJH720/churn-guard/issues/12) — `type: data`
- [#13 Baseline Modeling using Logistic Regression](https://github.com/PJH720/churn-guard/issues/13) — `type: modeling`

## Definition of Done
- ⚠️ Notebook runs locally; `telco_churn_cleaned.csv` produced → the team switched to the IBM Telco 2025 set (7,043 × 33) and shares `data/telco_churn_with_income.csv`; some `examples/` notebooks still use Colab paths.
- ✅ EDA shows churn-rate breakdowns by `Contract`, `PaymentMethod`, `InternetService`, `Tenure_Group`; ordering **Month-to-month > One year > Two year** confirmed.
- ✅ LR baseline trained with `class_weight="balanced"`; Confusion Matrix + Recall/F1/ROC-AUC reported (not Accuracy) — `examples/Telco_Customer_Churm2025_002 (1).ipynb`, recall 0.8717 at threshold 0.4.
- ⚠️ Coefficients read for interpretation; insights went into the Demo Day deck, because 6/26 became the topic vote.

## Dependencies / risks
- Class imbalance (26.5%) — use a stratified split + balanced class weights.
- Do **not** drop the 11 `tenure==0` rows; coerce `TotalCharges` to 0.
