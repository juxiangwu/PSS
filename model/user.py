# -*- coding:utf-8 -*-

# 定义用户信息
from config.appconfig import db

class User(db.Model):
    __tablename__ = "t_user"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(1024))
    phone = db.Column(db.String(16))
    telephone = db.Column(db.String(32))
    fax = db.Column(db.String(32))
    qq = db.Column(db.String(32))
    email = db.Column(db.String(128))
    password = db.Column(db.String(1024))

    def __init__(self,name,password=None,phone=None,address=None,telephone=None,fax=None,qq=None,email=None):
        #self.id = 0
        self.name = name
        self.address = address
        self.phone = phone
        self.telephone = telephone
        self.fax = fax
        self.qq = qq
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User@id=%d,name=%s>' % (self.id,self.name)

