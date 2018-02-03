# -*- coding:utf-8 -*-

# ??SKU????

from config.appconfig import db

class ProductSKUPropertyGroup(db.Model):
    __tablename__ = 't_product_sku_property_group'
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
            return '<ProductSKUPropertyGroup>@id=%d,shopId=%d,productId=%d,name=%s' %(
                self.id,self.shopId,self.productId,self.name)
        else:
            return '<ProductSKUPropertyGroup>@shopId=%d,productId=%d,name=%s' %(
                self.shopId,self.productId,self.name)