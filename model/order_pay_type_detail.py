# -*- coding:utf-8 -*-

# 订单支付方式详情

from config.appconfig import db

class OrderPayTypeDetail(db.Model):
    __tablename__ = 't_order_pay_type_detail'
    
    id = db.Column('id',db.Integer,primary_key = True)
    shopId = db.Column('shop_id',db.Integer)
    orderId = db.Column('order_id',db.Integer)
    payType = db.Column('pay_type',db.Integer)
    payValue = db.Column('pay_value',db.Float)
    payDate = db.Column('pay_date',db.DateTime)

    def __init__(self,shopId,orderId,payType,payValue,payDate):
        self.shopId = shopId
        self.orderId = orderId
        self.payType = payType
        self.payValue = payValue
        self.payDate = payDate

    def __repr__(self):
        if self.id:
            return '<OrderPayTypeDetail@id=%d,shopId=%d,orderId=%d,payType=%d,payValue=%f>' %(
            self.id,self.shopId,self.orderId,self.payType,self.payValue)
        else:
            return '<OrderPayTypeDetail@shopId=%d,orderId=%d,payType=%d,payValue=%f>' %(
            self.shopId,self.orderId,self.payType,self.payValue)