# Support

Need help with Churn Guard? Here's where to go.

## Start here

- 📖 **[README](README.md)** — the problem, final results, team contributions, and how to run the notebooks ([한국어](README.ko.md)).
- 🏗️ **[Architecture](wiki/Architecture.md)** & **[Roadmap](wiki/Roadmap.md)** — the data flow, data conventions, and the planned vs. actual timeline.
- 🗺️ **[Project Board](docs/PROJECT_BOARD.md)** & **[milestones](docs/milestones/)** — the original work plan and how each item ended up.

## Asking questions

- 💬 **[Discussions](https://github.com/PJH720/churn-guard/discussions)** — questions on methodology, metric choice (Recall/F1/ROC-AUC), the income join, or retention ideas. No question is too small (새싹반 friendly!).
- 🐛 **[Issues](https://github.com/PJH720/churn-guard/issues/new/choose)** — pick a structured form: Bug, Data Quality, EDA/Analysis, Modeling Experiment, Retention Idea, or Documentation.

## Common first stop

Notebook won't run? It's usually one of two things:

- **File path:** some notebooks in `examples/` use Google Colab paths. Point them at the files under `data/`.
- **Missing package:** `pyproject.toml` doesn't list every dependency yet. Run `uv pip install scikit-learn shap imbalanced-learn openpyxl` after `uv sync`.

See [CONTRIBUTING.md](CONTRIBUTING.md#local-setup) for the full setup.

## What this is not

This was a class project that ended at Demo Day (7/10). It is not a supported product. There is no SLA — responses are best-effort.
