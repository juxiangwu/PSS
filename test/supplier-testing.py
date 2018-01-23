# -*- coding:utf-8 -*-

# 供应商信息测试

from config.appconfig import db
from model.shop import Shop
from model.user import User
from model.supplier import Supplier

user = User.query.filter_by(id = 1).first()
shop = Shop.query.filter_by(id = 4,userId=1).first()

supplier = Supplier(name='EM',address='Guangzhou',mobilePhone = '13712345678',
                    telephone = '+86-020-12345678',fax='22456789',qq = '1000',
                    shopId = shop.id,userId = user.id)

db.session.add(supplier)
db.session.commit()
print(supplier)