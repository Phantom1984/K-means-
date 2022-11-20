import pandas as pd
import matplotlib.pyplot as plt
import json

tf = open("result.json", "r")
result = json.load(tf)  # result里面是处理好后的KMeans的聚类结果
tf.close()
Province = ['河北省', '山西省', '辽宁省', '吉林省', '黑龙江省',
            '江苏省', '浙江省', '安徽省', '福建省', '江西省',
            '山东省', '河南省', '湖北省', '湖南省', '广东省',
            '海南省', '四川省', '贵州省', '云南省', '陕西省',
            '甘肃省', '青海省', '台湾省', '内蒙古', '广西省',
            '西藏', '宁夏', '新疆', '北京市', '天津市',
            '上海市', '重庆市', '香港', '澳门']

for epoch in Province:
    data = pd.read_excel('省份/'+epoch+'.xlsx')
    df = pd.DataFrame(data)
    x = df['年龄'].tolist()
    y = df['家庭年收入(万)'].tolist()
    samples = list(map(list, zip(x, y)))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.scatter(x, y, c=result[epoch])
    plt.title(epoch+"聚类结果散点图")
    plt.savefig('聚类结果散点图/'+epoch+'.png')
