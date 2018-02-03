# -*-coding:utf-8 -*-

# 零售信息
import datetime
from config.appconfig import db
from config.constants import Constants
from model.retail_detail import RetailDetail

class RetailDetailDAO():

    def add(self,shopId,operatorId,orderType,
                orderTotalPrice,productCounts,memberId,
                orderRealTotalPrice,orderProfit,payType,
                orderId,orderDescription=None)
        now = datetime.datetime.now()
        rd = RetailDetail(shopId = shopId,operatorId=operatorId,
                orderType=orderType,
                orderTotalPrice=orderTotalPrice,
                productCounts=productCounts,
                memberId=memberId,
                orderRealTotalPrice=orderRealTotalPrice,
                orderProfit=orderProfit,
                payType=payType,
                retailDate=now,
                orderId=orderId,
                orderDescription=orderDescription)
        db.session.add(rd)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,rd

    def remove(self,id):
        if not id:
            return Constants.INVALID_ARGS
        data = RetailDetail.query.filter_by(id=id).first()
        res = db.session.delete(data)
        db.session.commit()
        return res

    def getById(self,id):
        if not id:
            return None
        data = RetailDetail.query.filter_by(id=id).first()
        return data
    
    def getByOrderId(self,shopId,orderId):
        if not shopId or not orderId:
            return None
        data = RetailDetail.query.filter_by(shopId=shopId,orderId=orderId).first()
        return data

    def getByPayType(self,shopId,payType):
        if not shopId or not payType:
            return None
        datas = RetailDetail.query.filter_by(shopId=shopId,payType=payType).all()
        return datas