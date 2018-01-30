# -*- coding:utf-8 -*-

# 商品属性分组

from config.appconfig import db

class ProductPropertyGroup(db.Model):
    __tablename__ = 't_product_property_group'
    id = db.Column('id',db.Integer,primary_key = True)
    shopId = db.Column('shop_id',db.Integer)
    productId = db.Column('product_id',db.Integer)
    name = db.Column('name',db.String(128))

    def __init__(self,shopId,productId,name):
        self.shopId = shopId
        self.productId = productId
        self.name = name

    def __repr__(self):
        if self.id:
            return '<ProductPropertyGroup@id=%d,shopId=%d,productId=%d,name=%s>' %(
                self.id,self.shopId,self.productId,self.name)
        else:
            return '<ProductPropertyGroup@shopId=%d,productId=%d,name=%s>' %(
                self.shopId,self.productId,self.name)
        