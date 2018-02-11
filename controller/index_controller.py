#-*- coding:utf-8 -*-

from config.appconfig import app
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import request
from flask import make_response
from tools.token_generator import generate_token
import os

@app.route('/home')
def home():
    ua = request.headers
    print(ua)
    rsp = make_response(render_template('all/index.html'))
    rsp.set_cookie('shopId','1')
    rsp.set_cookie('userId','1')
    return rsp # render_template("all/index.html")
# @app.route('/.js')
# def modern_js():
#     return render_template('modern/app.js')

@app.route('/classic.json')
def classic_json():
    return render_template("all/classic.json")

@app.route('/modern.json')
def modern_json():
   
    return render_template("all/modern.json")