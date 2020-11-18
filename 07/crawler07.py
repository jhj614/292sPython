# 题⽬要求：
#   根据已给⽹址爬取中国智库⽹前10⻚标题和对应的⽹址信息，并将爬取到的数据写⼊到
#    excel表格或则是CSV中。
# 使⽤技术点引导
#   requests
#   BeautifulSoup
#   for循环
#   openpyxl
# 地址： https://www.chinathinktanks.org.cn/content/list?id=3&pt=1&p1

import requests, openpyxl
from bs4 import BeautifulSoup as bs

url = 'https://www.chinathinktanks.org.cn/content/list?id=3&pt=1&p1={}'

# 伪装请求头
headers = {
    # 标记了请求从什么设备，什么浏览器上发出
    #'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}

saved_q = openpyxl.Workbook()
main_sheet = saved_q.active
main_sheet.title = 'Main'
main_sheet['A1'] = 'Title'
main_sheet['B1'] = 'URL'

for page in range(1,11):
    # print('Processing Page {}...'.format(page))
    res = requests.get(url=url.format(page),headers=headers)
    print(url.format(page))
    res_data = bs(res.text, 'html.parser')
    titlelist = res_data.find('ul', class_='list')
    # titles = titlelist.find_all(lambda tag: tag.name == 'a' and tag.get('title') and tag.text)

    titles = titlelist.find_all('a')

    for i in range(len(titles)):
        title = titles[i]['title']
        link = 'https:' + titles[i]['href']
        main_sheet.append([title, link])
        # print(titles[i]['title'])
        # print(titles[i]['href'])

saved_q.save('my_queries.xlsx')

print("Processing completed.")