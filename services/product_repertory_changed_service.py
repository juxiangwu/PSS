# -*-coding:utf-8 -*-
from config.message_cn import MessageConstants_CN
from config.constants import Constants
from dao.product_repertory_changed_dao import ProductRepertoryChangedDAO
import json

class ProductRepertoryChangedServices():
    def __init__(self):
        self.__dao = ProductRepertoryChangedDAO()

    def add(self,shopId,productId,skuId,changedType,
            operatorId,orderId,changedCount):
        code,res = self.__dao.add(shopId=shopId,productId=productId,skuId=skuId,changedType=changedType,operatorId=operatorId,
                                orderId=orderId,changedCount=changedCount)
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

    def queryId(self,id):
        data = self.__dao.getById(id=id)
        if not data:
            return "{\"datas\":[],\"total\":0}"
        else:
            return "{\"datas\":" + json.dumps(data.to_json()) + ",\"total\":1}"

    def queryByProductId(self,shopId,productId):
        datas = self.__dao.getByProductId(shopId=shopId,productId=productId)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        res = "{\"datas\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % total
        return res

    def queryByProductIdAndChangedType(self,shopId,productId,changedType):
        datas = self.__dao.getByProductIdAndChangedType(shopId=shopId,productId=productId,changedType=changedType)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        res = "{\"datas\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % total
        return res

