import pandas as pd
import matplotlib.pyplot as plt
import json

tf = open("result.json", "r")
result = json.load(tf)
tf.close()

data = pd.read_excel('省份/湖南省.xlsx')
df = pd.DataFrame(data)

x = df['年龄'].tolist()
y = df['家庭年收入(万)'].tolist()
samples = list(map(list, zip(x, y)))

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.scatter(x, y, c=result['湖南省'])
plt.title("湖南省聚类结果散点图")
plt.show()
# print(result)