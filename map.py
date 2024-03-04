from pyecharts.charts import Map
from pyecharts import options as opts

a = 0.4
b = 0.5
c = 0.6
min = 0.1
max = 3.1
"""
value = [0.776, 0.555, 0.574, 0.533, 0.756,  # 上海
         0.791,  # 江苏
         0.643,  # 浙江
         0.626,  # 福建
         0.607,  # 山东
         0.775,  # 广东
         0.8,   # 海南
         0.559,  # 吉林
         0.51,  # 黑龙江
         0.614,  # 安徽
         0.569,  # 江西
         0.583, 0.582, 0.574,  # 河南 湖北 湖南
         0.5,  # 山西
         0.765,  # 内蒙古
         0.573,  # 广西
         0.574,  # 重庆
         0.601,  # 四川
         0.512,   # 贵州
         0.533,  # 云南
         0,  # 西藏
         0.555,  # 陕西
         0.486,  # 甘肃
         0.405,  # 青海
         0.493, 0.516]
value = [0.942, 0.674, 0.68, 0.624, 0.857,  # 北京 天津  河北 辽宁 上海
         0.878,  # 江苏
         0.889,  # 浙江
         0.894,  # 福建
         0.747,  # 山东
         0.934,  # 广东
         0.964,   # 海南
         0.623,  # 吉林
         0.632,  # 黑龙江
         0.799,  # 安徽
         0.75,  # 江西
         0.768, 0.738, 0.783,  # 河南 湖北 湖南
         0.598,  # 山西
         0.909,  # 内蒙古
         0.748,  # 广西
         0.784,  # 重庆
         0.749,  # 四川
         0.695,   # 贵州
         0.749,  # 云南
         0,  # 西藏
         0.691,  # 陕西
         0.535,  # 甘肃
         0.573,  # 青海
         0.64, 0.638]
value = [0, 0, 0, 0, 0.901,  # 北京 天津  河北 辽宁 上海
         0.92,  # 江苏
         0.909,  # 浙江
         0,  # 福建
         0,  # 山东
         0,  # 广东
         0,   # 海南
         0,  # 吉林
         0,  # 黑龙江
         0.807,  # 安徽
         0.761,  # 江西
         0, 0.734, 0.783,  # 河南 湖北 湖南
         0,  # 山西
         0,  # 内蒙古
         0,  # 广西
         0.796,  # 重庆
         0.748,  # 四川
         0.683,   # 贵州
         0.74,  # 云南
         0,  # 西藏
         0,  # 陕西
         0,  # 甘肃
         0,  # 青海
         0, 0]
"""

value = [
0.110153,
0.135078,
0.144558,
0.186922,
0.202184,
0.227714,
0.507224,
0.744154,
0.45661,
0.39658,
0.582682,
0.45175,
0.528001,
0.485494,
0.252831,
0.353389,
0.464694,
0.429625,
0.426718,
0.63508,
0.521794,
0.413279,
0.662414,
0.531703,
1.300545,
0.367917,
0.572302,
2.303603,
0.536963,
3.066227,


         90]

attr = ['北京市', '天津市', '河北省', '山西省', '内蒙古自治区', '辽宁省', '吉林省', '黑龙江省',
        '上海市', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省',
        '广东省', '广西壮族自治区', '海南省', '重庆市', '四川省', '贵州省', '云南省', '陕西省', '甘肃省',
        '青海省', '宁夏回族自治区', '新疆维吾尔自治区', '西藏自治区']

pieces = [
    {'min': a, 'max': b, 'label': f'耦合协调度D值 {a}<评分≤{b}', 'color': '#FCF84D'},
    {'min': b, 'max': c, 'label': f'耦合协调度D值 {b}<评分≤{c}', 'color': '#DD675E'},
    {'min': c, 'label': f'耦合协调度D值 {c}<评分≤1.0', 'color': '#DD0200'}  # 有下限无上限
]
sequence = list(zip(attr, value))

def map_visualmap(sequence, year) -> Map:
    c = (
        Map(opts.InitOpts(width='1200px',height='600px'))               #  opts.InitOpts() 设置初始参数:width=画布宽,height=画布高
            .add(series_name=year, data_pair=sequence, maptype="china" )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))# 系列名称(显示在中间的名称 )、数据 、地图类型
            .set_global_opts(
            title_opts=opts.TitleOpts(title="地图"),
             visualmap_opts=opts.VisualMapOpts(is_piecewise=True, max_=max, min_=min, range_color=["#E0ECF8", "#045FB4"]),
            # visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=pieces),
        )
    )
    return c
map = map_visualmap(sequence, '2011全国c6')
map.render(path='./test.html')

