# -*- coding:utf-8 -*-

from config.constants import Constants
from config.message_cn import MessageConstants_CN
from dao.product_repertory_chaged_detail_dao import ProductRepertoryChangedDetailDAO
import json

class ProductRepertoryChangedDetailService():
    def __init__(self):
        self.__dao = ProductRepertoryChangedDetailDAO()

    def add(self,shopId,recordId,beforeCounts,afterCounts):
        code,res = self.__dao.add(shopId=shopId,recordId=recordId,beforeCounts=beforeCounts,afterCounts=afterCounts)
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

    def queryByRecordId(self,shopId,recordId):
        datas = self.__dao.getByRecordId(shopId=shopId,recordId=recordId)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        res = "{\"datas\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % total
        return res

    def queryById(self,id):
        data = self.__dao.getById(id=id)
        if not data:
            return "{\"datas\":[],\"total\":0}"
        return "{\"datas\":" + json.dumps(data.to_json()) + ",\"total\":1}"

