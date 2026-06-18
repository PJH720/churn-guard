# Phase 1 — Data Understanding & Baseline

**Milestone:** [#1](https://github.com/PJH720/churn-guard/milestone/1) · **Due:** 2026-06-25 · **Feeds:** Midterm @Day (6/26)

## Goal
Load the Kaggle Telco set, understand who churns, complete preprocessing, and stand up an **interpretable Logistic Regression baseline** to benchmark against.

## Scope
EDA on churn drivers (contract, payment, charges, tenure) · `TotalCharges` cleaning · one-hot encoding · scaling · stratified split · LR baseline. Maps to bootcamp **Ch04 Logistic Regression**.

## Issues
- [#11 Data Setup and EDA](https://github.com/PJH720/churn-guard/issues/11) — `type: eda`
- [#12 Data Preprocessing & Feature Engineering](https://github.com/PJH720/churn-guard/issues/12) — `type: data`
- [#13 Baseline Modeling using Logistic Regression](https://github.com/PJH720/churn-guard/issues/13) — `type: modeling`

## Definition of Done
- [ ] Notebook runs locally (Kaggle `file_path` fixed); `telco_churn_cleaned.csv` (7043×24) produced.
- [ ] EDA shows churn-rate breakdowns by `Contract`, `PaymentMethod`, `InternetService`, `Tenure_Group`; ordering **Month-to-month > One year > Two year** confirmed.
- [ ] LR baseline trained with `class_weight="balanced"`; Confusion Matrix + Recall/F1/ROC-AUC reported (not Accuracy).
- [ ] Coefficients read for interpretation; key insights captured for the Midterm deck.

## Dependencies / risks
- Class imbalance (26.5%) — use a stratified split + balanced class weights.
- Do **not** drop the 11 `tenure==0` rows; coerce `TotalCharges` to 0.
