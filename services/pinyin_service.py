# -*-coding:utf-8 -*-

from model.pinyin import Pinyin
from dao.pinyin_dao import PinyinDao

class PinyinService():
    def __init__(self):
        self.__dao = PinyinDao()

    def query(self,hanzi):
        return self.__dao.query(hanzi=hanzi)

    def getPinyin(self,hanzilist):
        if not hanzilist:
            return None
        charts = list(hanzilist)
        pcs = []
        for char in charts:
            res = self.query(char)
            pcs.append(res.capital)
        return ''.join(pcs)
