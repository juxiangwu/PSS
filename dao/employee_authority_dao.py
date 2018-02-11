# -*- coding:utf-8 -*-

# 员工权限

from config.appconfig import db
from model.employee_authority import EmployeeAuthority
from config.constants import Constants

class EmployeeAuthorityDAO():
    # REGISTER_SUCCESS = 0
    # REGISTER_FAILED = -1
    # INVALID_ARGS = -2

    def add(self,shopId,employeeId,authorityId):
        ea = EmployeeAuthority(shopId=shopId,employeeId=employeeId,authorityId=authorityId)
        db.session.add(ea)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,ea

    def remove(self,id):
        ea = EmployeeAuthority.query.filter_by(id=id).first()
        if not ea:
            return Constants.INVALID_ARGS
        res = db.session.delete(ea)
        db.session.commit()
        return res
    
    def removeByEmployeeId(self,employeeId):
        if not employeeId:
            return Constants.INVALID_ARGS
        res = EmployeeAuthority.query.filter_by(employeeId=employeeId).delete(synchronize_session=False)
        db.session.commit()
        return res

    def getById(self,id):
        if not id:
            return None
        ea = EmployeeAuthority.query.filter_by(id=id).first()
        return ea

    def getByEmployeeId(self,id):
        if not id:
            return None
        eas = EmployeeAuthority.query.filter_by(employeeId=id).all()
        return eas

    def getByRoleId(self,id):
        if not id:
            return None
        eas = EmployeeAuthority.query.filter_by(roleId = id).all()
        return eas

        