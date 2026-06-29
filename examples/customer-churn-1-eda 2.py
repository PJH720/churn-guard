# =============================================================================
# Customer Churn: EDA
# =============================================================================
# This script is part of a multi-notebook customer churn project.
#
# The goal is to clean the Telco Customer Churn dataset and explore the major
# patterns associated with churn. The cleaned dataset produced here is used by
# the later insights, modeling, and recommendations notebooks.
#
# Project Notebooks:
#   1. Customer Churn: EDA          - Clean, feature-engineer, explore patterns
#   2. Customer Churn: Insights     - Build segments, identify high-risk groups
#   3. Customer Churn: Modeling     - Train ML models to predict churn
#   4. Customer Churn: Recommendations - Turn findings into retention actions
#
# Notebook Goals:
#   - Load the raw Telco Customer Churn dataset
#   - Clean data quality issues, including TotalCharges
#   - Create churn-related helper columns
#   - Explore major churn patterns across customer, service, contract, billing
#   - Save a cleaned dataset for the later notebooks
# =============================================================================
# %%
import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

# %%
# -----------------------------------------------------------------------------
# File discovery (Kaggle environment)
# -----------------------------------------------------------------------------
for dirname, _, filenames in os.walk("/kaggle/input"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# %%
# -----------------------------------------------------------------------------
# Load raw data
# -----------------------------------------------------------------------------
data_filename = "WA_Fn-UseC_-Telco-Customer-Churn.csv"

try:
    base_dir = Path(__file__).resolve().parent
except NameError:
    base_dir = Path.cwd()

candidate_paths = [
    Path.cwd() / data_filename,
    base_dir / data_filename,
    base_dir / "Data" / data_filename,
    base_dir.parent / "churn-guard" / data_filename,
    base_dir.parent
    / "telco-customer-churn-on-icp4d-master (2020)"
    / "data"
    / "Telco-Customer-Churn.csv",
]

for candidate_path in candidate_paths:
    if candidate_path.exists():
        file_path = candidate_path
        break
else:
    searched_paths = "\n".join(f"- {path}" for path in candidate_paths)
    raise FileNotFoundError(
        f"Could not find {data_filename}. Searched these paths:\n{searched_paths}"
    )

df = pd.read_csv(file_path)

print("Loaded raw data from:", file_path)
print("Shape:", df.shape)
print(df.head())

# %%
# -----------------------------------------------------------------------------
# Initial inspection
# -----------------------------------------------------------------------------
df.info()
print(df.describe(include="all").T)
print(df.isna().sum())

# %%
# -----------------------------------------------------------------------------
# Data Cleaning: fix TotalCharges (stored as object, should be numeric)
# -----------------------------------------------------------------------------
df_clean = df.copy()

df_clean["TotalCharges"] = pd.to_numeric(df_clean["TotalCharges"], errors="coerce")

print("Missing values after converting TotalCharges:")
print(df_clean.isna().sum()[df_clean.isna().sum() > 0])

# Inspect rows where TotalCharges became NaN (tenure == 0, no charges yet)
print(df_clean[df_clean["TotalCharges"].isna()])

# Fill NaN TotalCharges with 0 (new customers with no charges yet)
df_clean["TotalCharges"] = df_clean["TotalCharges"].fillna(0)

print("Remaining missing values:", df_clean.isna().sum().sum())

# %%
# =============================================================================
# Exploratory Data Analysis
# =============================================================================
# The first goal is to understand the overall churn rate and how churn differs
# across customer groups.

# --- Churn flag (numeric) ---
df_clean["Churn_Flag"] = df_clean["Churn"].map({"Yes": 1, "No": 0})
print(df_clean[["Churn", "Churn_Flag"]].head())

churn_counts = df_clean["Churn"].value_counts()
churn_rate = df_clean["Churn_Flag"].mean()

print(churn_counts)
print(f"\nOverall churn rate: {churn_rate:.2%}")

# %%
# Plot overall churn counts
churn_counts.plot(kind="bar")
plt.title("Customer Churn Counts")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.show()

# %%
# --- Churn by Contract Type ---
contract_churn = (
    df_clean.groupby("Contract")["Churn_Flag"]
    .agg(Customer_Count="count", Churn_Rate="mean")
    .sort_values("Churn_Rate", ascending=False)
)
contract_churn["Churn_Rate_%"] = contract_churn["Churn_Rate"] * 100
print(contract_churn[["Customer_Count", "Churn_Rate_%"]])

contract_churn["Churn_Rate_%"].plot(kind="bar")
plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=45)
plt.show()

# %%
# =============================================================================
# Churn by Tenure
# =============================================================================
# Newer customers tend to be more likely to churn than long-term customers.

