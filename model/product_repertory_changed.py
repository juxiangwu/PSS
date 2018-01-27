# -*- coding:utf-8 -*-

# 商品库存变动信息

from config.appconfig import db

class ProductRepertoryChanged(db.Model):
    __tablename__ = 't_product_repertory_changed'
    id  = db.Column()