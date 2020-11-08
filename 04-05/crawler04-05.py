# 题⽬要求
# 根据已给的⽹址分析⽹站特征，将最新发布的岗位第⼀⻚的标题例如（28297-（⾼级）
# 海外战略分析经理）爬取到本地。
# 使⽤技术点引导
#   request s库
#   json()
#   for循环
# 地址为： https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1585450579819&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn

import requests
from bs4 import BeautifulSoup as bs

url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1585450579819&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'

res = requests.get(url)
res_json = res.json()

post_list = res_json['Data']['Posts']

for post in post_list:
    print(post['RecruitPostName'])