df_clean["Tenure_Group"] = pd.cut(
    df_clean["tenure"],
    bins=[-1, 12, 24, 48, 72],
    labels=["0-12 months", "13-24 months", "25-48 months", "49-72 months"],
)

tenure_churn = df_clean.groupby("Tenure_Group", observed=False)["Churn_Flag"].agg(
    Customer_Count="count", Churn_Rate="mean"
)
tenure_churn["Churn_Rate_%"] = tenure_churn["Churn_Rate"] * 100
print(tenure_churn[["Customer_Count", "Churn_Rate_%"]])

tenure_churn["Churn_Rate_%"].plot(kind="bar")
plt.title("Churn Rate by Tenure Group")
plt.xlabel("Tenure Group")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=45)
plt.show()

# %%
# =============================================================================
# Churn by Monthly Charges
# =============================================================================
# Check whether customers with higher monthly charges are more likely to churn.

print(df_clean.groupby("Churn")["MonthlyCharges"].describe())

df_clean.boxplot(column="MonthlyCharges", by="Churn")
plt.title("Monthly Charges by Churn Status")
plt.suptitle("")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.show()

# %%
# --- Churn by Internet Service ---
internet_churn = (
    df_clean.groupby("InternetService")["Churn_Flag"]
    .agg(Customer_Count="count", Churn_Rate="mean")
    .sort_values("Churn_Rate", ascending=False)
)
internet_churn["Churn_Rate_%"] = internet_churn["Churn_Rate"] * 100
print(internet_churn[["Customer_Count", "Churn_Rate_%"]])

internet_churn["Churn_Rate_%"].plot(kind="bar")
plt.title("Churn Rate by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=45)
plt.show()

# %%
# --- Churn by Payment Method ---
payment_churn = (
    df_clean.groupby("PaymentMethod")["Churn_Flag"]
    .agg(Customer_Count="count", Churn_Rate="mean")
    .sort_values("Churn_Rate", ascending=False)
)
payment_churn["Churn_Rate_%"] = payment_churn["Churn_Rate"] * 100
print(payment_churn[["Customer_Count", "Churn_Rate_%"]])

payment_churn["Churn_Rate_%"].plot(kind="bar")
plt.title("Churn Rate by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=45, ha="right")
plt.show()

# %%
# =============================================================================
# Service Feature Analysis
# =============================================================================
# Helper to quickly summarise churn rate for any categorical column.


def churn_summary(column):
    summary = (
        df_clean.groupby(column)["Churn_Flag"]
        .agg(Customer_Count="count", Churn_Rate="mean")
        .sort_values("Churn_Rate", ascending=False)
    )
    summary["Churn_Rate_%"] = summary["Churn_Rate"] * 100
    return summary[["Customer_Count", "Churn_Rate_%"]]


print(churn_summary("OnlineSecurity"))
print(churn_summary("TechSupport"))
print(churn_summary("OnlineBackup"))
print(churn_summary("DeviceProtection"))
print(churn_summary("PaperlessBilling"))

# %%
# =============================================================================
# Risk Factor Analysis
# =============================================================================
# A simple additive risk score using five churn-related conditions:
#   1. Month-to-month contract
#   2. Tenure <= 12 months
#   3. Fiber optic internet service
#   4. Electronic check payment method
#   5. Monthly charges above the median

df_clean["Risk_Factor_Count"] = 0

df_clean["Risk_Factor_Count"] += (df_clean["Contract"] == "Month-to-month").astype(int)
df_clean["Risk_Factor_Count"] += (df_clean["tenure"] <= 12).astype(int)
df_clean["Risk_Factor_Count"] += (df_clean["InternetService"] == "Fiber optic").astype(
    int
)
df_clean["Risk_Factor_Count"] += (
    df_clean["PaymentMethod"] == "Electronic check"
).astype(int)
df_clean["Risk_Factor_Count"] += (
    df_clean["MonthlyCharges"] > df_clean["MonthlyCharges"].median()
).astype(int)

risk_churn = df_clean.groupby("Risk_Factor_Count")["Churn_Flag"].agg(
    Customer_Count="count", Churn_Rate="mean"
)
risk_churn["Churn_Rate_%"] = risk_churn["Churn_Rate"] * 100
print(risk_churn[["Customer_Count", "Churn_Rate_%"]])

risk_churn["Churn_Rate_%"].plot(kind="bar")
plt.title("Churn Rate by Number of Risk Factors")
plt.xlabel("Number of Risk Factors")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.show()

# %%
# =============================================================================
# Save Cleaned Dataset
# =============================================================================
df_clean.to_csv("telco_churn_cleaned.csv", index=False)

print("Cleaned dataset saved as telco_churn_cleaned.csv")
print("Final shape:", df_clean.shape)
