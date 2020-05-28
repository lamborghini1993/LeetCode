# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2020-05-28 20:24:35
@Description: 自动分类
'''

import os
import shutil

for filename in os.listdir("."):
    if os.path.isdir(filename):
        continue
    num: str = filename.split("-", 2)[0]
    if not num.isdigit():
        continue
    num: int = int(num) // 100 * 100
    dirname = f"{num}-{num+99}"
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    shutil.move(filename, os.path.join(dirname, filename))
