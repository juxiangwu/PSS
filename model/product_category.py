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
    isLeaf = False

    def __init__(self,name,shopId,parentId,lft = -1,rgt = -1):
        #self.id = 0
        self.name = name
        self.shopId = shopId
        self.parentId = parentId
        self.lft = lft
        self.rgt = rgt

    #@staticmethod
    def to_json(self):
        # if obj is ProductCategory:
        return {
                "id":self.id,
                "name": self.name,
                "text": self.name,
                "shopId":self.shopId,
                "pid":self.parentId,
                "leaf":self.isLeaf,
                "lft":self.lft,
                "rgt":self.rgt
            }
        # else:
        #     return {}
    # def __repr__(self):
    #     if self.id:
    #         return '<ProductCategory@id=%d,name=%s,shopId=%d,parentId=%d>' % (self.id,self.name,self.shopId,self.parentId)
    #     else:
    #         return '<ProductCategory@name=%s,shopId=%d,parentId=%d>' % (self.name,self.shopId,self.parentId)
