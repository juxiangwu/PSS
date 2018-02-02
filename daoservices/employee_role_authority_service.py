# -*- coding:utf-8 -*-

from config.appconfig import db
from model.employee_role_authority import EmployeeRoleAuthority

class EmployeeRoleAuthorityService():
    REGISTER_SUCCESS = 0
    REGISTER_FAILED = -1
    NAME_EXISTED = -2
    INVALID_ARGS = -3

    def add(self,shopId,name,roleValue):
        if not shopId or not name or not roleValue:
            return self.REGISTER_FAILED,self.INVALID_ARGS

        era = EmployeeRoleAuthority(shopId=shopId,name=name,roleValue=roleValue)
        isNameExisted = EmployeeRoleAuthority.query.filter_by(shopId=shopId,name=name).first()
        if isNameExisted:
            return self.REGISTER_FAILED,self.NAME_EXISTED
        db.session.add(era)
        db.session.commit()
        return self.REGISTER_SUCCESS,era

    def remove(self,id):
        if not id:
            return self.INVALID_ARGS
        res = EmployeeRoleAuthority.query.filter_by(id=id).delete(synchronize_session=False)
        db.session.commit()
        return res

    def update(self,newdata):
        if not newdata:
            return self.INVALID_ARGS
        olddata = EmployeeRoleAuthority.query.filter_by(id=newdata['id']).first()
        if olddata.name != newdata['name'] and newdata['name']:
            isNameExisted = EmployeeRoleAuthority.query.filter_by(name=newdata['name'],shopId=newdata['shopId']).first()
            if isNameExisted:
                return self.NAME_EXISTED

        res = EmployeeRoleAuthority.query.filter_by(id=newdata['id']).update(newdata)
        db.session.commit()
        return res

    def getById(self,id):
        if not id:
            return None
        res = EmployeeRoleAuthority.query.filter_by(id=id).first()
        return res

    def getByShopId(self,shopId):
        if not shopId:
            return None
        res = EmployeeRoleAuthority.query.filter_by(shopId=shopId).all()
        return res
    