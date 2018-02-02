# -*- coding:utf-8 -*-

# 员工信息

from config.appconfig import db

class EmployeeInfo(db.Model):
    __tablename__ = 't_employee_info'
    id = db.Column('id',db.Integer,primary_key = True)
    name = db.Column('name',db.String(128))
    password = db.Column('password',db.String(1024))
    telephone = db.Column('telephone',db.String(16))
    email = db.Column('email',db.String(512))
    departmentId = db.Column('department_id',db.Integer)
    roleId = db.Column('role_id',db.Integer)
    shopId = db.Column('shop_id',db.Integer)
    isEnabled = db.Column('is_enabled',db.Boolean)

    def __init__(self,name,password,shopId,
                roleId,departmentId,
                telephone=None,email=None,isEnabled=True):
        self.name = name
        self.shopId = shopId
        self.password = password
        self.roleId = roleId
        self.departmentId = departmentId
        self.telephone = telephone
        self.email = email
        self.isEnabled=isEnabled

    def __repr__(self):
        if self.id:
            return '<EmployeeInfo@id=%d,roleId=%d,departmentId=%d,name=%s>' %(
                self.id,self.roleId,self.departmentId,self.name)
        else:
            return '<EmployeeInfo@roleId=%d,departmentId=%d,name=%s>' %(
                self.roleId,self.departmentId,self.name)

       