# -*- coding:utf-8 -*-

# ????

from config.appconfig import db

class EmployeeRole(db.Model):
    __tablename__ = 't_employee_role'
    id = db.Column('id',db.Integer,primary_key = True)
    shopId = db.Column('shop_id',db.Integer)
    name = db.Column('name',db.String(128))

    def __init__(self,shopId,name):
        self.shopId = shopId
        self.name = name

    def to_json(self):
        return{
            "id":self.id,
            "name":self.name,
            "shopId":self.shopId
        }

    def __repr__(self):
        if self.id:
            return '<EmployeeRole@id=%d,shopId=%d,name=%s>' % (
                self.id,self.shopId,self.name)
        else:
            return '<EmployeeRole@shopId=%d,name=%s>'%(self.shopId,self.name)

    