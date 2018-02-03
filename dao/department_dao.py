# -*- coding:utf-8 -*-

# 部门
from sqlalchemy.sql import text
from config.appconfig import db
from model.department_info import Department

class DepartmentDAO():

    REGISTER_SUCCESS = 0
    REGISTER_FAILED = -1
    NAME_EXISTED = -2
    INVALID_ARGS = -3

    def add(self,shopId,name,parentId,lft=-1,rgt=-1):
        department = Department(shopId=shopId,name=name,parentId=parentId,lft=lft,rgt=rgt)
        isNameExisted = Department.query.filter_by(name=name,shopId=shopId).first()
        if isNameExisted:
            return self.REGISTER_FAILED,self.NAME_EXISTED
        db.session.add(department)
        db.session.commit()
        return self.REGISTER_SUCCESS,department.id

    def addWithDepartment(self,department):
        if not department:
            return self.REGISTER_FAILED,self.INVALID_ARGS
        res = self.add(shopId = department.shopId,parentId=department.parentId,name = department.name)
        return res
    
    def getNodeById(self,id):
        node = Department.query.filter_by(id=id).first()
        return node

    def getRootNodes(self,shopId):
        res = Department.query.filter_by(shopId=shopId,parentId=-1).all()
        return res

    def getChildNodes(self,shopId,parentId):
        res = Department.query.filter_by(shopId=shopId,parentId=parentId).all()
        return res

    def getAllChildNodes(self,shopId,parentId,children):
        #sql = 'select count(*) from t_department_info where shop_id=:shopId and parent_id=:parentId'
        #res = db.engine.execute(text(sql),shopId=shopId,parentId=parentId)
        results = Department.query.filter_by(shopId=shopId,parentId=parentId).all()
        # for row in res:
        #     counts = row[0]
        if results == None or len(results) == 0:
            return
        #results = Department.query.filter_by(shopId=shopId,parentId=parentId).all()
        for dp in results:
            children.append(dp)
            self.getAllChildNodes(shopId=shopId,parentId=dp.id,children=children)
    
    def deleteNode(self,id):
        child = Department.query.filter_by(id=id).first()
        db.session.delete(child)
        db.session.commit()

    def deleteChildNodes(self,shopId,parentId):
        nodes = []
        self.getAllChildNodes(shopId=shopId,parentId=parentId,children=nodes)
        for dp in nodes:
            self.deleteNode(id=dp.id)
        return len(nodes)

    def update(self,newnode):
        if not newnode:
            return self.REGISTER_FAILED,self.INVALID_ARGS
        node = Department.query.filter_by(id=newnode['id'])
        if node.name != newnode['name'] and newnode['name']:
            isNameExisted = Department.query.filter_by(name=newnode['name'],shopId=newnode['shopId'])
            if isNameExisted:
                return self.REGISTER_FAILED,self.NAME_EXISTED

        res = Department.query.filter_by(id=newnode['id']).update(newnode)
        db.session.commit()
        return res