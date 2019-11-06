import sys
sys.path.append('..')
import urllib.request
import re
import time
import os
import random
import base

#初始化并创建一个工作簿

#创建一个名为sheetname的表单


def get_content(line="http://www.dianping.com/shop/5249640"):
    
    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko')
    opener1 = urllib.request.build_opener()
    opener1.addheaders = [headers]
    hotel_url =opener1.open(line).read()
    hotel_data = hotel_url.decode('utf-8')#ign
    num=re.compile('共为您找到(.*?)个',re.DOTALL).findall(hotel_data)
    name=re.compile('<title>(.*?)相关搜索结果',re.DOTALL).findall(hotel_data)
    num=str(''.join(num))
    name=str(''.join(name))
    return num,name

def spider(url_decode,city_list):
    wrong_list=[]
    for city in city_list:
        url="https://www.dianping.com/search/keyword/"+str(city)+"/0_"+url_decode
        try:
            count,name=get_content(url)
            
        except:
            wrong_list.append(city)
        sleepNum=random.randint(7,20)
        time.sleep(sleepNum)
    print(wrong_list)
#----------------------------------
#------------测试爬虫程序-------------
#----------------------------------
if __name__ == "__main__":
    url_decode="%E7%BE%8E%E9%A3%9F"
    spider(url_decode,range(1,11))

    