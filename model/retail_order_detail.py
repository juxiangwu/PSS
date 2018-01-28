# -*- coding:utf-8 -*-

# 零售详情

from config.appconfig import db

class RetailOrderDetail(db.Model):
    __tablename__ = 't_retail_item_detail'
    id = db.Column('id',db.Integer,primary_key = True)
    shopId = db.Column('shop_id',db.Integer)
    orderId = db.Column('order_id',db.Integer)
    productId = db.Column('product_id',db.Integer)
    skuId = db.Column('sku_id',db.Integer)
    productDiscount = db.Column('product_discount',db.Float)
    productDirectSub = db.Column('product_directly_sub',db.Float)

    def __init__(self,shopId,orderId,productId,skuId,
            productDiscount,productDirectSub):

        self.shopId = shopId
        self.orderId = orderId
        self.productId = productId
        self.skuId = skuId
        self.productDiscount = productDiscount
        self.productDirectSub = productDirectSub

    def __repr__(self):
        if self.id:
            return '<RetailOrderDetail@id=%d,orderId=%d,productId=%d,skuId=%d,productDiscount=%f,productDirectSub=%f>' % (
                    self.id,self.orderId,self.productId,self.skuId,self.productDiscount,self.productDirectSub)
        else:
            return '<RetailOrderDetail@orderId=%d,productId=%d,skuId=%d,productDiscount=%f,productDirectSub=%f>' % (
                    self.orderId,self.productId,self.skuId,self.productDiscount,self.productDirectSub)