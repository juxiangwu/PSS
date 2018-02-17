# -*- coding:utf-8 -*-

# 支持方式

from config.appconfig import db
from config.constants import Constants
from model.pay_type_info import PayTypeInfo

class PayTypeInfoDAO():

    def add(self,shopId,typeName,typeValue):
        if not shopId or not typeName or not typeValue:
            return Constants.REGISTER_FAILED,Constants.INVALID_ARGS
        isNameExisted = PayTypeInfo.query.filter_by(shopId=shopId,typeName=typeName).first()
        if isNameExisted:
            print('name existed')
            return Constants.REGISTER_FAILED,Constants.NAME_EXISTED

        data = PayTypeInfo(shopId=shopId,typeName=typeName,typeValue=typeValue)
        db.session.add(data)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,data

    def update(self,newdata):
        if not newdata or not newdata['id'] or not newdata['shopId'] or not newdata['typeName']:
            return Constants.REGISTER_FAILED,Constants.INVALID_ARGS
        olddata = PayTypeInfo.query.filter_by(id=newdata['id']).first()
        if olddata.typeName != newdata['typeName'] and newdata['typeName']:
            isNameExisted = PayTypeInfo.query.filter_by(shopId=newdata['shopId'],typeName=newdata['typeName']).first()
            if isNameExisted:
                return Constants.REGISTER_FAILED,Constants.NAME_EXISTED
        res = PayTypeInfo.query.filter_by(id=newdata['id']).update(newdata)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,res

    def remove(self,id):
        if not id:
            return Constants.REGISTER_FAILED,Constants.INVALID_ARGS
       
        data = PayTypeInfo.query.filter_by(id=id).first()
       
        db.session.delete(data)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,Constants.REGISTER_SUCCESS

    def getById(self,id):
        if not id:
            return None
        data = PayTypeInfo.query.filter_by(id=id).first()
        return data
    
    def getByShopId(self,shopId):
        if not shopId:
            return None
        else:
            datas = PayTypeInfo.query.filter_by(shopId=shopId).all()
            return datas