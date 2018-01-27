# -*-coding:utf-8 -*-
# 创建商品属性表

from config.appconfig import db

class ProductProperty(db.Model):
    __tablename__ = "t_product_property"
    id = db.Column('id',db.Integer,primary_key=True)
    shopId = db.Column('shop_id',db.Integer)
    productId = db.Column('product_id',db.Integer)
    propertyType = db.Column('prop_type',db.Integer)
    propertyName = db.Column('prop_name',db.String(128))
    propertyValue db.Column('prop_value',db.String(1024))

    def __init__(self,shopId,productId,propertyType,propertyName,propertyValue):
        self.shopId = shopId
        self.productId = productId
        self.propertyType = propertyType
        self.propertyName = propertyName
        self.propertyValue = propertyValue

    def __repr__(self):
        if self.id :
            return '<ProductProperty@id=%d,shopId=%d,productId=%d,productName=%s,productValue=%s>' %(self.id,
                    self.shopId,self.productId,self.propertyName,self.propertyValue)
        else:
            return '<ProductProperty@shopId=%d,productId=%d,productName=%s,productValue=%s>' %(
                    self.shopId,self.productId,self.propertyName,self.propertyValue)