# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 23:24:14 2018

@author: hong
"""

import requests
from lxml import etree
from downloader import *
from parse import parser_xiaoqu
from saver import insert_data
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(thread)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.ERROR, format=LOG_FORMAT)

def get_url_list(html):    
    hot_list = get_hot_xiaoqu(html)
    nearby = NearbyList(hot_list)
    nearby.all_nearby_set()  
    return nearby.resultSet
    
def get_loop_page(url,html):
    """
    解析按地域查找的页面
    """
    try:   
        num = get_page_num(url, html)
        if num == 0:
            sql = parser_xiaoqu(html)
            for i in sql:
                if i != None:
                    insert_data(i)
                else:
                    continue            
            return        
        for i in range(num):
            i+=1
            url = url+'/'+repr(i)
            html = get_page_source(url)
            sql = parser_xiaoqu(html)
            for i in sql:
                if i != None:
                    insert_data(i)
                else:
                    continue
        return
    except Exception as e:
        logging.error("url为： %s抓取失败"%url)


def finally_run(url):
    print("开始一个城市")
    try:       
        html = get_page_source(url)
    except Exception as e:
        logging.error("%s 请求发送失败,可能被封了"%url)
        return
    try:
        #从城市入口获取所有小区
        get_loop_page(url,html)
        print("按地址获取小区信息")
    except Exception as e:
        logging.error("%s 从城市入口获取所有小区失败"%url)
    try:       
        #获取附近小区列表
        nearby_list = get_url_list(html)
        print("获取附近小区完列表")
    except Exception as e:
        logging.error("%s 小区列表获取失败"%url)
    try:        
        for i in nearby_list:
            url = "https:"+i
            html2 = get_page_source(url)
            get_loop_page(url,html2)
            print("%s获取成功"%i)
    except Exception as e:
        logging.error("%s 从附近楼盘入手,获取详情失败"%url)
    print("一个城市搞定")
    
if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    
    a = requests.get("https://www.kujiale.com/huxing/china?kpm=9V8.ZQA.731697a.1535902181154", headers=headers).content.decode("utf")
    html = etree.HTML(a)
    li =  html.xpath("//li[@class='item ']/a/@href")
    li = set(li)
    
    #根列表
    urls=[]
    for i in li:
        i = "http:"+i
        urls.append(i)    
    
    #一个城市的链接
    test1 = 'http://www.kujiale.com/huxing/yulin'
    #获取页面信息
    

   