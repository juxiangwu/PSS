# -*- coding:utf-8 -*-

# 商店服务

from config.appconfig import db
from model.user import User
from model.shop import Shop
import datetime
class ShopService():
    REGISTER_SUCCESS = 0
    REGISTER_FAILED = -1
    SHOP_EXISTED = -2
    INVALID_DATA = -3

    def register(self,name,address,userId):
        now = datetime.datetime.now()
        shop = Shop(name=name,userId=userId,address = address,changedDate=now)
        isExisted = Shop.query.filter_by(name=name,userId=userId).first()
        if isExisted:
            return self.REGISTER_FAILED,self.SHOP_EXISTED
        db.session.add(shop)
        db.session.commit()
        return self.REGISTER_SUCCESS,shop.id

    def getShopsByUserId(self,userId):
        shops = Shop.query.filter_by(userId=userId).all()
        return shops

    def getShopById(self,id):
        shop = Shop.query.filter_by(id=id).first()
        return shop

    def getShopByName(self,name):
        shop = Shop.query.filter_by(name=name).first()
        return shop

    def updateShop(self,newshop):
        if newshop == None:
            return self.REGISTER_FAILED,self.INVALID_DATA
        oldshop = Shop.query.filter_by(id=newshop['id']).first()

        if oldshop.name != newshop['name'] and newshop['name']:
            isShopNameExisted = Shop.query.filter_by(name=newshop['name'],userId=newshop['id']).first()
            if isShopNameExisted != None:
                return self.REGISTER_FAILED,self.SHOP_EXISTED
        now = datetime.datetime.now()
        newshop['changedDate'] = now
        res = Shop.query.filter_by(id=newshop['id']).update(newshop)
        db.session.commit()
        return res