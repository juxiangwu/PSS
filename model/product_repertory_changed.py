# -*- coding:utf-8 -*-

# 商品库存变动信息

from config.appconfig import db

class ProductRepertoryChanged(db.Model):
    __tablename__ = 't_product_repertory_changed'
    id  = db.Column('id',db.Integer,primary_key=True)
    shopId = db.Column('shop_id',db.Integer)
    productId = db.Column('product_id',db.Integer)
    skuId = db.Column('sku_id',db.Integer)
    changedDate = db.Column('changed_date',db.DateTime)
    changedType = db.Column('changed_type',db.Integer)
    operatorId = db.Column('operator_id',db.Integer)
    orderId = db.Column('order_id',db.Integer)
    changedCount = db.Column('changed_count',db.Integer)

    def __init__(self,shopId,productId,skuId,changedDate,changedType,operatorId,orderId,changedCount):
        self.shopId = shopId
        self.productId = productId
        self.skuId = skuId
        self.changedDate = changedDate
        self.changedType = changedType
        self.operatorId = operatorId
        self.orderId = orderId
        self.changedCount = changedCount

    def to_json(self):
        return {
            "id":self.id,
            "shopId":self.shopId,
            "skuId":self.skuId,
            "changedDate":self.changedDate.strftime("%Y-%m-%d %H:%M:%S"),
            "changedType":self.changedType,
            "operatorId":self.operatorId,
            "orderId":self.orderId,
            "changedCount":self.changedCount
        }

    def __repr__(self):
        if self.id:
            return '<ProductRepertoryChanged@id=%d,shopId=%d,productId=%d,skuId=%d,orderId=%d,changedCount=%d>' % (self.id,self.shopId,self.productId,self.skuId,self.orderId,self.changedCount)
        else:
            return '<ProductRepertoryChanged@shopId=%d,productId=%d,skuId=%d,orderId=%d,changedCount=%d>' % (self.shopId,self.productId,self.skuId,self.orderId,self.changedCount)
