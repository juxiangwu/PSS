# -*-coding:utf-8 -*-

import json
from dao.department_dao import DepartmentDAO
from config.constants import Constants
from config.message_cn import MessageConstants_CN


class DepartmentService():
    def __init__(self):
        self.__dao = DepartmentDAO()

    def query(self, shopId, parentId):
        nodes = self.__dao.getChildNodes(shopId=shopId, parentId=parentId)
        jsonobjs = []
        for node in nodes:
            childCounts = self.__dao.getChildNodes(
                shopId=shopId, parentId=node.id)
            if len(childCounts) > 0:
                node.isLeaf = False
            else:
                node.isLeaf = True

            jsonobjs.append(node.to_json())
        total = len(nodes)
        # res = {
        #     "datas": jsonobjs,
        #     "total": total}
        res = "{\"datas\":" + json.dumps(jsonobjs)+",\"total\":%d}" % (total)
        return res

    def add(self,shopId,parentId,name):
        code,res = self.__dao.add(shopId=shopId,name=name,parentId=parentId)
        result = {}
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.NAME_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_DEPARTMENT_NAME_EXISTED % (name)
            elif res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
            result['data'] = res.to_json()
        return code,result

    def remove(self,shopId,nodeId):
        self.__dao.deleteChildNodes(shopId=shopId,parentId=nodeId)
        if nodeId != -1:
            self.__dao.deleteNode(id=nodeId)
        # TODO:需要更新员工的部门信息
        result = {}
        result['success'] = True
        result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return Constants.REGISTER_SUCCESS,result

    
    def update(self,newdata):
        code,res = self.__dao.update(newdata)
        result = {}
        print('update:',code,res)
        if code == Constants.REGISTER_FAILED:
            result['success'] = False
            if res == Constants.NAME_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_DEPARTMENT_NAME_EXISTED % (newdata['name'])
            elif res == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['msg'] = MessageConstants_CN.MSG_OPERATE_SUCCESS
        return code,result
