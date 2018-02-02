# -*- coding:utf-8 -*-

# 供应商数据访问

from config.appconfig import db
from model.supplier import Supplier

class SupplierService():

    REGISTER_SUCCESS = 0
    REGISTER_FAILED = -1
    NAME_EXISTED = -2

    def add(self,name,shopId,userId,address=None,mobilePhone=None,
        telephone=None,fax=None,qq=None,email=None):
        supplier = Supplier(name=name,shopId=shopId,userId=userId,
                address=address,mobilePhone=mobilePhone,telephone=telephone,fax=fax,qq=qq,email=email)
        print(supplier)
        isNameExisted = Supplier.query.filter_by(name=name,shopId=shopId).first()

        if isNameExisted != None:
            return self.REGISTER_FAILED,self.NAME_EXISTED
        db.session.add(supplier)
        db.session.commit()
        return self.REGISTER_SUCCESS,supplier.id

    def getSupplierByName(self,name,shopId):
        supplier = Supplier.query.filter_by(name=name,shopId=shopId).first()
        return supplier

    def getSupplierById(self,id):
        supplier = Supplier.query.filter_by(id=id).first()
        return supplier

    def getSuppliersByShopId(self,shopId):
        suppliers = Supplier.query.filter_by(shopId=shopId).all()
        return suppliers

    def update(self,newsupplier):
        oldsupplier = Supplier.query.filter_by(id=newsupplier['id']).first()
        
        if oldsupplier.name != newsupplier['name'] and newsupplier['name']:
            isNameExisted = Supplier.query.filter_by(name=newsupplier['name'],shopId=newsupplier['shopId'])
            if isNameExisted:
                return self.REGISTER_FAILED,self.NAME_EXISTED
        
        res = Supplier.query.filter_by(id=newsupplier['id']).update(newsupplier)
        db.session.commit()
        return res