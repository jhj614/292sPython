# 91群爬虫精进阶段
# 第1节 了解爬⾍和浏览器的原理习题

# 1、题⽬要求：
# 请使⽤requests爬取⽂章，开掘⼀座⽂学理论富矿
# 并使⽤open⽅法将爬取的数据写⼊⽂件data.txt中
# 地址为：https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc

import requests as r

txt_url = 'https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc'
res = r.get(txt_url)
f = open('data.txt','w')
f.write(res.text)
f.close()

# 2、题⽬要求：
# 请使⽤request s请求百度logo图⽚ 并且使⽤open⽅法将图⽚保存下来
# 温馨提示：
# 1.结合open函数的使⽤将图⽚写⼊到本地（任意路径下都可以）
# 2.wb为⼆进制写⼊
# 地址为：https://www.baidu.com/img/bd_logo1.png

pic_url = 'https://www.baidu.com/img/bd_logo1.png'
res = r.get(pic_url)
f = open('pic.png','wb')
f.write(res.content)
f.close()