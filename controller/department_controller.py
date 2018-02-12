# -*-coding:utf-8 -*-

import json
from flask import request
from config.constants import Constants
from config.appconfig import app
from config.message_cn import MessageConstants_CN
from services.department_service import DepartmentService

@app.route('/query_department/<shopId>/<parentId>',methods=['GET'])
def query_department(shopId,parentId):
    node = request.args.get('node')
    ds = DepartmentService()
    
    if not shopId.isdigit() or not parentId.isdigit():
        res = {}
        res['success'] = False
        res['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
        return json.dumps(res)
    
    if not node or not node.isdigit():
        res = ds.query(shopId=shopId,parentId=-1)
        return res
    else:
        res = ds.query(shopId=shopId,parentId=node)
        return res

@app.route('/add_department',methods=['POST'])
def add_department():
    print(request.form)
    ds = DepartmentService()
    try:
        name = request.form['name']
        shopId = request.form['shopId']
        parentId = request.form['pid']
        
        if not name or not shopId or not parentId:
            result = {}
            result['success'] = False
            result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            return json.dumps(result)
        

        _,res = ds.add(shopId=shopId,parentId=parentId,name=name)
        print(res)
        return json.dumps(res)
        
    except Exception as ex:
        print(ex)
        res = {}
        res['success'] = False
        res['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        return json.dumps(res)

@app.route('/remove_department',methods=['POST'])
def remove_department():
    print(request.form)
    ds = DepartmentService()
    try:
        shopId = request.form['shopId']
        nodeId = request.form['id']
        if not shopId or not nodeId:
            res = {}
            res['success'] = False
            res['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            return json.dumps(res)
        _,result = ds.remove(shopId=shopId,nodeId=nodeId)
        return json.dumps(result)
    except Exception as ex:
        result = {}
        result['success'] = True
        result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        return json.dumps(result)

@app.route('/update_department',methods=['POST'])
def update_department():
    print(request.form)
    ds = DepartmentService()
    try:
        nodeId = request.form['id']
        shopId = request.form['shopId']
        name = request.form['name']
        newdata = {}
        newdata['id'] = nodeId
        newdata['shopId'] = shopId
        newdata['name'] = name
        _,result = ds.update(newdata)
        print(result)
        return json.dumps(result)
    except Exception as ex:
        print(ex)
        res = {}
        res['success'] = False
        res['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        return json.dumps(res)