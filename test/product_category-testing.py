# -*- coding:utf-8 -*-

# 商品信息测试

from config.appconfig import db
from model.shop import Shop
from model.user import User
from model.product_category import ProductCategory

user = User.query.filter_by(id = 1).first()
shop = Shop.query.filter_by(id = 4).first()

c1 = ProductCategory(name=u'商品分类',shopId = shop.id,parentId=-1)

db.session.add(c1)
db.session.commit()
print(c1)

c2 = ProductCategory(name=u'外套',shopId = shop.id,parentId = c1.id)
db.session.add(c2)
db.session.commit()
print(c2)