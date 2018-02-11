# -*- coding:utf-8 -*-
# 定义商店信息

from config.appconfig import db
import datetime

class Shop(db.Model):
    __tablename__ = "t_shop"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128))
    address = db.Column('address',db.String(1024))
    userId = db.Column("owner_id",db.Integer)
    code = db.Column('code',db.String(128))
    changedDate = db.Column('changed_date',db.DateTime)

    def __init__(self,name,userId,code,changedDate=None,address = None):
        #self.id = 0
        self.name = name
        self.address = address
        self.userId = userId
        self.changedDate = changedDate
        self.code = code
    # @staticmethod
    def to_json(self):
        return {
            'name':self.name,
            'address':self.address,
            'userId':self.userId,
            'changeDate':self.changedDate.strftime("%Y-%m-%d %H:%M:%S"),
            'code':self.code
        }
    
    # def __repr__(self):
    #     if self.id:
    #         return '<Shop@id=%d,userId=%d,name=%s>' % (self.id,self.userId,self.name)
    #     else:
    #         return '<Shop@userId=%d,name=%s>' % (self.userId,self.name)