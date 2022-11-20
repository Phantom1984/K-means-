# 聚类
import pandas as pd
from sklearn.cluster import KMeans
import json
'''
data = pd.read_excel('省份/湖南省.xlsx')
df = pd.DataFrame(data)
'''
Province = ['河北省', '山西省', '辽宁省', '吉林省', '黑龙江省',
            '江苏省', '浙江省', '安徽省', '福建省', '江西省',
            '山东省', '河南省', '湖北省', '湖南省', '广东省',
            '海南省', '四川省', '贵州省', '云南省', '陕西省',
            '甘肃省', '青海省', '台湾省', '内蒙古', '广西省',
            '西藏', '宁夏', '新疆', '北京市', '天津市',
            '上海市', '重庆市', '香港', '澳门']
# 这是给那个坑爹的地图包用的
Province_fixed = {'河北省': '河北', '山西省': '山西', '辽宁省': '辽宁', '吉林省': '吉林', '黑龙江省': '黑龙江',
                  '江苏省': '江苏', '浙江省': '浙江', '安徽省': '安徽', '福建省': '福建', '江西省': '江西',
                  '山东省': '山东', '河南省': '河南', '湖北省': '湖北', '湖南省': '湖南', '广东省': '广东',
                  '海南省': '海南', '四川省': '四川', '贵州省': '贵州', '云南省': '云南', '陕西省': '陕西',
                  '甘肃省': '甘肃', '青海省': '青海', '台湾省': '台湾', '内蒙古': '内蒙古', '广西省': '广西',
                  '西藏': '西藏', '宁夏': '宁夏', '新疆': '新疆', '北京市': '北京', '天津市': '天津',
                  '上海市': '上海', '重庆市': '重庆', '香港': '香港', '澳门': '澳门'}
'''    
x = df['年龄'].tolist()
y = df['家庭年收入(万)'].tolist()
samples = list(map(list, zip(x, y)))
# print(result)
'''
k = 3
iteration = 500
result = {}
# 获取34个省份的聚类结果，并保存在字典中
for epoch in Province:
    data = pd.read_excel('省份/' + epoch + '.xlsx')
    df = pd.DataFrame(data)
    x = df['年龄'].tolist()
    y = df['家庭年收入(万)'].tolist()
    samples = list(map(list, zip(x, y)))
    model = KMeans(n_clusters=k, max_iter=iteration,
                   random_state=0)
    model.fit(samples)
    result[epoch] = model.labels_
# print(result)

# 按省分类，第一类、第二类、第三类
result_01 = {}
result_02 = {}
result_03 = {}
a = 0
b = 0
c = 0
for epoch in Province:
    for i in result[epoch]:
        if i == 0:
            a = a + 1
        if i == 1:
            b = b + 1
        if i == 2:
            c = c + 1
    result_01[Province_fixed[epoch]] = a
    result_02[Province_fixed[epoch]] = b
    result_03[Province_fixed[epoch]] = c
    a = 0
    b = 0
    c = 0
tf = open("result_01.json", "w")
json.dump(result_01, tf)
tf.close()

tf = open("result_02.json", "w")
json.dump(result_02, tf)
tf.close()

tf = open("result_03.json", "w")
json.dump(result_03, tf)
tf.close()
'''
print(result_01)
print(result_02)
print(result_03)
'''
# data_zs = 1.0*(data-data.mean())/data.std()  # 数据标准化

# model.labels_ 为KMeans函数的返回值，是一个列表，里面的数字代表对应数据点的类
