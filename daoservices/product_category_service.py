# -*- coding:utf-8 -*-

# 商品分类
from config.appconfig import db
from config.constants import Constants
from model.product_category import ProductCategory

class ProductCategoryService():

    def add(self,shopId,name,parentId,lft=-1,rgt=-1):
        if not shopId or not name or not parentId:
            return Constants.REGSISTER_FAILED,Constants.INVALID_ARGS
        isNameExisted = ProductCategory.query.filter_by(shopId=shopId,name=name).first()
        
        if isNameExisted:
            return Constants.REGSISTER_FAILED,Constants.INVALID_ARGS
        
        pc = ProductCategory(name=name,shopId=shopId,parentId=parentId,lft=lft,rgt=rgt)
        db.session.add(pc)
        db.session.commit()
        return Constants.REGISTER_SUCCESS,pc

    def getNodeById(self,id):
        if not id:
            return None
        node = ProductCategory.query.filter_by(id=id).first()
        return node
    
    def getRootNodes(self,shopId):
        if not shopId:
            return None
        nodes = ProductCategory.query.filter_by(shopId=shopId,parentId=-1).all()
        return nodes

    def getChildNodes(self,shopId,parentId):
        if not shopId or not parentId:
            return None
        nodes = ProductCategory.query.filter_by(shopId=shopId,parentId=parentId).all()
        return nodes

    def getAllChildNodes(self,shopId,parentId,nodes):
        results = ProductCategory.query.filter_by(shopId=shopId,parentId=parentId).all()
        if results == None or len(results) == 0:
            return
        for pc in results:
            nodes.append(pc)
            self.getAllChildNodes(shopId=shopId,parentId=pc.id,nodes = nodes)
    
    def deleteNode(self,id):
        child = ProductCategory.query.filter_by(id=id).first()
        res = db.session.delete(child)
        db.session.commit()
        return res

    def deleteChildNodes(self,shopId,parentId):
        nodes = []
        self.getAllChildNodes(shopId=shopId,parentId=parentId,nodes=nodes)
        for node in nodes:
            self.deleteNode(id = node.id)
        return len(nodes)

    def update(self,newdata):
        if not newdata or not newdata['id'] or not newdata['shopId']:
            return Constants.REGSISTER_FAILED,Constants.INVALID_ARGS

        olddata = ProductCategory.query.filter_by(id=newdata['id']).first()
        if olddata.name != newdata['name'] and newdata['name']:
            isNameExisted = ProductCategory.query.filter_by(name=newdata['name'],shopId=newdata['shopId']).first()
            if isNameExisted:
                return Constants.REGSISTER_FAILED,Constants.NAME_EXISTED
        
        res = ProductCategory.query.filter_by(id=newdata['id']).update(newdata)
        db.session.commit()
        return res