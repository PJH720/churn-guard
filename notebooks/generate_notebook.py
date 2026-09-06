import nbformat as nbf

nb = nbf.v4.new_notebook()

code = """
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from lightgbm import LGBMClassifier
from sklearn.cluster import KMeans

# 1. 데이터 로드
DATA_PATH = '../data/telco_churn_with_income.csv'
df = pd.read_csv(DATA_PATH)
df_orig = df.copy()

# 전처리
df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce').fillna(0)

addon_cols = ['Online Security', 'Online Backup', 'Device Protection', 'Tech Support', 'Streaming TV', 'Streaming Movies']
valid_addon_cols = [c for c in addon_cols if c in df.columns]
if valid_addon_cols:
    df['Addon_Count'] = df[valid_addon_cols].apply(lambda x: (x == 'Yes').sum(), axis=1)

if 'Zip Code' in df.columns:
    df['Zip Code'] = df['Zip Code'].astype(str)
    df['Zip3'] = df['Zip Code'].str[:3]
    zip3_counts = df['Zip3'].value_counts()
    df['Zip3_Group'] = df['Zip3'].apply(lambda x: x if zip3_counts.get(x, 0) >= 50 else 'Other')

if 'City' in df.columns:
    city_counts = df['City'].value_counts()
    df['City_Group'] = df['City'].apply(lambda x: x if city_counts.get(x, 0) >= 30 else 'Other')

cluster_features = ['Tenure Months', 'Monthly Charges', 'Total Charges']
if 'Income_Charge_Ratio' in df.columns:
    cluster_features.append('Income_Charge_Ratio')

valid_cluster_features = [c for c in cluster_features if c in df.columns]
if valid_cluster_features:
    X_cluster = df.dropna(subset=valid_cluster_features)[valid_cluster_features]
    scaler = StandardScaler()
    X_cluster_scaled = scaler.fit_transform(X_cluster)
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    df.loc[X_cluster.index, 'Cluster_Label'] = kmeans.fit_predict(X_cluster_scaled)
    df['Cluster_Label'] = df['Cluster_Label'].astype(str)

INCOME_ORDER = ['Low', 'Medium', 'High', 'Very High']
if 'Area_Income_Level' in df.columns:
    df['Area_Income_Level'] = pd.Categorical(df['Area_Income_Level'], categories=INCOME_ORDER, ordered=True)

target = 'Churn Value'
num_features = ['Tenure Months', 'Monthly Charges', 'Total Charges', 'Addon_Count', 'Latitude', 'Longitude', 'Area_Median_Income', 'Area_Total_Households', 'Income_Charge_Ratio']
num_features = [c for c in num_features if c in df.columns]
cat_features = ['Gender', 'Senior Citizen', 'Partner', 'Dependents', 'Phone Service', 'Multiple Lines', 'Internet Service', 'Online Security', 'Online Backup', 'Device Protection', 'Tech Support', 'Streaming TV', 'Streaming Movies', 'Contract', 'Paperless Billing', 'Payment Method', 'City_Group', 'Zip3_Group', 'Cluster_Label']
cat_features = [c for c in cat_features if c in df.columns]
ordinal_features = ['Area_Income_Level'] if 'Area_Income_Level' in df.columns else []

all_features = num_features + cat_features + ordinal_features
analysis_idx = df.dropna(subset=all_features + [target]).index

X = df.loc[analysis_idx, all_features]
y = df.loc[analysis_idx, target]

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_features)
    ],
    remainder='drop'
)
if ordinal_features:
    preprocessor.transformers.append(
        ('ord', OrdinalEncoder(categories=[INCOME_ORDER], handle_unknown='use_encoded_value', unknown_value=-1), ordinal_features)
    )

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('smote', SMOTE(random_state=42, k_neighbors=5)),
    ('classifier', LGBMClassifier(random_state=42, verbose=-1, n_jobs=-1, learning_rate=0.05, max_depth=5, n_estimators=100))
])

# 2. 모델 학습 및 확률 예측
pipeline.fit(X, y)
churn_prob = pipeline.predict_proba(X)[:, 1]

# 3. 리텐션 전략 매핑 DataFrame 생성
customer_ids = df_orig.loc[analysis_idx, 'CustomerID']
contracts = df_orig.loc[analysis_idx, 'Contract']
internet_service = df_orig.loc[analysis_idx, 'Internet Service']
monthly_charges = df_orig.loc[analysis_idx, 'Monthly Charges']

ratio_col = 'Income_Charge_Ratio' if 'Income_Charge_Ratio' in df_orig.columns else 'City_Charge_Ratio'
if ratio_col not in df_orig.columns:
    df_orig[ratio_col] = df_orig['Monthly Charges'] / df_orig['Monthly Charges'].mean()

ratio_vals = df_orig.loc[analysis_idx, ratio_col]

result_df = pd.DataFrame({
    'CustomerID': customer_ids,
    'Contract': contracts,
    'Internet Service': internet_service,
    ratio_col: ratio_vals,
    'Monthly Charges': monthly_charges,
    'Churn_Probability': churn_prob
})

def get_retention_action(row):
    action = []
    if row['Contract'] == 'Month-to-month':
        action.append('장기 약정(1~2년) 전환 유도')
    if row['Internet Service'] == 'Fiber optic':
        action.append('결합 쿠폰 제공')
    if row[ratio_col] > 1.2:
        action.append('지역 특화 요금제 제안')
    
    if not action:
        return '기본 유지 혜택 제공'
    return ' '.join(action)

result_df['Retention_Action_Plan'] = result_df.apply(get_retention_action, axis=1)

# Churn 확률이 높은 순으로 정렬
high_risk_customers = result_df.sort_values(by='Churn_Probability', ascending=False)
high_risk_customers.head(10)
"""

cells = [
    nbf.v4.new_markdown_cell("# 🎯 고객별 리텐션 전략 매핑 (Retention Strategy Mapping)\n\n앙상블 모델의 이탈 확률(`Churn_Probability`) 예측 결과를 바탕으로, **각 고객의 계약 형태(Contract), 인터넷 서비스(Internet Service), 요금 부담률(Income_Charge_Ratio 등)**을 고려하여 맞춤형 리텐션(유지) 액션 플랜을 도출합니다."),
    nbf.v4.new_code_cell(code)
]
nb['cells'] = cells

with open('customer_retention_strategy.ipynb', 'w') as f:
    nbf.write(nb, f)
