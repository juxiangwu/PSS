# -*- coding:utf-8 -*-
# 订单支付详情

from config.appconfig import db
from config.constants import Constants
from model.order_pay_type_detail import OrderPayTypeDetail
import datetime

class OrderPayTypeDetailDAO():

    def add(self,shopId,orderId,payType,payValue):
        now = datetime.datetime.now()
        data = OrderPayTypeDetail(shopId=shopId,orderId=orderId,payType=payType,
                    payValue=payValue,payDate=now)
        db.session.add(data)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,data

    def remove(self,id):
        if not id:
            return Constants.REGISTER_FAILED,Constants.INVALID_ARGS
        data = OrderPayTypeDetail.query.filter_by(id=id).first()
        res = db.session.delete(data)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,res

    def removeByOrderId(self,shopId,orderId):
        if not orderId:
            return
        datas = self.getByOrderId(shopId=shopId,orderId=orderId)
        if not datas:
            return
        for data in datas:
            db.session.delete(data)
            db.session.commit()

    def update(self,newdata):
        if not newdata:
            return Constants.REGISTER_FAILED,Constants.INVALID_ARGS
        res = OrderPayTypeDetail.query.filter_by(newdata['id']).update(newdata)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,res

    def getByShopId(self,shopId):
        if not shopId:
            return None
        # datas = OrderPayTypeDetail.query.filter_by(shopId = shopId).all()
        # return datas
        datas = OrderPayTypeDetail.query.filter_by(shopId=shopId).group_by(OrderPayTypeDetail.shopId).all()
        return datas

    def getByOrderId(self,shopId,orderId):
        if not shopId or not orderId:
            return None
        datas = OrderPayTypeDetail.query.filter_by(shopId=shopId,orderId=orderId).all()
        return datas

    def getById(self,id):
        if not id:
            return None
        data = OrderPayTypeDetail.query.filter_by(id=id).first()
        return data