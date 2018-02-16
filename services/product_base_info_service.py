# -*-coding:utf-8 -*-

from config.constants import Constants
from config.message_cn import MessageConstants_CN
from dao.product_base_info_dao import ProductBaseInfoDAO

import json
import datetime

class ProductBaseInfoService():
    def __init__(self):
        self.__dao = ProductBaseInfoDAO()
    
    def add(self,shopId,name,barcode,pinyinCode,categoryId,
                categoryName,unitName,puchasePrice,retailPrice,
                wholesalePrice,supplierName,supplierId,createDateTime,
                modifyDateTime,isEnabled=True):
        
        result = {}
         
        if not barcode:
           result['success'] = False
           result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            return result 

        now = datetime.datetime.now()
        code,res = self.__dao.add(name=name,code=code,barcode=barcode,pinyinCode=pinyinCode,categoryId=categoryId,
                        wholesalePrice=wholesalePrice,unitName=unitName,puchasePrice=puchasePrice,retailPrice=retailPrice,
                        modifyDateTime=now,isEnabled=True)
       
        
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.BARCODE_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_BARCODE_EXISTED % barcode
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
       
        return result

    def update(self,newdata):
        code,res = self.__dao.update(newdata)
        result = {}
        if code == Constants.REGISTER_FAILED
            result['success'] = False
            if res == Constants.BARCODE_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_BARCODE_EXISTED % newdata['barcode']
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return result

    def remove(self,id):
        code,res = self.__dao.remove(id)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return result

    def queryByShopId(self,shopId):
        datas = self.__dao.getByShopId(shopId=shopId)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
        jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        res = "{\"datas\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % total
        return res

    def queryById(self,id):
        data = self.__dao.getById(id = id)
        if not data:
            return "{\"datas\":[],\"total\":0}"
        return return "{\"datas\":" + json.dumps(data.to_json())+ ",\"total\":1}"

    def queryByShopIdWithPage(self,shopId,page = 1,pageSize = 50):
        datas = self.__dao.getByShopIdWithPage(shopId=shopId,page=page,pageSize=pageSize)
        if not datas:
            return "{\"datas\":[],\"total\":0}"
         jsonobjs = []
        total = len(datas)
        for data in datas:
            jsonobjs.append(data.to_json())
        res = "{\"datas\":" + json.dumps(jsonobjs) + ",\"total\":%d}" % total
        return res