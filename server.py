# -*-coding:utf-8 -*-

from config.appconfig import app

from controller import interceptor
from controller import index_controller
from controller import user_controller
from controller import product_category_controller
from controller import shop_controller
from controller import department_controller
from controller import paytype_controller

app.run(debug=True,host='0.0.0.0',port=3000)
