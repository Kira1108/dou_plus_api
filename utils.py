import json

def _make_citymap():
    with open('./extras/city.txt','r', encoding = 'GBK') as f:
        content = f.read()
        citymap = {}
    for k,v in json.loads(content).items():
        for c in v:
            citymap[c] = k
    return citymap

class CityConverter:

    citymap = _make_citymap()

    @classmethod
    def parse(cls, city = '北京'):
        return cls.citymap.get(city,'未知')



province_list = sorted(['江苏','河南','山东','安徽','广东','河北','浙江','陕西',
'四川','山西','福建','湖南', '湖北', '贵州', '云南', '江西',
'辽宁', '内蒙古', '广西', '甘肃', '重庆', '新疆', '黑龙江',
'吉林', '天津', '上海', '北京', '海南', '宁夏', '西藏', '青海','台湾'])

city_list = sorted(['四线城市', '五线城市', '一线城市', '三线城市', '未知', '二线城市'])


age_list = sorted(['18-23', '24-30', '31-40', '41-50', '<18', '>50'])
