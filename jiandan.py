#!/use/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import json
import re
import os
# req=urllib.request.Request(url,headers=head)
# response=urllib.request.urlopen(req)
# img=response.read()
# with open('meizhi.jpg','wb')as f:
# 	f.write(img)
def url_open(url):
	head={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
	req=urllib.request.Request(url,headers=head)
	response=urllib.request.urlopen(url)
	html=response.read()
	return html

def get_page(url):
	html=url_open(url).decode('utf-8')

	a=html.find('righttext')+23
	b=html.find(']',a)
	return(html[a:b])
def find_imgs(url):
	html=url_open(url).decode('utf-8')
	img_addrs=[]
	a=html.find('img src=')
	while a!=-1:
		b=html.find('.jpg',a,a+255)
		if b!=-1:
			img_addrs.append(html[a+9:b+4])
		a=html.find('img src=',b)
	else:
		b=a+9
	a=html.find('img src=',b)
	for each in img_addrs:
		print(each)
def save_imgs(folder,img_addrs):
	for each in img_addrs:
		filename=each.spilt('/')[-1]
		with open(filename,'wb')as f:
			img=url_open(each)
			f.write(img)
def download_mm(folder='OOXX',pages=10):
	os.makedirs(folder,exist_ok=True)
	os.chdir(folder)
	url=('http://janjian.net/ooxx')
	page_num=int(get_page(url))

	for i in range(pages):
		page_num-=i
		page_url=url+'/page-'+str(page_num)+'#comments'
		img_addrs=find_imgs(page_url)
		save_imgs(folder,img_addrs)
if __name__=='__main__':
	download_mm()