# -*- coding:utf-8 -*-

# 商品库存

from config.appconfig import db

class ProductRepertory(db.Model):
    __tablename__ = 't_product_repertory'
    id = db.Column('id',db.Integer,primary_key = True)
    shopId = db.Column('shop_id',db.Integer)
    productId = db.Column('product_id',db.Integer)
    skuId = db.Column('sku_id',db.Integer)
    totalCounts = db.Column('total_counts',db.Integer)

    def __init__(self,shopId,productId,skuId,totalCounts):
        self.shopId = shopId
        self.productId = productId
        self.skuId = skuId
        self.totalCounts = totalCounts
    
    def to_json(self):
        return {
            "id":self.id,
            "shopId":self.shopId,
            "productId":self.productId,
            "skuId":self.skuId,
            "totalCounts":self.totalCounts
        }

    def __repr__(self):
        if self.id:
            return '<ProductRepertory>@id=%d,shopId=%d,productId=%d,skuId=%d,totalCounts=%d>' %(
                    self.id,self.shopId,self.productId,self.skuId,self.totalCounts)

        else:
            return '<ProductRepertory>@shopId=%d,productId=%d,skuId=%d,totalCounts=%d>' %(
                    self.shopId,self.productId,self.skuId,self.totalCounts)
