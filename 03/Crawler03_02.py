import requests as r
from bs4 import BeautifulSoup as bs

url = 'https://movie.douban.com/chart'

#定义请求头（第六课会讲）
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

# 获取数据,传入参数,第一个为url,第二个为请求头
res = r.get(url, headers=headers)
html = res.text

# 解析数据
soup = bs(html,'html.parser')
print(soup)

exit()


toc = soup.find(class_='book-mulu')
items = toc.find_all('li')
for item in items:
    print(item.text)
