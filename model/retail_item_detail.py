# -*- coding:utf-8 -*-

# ????

from config.appconfig import db

class RetailItemDetail(db.Model):
    __tablename__ = 't_retail_item_detail'
    id = db.Column('id',db.Integer,primary_key = True)
    shopId = db.Column('shop_id',db.Integer)
    orderId = db.Column('order_id',db.Integer)
    productId = db.Column('product_id',db.Integer)
    skuId = db.Column('sku_id',db.Integer)
    productDiscount = db.Column('product_discount',db.Float)
    productDirectSub = db.Column('product_directly_sub',db.Float)
    payType = db.Column('pay_type',db.Integer)
    retailPrice = db.Column('retail_price',db.Float)

    def __init__(self,shopId,orderId,productId,skuId,
            productDiscount,productDirectSub,payType,retailPrice):

        self.shopId = shopId
        self.orderId = orderId
        self.productId = productId
        self.skuId = skuId
        self.productDiscount = productDiscount
        self.productDirectSub = productDirectSub
        self.payType = payType
        self.retailPrice = retailPrice

    def to_json(self):
        return {
            "id":self.id,
            "shopId":self.shopId,
            "orderId":self.orderId,
            "productId":self.productId,
            "skuId":self.skuId,
            "productDiscount":self.productDiscount,
            "productDirectSub":self.productDirectSub,
            "payType":self.payType,
            "retailPrice":self.retailPrice
        }

    def __repr__(self):
        if self.id:
            return '<RetailOrderDetail@id=%d,orderId=%d,productId=%d,skuId=%d,productDiscount=%f,productDirectSub=%f>' % (
                    self.id,self.orderId,self.productId,self.skuId,self.productDiscount,self.productDirectSub)
        else:
            return '<RetailOrderDetail@orderId=%d,productId=%d,skuId=%d,productDiscount=%f,productDirectSub=%f>' % (
                    self.orderId,self.productId,self.skuId,self.productDiscount,self.productDirectSub)