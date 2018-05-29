import scrapy
from tutorial.items import DmozlItem
class DmozSpider(scrapy.Spider):
    name='dmoz'
    allowed_domains=['dmoz.org']
    start_urls=[
        'http://www.chinadmoz.org/city/232/'
        ]
    def parse(self,response):
        sel=scrapy.selector.Selector(response)
        sites=sel.xpath('//ul[@class="tab-sorting"]/li')
        items=[]
        for site in sites:
            item=DmozlItem()
            item['title']=site.xpath('a/text()').extract()
            item['link']=site.xpath('a/@href').extract()
            item['desc']=site.xpath('text()').extract()
            items.append(item)

        return items
