import pandas as pd


classScore = pd.read_csv("../data/score_raw.csv")

emotion = classScore[['Climate', 'Sensitivity', 'Respect']].mean(axis=1)
organization = classScore[['Behavior', 'Productivity', 'Instruction_Fromat']].mean(axis=1)
instruction = classScore[['Content_Understanding', 'Feedback', 'Language']].mean(axis=1)
quality = classScore[['Climate', 'Sensitivity', 'Respect','Behavior', 'Productivity', 'Instruction_Fromat','Content_Understanding', 'Feedback', 'Language']].mean(axis=1)


new_set = pd.DataFrame({'quality':quality, 'emotion':emotion,'organization':organization,'instruction':instruction,'Whole_Class':classScore['Whole_Class'],'Individual':classScore['Individual'],'Multiple':classScore['Multiple'],'Peers':classScore['Peers'],'Task':classScore['Task']})
new_set_format = new_set.applymap("{0:.2f}".format)
pearson_new_set = new_set.corr().applymap("{0:.2f}".format)
spearman_new_set = new_set.corr(method='spearman').applymap("{0:.2f}".format)

new_set_format.to_csv("../data/new_set_quality.csv", index=False)
pearson_new_set.to_csv("../data/pearson_new_set_quality.csv", index=False)
spearman_new_set.to_csv("../data/spearman_new_set_quality.csv", index=False)
