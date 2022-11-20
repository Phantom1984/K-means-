# 删除重复数据
import pandas as pd

data = pd.read_excel('data_processed.xlsx')
df = pd.DataFrame(data)

df = df.drop_duplicates(keep="first")
print(df)
