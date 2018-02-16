# -*- coding:utf-8 -*-
# 商品SKU属性


from config.appconfig import db

class ProductSKUProperty(db.Model):
    __tablename__ = 't_product_sku_property'
    id = db.Column('id',db.Integer,primary_key = True)
    shopId = db.Column('shop_id',db.Integer)
    productId = db.Column('product_id',db.Integer)
    skuId = db.Column('sku_id',db.Integer)
    productProperties = db.Column('product_prop_id',db.String(128))

    def __init__(self,shopId,productId,skuId,productProperties):
        self.shopId = shopId
        self.productId = productId
        self.skuId = skuId
        self.productProperties = productProperties

    def to_json(self):
        return {
            "id":self.id,
            "productId":self.productId,
            "skuId":self.skuId,
            "productProperties":self.productProperties
        }

    def __repr__(self):
        if self.id:
            return '<ProductSKUProperty@id=%d,shopId=%d,productId=%d,skuId=%d,productProperties=%s>' %(
                self.id,self.shopId,self.productId,self.skuId,self.productProperties)
        else:
            return '<ProductSKUProperty@shopId=%d,productId=%d,skuId=%d,productProperties=%s>' %(
                self.shopId,self.productId,self.skuId,self.productProperties)