import pandas as pd
import numpy as np

def cronbach_alpha(df):
    # 1. Transform the df into a correlation matrix
    df_corr = df.corr()

    # 2.1 Calculate N
    # The number of variables equals the number of columns in the df
    N = df.shape[1]

    # 2.2 Calculate R
    # For this, we'll loop through the columns and append every
    # relevant correlation to an array calles "r_s". Then, we'll
    # calculate the mean of "r_s"
    rs = np.array([])
    for i, col in enumerate(df_corr.columns):
        sum_ = df_corr[col][i+1:].values
        rs = np.append(sum_, rs)
    mean_r = np.mean(rs)

    # 3. Use the formula to calculate Cronbach's Alpha
    cronbach_alpha = (N * mean_r) / (1 + (N - 1) * mean_r)
    return cronbach_alpha

classScore = pd.read_csv("../data/score_raw.csv")
cronbach_alpha_value = cronbach_alpha(classScore)
print(cronbach_alpha_value )

# 一般探索性研究，Cranbach's a系数在0.6以上，基准研究在0.8以上，通常情况下Cranbach's a系数在0.6以上，被认为可信度较高






