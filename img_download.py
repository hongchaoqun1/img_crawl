# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 14:08:12 2018

@author: hong
"""

import requests
from lxml import etree
from saver import get_all
import logging


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(thread)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.ERROR, format=LOG_FORMAT)
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    
a = requests.get("https://www.kujiale.com/huxing/china?kpm=9V8.ZQA.731697a.1535902181154", headers=headers).content.decode("utf")
html = etree.HTML(a)
#所有的城市名称, 注意这里有一个全部是不要的
li =  html.xpath("//li[@class='item ']/a/text()")

result = get_all()

for i in range(len(result)):
    try:
        imgName = './img/'+repr(result[i]['id'])+"_"+result[i]['location']+"_"+result[i]['hourse_name']+"_"+result[i]['house_type']+'_'+result[i]['construction_area']+'.jpg'
        img = requests.get(result[i]['src'], headers=headers)
        with open(imgName, 'ab') as f:
            f.write(img.content)
            f.close()
    except Exception as e:
        logging.error("id 为%s的图片获取失败")
    
