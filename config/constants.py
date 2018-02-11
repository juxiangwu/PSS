# -*-coding:utf-8 -*-
# 常量

class Constants():
    REGISTER_SUCCESS = 0
    REGISTER_FAILED = -1
    NAME_EXISTED = -2
    INVALID_ARGS = -3
    BARCODE_EXISTED = -4
    PROP_VALUE_EXISTED = -5
    SHOP_EXISTED = -6

    # 商品属性类型
    # SKU
    PRODUCT_PROP_TYPE_SKU = 1
    # 整数
    PRODUCT_PROP_TYPE_INT = 2
    # 浮点
    PRODUCT_PROP_TYPE_FLOAT = 3
    # 字符串
    PRODUCT_PROP_TYPE_STRING = 4
    # 日期
    PRODUCT_PROP_TYPE_DATE = 5

    # 库存变动类型
    REPERTORY_CHANGED_TYPE_NONE = -1
    # 销售
    REPERTORY_CHANGED_TYPE_SELL = 1
    # 进货
    REPERTORY_CHANGED_TYPE_PURCHASE = 2
    # 销售退货
    REPERTORY_CHANGED_TYPE_SELL_RETURN = 3
    # 库存退货
    REPERTORY_CHANGED_TYPE_PURCHASE_RETURN = 4
    # 调入
    REPERTORY_CHANGED_TYPE_EX_IN = 5
    # 调出
    REPERTORY_CHANGED_TYPE_EX_OUT = 6

    # 支付方式
    # 现金
    PAY_TYPE_CASH = 1
    # 银行卡
    PAY_TYPE_BANKCARD = 2
    # 支付宝
    PAY_TYPE_ZHIFUBAO = 3
    # 微信
    PAY_TYPE_WEIXIN = 4
    # 会员卡
    PAY_TYPE_MEMBER_CARD = 5
    # 组合
    PAY_TYPE_COMPOSIZE = 6
