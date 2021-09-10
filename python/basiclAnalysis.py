import pandas as pd

classScore = pd.read_csv("../data/score_raw.csv")
des = classScore.describe()
corr = classScore.corr().applymap("{0:.2f}".format)