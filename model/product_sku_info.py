# -*- coding:utf-8 -*-
# 商品SKU信息

from config.appconfig import db

class ProductSKUInfo(db.Model):
    __tablename__ = 't_product_sku_info'
    id = db.Column('id',db.Integer,primary_key = True)
    shopId = db.Column('shop_id',db.Integer)
    productId = db.Column('product_id',db.Integer)
    skuCode = db.Column('sku_code',db.String(128))
    storeCounts = db.Column('store_counts',db.Integer)

    def __init__(self,shopId,productId,skuCode,storeCounts=0):
        self.shopId = shopId
        self.productId = productId
        self.skuCode = skuCode
        self.storeCounts = storeCounts

    def __repr__(self):
        if self.id:
            return '<ProductSKUInfo@id=%d,shopId=%d,productId=%d,skuCode=%s,storeCounts=%d>' %(self.id,
                self.shopId,self.productId,self.skuCode,self.storeCounts)
        else:
            return '<ProductSKUInfo@shopId=%d,productId=%d,skuCode=%s,storeCounts=%d>' %(
                self.shopId,self.productId,self.skuCode,self.storeCounts)