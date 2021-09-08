import pandas as pd


classScore = pd.read_csv("../data/score.csv")
first_3_Column = classScore[['Positive_Climate', 'Teachers_Sensitivity', 'Regard_Student_Perspective']]
second_3_Column = classScore[['Behavior_Management', 'Productivity', 'Instruction_Learning_Format']]
third_3_Column = classScore[['Content_Understanding', 'Quality_OF_Feedback', 'Language_Development']]

mean_first = first_3_Column.mean(axis=1)
mean_second = second_3_Column.mean(axis=1)
mean_third = third_3_Column.mean(axis=1)

new_set = pd.DataFrame({'first':mean_first,'second':mean_second,'third':mean_third,'TSs':classScore['TSs'],'TU':classScore['TU'],'SL':classScore['SL'],'SS':classScore['SS'],'CX':classScore['CX'],'School':classScore['School']})
detail_information_new_set = new_set.describe().applymap("{0:.2f}".format)
pearson_new_set = new_set.corr().applymap("{0:.2f}".format)
kendall_new_set = new_set.corr(method='kendall').applymap("{0:.2f}".format)
spearman_new_set = new_set.corr(method='spearman').applymap("{0:.2f}".format)





