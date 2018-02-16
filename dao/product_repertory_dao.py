# -*-coding:utf-8 -*-

from config.appconfig import db
from config.constants import Constants
from model.product_repertory import ProductRepertory

class ProductRepertoryDAO():
    
    def add(self,shopId,productId,skuId,totalCounts):
        if not shopId or not productId or not skuId or not totalCounts:
            return Constants.REGSISTER_FAILED,Constants.INVALID_ARGS
        
        pr = ProductRepertory(shopId=shopId,productId=productId,skuId=skuId,totalCounts=totalCounts)
        db.session.add(pr)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,pr

    
    def update(self,newdata):
        if not newdata:
            return Constants.REGISTER_SUCCESS,Constants.INVALID_ARGS
        res = ProductRepertory.query.filter_by(newdata['id']).update(newdata)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,res

    def getById(self,id):
        if not id:
            return None
        data = ProductRepertory.query.filter_by(id=id).first()
        return data
    
    def getByProductId(self,shopId,productId):
        if not shopId or not productId:
            return None
        datas = ProductRepertory.query.filter_by(shopId=shopId,productId=productId).all()
        return datas
    
    def getBySKUId(self,shopId,skuId):
        if not shopId or not skuId:
            return None
        datas = ProductRepertory.query.filter_by(shopId=shopId,skuId=skuId).all()
        return datas
    