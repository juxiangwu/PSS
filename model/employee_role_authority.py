# -*- coding:utf-8 -*-

# 员工权限授权

from config.appconfig import db

class EmployeeRoleAuthority(db.Model):
    __tablename__ = 't_role_authority'
    id = db.Column('id',db.Integer,primary_key=True)
    shopId = db.Column('shop_id',db.Integer)
    name = db.Column('name',db.String(128))
    roleValue = db.Column('role_value',db.Integer)


    def __init__(self,shopId,name,roleValue):
        self.shopId = shopId
        self.name = name
        self.roleValue = roleValue

    def __repr__(self):
        if self.id:
            return '<EmployeeRoleAuthority@id=%id,shopId=%d,name=%s,roleValue=%d>' %(
                self.id,self.shopId,self.name,self.roleValue)
            else:
                return '<EmployeeRoleAuthority@shopId=%d,name=%s,roleValue=%d>' % (
                self.shopId,self.name,self.roleValue)

    