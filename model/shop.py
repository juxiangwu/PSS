# -*- coding:utf-8 -*-
# 定义商店信息

from config.appconfig import db

class Shop(db.Model):
    __tablename__ = "t_shop"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128))
    address = db.Column('address',db.String(1024))
    userId = db.Column("owner_id",db.Integer)

    def __init__(self,name,userId,address = None):
        #self.id = 0
        self.name = name
        self.address = address
        self.userId = userId

    def __repr__(self):
        return '<Shop@id=%d,userId=%d,name=%s>' % (self.id,self.userId,self.name)
