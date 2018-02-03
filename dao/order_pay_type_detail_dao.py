# -*- coding:utf-8 -*-
# 订单支付详情

from config.appconfig import db
from config.constants import Constants
from model.order_pay_type_detail import OrderPayTypeDetail
import datetime

class OrderPayTypeDetailDAO():

    def add(self,shopId,orderId,payType,payValue,payDate):
        now = datetime.datetime.now()
        data = OrderPayTypeDetail(shopId=shopId,orderId=orderId,payType=payType,
                    payValue=payValue,payDate=now)
        db.session.add(data)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,data

    def remove(self,id):
        if not id:
            return Constants.INVALID_ARGS
        data = OrderPayTypeDetail.query.filter_by(id=id).first()
        res = db.session.delete(data)
        db.session.commit()
        return res
    