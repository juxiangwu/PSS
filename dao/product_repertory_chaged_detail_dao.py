# -*- coding:utf-8 -*-

# 库存变量明细
from config.appconfig import db
from config.constants import Constants
from model.product_repertory_changed_detail import ProductRepertoryChangedDetail

class ProductRepertoryChangedDetailDAO():
    
    def add(self,shopId,recordId,beforeCounts,afterCounts):
        if not shopId or not recordId or not beforeCounts or not afterCounts:
            return Constants.REGSISTER_FAILED,Constants.INVALID_ARGS
        
        prcd = ProductRepertoryChangedDetail(shopId=shopId,recordId=recordId,
                        beforeCounts=beforeCounts,afterCounts=afterCounts)
        db.session.add(prcd)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,prcd

    def getById(self,id):
        if not id:
            return None
        data = ProductRepertoryChangedDetail.query.filter_by(id=id).first()
        return data

    def getByRecordId(self,shopId,recordId):
        if not recordId or not shopId:
            return None
        datas = ProductRepertoryChangedDetail.query.filter_by(shopId=shopId,recordId=recordId).all()
        return datas
