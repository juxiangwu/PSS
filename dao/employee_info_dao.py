# -*- coding:utf-8 -*-

# 员工信息
from config.appconfig import db
from model.employee_info import EmployeeInfo
from config.constants import Constants
from sqlalchemy.sql import func

class EmployeeInfoDAO():
     
    # REGISTER_SUCCESS = 0
    # REGISTER_FAILED = -1
    # NAME_EXISTED = -2
    # INVALID_ARGS = -3

    def add(self,shopId,name,password,departmentId,roleId,telephone = None,
            email=None,isEnabled=True):
        ei = EmployeeInfo(name=name,password=password,shopId=shopId,roleId=roleId,
                departmentId=departmentId,telephone=telephone,email=email)
        isNameExisted = EmployeeInfo.query.filter_by(name=name,shopId=shopId,departmentId=departmentId).first()

        if isNameExisted:
            return Constants.REGISTER_FAILED,Constants.NAME_EXISTED
        
        db.session.add(ei)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,ei

    def remove(self,id):
        ei = EmployeeInfo.query.filter_by(id=id).first()
        res = db.session.delete(ei)
        db.session.commit()
        return res

    def update(self,newEmployeeInfo):
        if not newEmployeeInfo:
            return self.REGISTER_FAILED,self.INVALID_ARGS
        oldEI = EmployeeInfo.query.filter_by(id=newEmployeeInfo['id']).first()
        if oldEI.name != newEmployeeInfo['name'] and newEmployeeInfo['name']:
            isNameExisted = EmployeeInfo.query.filter_by(shopId = newEmployeeInfo['shopId'],
                        departmentId=newEmployeeInfo['departmentId'],
                        name=newEmployeeInfo['name']).first()
            if isNameExisted:
                return Constants.REGISTER_FAILED,Constants.NAME_EXISTED
        
        EmployeeInfo.query.filter_by(id=newEmployeeInfo['id']).update(newEmployeeInfo)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,Constants.REGISTER_SUCCESS

    def getById(self,id):
        ei = EmployeeInfo.query.filter_by(id=id).first()
        return ei

    def getByDepartmentId(self,shopId,departmentId):
        eis = EmployeeInfo.query.filter_by(departmentId=departmentId,shopId=shopId).all()
        return eis

    def getByShopId(self,shopId):
        eis = EmployeeInfo.query.filter_by(shopId = shopId).all()
        return eis
        
    def getMaxCode(self,shopId):
        code = EmployeeInfo.query(func.max('code')).all()
        return code