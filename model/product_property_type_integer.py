# -*- coding:utf-8 -*-
# 整数类型商品属性

from config.appconfig import db

class ProductPropertyTypeInteger(db.Model):
    __tablename__ = 't_product_property_type_int'
    id = db.Column('id',db.Integer,primary_key=True)
    name = db.Column('name',db.String(128))
    value = db.Column('property_value',db.Integer)
    shopId =  db.Column('shop_id',db.Integer)
    productId = db.Column('product_id',db.Integer)

    def __init__(self,name,value,shopId,productId):
        self.name = name
        self.value = value
        self.shopId = shopId
        self.productId = productId

    def __repr__(self):
        return '<ProductPropertyTypeInteger@id=%d,name=%s,value=%d,shopId=%d,productId=%d>' % (self.id,
                self.name,self.value,self.shopId,self.productId)
    