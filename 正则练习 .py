#!/user/bin/env python3
#-*- conding:utf-8 -*-
import re
import requests
response=requests.get('https://book.douban.com/').text
pattern=re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">.(.*?)</span>.*?year>(.*?)</span>.*?</li>',re.S)
result=re.findall(pattern,response)
print(result)
# for i in result:
# 	href,title,author,year=i
# 	print(href,title,author,year)