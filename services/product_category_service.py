# -*- coding:utf-8 -*-

from dao.product_category_dao import ProductCategoryDAO
from model.product_category import ProductCategory
from config.constants import Constants
from config.message_cn import MessageConstants_CN

import json

class ProductCategoryService():
    def __init__(self):
        self.__dao = ProductCategoryDAO()

    def queryCategory(self,shopId,parentId):
        
        nodes = self.__dao.getChildNodes(shopId=shopId,parentId=parentId)
        jsonstr = []
        for node in nodes:
            childCounts = self.__dao.getChildNodes(shopId,node.id)
            if len(childCounts) <= 0:
                node.isLeaf = True
            else:
                node.isLeaf = False
            jsonstr.append(node.to_json())
        total = len(nodes)
        res = "{\"datas\":" + json.dumps(jsonstr)+",\"total\":%d}" % (total)
        return res

    def addCategory(self,shopId,parentId,name):
        code,res = self.__dao.add(shopId=shopId,name=name,parentId=parentId)
        result = {}
        if code == Constants.REGISTER_FAILED:
            if res == Constants.INVALID_ARGS:
                result['success'] = False
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            elif res == Constants.NAME_EXISTED:
                result['success'] = False
                result['msg'] = MessageConstants_CN.MSG_CATEGORY_NAME_EXISTED % (name)
            else:
                result['success'] = False
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['data'] = res.to_json()
            result['msg'] = u'操作成功'
        # jstr = json.dumps(result)
        return code,result

    def remove(self,shopId,id):
        
        self.__dao.deleteChildNodes(shopId=shopId,parentId=id)
        if id != -1:
            self.__dao.deleteNode(id=id)
        # TODO:需要更新产品的分类信息
        result = {}
        result['success'] = True
        result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return Constants.REGISTER_SUCCESS,result
        
    def update(self,newdata):
        print('update:newdata:',newdata)
        code,res = self.__dao.update(newdata)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.NAME_EXISTED:
                # print('name existed')
                result['msg'] = MessageConstants_CN.MSG_CATEGORY_NAME_EXISTED % newdata['name']
            elif res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
            
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return code,result

    def __nodes_to_json(self,nodes):
        jstr = json.dumps(nodes,default=ProductCategory.to_json)