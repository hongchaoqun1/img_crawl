# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 22:56:22 2018

@author: hong
"""

from config import connection

def insert_data(sql):
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = sql
            cursor.execute(sql)
            # 获取查询结果
            #result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    except:
        print("插入失败")

def get_all():
    with connection.cursor() as cursor:
        sql = "SELECT * from kujiale_img"
        cursor.execute(sql)
        result = cursor.fetchall()  
    return result
     
def close_conn():
    connection.close()
