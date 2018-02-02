# -*- coding:utf-8 -*-

# 用户服务逻辑

from config.appconfig import db
from model.user import User
import datetime

class UserService():

    REGISTER_SUCCESS = 0
    REGISTER_FAILED = -1
    USER_NAME_EXISTED = -2
    USER_EMAIL_EXISTED = -3
    USER_NO_EXISTED = -4
    
    # 注册用户
    def register(self,name,passowrd,address=None,phone=None,telephone=None,fax=None,qq=None,email=None):
        # 检查用户是否存在
        isUserNameExisted = User.query.filter_by(name=name).first()
        if isUserNameExisted:          
            return self.REGISTER_FAILED,self.USER_NAME_EXISTED

        isUserEmailExisted = User.query.filter_by(email = email).first()
        if isUserEmailExisted:
            return self.REGISTER_FAILED,self.USER_EMAIL_EXISTED
        
        now = datetime.datetime.now()
        user = User(name=name,password=passowrd,address=address,phone=phone,
                    telephone=telephone,fax=fax,qq=qq,email=email,changedDate=now)
        db.session.add(user)
        db.session.commit()
        return self.REGISTER_SUCCESS,user.id

    # 使用用户名和密码登录
    def loginByName(self,name,password):
        user = User.query.filter_by(name=name,password=password).first()
        if user:
            return user.id
        else:
            return -1

    # 使用Email和密码登录
    def loginByEmail(self,email,password):
        user = User.query.filter_by(email= email,password=password).first()
        if user:
            return user.id
        else:
            return self.USER_NO_EXISTED
    
    # 通过用户名查询用户信息
    def getUserByName(self,name):
        user = User.query.filter_by(name=name).first()
        return user

    # 通过ID查询用户信息
    def getUserById(self,id):
        user = User.query.filter_by(id=id).first()
        return user

    # 更新用户
    def updateUser(self,user):
        oldUser = User.query.filter_by(id=user['id']).first()
        
        #print('oldUser:',oldUser)
       
        if oldUser.name != user['name'] and user['name']:
            isNameExisted = User.query.filter_by(name = user['name']).first()
           
            if isNameExisted != None:
                return self.REGISTER_FAILED,self.USER_NAME_EXISTED
        
        if oldUser.email != user['email'] and user['email']:
            isEmailExisted = User.query.filter_by(email=user['email']).first()
            if isEmailExisted != None:
                return self.REGISTER_FAILED,self.USER_EMAIL_EXISTED
        now = datetime.datetime.now()
        user['changedDate'] = now
        #print("UserService:updateUser:",user)
        res = User.query.filter_by(id=user['id']).update(user)
        db.session.commit()
        # return res
        return res