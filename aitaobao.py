import requests
import os
import json
url='http://ai.taobao.com/search/index.htm?prepvid=200_11.224.194.123_298_1527496342285&extra=&spm=a231o.7076277.1998549605.4.300946084dejuU&pid=mm_10011550_0_0&app_pvid=200_11.224.194.123_298_1527496342285&channelId=4&cat=50010394&key=%E4%BC%98%E8%A1%A3%E5%BA%93%E5%A5%B3&unid=&clk1=&source_id='
head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
response=requests.get(url,headers=head)
print(response.content)
