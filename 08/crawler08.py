import requests, openpyxl
from bs4 import BeautifulSoup as bs

url = 'https://www.shobserver.com/news/list?section=42'

# 伪装请求头
headers = {
    # 标记了请求从什么设备，什么浏览器上发出
    #'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}

saved_q = openpyxl.Workbook()
main_sheet = saved_q.active
main_sheet.title = 'Main'
main_sheet['A1'] = '标题'
main_sheet['B1'] = '内容'
main_sheet['C1'] = '作者及日期'

# print('Processing Page {}...'.format(page))
res = requests.get(url=url,headers=headers)
res_data = bs(res.text, 'html.parser')

titles = res_data.find_all('div', class_='chengshi_wz_h')
contents = res_data.find_all('div', class_='chengshi_wz_m')
authors = res_data.find_all('div', class_='chengshi_wz_f')

for i in range(len(titles)):
    title = titles[i].text
    content = contents[i].text
    author = authors[i].text.replace('\r\n', '')

    print(title, content, author)

    main_sheet.append([title, content, author])

saved_q.save('crawler08.xlsx')
saved_q.close()

print("Processing completed.")