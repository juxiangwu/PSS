# -*- coding:utf-8 -*-

# 商品属性

from config.appconfig import db
from config.constants import Constants
from model.product_property import ProductProperty
#  1:SKU属性,2:整数型,3:浮点型,4:字符串型,5:日期型
class ProductPropertyService():

    def add(self,shopId,productId,propertyType,propertyName,propertyValue,groupId):
        if not shopId or not productId or not propertyType or not propertyName or not propertyValue or not groupId:
            return Constants.REGSISTER_FAILED,Constants.INVALID_ARGS
        isValueExisted = ProductProperty.query.filter_by(shopId=shopId,
                            productId=productId,
                            propertyType=propertyType,
                            propertyValue=propertyValue,
                            groupId = groupId).first()
        if isValueExisted:
            return Constants.REGSISTER_FAILED,Constants.PROP_VALUE_EXISTED
        pp = ProductProperty(shopId=shopId,productId=productId,propertyType=propertyType,
                propertyName=propertyName,propertyValue=propertyValue,groupId=groupId)
        db.session.add(pp)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,pp

    def remove(self,id):
        if not id:
            return Constants.INVALID_ARGS
        data = ProductProperty.query.filter_by(id=id).first()
        res = db.session.delete(data)
        db.session.commit()
        return res

    def update(self,newdata):
        if not newdata:
            return Constants.INVALID_ARGS
        olddata = ProductProperty.query.filter_by(id=newdata['id']).first()
        if olddata.propertyName == newdata['propertyName'] and newdata['propertyName']:
            isValueExisted = ProductProperty.query.filter_by(shopId=newdata['shopId'],
                            productId=newdata['productId'],
                            propertyType=newdata['propertyType'],
                            propertyValue=newdata['propertyValue'],
                            groupId = newdata['groupId']).first()
            if isValueExisted:
                return Constants.PROP_VALUE_EXISTED
        res = ProductProperty.query.filter_by(id=newdata['id']).update(newdata)
        db.session.commit()
        return res

    def getById(self,id):
        if not id:
            return None
        data = ProductProperty.query.filter_by(id=id).first()
        return data

    def getByProductId(self,shopId,productId):
        if not shopId or not productId:
            return None
        
        datas = ProductProperty.query.filter_by(shopId=shopId,productId=productId).all()
        return datas

    def getByPropertyGroupId(self,shopId,groupId,productId):
        if not shopId or not groupId or not productId:
            return None
        
        datas = ProductProperty.query.filter_by(shopId=shopId,productId=productId,groupId=groupId).all()
        return datas
        
    