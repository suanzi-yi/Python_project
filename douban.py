import requests
from bs4 import BeautifulSoup
import re

#获取响应
head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
url="http://www.baidu.com"
respone=requests.get(url,headers=head)

# print(respone)
print(respone.headers)
# respone.encoding="uft-8"
# print(respone.text)
# print(type(respone.content))

#转化为对象
soup=BeautifulSoup(respone.content,'lxml')
item=soup.find_all('div')
item=str(item)
# print(soup.prettify())
findlink=re.compile(r'<a class="mnav c-font-normal c-color-t" href="(.*?)"',re.S)
text=re.findall(findlink,item)
print(text)
# print(soup.prettify())#打印文本
# print(soup.title)
# print(soup.head)
# print(soup.a)
# print(soup.p)
# print(type(soup.a))
# print(type(soup.p))
# print(type(soup.title))
# print(type(soup.head))
a_list=soup.find_all('a')
print(type(a_list))
# print(soup.select('a'))
# print(soup.select('title'))
# print(soup.select('.sister'))
# print(soup.select('#link1'))
# print()
# for item in a_list:
#     print(item.get('href'))

#存入.text文件中
# text=''
# for a in a_list:
#     href=a.get('href')
#     text+=href+'\n'
#     with open('url2.txt','w')as f:
#         f.write(text)

