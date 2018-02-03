# -*-coding:utf-8 -*-

# 商品SKU

from config.appconfig import db
from config.constants import Constants
from model.product_sku_info import ProductSKUInfo

class ProductSKUInfoDAO():

    def add(self,shopId,productId,skuCode,storeCounts):
        if not shopId or not productId or not skuCode or not storeCounts:
            return Constants.REGSISTER_FAILED,Constants.INVALID_ARGS
        psi = ProductSKUInfo(shopId=shopId,productId=productId,skuCode=skuCode,storeCounts=storeCounts)
        db.session.add(psi)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,psi

    def update(self,newdata):
        if not newdata:
            return Constants.INVALID_ARGS
        res = ProductSKUInfo.query.filter_by(id=newdata['id']).update(newdata)
        db.session.commit()
        return res

    def remove(self,id):
        if not id:
            return Constants.INVALID_ARGS
        data = ProductSKUInfo.query.filter_by(id=id).first()
        res = db.session.delete(data)
        db.session.commit()
        return res
    
    def getById(self,id):
        if not id:
            return None
        data = ProductSKUInfo.query.filter_by(id=id).first()
        return data

    def getBySKUCode(self,shopId,code):
        if not code or not shopId:
            return None
        data = ProductSKUInfo.query.filter_by(shopId=shopId,skuCode=code).first()
        return data
    
    def getByProductId(self,shopId,productId):
        if not shopId or not productId:
            return None
        datas = ProductSKUInfo.query.filter_by(shopId=shopId,productId=productId).all()
        return datas
    