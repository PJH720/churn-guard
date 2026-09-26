# Contributing to Churn Guard

Thanks for your interest! Churn Guard is a 새싹반 (AI@Sogang 2기, team 2) ML mini-project. It was presented at Demo Day on 7/10, and the repo is now kept as an open-source record. Small, notebook-driven contributions are welcome. These guidelines keep the work consistent and reviewable.

## Local setup

```bash
git clone https://github.com/PJH720/churn-guard.git
cd churn-guard
uv sync
uv pip install scikit-learn shap imbalanced-learn openpyxl   # not yet in pyproject.toml (see issue #2)
```

The data is in the repo:

- `data/2025/` — IBM Telco 2025 extension (7,043 × 33), the main dataset
- `data/ACSST5Y2024.S1901_*/` — US Census ACS 2024 household income
- `data/telco_churn_with_income.csv` — the income-joined table used by `notebooks/`

> ⚠️ Some notebooks in `examples/` were written in Google Colab and still use Colab paths. To run them locally, point the paths at the files under `data/` (issue [#3](https://github.com/PJH720/churn-guard/issues/3)).

## Before you change code

Read the [README data conventions](README.md#data-conventions) and [wiki/Architecture.md](wiki/Architecture.md) first. These rules are load-bearing:

- Target is `Churn Value`. Drop `Churn Label`, `Churn Score`, and `Churn Reason` (leakage).
- `Total Charges` has 11 blanks, all at tenure 0. Fill them with 0; don't drop the rows.
- `City`, `Zip Code`, `Latitude`, and `Longitude` are join keys and EDA inputs, not model features.

## Branch strategy

- `main` is the integration branch — keep it runnable.
- Branch per unit of work using a typed prefix:
  - `feat/…` new analysis, model, or feature
  - `fix/…` bug or data-quality fix
  - `docs/…` documentation only
  - `chore/…` tooling / housekeeping
- Rebase or merge `main` before opening a PR.

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`, `perf:`. Keep messages imperative and scoped.

## Pull requests

1. Open a PR against `main` using the [PR template](.github/PULL_REQUEST_TEMPLATE.md).
2. Link the issue it closes (`Closes #NN`).
3. Apply existing labels — reuse the taxonomy (`phase: *`, `type: *`, `priority: *`); don't invent new ones.
4. If you change a number that the README reports, update the README table and say which notebook cell it came from.

## Issues

Open issues through the [structured forms](.github/ISSUE_TEMPLATE/): Bug, Data Quality, EDA/Analysis, Modeling Experiment, Retention Idea, Documentation. Not sure which? Start a [Discussion](https://github.com/PJH720/churn-guard/discussions).

## Modeling conventions

Optimize **recall first** with a precision ≥ 0.45 floor, then check F1 and ROC-AUC. Never rank models by accuracy (26.5% churn base rate). Always show a confusion matrix. See [docs/adr/0001-recall-first-evaluation.md](docs/adr/0001-recall-first-evaluation.md).

The Demo Day judges added two cautions, which new work should follow:

- Report AUC and F1 alongside recall rather than optimizing recall alone.
- Prefer class weighting (`class_weight`, `scale_pos_weight`) over SMOTE, which creates unrealistic values in encoded categorical columns.

## Data note

The IBM Telco Customer Churn data (2025 extension and the 2020 Kaggle version) is *© its original authors*. The income data comes from the US Census Bureau (ACS 2024, table S1901). The project's MIT license covers our **code, analysis, and docs**, not the datasets. Follow each source's terms before redistributing the data.
