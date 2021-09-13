import pandas as pd


classScore = pd.read_csv("../data/score_raw.csv")
first_3_Column = classScore[['Climate', 'Sensitivity', 'Respect']]
second_3_Column = classScore[['Behavior', 'Productivity', 'Instruction_Fromat']]
third_3_Column = classScore[['Content_Understanding', 'Feedback', 'Language']]

emotion = first_3_Column.mean(axis=1)
organization = second_3_Column.mean(axis=1)
instruction = third_3_Column.mean(axis=1)

# ,'TSs':classScore['TSs']
new_set = pd.DataFrame({'emotion':emotion,'organization':organization,'instruction':instruction,'School':classScore['School']})
new_set_format = new_set.applymap("{0:.2f}".format)

new_set_format.to_csv("../data/a.csv", index=False)





# detail_information_new_set = new_set.describe().applymap("{0:.2f}".format)
# pearson_new_set = new_set.corr().applymap("{0:.2f}".format)
# kendall_new_set = new_set.corr(method='kendall').applymap("{0:.2f}".format)
# spearman_new_set = new_set.corr(method='spearman').applymap("{0:.2f}".format)





# 1. Table. 1要把教师指导活动和学生指导活动占的时间加总一下（whole class+individual两部分求和，Peers 和task求和），加上multiple总共三部分，求这三部分和classroom quality 的关系，
# 先求跟emotion，organization以及instruction关系，再求各个变量之间关系。emotion就是climate，sensitivity，respect三个变量的平均值，organization是productivity，bahavior，instruction format平均值以及instruction是反馈，content和language三个变量的均值。
# 2.加个变量—-学校类型—对教师指导活动，和学生指导活动，multiple 三种类型的影响。以及学校类型和emotion，organization以及instruction的相关性
# 3. 算下Cronbach’s alpha系数