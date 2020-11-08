# 题⽬要求
#   爬取1905电影⽹，将电影资讯前3⻚标题，详情内容爬取下来

#使⽤技术点引导
#   request s
#   Beaut if ulSoup

# 结果：

#《风平浪静》领跑同档期新片 章宇宋佳热搜霸屏
# 由李霄峰执导、黄渤监制、顿河担任制片人，章宇、宋佳、王砚辉领衔主演，李鸿其特别出演，
# 邓恩熙、周政杰主演，陈瑾、张建亚、叶青友情出演的2020最值得期待的华语犯罪电影《风平浪静》正在热映。

import requests
from bs4 import BeautifulSoup as bs

# 伪装请求头
headers = {
    # 标记了请求从什么设备，什么浏览器上发出
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

for page in range(1,4):
    url = 'https://www.1905.com/news/zixun/{}.shtml'.format(page)
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    soup= bs(res.text,'html.parser')
    titles = soup.find_all('h3', class_='title')
    contents = soup.find_all('p', class_='des')
    others = soup.find_all('div', class_= 'rel-other clearFloat')

    for i in range(len(titles)):
        print(titles[i].text, contents[i].text)
        newsdate = others[i].find('span', class_='timer fl')
        otherinfo = others[i].find_all('a', class_='type-url fl')
        print(newsdate.text, end=' ')
        for j in range(len(otherinfo)):
            print(otherinfo[j].text, end=' ')
        print()
