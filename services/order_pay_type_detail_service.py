# -*-coding:utf-8 -*-

from config.constants import Constants
from config.message_cn import MessageConstants_CN
from dao.order_pay_type_detail import OrderPayTypeDetailDAO
import json

class OrderPayTypeDetailService():
    def __init__(self):
        self.__dao = OrderPayTypeDetailDAO()

    def add(self,shopId,orderId,payType,payValue):
       
        code,res = self.__dao.add(shopId=shopId,orderId=orderId,payType=payType,payValue=payValue)
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

    def removeByOrderId(self,shopId,orderId):
        self.__dao.removeByOrderId(shopId=shopId,orderId=orderId)
        return Constants.REGISTER_SUCCESS,Constants.REGISTER_SUCCESS
    
    def remove(self,id):
        self.__dao.remove(id=id)
        return Constants.REGISTER_SUCCESS,Constants.REGISTER_SUCCESS
    
    def queryByOrderId(self,shopId):
        datas = self.__dao.getByShopId(shopId=shopId)
        result = {}
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        jsonobjs = []
        for data in datas:
            jsonobjs.append(data.to_json())
        total = len(datas)
        res = "{\"datas\":"+json.dumps(jsonobjs)+",total:%d}" % total
        return res

    def queryById(self,id):
        data = self.__dao.getById(id=id)
        if not data:
            return "{\"datas\":[],\"total\":0}"
        res = "{\"datas\":"+json.dumps(data.to_json()) +",\"total\":1}"
        return res

    def queryByShopId(self,shopId):
        datas = self.__dao.getByShopId(shopId=shopId)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        total = len(datas)
        jsonobjs = []
        for data in datas:
            jsonobjs.append(data.to_json())
        res = "{\"datas\":"+json.dumps(jsonobjs) + ",\"total\":%d}" % total
        return res