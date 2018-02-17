# -*-coding:utf-8 -*-

from config.message_cn import MessageConstants_CN
from config.constants import Constants
from dao.retail_item_detail_dao import RetailItemDetailDAO
import json

class RetailItemDetailService():
    def __init__(self):
        self.__dao = RetailItemDetailDAO()

    def add(self,shopId,orderId,productId,skuId,
            productDiscount,productDirectSub,payType,retailPrice):
        code,res = self.__dao.add(shopId=shopId,orderId=orderId,productId=productId,skuId=skuId,
                                productDirectSub=productDirectSub,productDiscount=productDiscount,
                                payType=payType,retailPrice=retailPrice)
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
        code,res = self.__dao.remove(id=id)
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
        data = self.__dao.getById(id)
        if not data:
            return "{\"datas\":[],\"total\":0}"
        return "{\"datas\":" + json.dumps(data.to_json()) +",\"total\":1}"
    
    def queryByOrderId(self,shpoId,orderId):
        datas = self.__dao.getByOrderId(shopId=shopId,orderId=orderId)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        return "{\"datas\":" + json.dumps(jsonobjs) +",\"total\":%d}" % total
    
    def queryByProductId(self,shopId,productId):
        datas = self.__dao.getByProductId(shopId=shopId,productId=productId)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
         jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        return "{\"datas\":" + json.dumps(jsonobjs) +",\"total\":%d}" % total

    def queryBySKUId(self,shopId,skuId):
        data = self.__dao.getBySKUId(shopId=shopId,skuId=skuId)
        if not data:
            return "{\"datas\":[],\"total\":0}"
        return "{\"datas\":" + json.dumps(data.to_json()) +",\"total\":1}"

    def queryByPayType(self,shopId,payType):
        datas = self.__dao.getByPayType(shopId=shopId,payType=payType)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
         jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        return "{\"datas\":" + json.dumps(jsonobjs) +",\"total\":%d}" % total
    