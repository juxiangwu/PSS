# -*- coding:utf-8 -*-

# 商品库存变动明细

from config.appconfig import db
from config.constants import Constants

class ProductRepertoryChangedDetail(db.Model):
    __tablename__ = 't_product_repertory_changed_detail'
    id = db.Column('id',db.Integer,primary_key = True)
    shopId = db.Column('shop_id',db.Integer)
    recordId = db.Column('record_id',db.Integer)
    beforeCounts = db.Column('before_counts',db.Integer)
    afterCounts = db.Column('after_counts',db.Integer)

    def __init__(self,shopId,recordId,beforeCounts,afterCounts):
        self.shopId = shopId
        self.recordId = recordId
        self.beforeCounts = beforeCounts
        self.afterCounts = afterCounts

    def to_json(self):
        return {
            "id":self.id,
            "shopId":self.shopId,
            "recordId":self.recordId,
            "beforeCounts":self.beforeCounts,
            "afterCounts":self.afterCounts
        }

    def __repr__(self):
        if self.id:
            return '<ProductRepertoryChangedDetail@id=%d,shopId=%d,recordId=%d,beforeCounts=%d,afterCounts=%d>' % (
                self.id,self.shopId,self.recordId,self.beforeCounts,self.afterCounts)

        else:
            return '<ProductRepertoryChangedDetail@shopId=%d,recordId=%d,beforeCounts=%d,afterCounts=%d>' % (
                self.shopId,self.recordId,self.beforeCounts,self.afterCounts)