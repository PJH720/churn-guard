import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 2025 Telco Customer Churn 데이터셋 로드
real_filename = '../data/Telco-Customer-Churn2025.csv'
df = pd.read_csv(real_filename)
print('Dataset loaded successfully. Shape:', df.shape)
