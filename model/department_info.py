# -*- coding:utf-8 -*-

# 创建部门

from config.appconfig import db

class Department(db.Model):
    __tablename__ = 't_department_info'
    id = db.Column('id',db.Integer,primary_key = True)
    shopId = db.Column('shop_id',db.Integer)
    name = db.Column('name',db.String(128))
    parentId = db.Column('parent_id',db.Integer)
    lft = db.Column('lft',db.Integer)
    rgt = db.Column('rgt',db.Integer)

    def __init__(self,shopId,name,parentId,lft=-1,rgt=-1):
        self.name = name
        self.shopId = shopId
        self.parentId = parentId
        self.lft = lft
        self.rgt = rgt

    def __repr__(self):
        if self.id:
            return '<Department@id=%d,shopId=%d,name=%s,parentId=%d>' %(
            self.id,self.shopId,self.name,self.parentId)
        else:
            return '<Department@shopId=%d,name=%s,parentId=%d>' % (
            self.shopId,self.name,self.parentId)
    