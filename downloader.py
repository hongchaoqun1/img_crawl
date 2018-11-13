# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 22:57:14 2018

@author: hong
"""

import requests
from lxml import etree
import logging
from random import choice

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(thread)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.ERROR, format=LOG_FORMAT)


#抓取页面信息
def get_page_source(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    
    a = requests.get(url, headers=headers).content.decode("utf")
    html = etree.HTML(a)
    return html

#抓取数据列表的长度
def get_page_num(url,html):
    try:
        aList = html.xpath('//*[@id="pagination"]/div/a/text()')
        num = aList[-2]
        if num == None:
            num = 0
        else:
            num = int(num)
    except Exception as e:
        logging.error("url为： %s抓取失败"%url)
        num = 0
    return num

def get_list_of_xiaoqu():
    pass

#抓取最热信息的链接
def get_hot_xiaoqu(html):
    newXiaoqu = html.xpath('//*[@id="content"]/div[2]/div[2]/div[2]/div[1]/ul/li/a/@href')
    return newXiaoqu

class NearbyList:
    """
      获取附近楼盘的类
      初始化参数是最热楼盘获得到的列表
      内部的数据有resultList,resultSet最后用来使用
    """
    def __init__(self, params):
        self.params = list(params)
        self.resultList = []
        self.resultSet = set()
    #抓取附近小区的链接
    def get_nearby_xiaoqu(self,html):
        #获取附近小区列表
        nearbyList = html.xpath('//*[@id="content"]/div[2]/div[3]/div[2]/div[1]/ul/li/a/@href')
        for i in nearbyList:
            self.resultList.append(i)
                
        
    def loop_nearby_list(self):
        jishu = 0
        while True:
            jishu+=1
            #用于随机抽取一条记录
            sub = set(self.resultList)
            resultListLength = len(self.resultList)
            i = choice(list(sub))
            i = "https:"+i
            html = get_page_source(i)
            self.get_nearby_xiaoqu(html)  
            
            if (resultListLength - len(set(self.resultList))) == 0 or jishu==50:
                break
    
        print("下一个")
    
    def all_nearby_set(self):
        print("开始查找附近的小区")
        for i in self.params:
            self.resultList.append(i)
            self.loop_nearby_list()
        self.resultSet = set(self.resultList)
    
    

if __name__ == "__main__":
    pass