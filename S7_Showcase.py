# 可视化
from pyecharts.charts import Map
from pyecharts import options as opts
import json

tf = open("result_01.json", "r")
result_01 = json.load(tf)
tf.close()
# print(result_01)

tf = open("result_02.json", "r")
result_02 = json.load(tf)
tf.close()
# print(result_02)

tf = open("result_03.json", "r")
result_03 = json.load(tf)
tf.close()
# print(result_03)

result_01 = list(zip(result_01.keys(), result_01.values()))
result_02 = list(zip(result_02.keys(), result_02.values()))
result_03 = list(zip(result_03.keys(), result_03.values()))


def myMap(data1, string1, data2, string2, data3, string3, x):
    map_ = Map()
    map_.add(
        series_name=string1,
        data_pair=data1,
        maptype='china',
        zoom=1
    )
    map_.add(
        series_name=string2,
        data_pair=data2,
        maptype='china',
        zoom=1
    )
    map_.add(
        series_name=string3,
        data_pair=data3,
        maptype='china',
        zoom=1
    )
    map_.set_global_opts(
        title_opts=opts.TitleOpts(
            title='旅行者足迹数据可视化展示',
            subtitle='数据来源：刘老师',
            pos_right='center',
            pos_top='5%'
        ),
        visualmap_opts=opts.VisualMapOpts(
            max_=3000,
            min_=1500,
            range_color=['#1E9600', '#FFF200', '#FF0000']
        )
    )
    map_.render('map'+x+'.html')


myMap(result_01, '第一类游客', result_02, '第二类游客', result_03, '第三类游客', '02')


# 若要绘制旅行者访问数量地图，请删除注释
'''
data_footsteps = [('北京', 5803),
                  ('天津', 5899),
                  ('河北', 5971),
                  ('山西', 5794),
                  ('内蒙古', 5753),
                  ('辽宁', 5868),
                  ('吉林', 5849),
                  ('黑龙江', 5891),
                  ('上海', 5879),
                  ('江苏', 5795),
                  ('浙江', 5883),
                  ('安徽', 5837),
                  ('福建', 5882),
                  ('江西', 5864),
                  ('山东', 5811),
                  ('河南', 5797),
                  ('湖北', 5867),
                  ('湖南', 5834),
                  ('广东', 5841),
                  ('广西', 5944),
                  ('海南', 5839),
                  ('重庆', 5818),
                  ('四川', 5873),
                  ('贵州', 5866),
                  ('云南', 5893),
                  ('西藏', 5901),
                  ('陕西', 5862),
                  ('甘肃', 5860),
                  ('青海', 5855),
                  ('宁夏', 5885),
                  ('新疆', 5856),
                  ('台湾', 5778)]
map_ = Map()
map_.add(
    series_name = '旅行者访问数量',
    data_pair = data_footsteps,
    maptype = 'china',
    zoom = 1
)
map_.set_global_opts(
    title_opts = opts.TitleOpts(
        title = '旅行者足迹数据可视化展示',
        subtitle = '数据来源：刘老师',
        pos_right = 'center',
        pos_top = '5%'
    ),
    visualmap_opts = opts.VisualMapOpts(
        max_ = 6000,  # max_ = 53617,
        min_ = 5500,  # min_ = 10990,
        range_color = ['#1E9600', '#FFF200', '#FF0000']
    )
)
map_.render('map01.html')
'''

