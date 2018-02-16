# -*-coding:utf-8 -*-
from config.appconfig import db

class Pinyin(db.Model):
    __tablename__ = "t_pinyin"
    id = db.Column('id',db.Integer,primary_key=True)
    hanzi = db.Column('hanzi',db.String(128))
    capital = db.Column('capital',db.String(128))

    def __init__(self,hanzi,cap):
        self.hanzi = hanzi
        self.capital = cap

    def __repr__(self):
        return '<hanzi=%s,cap=%s>' % (self.hanzi,self.capital)