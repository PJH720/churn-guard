# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Notebook 1 — EDA, data cleaning, and churn feature engineering
  (`customer-churn-1-eda.ipynb`), producing `telco_churn_cleaned.csv` (7043×24).
- Established data conventions: `df_clean` working copy, `Churn_Flag` target,
  `TotalCharges` coercion, `Tenure_Group`, `Risk_Factor_Count`, `churn_summary()`.
- GitHub scaffolding: structured issue forms, label taxonomy, PR template.
- Three milestones + nine phase issues (#11–#19) mirroring the class phases.
- Project docs: `README.md`, `AGENTS.md`, `docs/PROJECT_BOARD.md`,
  `docs/milestones/`, `wiki/Roadmap.md`, `wiki/Architecture.md`.
- Community/governance docs: `LICENSE` (MIT), `CONTRIBUTING.md`,
  `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, `.github/CODEOWNERS`,
  and ADR `docs/adr/0001-recall-first-evaluation.md`.

### Changed
- Stopped tracking `CLAUDE.md` (kept local; ignored so it is not shown on GitHub).

### Planned
- Notebook 2 — customer segmentation & high-risk group identification.
- Notebook 3 — Logistic Regression baseline → Random Forest / LightGBM.
- Notebook 4 — model interpretation → 3 risk factors + 3 retention actions.
- `requirements.txt` for a reproducible environment ([#2](https://github.com/PJH720/churn-guard/issues/2)).
- Fix the hardcoded Kaggle data path so notebooks run locally ([#3](https://github.com/PJH720/churn-guard/issues/3)).

[Unreleased]: https://github.com/PJH720/churn-guard/commits/main
