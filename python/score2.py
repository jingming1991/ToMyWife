import pandas as pd
import scipy.stats as stats


classScore = pd.read_csv("../data/score.csv")
des = classScore.describe()
a = classScore.corr().applymap("{0:.2f}".format)
print(a)



# random_a = stats.norm.rvs(loc=3.26, scale=1.16, size=30)
# random_b = stats.norm.rvs(loc=49, scale=15.26, size=30)
# random_pearson = stats.pearsonr(random_a, random_b)

