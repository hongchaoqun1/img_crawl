# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 22:58:42 2018

@author: hong
"""

import pymysql as MySQLdb
import redis

config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'',
          'db':'daomang',
          'charset':'utf8mb4',
          'cursorclass':MySQLdb.cursors.DictCursor,
          }

# Connect to the database
connection = MySQLdb.connect(**config)

pool = redis.ConnectionPool(host='localhost', port=6379)
r = redis.Redis(connection_pool=pool)