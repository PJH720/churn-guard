# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- README (English and Korean) rewritten to the Demo Day final state: presented
  and reproduced numbers side by side, team contributions, judge feedback,
  limitations, and project timeline.
- `wiki/Roadmap.md`, `wiki/Architecture.md`, `docs/PROJECT_BOARD.md`,
  `docs/milestones/`, `CONTRIBUTING.md`, and `SUPPORT.md` updated to the 2025
  dataset and the completed project.
- `pyproject.toml` description filled in.

## [0.1.0] - 2026-09-07

Demo Day deliverables (presented 2026-07-10, AI@Sogang 2기 새싹반 team 2),
uploaded to this repository on 2026-09-07.

### Added
- IBM Telco 2025 extension dataset (7,043 × 33) under `data/2025/`, replacing
  the 2020 Kaggle set (kept for reference).
- US Census ACS 2024 (S1901) household income joined by zip code / ZCTA
  (`notebooks/census_income_join.ipynb` → `data/telco_churn_with_income.csv`).
- Income segmentation, `Income_Charge_Ratio`, t-test, and K-Means
  (`notebooks/income_segmentation_churn_analysis.ipynb`).
- Combined income / region / cluster model and member-model comparison
  (`notebooks/ensemble_segmentation_churn_analysis.ipynb`).
- Per-customer retention action mapping
  (`notebooks/customer_retention_strategy.ipynb` → `data/retention_action_plan.csv`).
- Member notebooks in `examples/`: logistic-regression baseline, threshold
  tuning, 4 feature sets × LR / RF / LightGBM, decision-tree segmentation,
  city-size segmentation with `City_Charge_Ratio`, and SHAP.
- Team reports `docs/Telco_Churn_Baseline_Report_조정헌.docx` and
  `docs/Telco_Churn_Project_Report_조정헌.docx`.
- Figures in `docs/figures/`.
- Korean README (`README.ko.md`).

### Earlier scaffolding (June 2026)
- Notebook 1 — EDA, data cleaning, and churn feature engineering on the 2020
  dataset (`examples/customer-churn-1-eda.ipynb`).
- GitHub scaffolding: structured issue forms, label taxonomy, PR template,
  three milestones, and nine phase issues (#11–#19).
- Project docs: `docs/PROJECT_BOARD.md`, `docs/milestones/`,
  `wiki/Roadmap.md`, `wiki/Architecture.md`.
- Community docs: `LICENSE` (MIT), `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`,
  `SECURITY.md`, `SUPPORT.md`, `.github/CODEOWNERS`, and ADR
  `docs/adr/0001-recall-first-evaluation.md`.

### Not done
- Full local reproducibility: some `examples/` notebooks use Colab paths, and
  `pyproject.toml` does not list scikit-learn, SHAP, imbalanced-learn, or
  openpyxl ([#2](https://github.com/PJH720/churn-guard/issues/2),
  [#3](https://github.com/PJH720/churn-guard/issues/3)).

[Unreleased]: https://github.com/PJH720/churn-guard/compare/524fa2d...main
[0.1.0]: https://github.com/PJH720/churn-guard/commit/524fa2d
