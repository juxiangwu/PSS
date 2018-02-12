# -*-coding:utf-8 -*-

import json
from dao.employee_authority_group_dao import EmployeeAuthorityGroupDAO
from config.constants import Constants
from config.message_cn import MessageConstants_CN

class EmployeeAuthorityGroupService()

    def __init__(self):
        self.__dao = EmployeeAuthorityGroupDAO()

    def query(self,shopId):
        results = self.__dao.getByShopId(shopId=shopId)
        jsonobjs = []
        for result in results:
            jsonobjs.append(results.to_json())
        total = len(results)
        res = "{\"datas\":" + json.dumps(results) +",\"total\":%d}" % (total)
        return res


    def add(self,shopId,name,authorityId):
        code,res = self.__dao.add(shopId=shopId,name=name,authorityId=authorityId)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.NAME_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_AUTHORITY_GROUP_NAME_EXISTED % (name)
            elif res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return json.dumps(result)

