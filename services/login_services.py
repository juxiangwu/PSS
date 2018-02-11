# -*- coding:utf-8 -*-

from dao.user_dao import UserDAO
from model.user import User

class LoginService():
    def __init__(self):
        self.__userDao = UserDAO()

    def login(self,name,password):
        res = self.__userDao.loginByName(name,password)
        return res