# -*- coding:utf-8 -*-

# 数据库定义
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

#                  dialect+driver://username:password@host:port/database?charset=utf8
# 配置 sqlalchemy  数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:356007@127.0.0.1:3306/pss?charset=utf8'
# 初始化
db = SQLAlchemy(app)