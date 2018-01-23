# -*- coding:utf-8 -*-
# 商店信息测试

from config.appconfig import db
from model.shop import Shop
from model.user import User

user = User.query.filter_by(id = 1).first()

print(user)

shop = Shop(name = 'Moyani',address = "Guangzhou",userId = user.id)
db.session.add(shop)
db.session.commit()
print(shop)
