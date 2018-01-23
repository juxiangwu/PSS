# -*- coding:utf-8 -*-

# 商品基本信息测试
import datetime
from config.appconfig import db
from model.shop import Shop
from model.user import User
from model.product_category import ProductCategory
from model.product_base_info import ProductBaseInfo
from model.supplier import Supplier

user = User.query.filter_by(id=1).first()
shop = Shop.query.filter_by(id=4).first()
category = ProductCategory.query.filter_by(id=6).first()
supplier = Supplier.query.filter_by(id=1).first()

print(user,shop,category)
now = datetime.datetime.now()
pbi = ProductBaseInfo(shopId = shop.id,name=u"牛仔外套",
                    code='WT001014',barcode='WT001014',
                    pinyinCode='MNDY',categoryName=category.name,
                    categoryId=category.id,unitName=u'件',
                    puchasePrice=100.0,retailPrice=259.0,
                    wholesalePrice=129.0,supplierId=supplier.id,
                    supplierName = supplier.name,isEnabled=True,
                    modifyDateTime=now,createDateTime=now)

db.session.add(pbi)
db.session.commit()
print(pbi)