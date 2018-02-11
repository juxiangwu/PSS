# -*-coding:utf-8 -*-

# 角色权限分组

from config.appconfig import db
from config.constants import Constants

from model.employee_authority_group import EmployeeAuthorityGroup

class EmployeeAuthorityGroupDAO():
    
    def add(self,name,shopId,authorityId):
        if not name or not shopId or not authorityId:
            return Constants.REGISTER_FAILED,Constants.INVALID_ARGS
        isNameExisted = EmployeeAuthorityGroup.query.filter_by(shopId=shopId,name=name).first()
        if isNameExisted:
            return Constants.REGISTER_FAILED,Constants.NAME_EXISTED
        eag = EmployeeAuthorityGroup(shopId=shopId,name=name,authorityId = authorityId)
        db.session.add(eag)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,eag

    def update(self,newdata):
        if not newdata:
            return Constants.INVALID_ARGS
        olddata = EmployeeAuthorityGroup.query.filter_by(id=newdata['id']).first()
        if olddata.name != newdata['name'] and newdata['name']:
            isNameExisted = EmployeeAuthorityGroup.query.filter_by(shopId=newdata['shopId'],name=newdata['name'])
            if isNameExisted:
                return Constants.NAME_EXISTED
        res = EmployeeAuthorityGroup.query.filter_by(id=newdata['id']).update(newdata)
        db.session.commit()
        return res

    def remove(self,id):
        if not id:
            return Constants.INVALID_ARGS
        data = EmployeeAuthorityGroup.query.filter_by(id=id).first()
        res = db.session.delete(data)
        db.session.commit()
        return res

    def getById(self,id):
        if not id:
            return None
        data = EmployeeAuthorityGroup.query.filter_by(id=id).first()
        return data

    def getByShopId(self,shopId):
        if not shopId:
            return None
        datas = EmployeeAuthorityGroup.query.filter_by(shopId=shopId).all()
        return datas