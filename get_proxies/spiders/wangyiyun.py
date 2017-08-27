from scrapy.spider import Spider
from scrapy import Request
from bs4 import BeautifulSoup
from urllib import parse
from scrapy import Selector
from get_proxies import items
import os
class WangYiYun(Spider):

    catList=['华语','欧美','日语','韩语','粤语','小语种','流行','摇滚','民谣','电子','舞曲','说唱','轻音乐','爵士','乡村','R&B/Soul','古典','民族','英伦','金属','朋克','蓝调','雷鬼','世界音乐','拉丁','另类/独立','New Age','古风','后摇','Bossa Nova','清晨','夜晚','学习','工作','午休','下午茶','地铁','驾车','运动','旅行','散步','酒吧','怀旧','清新','浪漫','性感','伤感','治愈','放松','孤独','感动','兴奋','快乐','安静','思念','影视原声','ACG','校园','游戏','70后','80后','90后','网络歌曲','KTV','经典','翻唱','吉他','钢琴','器乐','儿童','榜单','00后'
]
    name='wangyiyun'
    header={
        'header':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    page_num=0
    url='http://music.163.com/discover/playlist/?cat=华语' +catList[page_num]

    def start_requests(self):
        #创建目录用来存储所有的歌单


        yield Request(self.url,headers=self.header)
    def parse(self, response):
        sel=Selector(response)
        nextUrl=sel.xpath('//*[@id="m-pl-pager"]/div/a[11]/@href').extract()
        urlList=[]
        try:
            for i in range(1,36):
                urlList.append(sel.xpath('//*[@id="m-pl-container"]/li[%d]/p[1]/a/@href' % i).extract())
        except Exception as e:
            print(e)

        if nextUrl!=None:
            for i in range(0,len(urlList)):
                url=urlList[i]
                yield Request(url=url,headers=self.header,callback=self.parse2())
        else:
            self.page_num=self.page_num+1
            if self.page_num==len(self.catList):
                return
            yield Request(url=self.page_num,headers=self.header,callback=self.parse())

    def parse2(self,response):
        sel=Selector(response)


