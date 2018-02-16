# -*-coding:utf-8 -*-
from config.message_cn import MessageConstants_CN
from config.constants import Constants
from dao.product_sku_info_dao import ProductSKUInfoDAO
import json

class ProductSKUInfoService():

    def __init__(self):
        self.__dao = ProductSKUInfoDAO()

    def add(self,shopId,productId,skuCode,storeCounts):
        code,res = self.__dao.add(shopId=shopId,productId=productId,skuCode=skuCode,storeCounts=storeCounts)
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

    def update(self,newdata):
        code,res = self.__dao.update(newdata)
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

    def remove(self,id):
        code,res = self.__dao.remove(id)
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

    def queryById(self,id):
        data = self.__dao.getById(id)
        if not data:
            return "{\"datas\":[],\"total\":0}"
        return "{\"datas\":" + json.dumps(data.to_json()) + ",\"total\":1}"

    def queryBySKUCode(self,shopId,skuCode):
         data = self.__dao.getBySKUCode(shopId,skuCode)
        if not data:
            return "{\"datas\":[],\"total\":0}"
        return "{\"datas\":" + json.dumps(data.to_json()) + ",\"total\":1}"
    
    def queryByProductId(self,shopId,productId):
        datas = self.__dao.getByProductId(shopId=shopId,productId=productId)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
         return "{\"datas\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % (total)  

