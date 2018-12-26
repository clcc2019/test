# coding=utf-8

import re
import requests
from bs4 import BeautifulSoup
def GetToken():
    id = 2049

    index = 'http://www.dtpwxn.top/?forum-1.htm'
    index_html = requests.get(index).text
    
    index_id = re.search(r'/?-\d{4}',index_html)#得到id

    now_id = int(re.search(r'[^-]{4}',index_id.group()).group()) #去掉-
    

    mo_time = re.search(r'\d{1,2}[\u4e00-\u9fa5]{3}',index_html).group() #得到时间
    
    print('此 Token在 %s 更新'% mo_time)
    
    if now_id > id:
    
        id = now_id
        
        url = 'http://www.dtpwxn.top/?thread-%s.htm'% id
        html = requests.get(url).text
    
        token = re.search(r'[a-z0-9]{96}',html)
        T = token.group()
        print(T)
    else:
        return '暂时无更新'

    
GetToken()

