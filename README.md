# 🛡️ Churn Guard — Customer Churn Prediction & Retention Strategy

[English](./README.md) | [한국어](./README.ko.md)

> **The Zip Code column is usually thrown away. We joined it to public income data and turned it into a way to decide *who* gets *which* retention offer.**
> AI@Sogang Cohort 2 · Sprout Track Team 2 · Demo Day 2026-07-10 · judged by industry practitioners

**Jump to:** [Results](#results) · [Team & contributions](#team--contributions) · [Notebooks](#notebooks) · [Judges' feedback](#demo-day-feedback--next-steps) · [Project board](docs/PROJECT_BOARD.md) · [Roadmap](wiki/Roadmap.md) · [Architecture](wiki/Architecture.md) · [Notion](https://royal-leaf-0a8.notion.site/2-Churn-Guard-008c77aed06e821db2668139a7a9f6fc)

---

## The problem with dropping Zip Code

Churn Guard is a binary-classification project on the **IBM Telco Customer Churn dataset, 2025 extended release**: 7,043 customers × 33 columns, with a base churn rate of **26.54%**. The 2020 Kaggle version (21 columns) was used only as an analysis reference.

Most write-ups on this data drop the `Zip Code` column. With 1,652 unique values, one-hot encoding blows up the feature space.

But a zip code says **where a customer lives and what they can afford to pay**. So instead of encoding it, this project used it as a **join key to US Census income data**.

The goal was not a leaderboard score. It was to show **why customers churn, using explainable AI (SHAP), and to propose retention actions that can actually be run**, with their cost attached.

## Results

This table shows two sets of numbers side by side: the ones presented at Demo Day (7/10), and the ones you get by re-running the notebooks committed to this repo. Where they differ, it is because the slides were built from intermediate runs.

| Item | Presented at Demo Day | Reproduced from notebooks | Source |
|---|---|---|---|
| Best baseline recall (threshold tuned, precision ≥ 0.45) | Random Forest **recall 0.893** (threshold 0.35) | Same (0.8930) | `examples/Telco_Customer_Churm2025_003 AI_Sogang_mini.ipynb` |
| Combined model (income, geo, and cluster features) | ROC-AUC 0.8356 / recall 0.8934 | ROC-AUC **0.8490** / recall **0.8761** (threshold 0.20) | `notebooks/ensemble_segmentation_churn_analysis.ipynb`, cell 14 |
| City-size-feature LightGBM | ROC-AUC 0.8645 / recall 0.80 | ROC-AUC **0.8526** / recall 0.79 | `examples/ai_sogang_project_final.ipynb` |
| Income join rate | 99.94% (1,651 of 1,652 zip codes) | Same | `notebooks/census_income_join.ipynb` |
| Charge-burden t-test (churned vs retained) | 1.08% vs 0.87%, p = 4.76e-31, t = 11.72 | Same | `notebooks/income_segmentation_churn_analysis.ipynb` |
| Low-income churn rate | 30.00% | **27.51%** | Same as above |
| Low-income + month-to-month → low-income + two-year churn | 46.75% → 7.89% | **44.41% → 1.85%** | Same as above |

> The combined-model figures on the slides (0.8356 / 0.8934) are typed directly into cell 19 of the notebook. The computed values come from cell 14.

**Top churn risk factors (SHAP top 3):** month-to-month contract, no dependents, and short tenure. Next come no online security or tech support, electronic-check payment, and fiber-optic internet.

**What the income feature actually did:** The income-relative charge burden (`Income_Charge_Ratio`) is significantly higher for churned customers. But its correlation with churn (0.15) is weaker than the raw monthly charge (0.19), and it does not appear in the SHAP top 15. So the income data earned its place **as a targeting criterion for retention offers, not as a model-accuracy boost**.

## What the data showed

**Income alone barely separates churners.** Churn by income segment is 27.5% / 26.6% / 26.7% / 26.3%, essentially flat.

![Churn rate by income segment](docs/figures/churn_rate_by_income_segment.png)

**Cross income with contract type and the picture changes.** The same customers split by contract range from **44.4% down to 1.9%** churn. Low income × month-to-month is the danger zone, and the contract is the lever.

![Churn rate heatmap: income segment × contract type](docs/figures/churn_rate_by_income_x_contract.png)

**The segment dashboard** shows churn by income segment, contract, and cluster, plus the charge-burden distribution.

![Segment analysis dashboard](docs/figures/segment_dashboard.png)

**A decision tree** checked the clusters against rules a person can read.

![Decision-tree segmentation](docs/figures/decision_tree_segmentation.png)

**Add-on services keep customers.** Customers with only one add-on churn at 45.76%; customers with all six churn at 5.28% (`examples/AI_SOGANG_PROJECT_DEMODAY(7_10).ipynb`).

## Retention strategy and costing

These are the three retention actions proposed at Demo Day:

1. **Price relief:** offer the top 25% by charge burden in the low-income segment 20% off for 3 months, or a move to a cheaper plan.
2. **Contract conversion:** offer low- and medium-income month-to-month customers 15% off plus a waived early-termination fee for moving to a 1–2 year contract.
3. **Add-on bundle:** offer high-risk customers with no add-ons a security and device-protection "peace-of-mind bundle" at $5–10 off per month.

**Costing for action 1**

| Item | Presented at Demo Day | Recomputed with the reproduced churn rate |
|---|---|---|
| Target | 1,621 low-income × top 25% ≈ 405 customers | Same |
| Marketing cost | 405 × $64.6 × 20% × 3 months = $15,697 | Same |
| Expected churners if nothing is done | 405 × 30% ≈ 121 | 405 × 27.51% ≈ 111 |
| Revenue kept (half of expected churners retained for a year) | 60 × $64.6 × 12 months = $46,512 | 55 × $64.6 × 12 months = $42,636 |
| **Net effect** | **≈ $30K per year** | **≈ $27K per year** |

The 50% retention rate is a deliberately conservative **assumption**, not a measurement.

Per-customer churn probabilities and assigned actions are in [`data/retention_action_plan.csv`](data/retention_action_plan.csv). It covers the 6,475 customers with income data.

| Action | Customers |
|---|---|
| Basic retention benefit | 2,014 |
| Long-term contract offer + bundle coupon | 1,957 |
| Long-term contract offer | 1,614 |
| Bundle coupon | 890 |

## Team & contributions

Contributions are based on the team's KakaoTalk chat log (6/22–7/8), the 7/1 meeting notes, and the files each member shared. Detailed per-member contributions and meeting notes are on the [team Notion](https://royal-leaf-0a8.notion.site/2-Churn-Guard-008c77aed06e821db2668139a7a9f6fc) (Korean).

| Name | Role | Main contributions |
|---|---|---|
| **JaeHyun Park (박재현)** | PM · data enrichment | Sourced the US Census ACS 2024 (S1901) income data and joined it by zip code / ZCTA (`data/telco_churn_with_income.csv`). Designed the income features (`Area_Median_Income`, `Income_Charge_Ratio`, `Area_Income_Level`) and ran the income- and household-based segmentation. Opened the 7/1 Zoom meeting and managed Notion and GitHub. |
| **지덕현** | Modeling | By the 7/1 midpoint meeting, clustered customers with K-Means on tenure and monthly charges and used a decision tree to find the highest-risk segment (month-to-month, fiber optic, no tech support) (7/1 meeting notes). Then built the city-size segmentation and the `City_Charge_Ratio` feature, and the optimized LightGBM (`examples/ai_sogang_project_final.ipynb`). Ran Lasso feature-selection experiments and compared SMOTE with `scale_pos_weight`: SMOTE dropped recall to 0.66, so the team adopted class weighting. Also set meeting agendas and the task split. |
| **조정헌** | Baseline · interpretation | Built the logistic-regression baseline and tuned its threshold (recall 0.8717 at 0.4). Built the decision-tree rule-based segmentation, compared 4 feature sets × LR / RF / LightGBM, and interpreted the results with SHAP and feature importance. The format of these reports (`docs/Telco_Churn_*_조정헌.docx`) became the team's standard for sharing results. |
| 최서빈 | Mentor | Gave feedback on topic selection and advice on how to collaborate. |

> The comparison table on the slides and in `ensemble_segmentation_churn_analysis.ipynb` labels the models "Jeonghyun (Geo-LGBM)" and "Duckhyun (Cluster-LR)". According to the chat log and shared files, the city-based LightGBM is 지덕현's work and the LR (recall 0.8717) is 조정헌's.

## Notebooks

The notebooks are the team members' parallel work collected in one place. They are not a single chained pipeline, so open each one on its own.

| Notebook | What it covers | Author |
|---|---|---|
| `examples/AI_SOGANG_PROJECT_DEMODAY(7_10).ipynb` | Early EDA, logistic-regression baseline, churn by number of add-ons | 지덕현 |
| `examples/Telco_Customer_Churm2025_002 (1).ipynb` | Logistic-regression baseline, threshold tuning, region-feature experiments, decision-tree segmentation | 조정헌 |
| `examples/Telco_Customer_Churm2025_003 AI_Sogang_mini.ipynb` | 4 feature sets × LR / RF / LightGBM, threshold tuning, SHAP | 조정헌 |
| `examples/ai_sogang_project_final.ipynb` | City-size segmentation, `City_Charge_Ratio`, LightGBM tuning, SHAP-based retention | 지덕현 |
| `notebooks/census_income_join.ipynb` | ACS income join by ZCTA → `data/telco_churn_with_income.csv` | JaeHyun Park |
| `notebooks/income_segmentation_churn_analysis.ipynb` | `Income_Charge_Ratio`, t-test, income segment × contract, K-Means | JaeHyun Park |
| `notebooks/ensemble_segmentation_churn_analysis.ipynb` | Combined income/geo/cluster model and comparison with members' models | Team |
| `notebooks/customer_retention_strategy.ipynb` | Per-customer churn probability → retention action. The result is saved as `data/retention_action_plan.csv` (the notebook has no export cell) | Team |

Reports: [`docs/Telco_Churn_Baseline_Report_조정헌.docx`](docs/Telco_Churn_Baseline_Report_조정헌.docx), [`docs/Telco_Churn_Project_Report_조정헌.docx`](docs/Telco_Churn_Project_Report_조정헌.docx)

## Quickstart

```bash
git clone https://github.com/PJH720/churn-guard.git
cd churn-guard
uv sync
uv pip install scikit-learn shap imbalanced-learn openpyxl
```

The raw data (`data/2025/`, `data/ACSST5Y2024.S1901_*/`) and the joined dataset (`data/telco_churn_with_income.csv`) ship with the repo.

Some notebooks under `examples/` were written in Google Colab and use Colab file paths. To run them locally, point those paths at the files under `data/`.

## Data conventions

- **Target:** `Churn Value` (1 = churned). `Churn Label`, `Churn Score`, and `Churn Reason` are only known after a customer churns, so they are **excluded as leakage**.
- **11 blank `Total Charges` values:** all belong to brand-new customers with 0 months of tenure. Fill them with 0; don't drop the rows.
- **Geography:** `City`, `Zip Code`, `Latitude`, and `Longitude` never go into a model directly. They are used for EDA and as join keys for external data.
- **Evaluation:** recall first, with a precision ≥ 0.45 floor, alongside F1 and ROC-AUC. With a 26.5% base rate, never rank models by accuracy.

## Demo Day feedback & next steps

Feedback from the two industry judges:

- **Feature engineering is the strongest part.** They encouraged extending the external-data approach, as with zip code → income.
- **Avoid SMOTE.** It produces unrealistic values for one-hot-encoded categorical features. Class weights such as `scale_pos_weight` are enough.
- **Lasso doesn't fit this problem.** The judges said its linear-regression basis doesn't suit a binary target.
- **Don't force class balance.** In practice the real-world distribution is usually kept.
- **Don't optimize recall alone.** Evaluate on overall metrics such as AUC and F1. Threshold tuning only makes sense when there is a clear risk-hedging purpose.
- **Look at feature combinations, interactions, and causality**, not just one-to-one feature–target correlation.
- **Work backwards from edge cases**, where customers look alike but only some churn.

## Limitations

- **The ≈$27K–30K figure rests on a 50% retention assumption.** An A/B test on the 405 targeted customers would replace it with a measured rate.
- **Income is joined at zip-code (ZCTA) level.** Every customer in a zip code inherits the same median income.
- **The 568 customers (8.1%) without income data are excluded from the income-based analysis**, which is why segments and actions cover 6,475 customers.
- **Correlation, not causation.** The t-test shows churned customers carry a heavier charge burden. It does not prove that lowering prices reduces churn.
- **The notebooks don't share one test split.** Members' numbers come from different preprocessing and splits, so comparisons between them are not strict.

## Project timeline

| Date | What happened |
|---|---|
| 6/22 | Team formed, mentor assigned |
| 6/26 | Four topic proposals, mentor feedback, vote |
| 6/27 | Topic chosen: customer churn prediction and retention strategy |
| 6/28 | Kickoff: roles assigned, switched to the IBM 2025 extended dataset |
| 6/29 | Preprocessing and EDA progress shared |
| 7/1 | Mid-project meeting: members shared their segmentations (income, city size, decision tree) and agreed to push each through LightGBM and compare recall |
| 7/2 | 4 feature sets with income data compared across 3 models; SHAP interpretation |
| 7/8 | Final consolidation: compared members' code, shared Lasso and SMOTE experiments, built the slides |
| **7/10** | **Demo Day**: 7-minute talk plus 5-minute Q&A, judged by practitioners |

Meeting notes are on the [team Notion](https://royal-leaf-0a8.notion.site/2-Churn-Guard-008c77aed06e821db2668139a7a9f6fc); the work plan is on the [project board](docs/PROJECT_BOARD.md).

## Repository layout

| Path | What's there |
|---|---|
| `notebooks/` | Income join, segmentation, combined model, retention actions |
| `examples/` | Members' modeling notebooks, reference notebooks |
| `data/2025/` | IBM Telco 2025 raw data (xlsx) |
| `data/ACSST5Y2024.S1901_*/` | US Census ACS 2024 household income, raw |
| `data/telco_churn_with_income.csv` | Income-joined dataset |
| `data/retention_action_plan.csv` | Per-customer retention actions |
| `docs/figures/` | Charts used in this README and the Demo Day slides |
| `docs/` | Project board, milestones, members' reports |
| `wiki/` | Roadmap, architecture |
