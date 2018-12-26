# coding=utf-8

import re
import requests
from bs4 import BeautifulSoup
def GetToken():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'bbs_sid=0p217a599bm08h15siu4ng1hs4; UM_distinctid=167e969062dcc-0142d7602e0578-77103a42-100200-167e969062e4d3; CNZZDATA1274423427=1216749288-1545806831-%7C1545825191; cookie_test=dHTwtz0Oy2dRg_2FHxYTJmgOPTVht8EfipD9nbz5N_2BD5DnYRhs',
        'Host': 'www.dtpwxn.top',
        'Referer': 'http://www.dtpwxn.top/?forum-1.htm',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3649.0 Safari/537.36',
    }
    id = 2049
    index = 'http://www.dtpwxn.top/?forum-1.htm'
    IndexHtml = requests.get(index,headers=headers).text 
    IndexId = re.search(r'/?-\d{4}',IndexHtml)
    NowId = int(re.search(r'[^-]{4}',IndexId.group()).group())
    Tim = re.search(r'\d{1,2}[\u4e00-\u9fa5]{3}',IndexHtml).group()
    print('最后更新时间：')
    print('>>>>此 Token在 %s 更新<<<<'% Tim)
    if NowId > id:
        id = NowId
        url = 'http://www.dtpwxn.top/?thread-%s.htm'% id
        html = requests.get(url,headers=headers).text
    
        token = re.search(r'[a-z0-9]{96}',html)
        T = token.group()
        print(T)
    else:
        return '暂时无更新'

GetToken()

