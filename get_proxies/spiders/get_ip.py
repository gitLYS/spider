from scrapy.spiders import Spider
from scrapy import Request
from scrapy.selector import Selector
from get_proxies.items import Proxy
import requests
from bs4 import BeautifulSoup
from mysql import connector as cnn


class Get_Ip(Spider):
    name='get_ip'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
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
        url="http://www.xicidaili.com/nn/"+str(self.page_num)
        yield Request(url,headers=self.headers)


    def parse(self, response):
        proxy=Proxy()
        sel=Selector(response)
        ips=sel.xpath('//*[@class="country"][1]').xpath('.//following-sibling::td[1]/text()').extract()
        ports=sel.xpath('//*[@class="country"][1]').xpath('.//following-sibling::td[2]/text()').extract()
        types=sel.xpath('//*[@class="country"][1]').xpath('.//following-sibling::td[5]/text()').extract()
        flag=0
        conn=cnn.connect(**self.config)
        cur=conn.cursor()
        try:

            for i in range(0,len(ips)):
                proxy['ip']=ips[i]
                proxy['port']=ports[i]
                proxy['flag']=flag
                proxy['type']=types[i]

                #验证代理ip是否可用
                try:
                    header={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
                    proxy={
                        "http":"sock5://"+ips[i]+':'+ports[i],
                        "https":"sock5://"+ips[i]+':'+ports[i]
                    }
                    r=requests.get('https://music.163.com/',proxies={'http':ips[i]+':'+ports[i]},timeout=60)
                except Exception as e:
                    print('connected aild!')
                    print(e)
                else:
                    print('success!')
                    bsObj=BeautifulSoup(r.text,'lxml')
                    print(bsObj.title)
                    flag=1
                    f.writelines(ips[i]+','+str(ports[i])+','+str(flag)+','+types[i]+'\n')
                    sql="insert proxies values('%s','%s',%d,'%s')" % (ips[i],ports[i],flag,types[i])
                    cur.execute(sql)
                    cur.execute('commit')
        except Exception as e:
            print(e)
            cur.close()
            conn.close()
        cur.close()
        conn.close()
        self.page_num=self.page_num+1
        url="http://www.xicidaili.com/nn/"+str(self.page_num)
        if self.page_num==500:
            return
        yield Request(url,headers=self.headers)





