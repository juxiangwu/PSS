# -*- coding:utf-8 -*-
# 供应商信息

from config.appconfig import db

class Supplier(db.Model):
    __tablename__ = 't_supplier_info'
    id = db.Column('id',db.Integer,primary_key = True)
    name = db.Column('name',db.String(128))
    address = db.Column('address',db.String(1024))
    mobilePhone = db.Column('phone',db.String(16))
    telephone = db.Column('telephone',db.String(32))
    fax = db.Column('fax',db.String(32))
    qq = db.Column('qq',db.String(16))
    shopId = db.Column('shop_id',db.Integer)
    userId = db.Column('owner_id',db.Integer)

    def __init__(self,name,shopId,userId,address=None,mobilePhone=None,telephone=None,fax=None,qq=None):
        #self.id = 0
        self.name = name
        self.address = address
        self.mobilePhone = mobilePhone
        self.telephone = telephone
        self.fax = fax
        self.qq = qq 
        self.shopId = shopId
        self.userId = userId

    def __repr__(self):
        if self.id:
            return '<Supplier@id=%d,userId=%d,shopId=%d,name=%s>' % (self.id,self.userId,self.shopId,self.name)
        else:
            return '<Supplier@userId=%d,shopId=%d,name=%s>' % (self.userId,self.shopId,self.name)
