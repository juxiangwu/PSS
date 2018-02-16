# -*-coding:utf-8 -*-
from config.constants import Constants
from config.message_cn import MessageConstants_CN
from dao.product_property_group_dao import ProductPropertyGroupDAO
import json

class ProductPropertyGroupService():
    def __init__(self):
        self.__dao = ProductPropertyGroupDAO()

    def add(self,shopId,productId,name):
        code,res = self.__dao.add(shopId=shopId,productId=productId,name=name)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.NAME_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_PRODUCT_PROPERTY_NAME_EXISTED % name
            elif res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return result

    def queryByProductId(self,shopId,productId):
        datas = self.__dao.getByProdcutId(shopId=shopId,productId=productId)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        jsonobjs = []
        total = len(datas)
        for data in jsonobjs:
            jsonobjs.append(data.to_json())
        res = "{\"datas\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % total
        return res

    def queryById(self,shopId,id):
        data = self.__dao.getById(id=id)
        if not data:
            return return "{\"datas\":[],\"total\":0}"
        res = "{\"datas\":" + json.dumps(data) + ",\"total\":0}"
        return res

    def update(self,newdata):
        code,res = self.__dao.update(newdata)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.NAME_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_PRODUCT_PROPERTY_NAME_EXISTED % newdata['name']
            elif res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return result

    def removeById(self,id):
        code,res = self.__dao.remove(id=id)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return result

    def removeByProductId(self,shopId,productId):
        self.__dao.removeByProductId(shopId=shopId,productId=productId)
        result = {}
        result['success'] = True
        result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return result
