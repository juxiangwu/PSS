# -*- coding:utf-8 -*-

# 支持方式

from config.appconfig import db

class PayTypeInfo(db.Model):
    __tablename__ = 't_pay_type_info'
    id = db.Column('id',db.Integer,primary_key = True)
    shopId = db.Column('shop_id',db.Integer)
    typeName = db.Column('type_name',db.String(128))
    typeValue = db.Column('type_value',db.String(128))

    def __init__(self,shopId,typeName,typeValue):
        self.shopId = shopId
        self.typeName = typeName
        self.typeValue = typeValue

    def __repr__(self):
        if self.id:
            return '<PayTypeInfo@id=%d,shopId=%d,typeName=%s,typeValue=%s>' %(
                    self.id,self.shopId,self.typeName,self.typeValue)
        else:
             return '<PayTypeInfoshopId=%d,typeName=%s,typeValue=%s>' %(
                    self.shopId,self.typeName,self.typeValue)