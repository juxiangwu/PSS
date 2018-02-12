# -*- coding:utf-8 -*-

# 数据库定义
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache
import memcache
import os

curdir = os.getcwd()
static_dir = curdir+'/static'
template_dir = curdir+'/templates'

app = Flask(__name__,static_folder=static_dir,template_folder=template_dir)

cacheClient = memcache.Client(servers=['127.0.0.1:11211'])
# dialect+driver://username:password@host:port/database?charset=utf8
# 配置 sqlalchemy  数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:356007@127.0.0.1:3306/pss?charset=utf8'
# 初始化
db = SQLAlchemy(app)
cache = Cache(config={'CACHE_TYPE': 'memcached',
                'CACHE_MEMCACHED_SERVERS':["127.0.0.1:11211"]})
cache.init_app(app)
