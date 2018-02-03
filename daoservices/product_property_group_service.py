# -*- coding:utf-8 -*-

# 属性分组
from config.appconfig import db
from config.constants import Constants
from model.product_property_group import ProductPropertyGroup

class ProductPropertyGroupService():

    def add(self,shopId,productId,name):
        if not shopId or not productId or not name:
            return Constants.REGSISTER_FAILED,Constants.INVALID_ARGS
        isNameExisted = ProductPropertyGroup.query.filter_by(shopId=shopId,productId=productId,name=name).first()
        if isNameExisted:
            return Constants.REGISTER_SUCCESS,Constants.NAME_EXISTED
        ppg = ProductPropertyGroup(shopId=shopId,productId=productId,name=name)
        db.session.add(ppg)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,ppg

    def remove(self,id):
        if not id:
            return Constants.INVALID_ARGS
        ppg = ProductPropertyGroup.query.filter_by(id=id).first()
        res = db.session.delete(ppg)
        db.session.commit()
        return res

    def update(self,newdata):
        if not newdata or not newdata['id'] or not newdata['productId'] or not newdata['shopId']:
            return Constants.INVALID_ARGS
        olddata = ProductPropertyGroup.query.filter_by(id = newdata['id']).first()
        if olddata.name != newdata['name'] and newdata['name']:
            isNameExisted = ProductPropertyGroup.query.filter_by(shopId=newdata['shopId'],
                        productId=newdata['productId'],name=newdata['name'])
            if isNameExisted:
                return Constants.REGSISTER_FAILED,Constants.NAME_EXISTED
        res = ProductPropertyGroup.query.filter_by(id=newdata['id']).update(newdata)
        db.session.commit()
        return res

    def getById(self,id):
        if not id:
            return None
        data = ProductPropertyGroup.query.filter_by(id=id).first()
        return data

    def getByProdcutId(self,shopId,productId):
        if not shopId or not productId:
            return None
        datas = ProductPropertyGroup.query.filter_by(shopId=shopId,productId=productId).all()
        return datas

    

