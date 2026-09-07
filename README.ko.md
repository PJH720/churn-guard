# 🛡️ Churn Guard — 고객 이탈 예측과 리텐션 전략

[English](./README.md) | [한국어](./README.ko.md)

> **우편번호는 보통 버려지는 변수입니다. 이 프로젝트는 우편번호를 공공 소득 데이터와 결합해 연 약 $30K의 순이익 방어로 바꿨습니다.**
> AI@Sogang 새싹반 2기 · 2026-07-10 데모데이 · 현직자 심사

**바로가기:** [노트북](#노트북) · [프로젝트 보드](docs/PROJECT_BOARD.md) · [로드맵](wiki/Roadmap.md) · [아키텍처](wiki/Architecture.md) · [마일스톤](https://github.com/PJH720/churn-guard/milestones)

---

## 우편번호를 버리면 생기는 문제

Churn Guard는 **IBM Telco 고객 이탈 데이터셋**(고객 7,043명 × 21개 컬럼, 기본 이탈률 **26.54%**)을 다루는 이진 분류 프로젝트입니다. 이 데이터셋을 다루는 대부분의 자료는 `Zip Code` 컬럼을 버립니다. 고유값이 1,652개나 되어 원-핫 인코딩하면 차원이 폭발하기 때문입니다.

하지만 우편번호는 잡음이 아닙니다. **고객이 어디에 살고 어느 정도의 지불 여력을 갖는지**를 대변하는 단서입니다. 그래서 이 프로젝트는 우편번호를 인코딩 대상이 아니라 **공공 소득 데이터와 이어붙이는 결합 키**로 사용했고, 그렇게 만들어진 변수는 요금 액수 자체보다 이탈을 더 잘 설명했습니다.

목표는 리더보드 점수가 아니었습니다. **관리자가 월요일에 바로 승인할 수 있는 위험 요인 3개와 리텐션 액션 3개**를, 비용과 방어 매출을 붙여서 제시하는 것이었습니다.

## 최종 결과

| 단계 | 수행 내용 | 결과 |
|---|---|---|
| **1. 결합** | 미 인구통계국 ACS 2024(S1901) 지역 중위 가구소득을 ZCTA(우편번호) 기준으로 결합 | 결합 성공률 **99.94%** (1,652개 중 1,651개, 결측 1건은 중위값 대체) |
| **2. 변수 설계** | `Income_Charge_Ratio` = 월 통신요금 ÷ 지역 중위 가구소득 — 고객이 **체감하는** 통신비 부담률 | 연속형 변수라 차원 폭발 없음 |
| **3. 검정** | 이탈 고객군과 유지 고객군에 대한 독립표본 T-검정 | 이탈 **1.08%** vs 유지 **0.87%** · **p = 4.76e-31**, t = **11.72** |
| **4. 세분화** | 소득 구간 × 약정 유형 기준 K-Means 군집화 및 SHAP 기여도 분석 | **저소득 + 무약정 고객군 이탈률 46.75%** — 기본 이탈률(26.5%)의 약 2배 |
| **5. 실행** | 리텐션 프로모션 비용과 방어 매출을 대조해 손익 산출 | **연 약 $30K 순이익 방어** |

최종 모델은 **LightGBM, ROC-AUC 0.8356**이며 재현율(recall) 중심으로 튜닝했습니다. 이탈 고객을 놓치는 비용이 할인 쿠폰 한 장보다 크기 때문입니다.

## 데이터가 보여준 것

**소득만으로는 이탈이 거의 갈리지 않습니다.** 소득 구간별 이탈률은 27.5% / 26.6% / 26.7% / 26.3%로 사실상 평평합니다. 여기서 멈추면 우편번호는 쓸모없어 보입니다.

![소득 구간별 이탈률](docs/figures/churn_rate_by_income_segment.png)

**소득을 약정 유형과 교차하면 이야기가 완전히 달라집니다.** 같은 고객을 약정 형태로 나누자 이탈률이 **44.4%에서 1.9%까지** 벌어졌습니다. 저소득 × 무약정이 위험 구간이고, 약정이 곧 지렛대입니다.

![소득 구간 × 약정 유형별 이탈률 히트맵](docs/figures/churn_rate_by_income_x_contract.png)

**세그먼트 종합 대시보드** — 소득 구간별·약정별·군집별 이탈률과, 이탈 고객 대비 유지 고객의 통신비 부담률 분포입니다.

![세그먼트 분석 대시보드](docs/figures/segment_dashboard.png)

**실제로 갈라지는 지점** — 소득·비용 변수 기반 의사결정나무로, 군집 결과를 사람이 읽을 수 있는 규칙과 대조해 검증했습니다.

![의사결정나무 세그멘테이션](docs/figures/decision_tree_segmentation.png)

## 리텐션 액션과 손익 계산

- **타겟:** 저소득군 중 통신비 부담률 상위 25% — **405명**
- **제안:** 3개월간 20% 요금 할인 → 마케팅 비용 **405명 × $64.6 × 20% × 3개월 = $15,697**
- **보수적 가정:** 이탈 예정자 121명 중 **50%(60명)** 만 1년간 유지 → **60명 × $64.6 × 12개월 = $46,512** 매출 방어
- **순효과:** $46,512 − $15,697 ≈ **연 $30K**
- **추가 효과:** 해당 고객을 2년 약정으로 전환하면 이탈률이 **46.75% → 7.89%** (**−38.86%p**)

개별 고객 단위의 이탈 위험도와 그에 맞는 제안을 보여주는 화면입니다.

![고객 이탈 예측 화면](docs/score.png)

## 노트북

각 노트북은 이전 단계의 산출물을 입력으로 받습니다. 순서대로 실행하십시오.

| # | 노트북 | 역할 |
|---|---|---|
| 1 | `examples/customer-churn-1-eda.ipynb` | EDA, 데이터 정제, 변수 생성 |
| 2 | `notebooks/census_income_join.ipynb` | ACS 소득 데이터 ZCTA 결합 → `data/telco_churn_with_income.csv` |
| 3 | `notebooks/income_segmentation_churn_analysis.ipynb` | `Income_Charge_Ratio` 설계 및 T-검정 |
| 4 | `notebooks/ensemble_segmentation_churn_analysis.ipynb` | K-Means 군집화, 세그먼트 × 약정별 이탈률 분석 |
| 5 | `notebooks/customer_retention_strategy.ipynb`<br>`notebooks/(logic only) shap_retention_strategy.ipynb` | SHAP 해석 → 리텐션 액션 → `data/retention_action_plan.csv` |
| — | `examples/ai_sogang_project_final.ipynb` | 데모데이 발표용 통합 노트북 |

## 실행 방법

```bash
git clone https://github.com/PJH720/churn-guard.git
cd churn-guard
uv sync                      # 또는: pip install pandas numpy matplotlib seaborn lightgbm ipykernel
jupyter notebook notebooks/census_income_join.ipynb
```

원본 데이터(`data/2025/`, `data/ACSST5Y2024.S1901_*/`)가 저장소에 함께 들어 있어 별도 다운로드 없이 실행됩니다.

## 데이터 규약 (반드시 지킬 것)

EDA 노트북에서 정해진 규약이며, 이후 노트북이 모두 이에 의존합니다.

- **작업 사본:** 모든 정제는 `df_clean = df.copy()` 위에서 수행하고 원본 `df`는 건드리지 않습니다.
- **타깃:** `Churn_Flag = df_clean["Churn"].map({"Yes":1,"No":0})` — 연산에는 `Churn_Flag`, 라벨 표시에는 `Churn`을 사용합니다.
- **`TotalCharges`는 더럽습니다:** `object`로 로드되며 공백 11건(모두 `tenure == 0`인 신규 고객)이 있습니다 → `pd.to_numeric(..., errors="coerce").fillna(0)`. **해당 행을 삭제하지 마십시오.**
- **파생 컬럼:** `Tenure_Group`(`pd.cut` 구간 `[-1,12,24,48,72]`), `Risk_Factor_Count`(0–5 복합 지표), `Income_Charge_Ratio`.
- **헬퍼:** `churn_summary(column)` → 범주별 `Customer_Count`와 `Churn_Rate_%`를 내림차순으로 반환합니다. 새로 만들지 말고 재사용하십시오.
- **평가 기준:** **재현율(Recall) 우선**, 다음으로 F1과 ROC-AUC. **정확도(Accuracy)로 순위를 매기지 마십시오** — 기본 이탈률이 26.5%라 오해를 부릅니다.

## 저장소 구조

| 경로 | 역할 |
|---|---|
| `notebooks/` | 분석 파이프라인 (소득 결합 → 세분화 → 리텐션 전략) |
| `examples/` | EDA 노트북, 데모데이 노트북, 참고 노트북 |
| `data/2025/` | IBM Telco 원본 데이터 (xlsx) |
| `data/ACSST5Y2024.S1901_*/` | 미 인구통계국 ACS 2024 가구소득 원본 데이터 |
| `data/telco_churn_with_income.csv` | 결합 산출물 — 이후 노트북이 읽는 인계 파일 |
| `data/retention_action_plan.csv` | 고객별 최종 리텐션 타겟팅 결과 |
| `docs/figures/` | 이 README와 데모데이 발표에 사용한 분석 그래프 |
| `docs/PROJECT_BOARD.md`, `docs/milestones/` | 마일스톤 및 이슈 관리 문서 |
| `wiki/Roadmap.md`, `wiki/Architecture.md` | 일정 및 기술 아키텍처 문서 |

## 한계와 다음 단계

- **$30K는 방어율 50%라는 가정 위에 있습니다.** 의도적으로 보수적으로 잡은 계획 수치일 뿐 측정값이 아닙니다. 타겟 405명을 대상으로 A/B 테스트를 돌리면 가정을 실제 방어율로 대체할 수 있습니다.
- **소득 결합은 ZCTA(우편번호) 단위입니다.** 같은 우편번호의 고객은 모두 같은 중위소득을 물려받으므로 우편번호 내부의 소득 편차가 반영되지 않습니다. 가구 단위 소득이 있다면 부담률 지표가 훨씬 정밀해집니다.
- **인과가 아니라 상관입니다.** T-검정은 이탈 고객의 통신비 부담이 더 무겁다는 사실을 보여줄 뿐, 요금을 낮추면 이탈이 줄어든다는 것을 증명하지는 않습니다. 그것은 위의 실험으로만 확인할 수 있습니다.

## 프로젝트 진행 맥락

| 일자 | 내용 |
|---|---|
| 6/23 – 7/8 | 프로젝트 진행 기간 |
| 6/26 | 중간 점검 — 문제 정의, EDA 인사이트, 로지스틱 회귀 베이스라인 공유 |
| **7/10** | **데모데이** — 최종 발표 및 현직자 심사 |

수업 단계에 맞춰 3개 마일스톤으로 작업을 나누어 진행했습니다. [프로젝트 보드](docs/PROJECT_BOARD.md)와 [로드맵](wiki/Roadmap.md)을 참고하십시오.
