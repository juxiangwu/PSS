# -*- coding:utf-8 -*-

# 商店服务

from config.appconfig import db
from model.user import User
from model.shop import Shop

class ShopService():
    REGISTER_SUCCESS = 0
    REGISTER_FAILED = -1
    SHOP_EXISTED = -2

    def register(self,name,address,userId):
        shop = Shop(name=name,userId=userId,address = address)
        isExisted = Shop.query.filter_by(name=name,userId=userId)
        if isExisted:
            return self.REGISTER_FAILED,self.SHOP_EXISTED
        db.session.add(shop)
        db.session.commit()
        return self.REGISTER_SUCCESS,shop.id

    