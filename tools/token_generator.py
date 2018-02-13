# -*-coding:utf-8 -*-
import time
import hashlib
import random
import string


def generate_token():
    m = hashlib.md5()
    m.update(bytes(str(time.time()), encoding='utf-8'))
    return m.hexdigest()


def generate_string(length=8):
    numOfNum = random.randint(1, length - 1)
    numOfLetter = length - numOfNum
    slcNum = [random.choice(string.digits) for i in range(numOfNum)]
    slcLetter = [random.choice(string.ascii_letters)
                 for i in range(numOfLetter)]
    slcChar = slcNum + slcLetter
    random.shuffle(slcChar)
    code = ''.join([i for i in slcChar]).upper()
    return code


def generate_employee_code(base=1000):
    return base + 1
