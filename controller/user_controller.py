# -*-coding:utf-8 -*-
from config.appconfig import app
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from tools.token_generator import generate_token
import os
    
@app.route("/login",methods=['POST'])
def login():
    return "Login"

@app.route('/register',methods=['GET'])
def register():
    return render_template('index2.html')


@app.route("/index")
def index():
    return "Index"

@app.route("/index/<shopId>")
def indexShop(shopId):
    return "index/shopId"