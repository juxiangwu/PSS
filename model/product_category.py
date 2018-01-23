# -*- coding:utf-8 -*-
# 商品分类

from config.appconfig import db

class ProductCategory(db.Model):
    __tablename__ = 't_product_category'
    id = db.Column('id',db.Integer,primary_key = True)
    name = db.Column('name',db.String(128))
    shopId = db.Column('shop_id',db.Integer)
    parentId = db.Column('category_parent_id',db.Integer)
    lft = db.Column('lft',db.Integer)
    rgt = db.Column('rgt',db.Integer)

    def __init__(self,name,shopId,parentId,lft = -1,rgt = -1):
        #self.id = 0
        self.name = name
        self.shopId = shopId
        self.parentId = parentId
        self.lft = lft
        self.rgt = rgt

    def __repr__(self):
        return '<ProductCategory@id=%d,name=%s,shopId=%d,parentId=%d>' % (self.id,self.name,self.shopId,self.parentId)
 
