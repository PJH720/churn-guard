<!--
Churn Guard PR template. Fill in the summary, then work through the checklist.
Unchecked boxes are fine for WIP — just say so in the summary.
-->

## Summary

<!-- What does this PR change, and why? Which pipeline stage does it touch (EDA / Insights / Modeling / Recommendations)? -->



## Linked issue

<!-- e.g. Closes #12 -->
Closes #

## Type of change

- [ ] EDA / data cleaning
- [ ] Insights / segmentation
- [ ] Modeling experiment
- [ ] Retention strategy / recommendations
- [ ] Documentation
- [ ] Bug fix

## Notebook reproducibility checklist

- [ ] The notebook runs **top-to-bottom without errors** after fixing `file_path`.
- [ ] No Kaggle-only path (`/kaggle/input/...`) is left hardcoded without a local fallback (support both, or default to the local repo-root CSV).
- [ ] `telco_churn_cleaned.csv` regenerates, and the final cell prints **`Final shape: (7043, 24)`**.

## Data conventions checklist

- [ ] Cleaning happens on `df_clean = df.copy()` (never the raw `df`).
- [ ] Target is `Churn_Flag = df_clean["Churn"].map({"Yes": 1, "No": 0})` (used for math; `Churn` kept for labels).
- [ ] Reused the `churn_summary(column)` helper instead of re-writing groupbys where applicable.
- [ ] Derived columns (`Tenure_Group`, `Risk_Factor_Count`) follow the established bins / scoring.

## Sanity checks

- [ ] Cleaned data has **0 missing values**.
- [ ] Overall churn rate is **≈ 26.54%**.
- [ ] Churn-rate ordering holds: Month-to-month > One year > Two year (by `Contract`).
- [ ] The 11 blank `TotalCharges` rows (tenure == 0) were **filled with 0, not dropped**.

## Modeling-only (delete if N/A)

- [ ] Confusion Matrix is included.
- [ ] Type II error (churners predicted as staying) is reported.
- [ ] Models are ranked by **Recall → F1 → ROC-AUC**, NOT by Accuracy.

## Notes for reviewers

<!-- Anything reviewers should know: assumptions, follow-ups, open questions. -->
