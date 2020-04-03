# coding=utf-8
# 收集数据
import time, json, requests

# 爬取腾讯疫情实时json数据
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
data = json.loads(requests.get(url=url).json()['data'])
# print(data)
# print(data.keys())
# print(data['areaTree'][0])

# 统计省份信息(34个省份)

num = data['areaTree'][0]['children']
print(len(num))
for item in num:
    print(item['name'], end=" ")
else:
    print("\n")

# 显示江苏省数据
jsIndex = -1
for i in num:
    jsIndex += 1
    if i['name'] == "江苏":
        break

jiangsu = num[jsIndex]['children']
for data in jiangsu:
    print(data)

# 解析数据
total = {}
for item in num:
    if item['name'] not in total:
        total.update({item['name']:0})
    for city in item['children']:
        total[item['name']] += int(city['total']['confirm'])
print(total)
