import datetime
from config.appconfig import db
from model.shop import Shop
from model.user import User
from model.product_category import ProductCategory
from model.product_base_info import ProductBaseInfo
from model.supplier import Supplier
from model.product_base_info import ProductBaseInfo
from model.product_property_type_integer import ProductPropertyTypeInteger

user = User.query.filter_by(id=1).first()
shop = Shop.query.filter_by(id=4).first()
category = ProductCategory.query.filter_by(id=6).first()
supplier = Supplier.query.filter_by(id=1).first()
product = ProductBaseInfo.query.filter_by(id=1).first()

ppti = ProductPropertyTypeInteger(name=u'红色',value=1,shopId=shop.id,productId=product.id)

db.session.add(ppti)
db.session.commit()
print(ppti)

