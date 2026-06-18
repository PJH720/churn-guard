# Security Policy

Churn Guard is an **educational ML mini-project** — a set of Jupyter notebooks analyzing the public Kaggle Telco Customer Churn dataset. There is no deployed service, no authentication, and no production infrastructure. "Security" here mostly means **not leaking secrets and respecting data terms**.

## Supported versions

The `main` branch is the only supported version. There are no releases or backports.

## Reporting a vulnerability

Please **do not open a public issue** for anything sensitive. Instead:

- Use GitHub's [private security advisory](https://github.com/PJH720/churn-guard/security/advisories/new), **or**
- Email the maintainer at **pjhlemont@gmail.com**.

Include what you found and how to reproduce it. As a small class project, expect a best-effort response within about a week.

## In scope

- Secrets accidentally committed to the repo (API keys, tokens, credentials).
- Personally identifiable information (PII) committed beyond the dataset's own anonymized fields.
- Malicious or unsafe code in notebooks or tooling.

## Out of scope

- The dataset itself (IBM/Kaggle "Telco Customer Churn"); its `customerID` values are anonymized sample data, not real customers.
- Findings that require a deployment or service that does not exist.

## Good practices for contributors

- Never commit credentials. There is no secret needed to run this project.
- Keep generated artifacts (`telco_churn_cleaned.csv`) and local tooling state out of git — they are already in `.gitignore`.
- Do not redistribute the raw dataset outside Kaggle's terms.
