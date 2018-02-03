# -*-coding:utf-8 -*-

# 零售详情

from config.appconfig import db
from config.constants import Constants
from model.retail_item_detail import RetailItemDetail

class RetailItemDetailDAO():
    
    def add(self,shopId,orderId,productId,skuId,
            productDiscount,productDirectSub,payType,retailPrice):
        rid = RetailItemDetail(shopId=shopId,orderId=orderId,
                    productId=productId,
                    skuId=skuId,
                    productDiscount=productDiscount,
                    productDirectSub=productDirectSub,
                    payType=payType,
                    retailPrice=retailPrice)

        db.session.add(rid)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,rid

    def remove(self,id):
        if not id:
            return Constants.INVALID_ARGS
        data = RetailItemDetail.query.filter_by(id=id).first()
        return data
    
    def getById(self,id):
        if not id:
            return None
        data = RetailItemDetail.query.filter_by(id=id).first()
        return data
    
    def getByOrderId(self,shopId,orderId):
        if not orderId or not shopId:
            return None
        datas = RetailItemDetail.query.filter_by(shopId=shopId,orderId=orderId).all()
        return datas
    
    def getByProductId(self,shopId,productId):
        if not shopId or not productId:
            return None
        datas = RetailItemDetail.query.filter_by(shopId=shopId,productId=productId).all()
        return datas

    def getBySKUId(self,shopId,skuId):
        if not shopId or not skuId:
            return None
        datas = RetailItemDetail.query.filter_by(shopId=shopId,skuId = skuId).all()
        return datas

    def getByPayType(self,shopId,payType):
        if not shopId or not payType:
            return None
        datas = RetailItemDetail.query.filter_by(shopId=shopId,payType=payType).all()
        return datas