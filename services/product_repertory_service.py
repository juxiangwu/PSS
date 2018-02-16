# -*- coding:utf-8 -*-
from config.constants import Constants
from config.message_cn import MessageConstants_CN
from dao.product_repertory_dao import ProductRepertoryDAO
import json

class ProductRepertoryService():
    def __init__(self):
        self.__dao = ProductRepertoryDAO()

    def add(self,shopId,productId,skuId,totalCounts):
        code,res = self.__dao.add(shopId=shopId,productId=productId,skuId=skuId,totalCounts=totalCounts)
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
            if res = Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return success

    def getById(self,id):
        data = self.__dao.getById(id=id)
        if not data:
            return "{\"datas\":[],\"total\":1}"
        return "{\"total\":" + json.dumps(data) + ",\"total\":1}"

    def getByProductId(self,shopId,productId):
        datas = self.__dao.getByProductId(shopId=shopId,productId=productId)
        if not datas:
            return "{\"datas\":[],\"total\":1}"
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_string())
        return "{\"total\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % total

    def getBySkuId(self,shopId,skuId):
        datas = self.__dao.getBySKUId(shopId=shopId,skuId=skuId)
        if not datas:
            return "{\"datas\":[],\"total\":1}"
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_string())
        return "{\"total\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % total