# -*- coding:utf-8 -*-

# 商品基本信息表

from config.appconfig import db

class ProductBaseInfo(db.Model):
    __tablename__ = "t_product_base_info"
    id = db.Column('id',db.Integer,primary_key = True)
    shopId = db.Column('shop_id',db.Integer)
    name = db.Column('name',db.String(128))
    code = db.Column('code',db.String(128))
    barcode = db.Column('barcode',db.String(128))
    pinyinCode = db.Column('pinyin_code',db.String(128))
    categoryName = db.Column('category_name',db.String(128))
    categoryId = db.Column('category_id',db.Integer)
    unitName = db.Column('unit_name',db.String(128))
    puchasePrice = db.Column('puchase_price',db.Float)
    retailPrice = db.Column('sell_price',db.Float)
    wholesalePrice = db.Column('wholesale_price',db.Float)
    supplierName = db.Column('supplier_name',db.String(128))
    supplierId = db.Column('supplier_id',db.Integer)
    isEnabled = db.Column('is_enabled',db.Boolean)
    createDateTime = db.Column('create_datetime',db.DateTime)
    modifyDateTime = db.Column('modify_datetime',db.DateTime)
    
    def __init__(self,shopId,name,code,barcode,pinyinCode,categoryId,
                categoryName,unitName,puchasePrice,retailPrice,
                wholesalePrice,supplierName,supplierId,createDateTime,
                modifyDateTime,isEnabled):
        self.shopId = shopId
        self.name = name
        self.code = code
        self.barcode = barcode
        self.pinyinCode = pinyinCode
        self.categoryId = categoryId
        self.categoryName = categoryName
        self.unitName = unitName
        self.puchasePrice = puchasePrice
        self.wholesalePrice = wholesalePrice
        self.retailPrice = retailPrice
        self.supplierId = supplierId
        self.supplierName = supplierName
        self.createDateTime = createDateTime
        self.modifyDateTime = modifyDateTime
        self.isEnabled = isEnabled

    def __repr__(self):
        if self.id:
            return '<ProductBaseInfo@id=%d,name=%s,shopId=%d,categoryId=%d>' %(self.id,self.name,self.shopId,self.categoryId)
        else:
            return '<ProductBaseInfo@name=%s,shopId=%d,categoryId=%d>' %(self.name,self.shopId,self.categoryId)