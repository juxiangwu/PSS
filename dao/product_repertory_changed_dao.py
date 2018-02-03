# -*-coding:utf-8 -*-

# 库存变动明细
import datetime
from config.appconfig import db
from config.constants import Constants
from model.product_repertory_changed import ProductRepertoryChanged

class ProductRepertoryChangedDAO():
    
    def add(self,shopId,productId,skuId,changedType,
            operatorId,orderId,changedCount):
        now = datetime.datetime.now()
        prc = ProductRepertoryChanged(shopId=shopId,productId=productId,skuId=skuId,
                changedDate=now,changedType=changedType,
                operatorId=operatorId,orderId=orderId,
                changedCount=changedCount)
        db.session.add(prc)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,prc

    def getByProductId(self,shopId,productId):
        if not productId or not shopId:
            return None
        datas = ProductRepertoryChanged.query.filter_by(shopId=shopId,productId=productId).all()
        return datas
    
    def getByProductIdAndChangedType(self,shopId,productId,changedType):
        if not shopId or not productId or not changedType:
            return None
        