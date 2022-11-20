# 数据预处理
import pandas as pd

data = pd.read_excel('dataset.xlsx')
df = pd.DataFrame(data)
'''
print(data.shape)
print(data.index)
print(data.columns)
'''
age_error = df[df['年龄'].isin([0])]
df = df.drop(age_error.index)

income_error = df[df['家庭年收入(万)'].isin([0])]
df = df.drop(income_error.index)

footsteps_error = df[df['足迹'] == '[]']
df = df.drop(footsteps_error.index)

# df.to_excel('data_processed.xlsx')
# print(df)
'''
print(df[df['年龄'].isin([0])])
print(df[df['家庭年收入(万)'].isin([0])])
print(df[df['足迹'] == '[]'])
'''

