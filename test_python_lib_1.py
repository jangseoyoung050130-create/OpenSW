import pandas as pd

mpg = pd.read_csv('mpg.csv')

mpg_new = mpg.copy()
mpg_new = mpg_new.assign(total = mpg_new['cty']+ mpg_new['hwy'])

mpg_new = mpg_new.assign(mean = mpg_new['total']/2)

print(mpg_new.sort_values('mean',ascending=False).head(3))