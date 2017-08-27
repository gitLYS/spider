import requests
from lxml import etree
import os

class GetIp():
    def get_ip(self):
        header={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }
        s = requests.get('http://www.xicidaili.com/nn/',headers=header)
        # bsObj=BeautifulSoup(s.text,'lxml')

        # all=bsObj.findAll("tr",{"class":"odd"})
        html=etree.HTML(s.text)
        ips=html.xpath('//*[@class="country"][1]/following-sibling::td[1]/text()')
        ports=html.xpath('//*[@class="country"][1]/following-sibling::td[2]/text()')
        proxies=[]
        try:
            os.remove('代理ip.txt')
        except:
            pass
        for i in range(0,len(ips)):
            proxies.append(ips[i]+':'+ports[i])
        with open('代理ip.txt','a') as f:
            for i in proxies:
                f.writelines(i+'\n')
        print('ok')
# GetIp().get_ip()
