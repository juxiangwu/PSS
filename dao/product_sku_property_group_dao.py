# -*-coding:utf-8 -*-

# 商品SKU属性分组

from config.appconfig import db
from config.constants import Constants
from model.product_sku_property_group import ProductSKUPropertyGroup

class ProductSKUPropertyGroupDAO():

    def add(self,shopId,productId,name):
        if not shopId or not productId or not name:
            return Constants.REGSISTER_FAILED,Constants.INVALID_ARGS

        isNameExisted = ProductSKUPropertyGroup.query.filter_by(shopId=shopId,productId=productId,name=name).first()
        if isNameExisted:
            return Constants.REGSISTER_FAILED,Constants.NAME_EXISTED

        pspg = ProductSKUPropertyGroup(shopId=shopId,productId=productId,name=name)
        db.session.add(pspg)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,pspg

    def remove(self,id):
        if not id:
            return Constants.INVALID_ARGS
        data = ProductSKUPropertyGroup.query.filter_by(id=id).first()
        res = db.session.delete(data)
        db.session.commit()
        return res

    def update(self,newdata):
        if not newdata:
            return Constants.INVALID_ARGS
        olddata = ProductSKUPropertyGroup.query.filter_by(id=newdata['id']).first()
        if olddata.name != newdata['name'] and newdata['name']:
            isNameExisted = ProductSKUPropertyGroup.query.filter_by(shopId=newdata['shopId'],productId=newdata['productId'],name=newdata['name']).first():
            if isNameExisted:
                return Constants.NAME_EXISTED
        res = ProductSKUPropertyGroup.query.filter_by(id=newdata['id']).update(newdata)
        db.session.commit()
        return res

    def getById(self,id):
        if not id:
            return None
        data = ProductSKUPropertyGroup.query.filter_by(id=id).first()
        return data
    
    def getByProductId(self,shopId,productId):
        if not productId or not shopId:
            return None
        datas = ProductSKUPropertyGroup.query.filter_by(shopId=shopId,productId=productId).all()
        return datas
        