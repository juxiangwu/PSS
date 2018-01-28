# -*- coding:utf-8 -*-
# 零售信息表

from config.appconfig import db

class RetailOrderInfo(db.Model):
    __tablename__ = 't_retail_detail'
    id = db.Column('id',db.Integer,primary_key = True)
    shopId = db.Column('shop_id',db.Integer)
    operatorId = db.Column('operator_id',db.Integer)
    orderType = db.Column('retail_type',db.Integer)
    orderTotalPrice = db.Column('order_total_price',db.Float)
    productCounts = db.Column('order_counts',db.Integer)
    memberId = db.Column('member_id',db.Integer)
    orderRealTotalPrice = db.Column('order_real_price',db.Float)
    orderProfit = db.Column('order_profit',db.Float)
    orderDescription = db.Column('order_desc',db.String(1024))


    def __init__(self,shopId,operatorId,orderType,
                orderTotalPrice,productCounts,memberId,
                orderRealTotalPrice,orderProfit,orderDescription=None):
                self.shopId = shopId
                self.operatorId = operatorId
                self.orderType = orderType
                self.orderTotalPrice = orderTotalPrice
                self.productCounts = productCounts
                self.memberId = memberId
                self.orderRealTotalPrice = orderRealTotalPrice
                self.orderProfit = orderProfit
                self.orderDescription = orderDescription


    def __repr__(self):
        if self.id:
            return '<RetailOrderInfo@id=%d,shopId=%d,operatorId=%d,orderType=%d,orderTotalPrice=%f,productCount=%d,memberId=%d,orderRealTotalPrice=%f,orderProfit=%f,orderDescription=%s>' %(
            self.id,self.shopId,self.operatorId,self.orderType,self.orderTotalPrice,self.productCounts,self.memberId,self.orderRealTotalPrice,orderProfit,orderDescription)
        else:
            return '<RetailOrderInfo@shopId=%d,operatorId=%d,orderType=%d,orderTotalPrice=%f,productCount=%d,memberId=%d,orderRealTotalPrice=%f,orderProfit=%f,orderDescription=%s>' %(
            self.shopId,self.operatorId,self.orderType,self.orderTotalPrice,self.productCounts,self.memberId,self.orderRealTotalPrice,orderProfit,orderDescription)