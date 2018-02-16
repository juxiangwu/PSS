# -*-coding:utf-8 -*-

from model.pinyin import Pinyin
class PinyinDao():
    def query(self,hanzi):
        if not hanzi:
            return None
        res = Pinyin.query.filter_by(hanzi=hanzi).first()
        return res