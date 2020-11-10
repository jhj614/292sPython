# 题⽬要求：
#   根据已给⽹址爬取果壳前⽂章标题和详情⻚内容保存到⽂件
# 使⽤技术点引导
#   request s
#   Beaut if ulSoup
#   for循环
# 解题思路：
#   利⽤json获取标题内容和⽂章id，然后⽤id拼接url去解析获取⽂章内容
#   https://www.guokr.com/science/category/theory

import requests, json
from bs4 import BeautifulSoup as bs

url = 'https://www.guokr.com/beta/proxy/science_api/articles?retrieve_type=by_category&page={}'

# 伪装请求头
headers = {
    # 标记了请求从什么设备，什么浏览器上发出
    #'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}

for page in range(1,4):
    res = requests.get(url=url.format(page), headers=headers)
    subjects = res.json()
    for subject in subjects:
        title = subject['title']
        print(title)

        url_base = 'https://www.guokr.com/article/{}'.format(subject['id'])
        article_res = requests.get(url=url_base)
        article_data = bs(article_res.text, 'html.parser')
        contents = article_data.find(id='js_content')
        print(contents.text)
