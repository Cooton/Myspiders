import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from multiprocessing import Pool
import re
import json
# import re
head={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
# url='http://maoyan.com/board/4'
# response=requests.get(url,headers=head)
# text=response.text
# soup=BeautifulSoup(text,'lxml')
# dd=soup.find_all('dd')
# for each_dd in dd:
#     for img in each_dd.select('.image-link .board-img'):
#         img_arrd=img['data-src']
#         print(each_dd.text,'图片地址为：%s'%img_arrd)
def get_one_page(url):
    try:
        response=requests.get(url,headers=head)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None
def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                       +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                       +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield {
            'index': item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }
def wtite_to_file(content):
    with open('reuslt.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
def main(offset):
    url='http://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        wtite_to_file(item)
if __name__=='__main__':

    pool=Pool()
    pool.map(main,[i*10 for i in range(10)])