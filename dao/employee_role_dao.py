# -*-coding:utf-8 -*-

from config.appconfig import db
from config.constants import Constants
from model.employee_role import EmployeeRole

# ????
class EmployeeRoleDAO():

    def add(self,shopId,name):
        if not shopId or not name:
            return Constants.INVALID_ARGS
        isNameExisted = EmployeeRole.query.filter_by(shopId=shopId,name=name).first()
        if isNameExisted:
            return Constants.REGISTER_FAILED,Constants.NAME_EXISTED
        
        er = EmployeeRole(shopId=shopId,name=name)
        db.session.add(er)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,er

    def remove(self,id):
        if not id:
            return Constants.REGISTER_FAILED,Constants.INVALID_ARGS
        data = EmployeeRole.query.filter_by(id=id).first()
        db.session.delete(data)
        db.commit()
        return Constants.REGISTER_SUCCESS,Constants.REGISTER_SUCCESS

    def update(self,newdata):
        if not newdata:
            return Constants.REGISTER_FAILED,Constants.INVALID_ARGS
        oldata = EmployeeRole.query.filter_by(id=newdata['id']).first()
        if oldata.name != newdata['name'] and newdata['name']:
            isNameExisted = EmployeeRole.query.filter_by(name=newdata['name'],shopId=newdata['shopId']).first()
            if isNameExisted:
                return Constants.REGISTER_FAILED,Constants.NAME_EXISTED
        
        res = EmployeeRole.query.filter_by(id=newdata['id']).update(newdata)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,res

    def getById(self,id):
        if not id:
            return None
        data = EmployeeRole.query.filter_by(id=id).first()
        return data

    def getByShopId(self,shopId):
        if not shopId:
            return None
        datas = EmployeeRole.query.filter_by(shopId = shopId).all()
        return datas;

