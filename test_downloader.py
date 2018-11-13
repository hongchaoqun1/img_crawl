# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 09:09:01 2018

@author: daomangdata01
"""

from downloader import *

url = "http://www.kujiale.com/huxing/ningbo"

def test_get_page_num(url):
    html = get_page_source(url)
    num = get_page_num(url,html)
    return num

if __name__ == "__main__":
    pass