# 请求
import requests
link="http://www.santostang.com/"
headers={'User-Agent':"Mozilla/5.0"}
respone=requests.get(link,headers=headers)
print(respone.encoding)
print(respone.status_code)
print(respone.headers)
print(respone.content)
print(respone.apparent_encoding)
print(respone.encoding)
# print(type(respone))
# print(respone.text)
# 响应
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(respone.text,'html.parser')
# title=soup.find('h1',class_='post-title')\
#     # .a.text.strip()
# print(title)
# with open('lean_1.txt','a+') as f:
#     f.write(str(title))
