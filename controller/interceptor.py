# -*-coding:utf-8 -*-

# 请求拦截
import json
from flask import request
from config.appconfig import app
from config.message_cn import MessageConstants_CN

@app.before_request
def before_request():
    url = request.url
    print('request url = ',request.url)
    # print(request.headers)
    # res = {}
    # if  (url.find('register') > 0) or  (url.find('login') > 0):
    #     pass
    # else:
    #     return json.dumps({'success':False,'msg':MessageConstants_CN.MSG_NOT_LOGIN})

    