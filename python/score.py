import pandas as pd


classScore = pd.read_csv("../data/score.csv")
first_3_Column = classScore[['Positive_Climate', 'Teachers_Sensitivity', 'Regard_Student_Perspective']]
second_3_Column = classScore[['Behavior_Management', 'Productivity', 'Instruction_Learning_Format']]
third_3_Column = classScore[['Content_Understanding', 'Quality_OF_Feedback', 'Language_Development']]

mean_first = first_3_Column.mean()
emotion = "{0:.2f}".format(mean_first.mean())

mean_second = second_3_Column.mean()
organization = "{0:.2f}".format(mean_second.mean())

mean_third = third_3_Column.mean()
instruction = "{0:.2f}".format(mean_third.mean())

new_set = pd.DataFrame({'Emotion':[emotion],'Organization':[organization],'Instruction':[instruction]})
pearson_new_set = new_set.corr()
print(new_set)
print(pearson_new_set)
# detail_information_new_set = new_set.describe().applymap("{0:.2f}".format)
# pearson_new_set =
# kendall_new_set = new_set.corr(method='kendall').applymap("{0:.2f}".format)
# spearman_new_set = new_set.corr(method='spearman').applymap("{0:.2f}".format)



#
# print(classScore)
# des = classScore.describe()
#
# diff = classScore.corr()
# print(des)
# print(diff)




