# -*- coding:utf-8 -*-

# 员工权限

from config.appconfig import db

class EmployAuthority(db.Model):
    __tablename__ = 't_employee_authority'
    id = db.Column('id',db.Integer,primary_key=True)
    shopId = db.Column('shop_id',db.Integer)
    employeeId = db.Column('employee_id'.db.Integer)
    authorityId = db.Column('authority_id',db.Integer)

    def __init__(self,shopId,employeeId,authorityId):
        self.shopId = shopId
        self.employeeId = employeeId
        self.authorityId = authorityId

    def __repr__(self):
        if self.id:
            return '<EmployAuthority@id=%d,shopId=%d,employeeId=%d,authorityId=%d>'%(
            self.id,self.shopId,self.employeeId,self.authorityId)
        else:
            return '<EmployAuthority@shopId=%d,employeeId=%d,authorityId=%d>'%(
            self.shopId,self.employeeId,self.authorityId)