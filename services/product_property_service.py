# -*-coding:utf-8 -*-

from config.message_cn import MessageConstants_CN
from config.constants import Constants
from dao.product_property_dao import ProductPropertyDAO
import json

class ProductPropertyService():
    def __init__(self):
        self.__dao = ProductPropertyDAO()

    def add(self,shopId,productId,propertyType,propertyName,propertyValue,groupId):
        code,res = self.__dao.add(shopId=shopId,productId=productId,
                                    propertyType=propertyType,propertyName=propertyName,
                                    propertyValue=propertyValue,groupId=groupId)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = True
            if res == Constants.PROP_VALUE_EXISTED
                result['msg'] = MessageConstants_CN.MSG_PROPERTY_NAME_EXISTED % propertyName
            elif res == Constants.PROP_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_PROPERTY_EXISTED %(propertyName,propertyValue)
            elif res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS

    def update(self,newdata):
        code,res = self.__dao.update(newdata)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            elif res == Constants.PROP_VALUE_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_PROPERTY_VALUE_EXISTED % (newdata['propertyValue'])
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return result

    def remove(self,id):
        code,res = self.__dao.remove(id = id)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = True
            if res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return result

    def queryById(self,id):
        data = self.__dao.getById(id=id)
        if not data
            return "{\"datas\":[],\"total\":0}"
        return "{\"datas\":" + json.dumps(data) + ",\"total\":1}"

    def queryByProductId(self,shopId,id):
        datas = self.__dao.getByProductId(shopId=shopId,productId=productId)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        res = "{\"datas\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % total
        return res

    def queryByGroupId(self,shopId,groupId,productId):
        datas = self.__dao.getByPropertyGroupId(self,shopId=shopId,groupId=groupId,productId=productId)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        res = "{\"datas\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % total
        return res
    



