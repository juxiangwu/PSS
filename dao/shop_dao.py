# -*- coding:utf-8 -*-

# 商店服务

from config.appconfig import db
from model.user import User
from model.shop import Shop
from config.constants import Constants

import datetime
class ShopDAO():
    # REGISTER_SUCCESS = 0
    # REGISTER_FAILED = -1
    # SHOP_EXISTED = -2
    # INVALID_DATA = -3

    def add(self,name,userId,code,address=None):
        now = datetime.datetime.now()
        shop = Shop(name=name,userId=userId,address = address,changedDate=now,code=code)
        isExisted = Shop.query.filter_by(name=name,userId=userId).first()
        if isExisted:
            return Constants.REGISTER_FAILED,Constants.SHOP_EXISTED
        db.session.add(shop)
        db.session.commit()
        return Constants.REGISTER_FAILED,shop

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
            return Constants.REGISTER_FAILED,Constants.INVALID_ARGS
        oldshop = Shop.query.filter_by(id=newshop['id']).first()

        if oldshop.name != newshop['name'] and newshop['name']:
            isShopNameExisted = Shop.query.filter_by(name=newshop['name'],userId=newshop['id']).first()
            if isShopNameExisted != None:
                return Constants.REGISTER_FAILED,Constants.SHOP_EXISTED
        now = datetime.datetime.now()
        newshop['changedDate'] = now
        res = Shop.query.filter_by(id=newshop['id']).update(newshop)
        db.session.commit()
        return res