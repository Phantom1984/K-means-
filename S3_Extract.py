# 省份提取
import openpyxl
import pandas as pd

mybook = openpyxl.load_workbook("data_footsteps.xlsx", data_only=True)
mySheet = mybook.active

data = pd.read_excel("data_processed.xlsx")
df = pd.DataFrame(data)

# 按行获取新书表的单元格（第一行除外--标题，不是数据）
myRows = list(mySheet.values)[1:]

mydics = {}
for myRow in myRows:  # 将足迹和对应ID存储在字典中
    mydics[myRow[0]] = myRow[1]

# mybook.save("结果表.xlsx")
# print(mydics)
'''
# 上海市
shanghaiID = []
for key in mydics:
    if "上海市" in mydics[key]:
        shanghaiID.append(key)
print(shanghaiID)
print(len(shanghaiID))
df = df[df['ID'].isin(shanghaiID)]
# print(df)
# df.to_excel('省份/上海市.xlsx')
'''

Province = ['河北省', '山西省', '辽宁省', '吉林省', '黑龙江省',
            '江苏省', '浙江省', '安徽省', '福建省', '江西省',
            '山东省', '河南省', '湖北省', '湖南省', '广东省',
            '海南省', '四川省', '贵州省', '云南省', '陕西省',
            '甘肃省', '青海省', '台湾省', '内蒙古', '广西省',
            '西藏', '宁夏', '新疆', '北京市', '天津市',
            '上海市', '重庆市', '香港', '澳门']
Province_ID = []
for shengfen in Province:
    for key in mydics:
        if shengfen in mydics[key]:
            Province_ID.append(key)
    df = df[df['ID'].isin(Province_ID)]
    df.to_excel('省份/'+shengfen+'.xlsx')
    Province_ID.clear()  # 清空列表
    df = pd.DataFrame(data)  # 刷新数据集
