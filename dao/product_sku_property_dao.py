# -*-coding:utf-8 -*-

# 商品SKU属性
from config.appconfig import db
from config.constants import Constants
from model.product_sku_property import ProductSKUProperty

class ProductSKUPropertyDAO():

    def add(self,shopId,productId,skuId,productProperties):
        if not productId or not skuId or not productProperties:
            return Constants.REGSISTER_FAILED,Constants.INVALID_ARGS

        psp = ProductSKUProperty(shopId=shopId,productId=productId,skuId=skuId,
                    productProperties=productProperties)
        db.session.add(psp)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,psp

    def remove(self,id):
        if not id:
            return Constants.INVALID_ARGS
        data = ProductSKUProperty.query.filter_by(id=id).first()
        res = db.session.delete(data)
        db.session.commit()
        return res

    def update(self,newdata):
        if not newdata:
            return Constants.INVALID_ARGS
        res = ProductSKUProperty.query.filter_by(id=newdata['id']).update(newdata)
        db.session.commit()
        return res

    def getById(self,id):
        if not id:
            return None
        data = ProductSKUProperty.query.filter_by(id=id).first()
        return data

    def getBySKUId(self,shopId,skuId):
        if not shopId or not skuId:
            return None
        data = ProductSKUProperty.query.filter_by(shopId = shopId,skuId=skuId).first()
        return data
    
    def getByProductId(self,shopId,productId):
        if not shopId or not productId:
            return None
        datas = ProductSKUProperty.query.filter_by(shopId=shopId,productId = productId).all()
        return datas