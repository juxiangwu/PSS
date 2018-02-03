# -*- coding:utf-8 -*-

# 支持方式

from config.appconfig import db
from config.constants import Constants
from model.pay_type_info import PayTypeInfo

class PayTypeInfoService():

    def add(self,shopId,typeName,typeValue):
        if not shopId or not typeName or not typeValue:
            return Constants.REGSISTER_FAILED,Constants.INVALID_ARGS
        isNameExisted = PayTypeInfo.query.filter_by(shopId=shopId,typeName=typeName)
        if isNameExisted:
            return Constants.REGSISTER_FAILED,Constants.NAME_EXISTED

        data = PayTypeInfo(shopId=shopId,typeName=typeName,typeValue=typeValue)
        db.session.add(data)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,data

    def update(self,newdata):
        if not newdata or not newdata['id'] or not newdata['shopId'] or not newdata['name']:
            return Constants.INVALID_ARGS
        olddata = PayTypeInfo.query.filter_by(newdata['id']).first()
        if olddata.name != newdata['name'] and newdata['name']:
            isNameExisted = PayTypeInfo.query.filter_by(shopId=newdata['shopId'],name=newdata['name'])
            if isNameExisted:
                return Constants.NAME_EXISTED
        res = PayTypeInfo.query.filter_by(id=newdata['id']).update(newdata)
        db.session.commit()
        return res

    def remove(self,id):
        if not id:
            return Constants.INVALID_ARGS
        data = PayTypeInfo.query.filter_by(id=id)
        res = db.session.delete(data)
        db.session.commit()
        return res

    def getById(self,id):
        if not id:
            return None
        data = PayTypeInfo.query.filter_by(id=id).first()
        return data
    