# -*-coding:utf-8 -*-

from config.constants import Constants
from config.message_cn import MessageConstants_CN
from dao.retail_detail_dao import RetailDetailDAO
import json

class RetailDetailService():
    def __init__(self):
        self.__dao = RetailDetailDAO()

    def add(self,shopId,operatorId,orderType,
                orderTotalPrice,productCounts,memberId,
                orderRealTotalPrice,orderProfit,payType,
                orderId,orderDescription=None):
        code,res = self.__dao.add(shopId=shopId,operatorId=operatorId,orderType=orderType,
                    orderTotalPrice=orderTotalPrice,productCounts=productCounts,memberId=memberId,
                    orderRealTotalPrice=orderRealTotalPrice,orderProfit=orderProfit,payType=payType,
                    orderId=orderId,orderDescription=orderDescription)
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

    def remove(self,id):
        code,res = self.__dao.remove(id)
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
        return "{\"datas\":[]"+json.dumps(data.to_json()) + ",\"total\":1}"

    def queryByOrderId(self,shopId,orderId):
        datas = self.__dao.getByOrderId(shopId=shopId,orderId=orderId)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        return "{\"datas\":[]"+json.dumps(jsonobjs + ",\"total\":%d}" % total

    def queryByPayType(self,shopId,payType):
         datas = self.__dao.getByPayType(shopId=shopId,payType=payType)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        return "{\"datas\":[]"+json.dumps(jsonobjs + ",\"total\":%d}" % total