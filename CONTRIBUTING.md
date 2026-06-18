# Contributing to Churn Guard

Thanks for your interest! Churn Guard is a 새싹반(Sprout) 2-week ML mini-project — small, notebook-driven, and built by a class team. These guidelines keep the work consistent and reviewable.

## Local setup

```bash
git clone https://github.com/PJH720/churn-guard.git
cd churn-guard
pip install pandas numpy matplotlib      # no requirements.txt yet (see issue #2)
jupyter notebook customer-churn-1-eda.ipynb
```

> ⚠️ The EDA notebook hardcodes a Kaggle `file_path`. To run locally, point it at the repo-root CSV `WA_Fn-UseC_-Telco-Customer-Churn.csv` (issue [#3](https://github.com/PJH720/churn-guard/issues/3)).

Running notebook 1 top-to-bottom should print `Final shape: (7043, 24)` and write `telco_churn_cleaned.csv` — the handoff artifact for downstream notebooks.

## Before you change code

Read **[AGENTS.md](AGENTS.md)** and **[wiki/Architecture.md](wiki/Architecture.md)** first. The data conventions there are load-bearing: `df_clean`, `Churn_Flag`, `TotalCharges` coercion (don't drop the 11 `tenure==0` rows), `Tenure_Group`, `Risk_Factor_Count`, and the `churn_summary()` helper. Downstream notebooks read `telco_churn_cleaned.csv`, not the raw CSV.

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
2. Link the issue it closes (`Closes #NN`) and attach it to the right **milestone** (Phase 1/2/3).
3. Apply existing labels — reuse the taxonomy (`phase: *`, `type: *`, `priority: *`); don't invent new ones.
4. Make sure notebook 1 still runs clean if you touched data prep.

## Issues

Open issues through the [structured forms](.github/ISSUE_TEMPLATE/): Bug, Data Quality, EDA/Analysis, Modeling Experiment, Retention Idea, Documentation. Not sure which? Start a [Discussion](https://github.com/PJH720/churn-guard/discussions).

## Modeling conventions

Optimize **Recall first**, then F1 and ROC-AUC — never rank models by Accuracy (26.5% churn base rate). Always show a Confusion Matrix and minimize Type-II error. See [docs/adr/0001-recall-first-evaluation.md](docs/adr/0001-recall-first-evaluation.md).

## Data note

The dataset (`WA_Fn-UseC_-Telco-Customer-Churn.csv`) is IBM/Kaggle's "Telco Customer Churn" — *Data files © Original Authors*. The project's MIT license covers our **code, analysis, and docs**, not the dataset. Do not relicense or redistribute the data outside Kaggle's terms.
