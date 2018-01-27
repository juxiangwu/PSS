# -*- coding:utf-8 -*-

# 商品库存变动信息

from config.appconfig import db

class ProductRepertoryChanged(db.Model):
    __tablename__ = 't_product_repertory_changed'
    id  = db.Column('id',db.Integer,primary_key=True)
    shopId = db.Column('shop_id',db.Integer)
    productId = db.Column('product_id',db.Integer)
    skuId = db.Column('sku_id',db.Integer)
    changedDate = db.Column('changed_date',db.Datetime)
    changedType = db.Column('changed_type',db.Integer)
    operatorId = db.Column('operator_id',db.Integer)

    def __init__(self,shopId,productId,skuId,changedDate,changedType,operatorId):
        self.shopId = shopId
        self.productId = productId
        self.skuId = skuId
        self.changedDate = changedDate
        self.changedType = changedType
        self.operatorId = operatorId

    def __repr__(self):
        if self.id:
            return '<ProductRepertoryChanged@id=%d,shopId=%d,productId=%d,skuId=%d>' % (self.id,self.shopId,self.productId,self.skuId)
        else:
            return '<ProductRepertoryChanged@shopId=%d,productId=%d,skuId=%d>' % (self.shopId,self.productId,self.skuId)
