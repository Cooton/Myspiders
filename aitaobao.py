import requests
import os
import json
# import re
# url='http://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32\
# 538762&clk1=581e470ce4d3fe2970220fccfe3d616e&keyword=%E6%96%B0%E6%AC%BE%\
# E5%A5%B3%E8%A3%85&spm=a2e15.8261149.07626516005.1&linkpid=430708_1007'
# def url_open(url):
#     head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
#     response=requests.get(url,headers=head)
#     return response
# html=url_open(url).text
# p = r'<img src="([^"]+\.webp)"'
# img_addrs = re.findall(p, html)
# print(img_addrs)
# # for each in img_addrs:
# #     img = url_open(each).content
# #     print(img)

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.heibanke.com/lesson/crawler_ex00/")
bsobj = BeautifulSoup(html,"html.parser")
print(bsobj.h1)