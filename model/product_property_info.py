# -*- coding:utf-8 -*-
# 商品属性信息表

from config.appconfig import db

class ProductPropertyInfo(db.Model):
    __tablename__ = 't_prodcut_property_info'
    id = db.Column('id',db.Integer,primary_key=True)
    propertyType = db.Column('property_type',db.Integer)
    shopId = db.Column('shop_id',db.Integer)
    productId = db.Column('product_id',db.Integer)

    def __init__(self,propertyType,shopId,productId):
        self.productId = productId
        self.shopId = shopId
        self.propertyType = propertyType

    def __repr__(self):
        return '<ProductPropertyInfo@id=%d,shopId=%d,productId=%d,propertyType=%d>' %(self.id,self.shopId,self.productId,self.propertyType)

