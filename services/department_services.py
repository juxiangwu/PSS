# -*-coding:utf-8 -*-

import json
from dao.department_dao import DepartmentDAO
from config.constants import Constants
from config.message_cn import MessageConstants_CN


class DepartmentService():
    def __init__(self):
        self.__dao = DepartmentDAO()

    def query_department(self, shopId, parentId):
        nodes = self.__dao.getChildNodes(shopId=shopId, parentId=parentId)
        jsonobjs = []
        for node in nodes:
            childCounts = self.__dao.getChildNodes(
                shopId=shopId, parentId=node.id)
            if len(childCounts) > 0:
                node.isLeaf = True
            else:
                node.isLeaf = False

            jsonobjs.append(node.to_json())
        total = len(nodes)
        res = {
            datas: jsonobjs,
            total: total}
        return json.dumps(res)
