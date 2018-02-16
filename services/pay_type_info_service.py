# -*-coding:utf-8 -*-

from config.constants import Constants
from config.message_cn import MessageConstants_CN
from dao.pay_type_info_dao import PayTypeInfoDAO
import json

class PayTypeInfoService():
    def __init__(self):
        self.__dao = PayTypeInfoDAO()

    def add(self,shopId,typeName,typeValue):
        code,res = self.__dao.add(shopId=shopId,typeName=typeName,typeValue=typeValue)
        result = {}

        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            elif res == Constants.NAME_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_PAY_TYPE_NAME_EXISTED % typeName
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
            elif res == Constants.NAME_EXISTED:
                if newdata['typeName']
                    result['msg'] = MessageConstants_CN.MSG_PAY_TYPE_NAME_EXISTED % newdata['typeName']
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

    def queryByShopId(self,shopId):
        datas = self.__dao.getByShopId(shopId=shopId)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        res = "{\"datas\":"+ json.dumps(datas) +",\"total\":%d}" % total
        return res

    def queryById(self,id):
        data = self.__dao.getById(id)
        if not data:
            return "{\"datas\":[],\"total\":0}"
        return "{\"datas\":"+json.dumps(data) + ",\"total\":1}" 