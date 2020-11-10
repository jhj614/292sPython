# 题⽬要求：
#   请⾃动获取⽤户输⼊的关键字完成搜索 360的关键词接⼝是q 统计出输⼊关键字后爬取下
#   来数据的数量,通过捕获异常的⽅法如果爬取失败输出爬取失败字样
# 使⽤技术点引导
#   requests
#   input ()
#   try...except ...
# 地址：
#   http://so.com/s

# 结果图⽚：

import requests
from bs4 import BeautifulSoup as bs

url = 'http://so.com/s'
my_search = input('您想搜什么？ ')

# 伪装请求头
headers = {
    # 标记了请求从什么设备，什么浏览器上发出
    #'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}

params = {
    'q': my_search,
    'src': 'srp',
    'fr': 'none',
    'psid': '447df4d51029defa06d149b340610762'
}

res = requests.get(url=url, params=params, headers=headers)

try:
    soup = bs(res.text, 'html.parser')
    found = soup.find('span', class_='nums')
    print(found.text)
except:
    print('爬取失败...')