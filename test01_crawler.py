# coding=utf-8
# 收集数据
import time, json, requests

# 爬取腾讯疫情实时json数据
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
data = json.loads(requests.get(url=url).json()['data'])
print(data)
print(data.keys())

# 统计省份信息(34个省份)
