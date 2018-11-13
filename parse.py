# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 13:48:33 2018

@author: daomangdata01
"""

from lxml import etree
from downloader import get_page_source

'''
def parser_loaction(html):
    """
     按地域查找出来的页面用这个方法来解析
    """
    try: 
        allDiv = html.xpath('//*/div[@class="info"]')
        num = len(allDiv)-4
        result_list = []
    
        for i in range(num):
            name = allDiv[i].xpath('./h4/a/text()')[0].strip()
            href = allDiv[i].xpath('./h4/a/@href')[0]
            houseType = allDiv[i].xpath('./p[@class="detail g9"]/span')[0].text.strip()
            constructionArea = allDiv[i].xpath('./p[@class="detail g9"]/span')[1].text.strip()
            location = allDiv[i].xpath('./p[@class="addr g9 ell"]/text()')[0]
            src = allDiv[i].xpath('//*[@id="search-res"]/ul/li[14]/div[1]/a/img/@src')[0]
            sql = 'INSERT INTO kujiale_img(hourse_name,house_href,house_type,construction_area,location,src) VALUES("%s","%s","%s","%s","%s","%s")'%(name,href,houseType,constructionArea,location,src)
            result_list.append(sql)
        return result_list
    except Exception as e:
        print("解析失败")
'''
    
def parser_xiaoqu(html):
    """
    按小区查找出来的页面用这个函数处理
    """
    try: 
        allDiv = html.xpath('//*/div[@class="info"]')
        allCover = html.xpath('//div[@class="cover"]')
        num = len(allDiv)-4
        result_list = []
    
        for i in range(num):
            name = allDiv[i].xpath('./h4/a/text()')[0].strip()
            href = allDiv[i].xpath('./h4/a/@href')[0]
            houseType = allDiv[i].xpath('./p[@class="detail g9"]/span')[0].text.strip()
            constructionArea = allDiv[i].xpath('./p[@class="detail g9"]/span')[1].text.strip()
            location = allDiv[i].xpath('./p[@class="addr g9 ell"]/text()')[0]
            src = allCover[i].xpath('./a/img/@src')[0]
            sql = 'INSERT INTO kujiale_img(hourse_name,house_href,house_type,construction_area,location,src) VALUES("%s","%s","%s","%s","%s","%s")'%(name,href,houseType,constructionArea,location,src)
            result_list.append(sql)
        return result_list
    except Exception as e:
        print("解析失败")    

if __name__ == "__main__":
    url = 'https://www.kujiale.com/huxing/huangsh?kpm=9V8.ZQA.6c8ef07.1536817297734'
    html = get_page_source(url)

    
