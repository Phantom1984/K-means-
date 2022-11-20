# 统计各省份访问人数
import pandas as pd

# 统计各省份访问人数
Province = ['河北省', '山西省', '辽宁省', '吉林省', '黑龙江省',
            '江苏省', '浙江省', '安徽省', '福建省', '江西省',
            '山东省', '河南省', '湖北省', '湖南省', '广东省',
            '海南省', '四川省', '贵州省', '云南省', '陕西省',
            '甘肃省', '青海省', '台湾省', '内蒙古', '广西省',
            '西藏', '宁夏', '新疆', '北京市', '天津市',
            '上海市', '重庆市', '香港', '澳门']
dic = {}
for epoch in Province:
    data = pd.read_excel('省份/'+epoch+'.xlsx')
    df = pd.DataFrame(data)
    dic.update({epoch: len(df)})
# print(dic)
result = pd.DataFrame(dic, index=[0])
result.to_excel('各省访客人数.xlsx')
# print(dic['上海市'])

