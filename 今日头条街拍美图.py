from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
import re
import  pymongo
import json
from requests import RequestException
def get_page_index(offset,keyword):
    data={
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3
    }
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    url='https://www.toutiao.com/search_content/?'+ urlencode(data)
    try:
        response=requests.get(url,headers=head)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None
def parse_page_index(html):
    data=json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield  item.get('article_url')
def get_page_detail(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    try:
        response=requests.get(url,headers=head)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错',url)
        return None
def parse_page_detail(html):

def main():
    html=get_page_index(0,'街拍')
    for url in parse_page_index(html):
        html=get_page_detail(url)


if __name__=='__main__':
    main()