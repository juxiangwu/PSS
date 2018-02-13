# -*-coding:utf-8 -*-

from config.constants import Constants
from config.message_cn import MessageConstants_CN
from dao.employee_role_authority_dao import EmployeeRoleAuthorityDAO
import json

class EmployeeRoleAuthorityService():
    
    def __init__(self):
        self.__dao = EmployeeRoleAuthorityDAO()

    def add(self,shopId,name,roleValue,authorityGroupId):
        code,res = self.__dao.add(shopId=shopId,name=name,roleValue=roleValue,authorityGroupId=authorityGroupId)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.NAME_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_EMPLOYEE_NAME_EXISTED % name
            elif res == Constants.INVALID_ARGS:
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
            if res == Constants.NAME_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_EMPLOYEE_AUTHORITY_NAME_EXISTED % name
            elif res == Constants.INVALID_ARGS:
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
            res = "{\"datas\":[],\"total\":0}"
            return res
        else:
            total = len(datas)
            jsonobjs = []
            for data in datas:
                jsonobjs.append(data.to_json())
            res = "{\"datas\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % total
            return res

    def queryByGroupId(self,shopId,groupId):
        datas = self.__dao.getByGroupId(shopId=shopId,groupId=groupId)
        if not datas:
             res = "{\"datas\":[],\"total\":0}"
            return res
        else:
            total = len(datas)
            jsonobjs = []
            for data in datas:
                jsonobjs.append(data.to_json())
            res = "{\"datas\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % total
            return res