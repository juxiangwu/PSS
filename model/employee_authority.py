# -*- coding:utf-8 -*-

# 员工权限

from config.appconfig import db


class EmployeeAuthority(db.Model):
    __tablename__ = 't_employee_authority'
    id = db.Column('id', db.Integer, primary_key=True)
    shopId = db.Column('shop_id', db.Integer)
    employeeId = db.Column('employee_id', db.Integer)
    authorityId = db.Column('authority_id', db.Integer)
    authorityGroupId = db.Column('authority_group_id', db.Integer)

    def __init__(self, shopId, employeeId, authorityId, authorityGroupId):
        self.shopId = shopId
        self.employeeId = employeeId
        self.authorityId = authorityId
        self.authorityGroupId = authorityGroupId

    def to_json(self):
        return {
            "id": self.id,
            "shopId": self.shopId,
            "employeeId": self.employeeId,
            "authorityId": self.authorityId,
            "authorityGroupId": self.authorityGroupId
        }

    def __repr__(self):
        if self.id:
            return '<EmployAuthority@id=%d,shopId=%d,employeeId=%d,authorityId=%d>' % (
                self.id, self.shopId, self.employeeId, self.authorityId)
        else:
            return '<EmployAuthority@shopId=%d,employeeId=%d,authorityId=%d>' % (
                self.shopId, self.employeeId, self.authorityId)
