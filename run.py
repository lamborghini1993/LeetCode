# -*- coding:utf-8 -*-
"""
@Author: lamborghini
@Date: 2018-12-08 10:02:02
@Desc: 
    1.自动将代码填充到markdown
    2.将markdown同步到hexo里面
"""

import os
import time

HEXO_DIE = "../lamborghini1993.github.io/source/_posts"
PYTHON_START = "```python "
PYTHON_END = "```"


def Time2Str(ti=-1, timeformat="%Y-%m-%d %H:%M:%S"):
    if ti < 0:
        ltime = time.localtime()
    else:
        ltime = time.localtime(ti)
    strtime = time.strftime(timeformat, ltime)
    return strtime


def Start():
    for sFile in os.listdir():
        if not sFile.endswith(".md"):
            continue
        lstResult = []
        lstLine = []
        sPython = ""
        curIndex = ""
        bIsPython = False
        pythonHead = os.path.splitext(sFile)[0]
        with open(sFile, "r", encoding="utf-8") as f:
            lstLine = f.readlines()
        for line in lstLine:
            if line.startswith(PYTHON_START):
                lstResult.append(line)
                bIsPython = True
                curIndex = line.replace(PYTHON_START, "")[:-1]
                if curIndex == "0":
                    curIndex = ""
            elif (len(line) == 3 and line == PYTHON_END) or line[:-1] == PYTHON_END:
                pFile = pythonHead + curIndex + ".py"
                with open(pFile, "r", encoding="utf-8") as f:
                    lines = f.read()
                    lstResult.append(lines)
                lstResult.append(line)
                bIsPython = False
                sPython = ""
            elif bIsPython:
                sPython += line
            else:
                lstResult.append(line)
        sResult = "".join(lstResult)
        Write2File(sResult, sFile)


def Write2File(sResult, sFile):
    with open(sFile, "w", encoding="utf-8") as f:
        f.write(sResult)
    sHexoFile = os.path.join(os.getcwd(), HEXO_DIE, "LeetCode-" + sFile)
    sHexoFile = os.path.abspath(sHexoFile)
    date = update = Time2Str()
    title = "LeetCode-" + os.path.splitext(sFile)[0]
    print(sHexoFile)
    if os.path.exists(sHexoFile):
        with open(sHexoFile, "r", encoding="utf-8") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if line.startswith("date: "):
                    date = line.replace("date: ", "")[:-1]
                    break
    hexoTitle = """---
title: %s
date: %s
update: %s
categories:
- LeetCode
tags:
- LeetCode
- python3
---
""" % (title, date, update)
    sResult = "%s\n%s" % (hexoTitle, sResult)
    sResult += "\n# github\n- https://github.com/lamborghini1993/LeetCode\n"
    with open(sHexoFile, "w", encoding="utf-8") as f:
        f.write(sResult)


if __name__ == "__main__":
    Start()
