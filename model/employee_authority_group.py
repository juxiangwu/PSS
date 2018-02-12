# -*- coding:utf-8 -*-
# 角色权限分组

from config.appconfig import db

class EmployeeAuthorityGroup(db.Model):
    __tablename__ = 't_role_authority_group'
    id = db.Column('id',db.Integer,primary_key=True)
    name = db.Column('name',db.String(128))
    shopId = db.Column('shop_id',db.Integer)
    authorityId = db.Column('authority_id',db.Integer)
    isLeaf = True
    def __init__(self,shopId,name,authorityId):
        self.shopId = shopId
        self.name = name
        self.authorityId = authorityId
        self.isLeaf = True

    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "shopId":self.shopId,
            "authorityId":self.authorityId,
            "leaf":True,
            "text":self.name
        }

    def __repr__(self):
        if self.id:
            return '<RoleAuthorityGroup@id=%d,shopId=%d,authorityId=%d,name=%s>' %(
                self.id,self.shopId,self.authorityId,self.name)
        else:
            return '<RoleAuthorityGroushopId=%d,authorityId=%d,name=%s>' %(
                self.shopId,self.authorityId,self.name)