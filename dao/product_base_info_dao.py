# -*- coding:utf-8 -*-

# 商品基本信息

import datetime
from config.appconfig import db
from config.constants import Constants
from model.product_base_info import ProductBaseInfo

class ProductBaseInfoDAO():

    def add(self,shopId,name,code,barcode,pinyinCode,categoryId,
                categoryName,unitName,puchasePrice,retailPrice,
                wholesalePrice,supplierName,supplierId,createDateTime,
                modifyDateTime,isEnabled=True):
        isBarcodeExisted = self.getByBarcode(shopId=shopId,barcode=barcode)
        if isBarcodeExisted:
            return Constants.REGSISTER_FAILED,Constants.BARCODE_EXISTED
        
        now = datetime.datetime.now()
        data = ProductBaseInfo(shopId=shopId,name=name,code=code,barcode=barcode,
                pinyinCode=pinyinCode,categoryId=categoryId,
                categoryName=categoryName,unitName=unitName,
                puchasePrice=puchasePrice,retailPrice=retailPrice,
                wholesalePrice=wholesalePrice,supplierName=supplierName,
                supplierId=supplierId,createDateTime=now,modifyDateTime=now,
                isEnabled=True)
        db.session.add(data)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,data

    def update(self,newdata):
        now = datetime.datetime.now()
        newdata['modifyDateTime'] = now
        res = ProductBaseInfo.query.filter_by(id=newdata['id']).update(newdata)
        db.session.commit()
        return res

    def remove(self,id):
        if not id:
            return Constants.INVALID_ARGS
        data = ProductBaseInfo.query.filter_by(id=id).first()
        res = db.session.remove(data)
        db.session.commit()
        return res

    def getById(self,id):
        if not id:
            return None
        data = ProductBaseInfo.query.filter_by(id=id).first()
        return data

    def getByShopId(self,shopId):
        if not shopId:
            return None
        datas = ProductBaseInfo.query.filter_by(shopId=shopId).all()
        return datas

    def getByShopIdWithPage(self,shopId,page = 1,pageSize=50):
        if not shopId: 
            return None
        datas = ProductBaseInfo.query.filter_by(shopId=shopId).limit(pageSize).offset((page-1) * pageSize).all()
        return datas

    def getByBarcode(self,shopId,barcode):
        if not shopId or not barcode:
            return None
        datas = ProductBaseInfo.query.filter_by(shopId=shopId,barcode=barcode).all()
        return datas

    def getByCode(self,shopId,code):
        if not shopId or not code:
            return None
        datas = ProductBaseInfo.query.filter_by(shopId=shopId,code=code).all()
        return datas

    def getBySupplierId(self,shopId,supplierId):
        if not shopId or not supplierId:
            return None
        datas = ProductBaseInfo.query.filter_by(shopId=shopId,supplierId=supplierId).all()
        return datas

