# -*-coding:utf-8 -*-
from config.constants import Constants
from config.message_cn import MessageConstants_CN
from dao.employee_role_dao import EmployeeRoleDAO
import json
class EmployeeRoleService()

    def __init__(self):
        self.__dao = EmployeeRoleDAO()

    def query(self,shopId):
        datas = self.__dao.getByShopId(shopId=shopId)
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        res = "{\"datas\":"+ json.dumps(jsonobjs) +",\"total\":%d}" % total
        return res

    def add(self,shopId,name):
        code,res = self.__dao.add(shopId=shopId,name=name)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            elif res == Constants.NAME_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_EMPLOYEE_ROLE_NAME_EXISTED % name
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return result

    def remove(self,id):
        code,res = self.__dao.remove(id)
        # TODO:需要更新员工角色
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
        return res

    def update(self,newdata):
        code,res = self.__dao.update(newdata)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.NAME_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_EMPLOYEE_ROLE_NAME_EXISTED % newdata['name']
            elif res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return result