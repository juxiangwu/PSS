# -*-coding:utf-8 -*-

from config.appconfig import app
from config.constants import Constants
from config.message_cn import MessageConstants_CN
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from tools.token_generator import generate_token
from services.product_category_service import ProductCategoryService
import json
import os

@app.route('/query_category/<shopId>/<parentId>',methods=['GET'])
def query_category(shopId,parentId):
    node = request.args.get('node')
    pcs = ProductCategoryService()
    
    if not node or not node.isdigit():
        res = pcs.queryCategory(shopId = shopId,parentId = -1)
        # print(res)
        return str(res)
    else:
        pid = int(node)
        res = pcs.queryCategory(shopId = shopId,parentId=pid)
        # print(res)
        return res
@app.route('/add_category',methods=['POST'])
def add_category():
    print(request.form)
    pcs = ProductCategoryService()
    try:
        shopId = request.form['shopId']
        parentId = request.form['pid']
        name = request.form['name']
        result = {}
        if not name or not shopId or not parentId:
            print('add_productcategory:invalid datas')
            result['success'] = False
            result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            return json.dumps(result)
        
        _,res = pcs.addCategory(shopId=shopId,parentId=parentId,name=name)
        return json.dumps(res)
    except Exception as ext:
        print('add_category',ext)
        result = {}
        result['success'] = False
        result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        return json.dumps(result)

@app.route('/remove_category',methods=['POST'])
def remove_category():
    print(request.form)
    pcs = ProductCategoryService()
    try:
        shopId = request.form['shopId']
        nodeId = request.form['id']
       
        if not shopId or not nodeId:
            res = {}
            res['success'] = False
            res['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            return json.dumps(res)
        _,result = pcs.remove(shopId=shopId,id=nodeId)
        return json.dumps(result)
    except Exception as ex:
        print('remove_category:',ex)
        res = {}
        res['success'] = False
        res['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        return json.dumps(res)

@app.route('/update_category',methods=['POST'])
def update_category():
    print(request.form)
    pcs = ProductCategoryService()
    try:
        nodeId = request.form['id']
        shopId = request.form['shopId']
        name = request.form['name']
        newdata = {}
        newdata['id'] = nodeId
        newdata['shopId'] = shopId
        newdata['name'] = name
        _,result = pcs.update(newdata)
        print(result)
        return json.dumps(result)
    except Exception as ex:
        print('remove_category:',ex)
        res = {}
        res['success'] = False
        res['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        return json.dumps(res)

