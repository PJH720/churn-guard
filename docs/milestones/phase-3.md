# Phase 3 — Interpretation & Retention Strategy

**Milestone:** [#3](https://github.com/PJH720/churn-guard/milestone/3) · **Due:** 2026-07-08 · **Demo Day:** 7/10 (industry judges)

**Status after Demo Day (7/10):** ✅ done · ⚠️ done differently · ⬜ no record. Details and evidence: [Project Board](../PROJECT_BOARD.md#final-status-after-demo-day-710).

## Goal
Explain the final model, derive the **Top-3 churn risk factors**, convert them into **3 retention actions**, and ship the Demo Day deck + clean code.

## Scope
Feature Importance / SHAP · risk-group definition · AARRR (Retention) action plan · final deck + rehearsal.

## Issues
- [#17 Extract Feature Importance & Identify Churn Drivers](https://github.com/PJH720/churn-guard/issues/17) — `type: modeling`
- [#18 Define Risk Groups & Propose Retention Strategies](https://github.com/PJH720/churn-guard/issues/18) — `type: retention`
- [#19 Finalize PPT, Code, and Rehearsal](https://github.com/PJH720/churn-guard/issues/19) — `type: docs`, `priority: medium`

## Definition of Done
- ✅ Feature Importance / SHAP extracted and visualized; Top-3 risk factors: month-to-month contract, no dependents, short tenure.
- ✅ High-risk customer profile defined from the data: low income × month-to-month.
- ⚠️ 3 retention actions, each tied to a finding — delivered as price relief for the low-income top-25% charge burden, contract conversion (15% off, no early-termination fee), and a security / device-protection bundle, with a cost estimate (~$30K presented / ~$27K reproduced).
- ⚠️ Deck built (43 slides) and presented on 7/10; no rehearsal record.

## Dependencies / risks
- Requires Phase 2's selected final model.
- Keep strategies data-backed and practically applicable — judges reward logical traceability.
