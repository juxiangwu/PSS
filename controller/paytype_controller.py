# -*-coding:utf-8 -*-

from config.appconfig import app
from services.pay_type_info_service import PayTypeInfoService
from config.constants import Constants
from config.message_cn import MessageConstants_CN
from flask import request
import json
import traceback

@app.route('/query_paytype/<shopId>',methods=['GET'])
def query_paytype(shopId):
    ptis = PayTypeInfoService()
    try:
        datas = ptis.queryByShopId(shopId=shopId)
        return datas
    except Exception as ex:
        print('query_paytype:')
        print(ex)
        res = {}
        res['sucess'] = False
        res['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        return json.dumps(res)

@app.route('/add_paytype',methods=['POST'])
def add_paytype():
    ptis = PayTypeInfoService()
    try:
        print(request.form)
        shopId = request.form['shopId']
        typeName = request.form['typeName']
        typeValue = request.form['typeValue']
        result = ptis.add(shopId=shopId,typeName=typeName,typeValue=typeValue)
        return json.dumps(result)
    except Exception as ex:
        print('add_paytype:')
        traceback.print_exc()
        res = {}
        res['success'] = True
        res['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        return json.dumps(res)

@app.route('/update_paytype',methods=['POST'])
def update_paytype():
    ptis = PayTypeInfoService()
    try:
        print(request.form)
        shopId = request.form['shopId']
        id = request.form['id']
        name = request.form['typeName']
        value = request.form['typeValue']
        newdata = {
            "id":id,
            "shopId":shopId,
            "typeName":name,
            "typeValue":value
        }
        # print(newdata)
        res = ptis.update(newdata)
        print(res)
        return json.dumps(res)
    except Exception as ex:
        print('update_paytype:error:')
        traceback.print_exc()
        res = {}
        res['success'] = False
        res['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        return json.dumps(res)

@app.route('/remove_paytype',methods=['POST'])
def remove_paytype():
    ptis = PayTypeInfoService()
    try:
        print(request.form)
        result = ptis.remove(request.form['id'])
        return json.dumps(result)
    except Exception as ex:
        res = {}
        res['success'] = False
        res['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        traceback.print_exc()
