# -*-coding:utf-8 -*-

from flask import request
from config.appconfig import app
from services.shop_service import ShopService
from config.message_cn import MessageConstants_CN
import json

@app.route('/add_shop',methods=['POST'])
def add_shop():
    try:
        userId = request.form['userId']
        name = request.form['name']
        address = request.form['address']
        shopService = ShopService()
        result = shopService.add(userId = userId,name=name,address=address)
        return json.dumps(result)
    except Exception as ex:
        error = {}
        error['success'] = False
        error['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        return json.dumps(error)
