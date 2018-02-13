# -*-coding:utf-8 -*-

from config.constants import Constants
from config.message_cn import MessageConstants_CN
from dao.employee_info_dao import EmployeeInfoDAO
from tools.token_generator import generate_employee_code
import json

class EmployeeInfoService():

    def __init__(self):
        self.__dao = EmployeeInfoDAO()

    def queryAll(self,shopId):
        datas = self.__dao.getByShopId(shopId=shopId)
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        res = "{\"datas\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % total
        return res

    def queryByDepartment(self,shopId,departmentId):
        datas = self.__dao.getByDepartmentId(shopId=shopId,departmentId=departmentId)
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        res = "{\"datas\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % total
        return res

    def add(self, name, password, shopId, roleId,
            departmentId, telephone=None, email=None, isEnabled=True):
        maxcode = self.__dao.getMaxCode(shopId=shopId)
        if not maxcode:
            maxcode = 1000
        print('maxcode = %d' % maxcode)
        code = generate_employee_code(base=maxcode)
        code,res = self.__dao.add(name=name,password=password,shopId=shopId,roleId=roleId,
                                departmentId=departmentId,telephone=telephone,email=email,
                                isEnabled=isEnabled,code=code)
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
            result['data'] = res.to_json()
        return result
    
    def remove(self,shopId,id):
        self.__dao.remove(id)
        result = {}
        result['success'] = True
        result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return Constants.REGISTER_SUCCESS,result

    def update(self,newdata):
        code,res = self.__dao.update(newdata)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.NAME_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_DEPARTMENT_NAME_EXISTED % newdata['name']
            elif res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return result
