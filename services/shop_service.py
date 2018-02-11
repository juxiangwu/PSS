# -*-coding:utf-8 -*-

from config.constants import Constants
from config.message_cn import MessageConstants_CN
from model.shop import Shop
from dao.shop_dao import ShopDAO
from tools.token_generator import generate_string

class ShopService():
    def __init__(self):
        self.__dao = ShopDAO()

    def add(self,userId,name,address=None):
        code = generate_string()
        res_code,obj = self.__dao.add(name=name,address=address,userId=userId,code=code)
        result = {}
        if res_code == Constants.REGISTER_FAILED:
            result['success'] = False
            if obj == Constants.SHOP_EXISTED:
                result['msg'] = MessageConstants_CN.MSG_SHOP_NAME_EXISTED % name
            elif obj == Constants.INVALID_ARGS:
                result['msg'] = MessageConstants_CN.MSG_INVALID_ARGS
            else:
                result['msg'] = MessageConstants_CN.MSG_INTER_ERROR
        else:
            result['success'] = True
            result['data'] = obj.to_json()
        return result
        