import pandas as pd

classScore = pd.read_csv("../data/score_raw.csv")
# 按照学校类型分组
score_by_school = classScore.groupby('School')
# 分组后统计均值
group_mean = score_by_school.mean()
# 分组后统计中位数
group_mid = score_by_school.median()

group_des  = score_by_school.aggregate(['mean', 'median'])