# -*-coding:utf-8 -*-

from config.constants import Constants
from config.message_cn import MessageConstants_CN
from dao.employee_authority_dao import EmployeeAuthorityDAO
import json

class EmployeeAuthorityService():
    
    def __init__(self):
        self.__dao = EmployeeAuthorityDAO()

    def queryEmployeeAuthorities(self,employeeId):
        datas = self.__dao.getByEmployeeId(employeeId)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        total = len(datas)
        jsonobjs = []
        for data in datas:
            jsonobjs.append(data.to_json())
        res = "{\"datas\":"+json.dumps(jsonobjs) +",\"total\":%d}" % total
        return res

    def add(self,shopId,employeeId,authorityId):
        code,res = self.__dao.add(shopId=shopId,employeeId=employeeId,authorityId=authorityId)
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
            result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return result

    def removeByEmployeeId(self,employeeId):
        code,res = self.__dao.removeByEmployeeId(employeeId)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
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
            result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return result
    