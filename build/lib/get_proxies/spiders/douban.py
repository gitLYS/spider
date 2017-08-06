from scrapy.spider import Spider
from scrapy import Request
from get_proxies.items import Movie
import json
import random

class UserAgent():
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
       ]

    def getUserAgent(self):
        return '\''+random.choice(self.user_agent_list)+'\''




class DouBan(Spider):
    name='douban'
    headers={
        'User-Agent': UserAgent().getUserAgent()
    }
    config={
    'user':'root',
    'password':'lys',
    'host':'127.0.0.1',
    'port':3306,
    'database':'lys'
    }
    page_num=1
    def start_requests(self):
        url='https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start='+str(self.page_num*20)
        yield Request(url,headers=self.headers)

    def parse(self, response):
        movieItem=Movie()
        datas=json.loads(response.body)
        with open('doubanMovie.csv','a') as f:
            for data in datas['data']:
                # movieItem['directors']=data['directors']
                directors=None
                if len(data['directors'])>0:
                    directors=data['directors'][0]
                if len(data['directors'])>1:
                    for i in range(1,len(data['directors'])):
                        directors=directors+','+data['directors'][i]
                movieItem['directors']=directors
                movieItem['rate']=data['rate']
                movieItem['star']=data['star']
                movieItem['title']=data['title']
                movieItem['url']=data['url']
                # movieItem['casts']=data['casts']
                casts=None
                if len(data['casts']):
                    casts=data['casts'][0]
                if len(data['casts'])>1:
                    for i in range(1,len(data['casts'])):
                        casts=casts+','+data['casts'][i]
                movieItem['casts']=casts
                movieItem['cover']=data['cover']
                movieItem['id']=data['id']
                f.writelines(data['title']+','+data['url']+'\n')

        if len(datas['data'])<20:
            return
        self.page_num=self.page_num+1
        url='https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start='+str(self.page_num*20)
        yield Request(url=url,headers=self.headers)






