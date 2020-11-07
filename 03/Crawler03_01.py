import requests as r
from bs4 import BeautifulSoup as bs

url = 'https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc'

res = r.get(url)
html = res.text
soup = bs(html,'html.parser')
# items = soup.find_all('class_="bjh-p"')
items = soup.find_all(class_="bjh-p")
for item in items:
    print(item.text,'\n')
