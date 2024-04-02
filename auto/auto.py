# -*- coding:utf-8 -*-
'''
@Description: 一键自动生成markdown博客
@Author: lamborghini1993
@Date: 2018-03-12 17:42:58
@UpdateDate: 2019-05-16 20:32:50
'''

import os
import time

CODE_INFO = {
    "<!--python": (".py", "python"),
    "<!--c++": (".cpp", "C++"),
    "<!--go": (".go", "go"),
}

CODE_END = ["```", "```\n"]
HEXO_DIE = "../lamborghini1993.github.io/source/_posts/LeetCode"
g_NowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
HEXO_TITLE = """---
title: {TITLE}
date: {DATE}
update: {UPDATE}
categories:
- LeetCode
tags:
- LeetCode
{TAGS}
---
"""


def GetCode(sHead, fileIndex, codeSuffix, mdCodePre):
    sCodeFile = sHead + fileIndex + codeSuffix
    with open(sCodeFile, "r", encoding="utf-8") as f:
        lines = f.read()
    lines = "%s\n%s\n```\n" % (mdCodePre, lines)
    return lines


def Write2CurMD(lstResult, sFile):
    sResult = "".join(lstResult)
    with open(sFile, "w", encoding="utf-8") as f:
        f.write(sResult)
        print("write to %s" % sFile)


def Write2HexoMD(lstResult, sFile, setTags):
    sHexoFile = os.path.join(os.getcwd(), HEXO_DIE, "LeetCode-" + sFile)
    sHexoFile = os.path.abspath(sHexoFile)
    date = update = g_NowTime
    if os.path.exists(sHexoFile):
        with open(sHexoFile, "r", encoding="utf-8") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if line.startswith("date: "):
                    date = line.replace("date: ", "")[:-1]
                if line.startswith("update: "):
                    update = line.replace("update: ", "")[:-1]
    title = "LeetCode-" + os.path.splitext(sFile)[0]
    lstTags = ["- " + tag for tag in setTags]
    tags = "\n".join(lstTags)
    sHexoTitle = HEXO_TITLE
    sHexoTitle = sHexoTitle.replace("{TITLE}", title)
    sHexoTitle = sHexoTitle.replace("{DATE}", date)
    sHexoTitle = sHexoTitle.replace("{UPDATE}", update)
    sHexoTitle = sHexoTitle.replace("{TAGS}", tags)
    sResult = "".join(lstResult)
    sResult = "%s\n%s\n# github\n- https://github.com/lamborghini1993/LeetCode\n" % (sHexoTitle, sResult)
    with open(sHexoFile, "w", encoding="utf-8") as f:
        f.write(sResult)
        print("write -> %s" % sHexoFile)


def Code2MD(sFile):
    lstLine = []
    bIsCode = False  # 是否是代码阶段
    fileIndex = ""  # 代码文件后缀索引
    codeSuffix = ""
    mdCodePre = ""
    lstResult = []  # 结果
    setTags = set([])

    sHead = os.path.splitext(sFile)[0]
    with open(sFile, "r", encoding="utf-8") as f:
        lstLine = f.readlines()
    for i in range(len(lstLine)):
        line = lstLine[i]
        if bIsCode:
            if line in CODE_END:
                sCode = GetCode(sHead, fileIndex, codeSuffix, mdCodePre)
                lstResult.append(sCode)
                bIsCode = False
            continue

        bAdd = False
        for codeInfo, tInfo in CODE_INFO.items():
            if line.startswith(codeInfo):
                lstResult.append(line)
                mdCodePre = "```" + tInfo[1]
                codeSuffix = tInfo[0]
                setTags.add(tInfo[1])
                fileIndex = line.replace(codeInfo, "")[0]
                if fileIndex == "0":
                    fileIndex = ""

                if i + 1 < len(lstLine) and lstLine[i + 1].startswith(mdCodePre):   # 有代码
                    bIsCode = True
                else:   # 无代码
                    sCode = GetCode(sHead, fileIndex, codeSuffix, mdCodePre)
                    lstResult.append(sCode)
                    bAdd = True
                break

        if not bIsCode and not bAdd:
            lstResult.append(line)

    Write2CurMD(lstResult, sFile)
    Write2HexoMD(lstResult, sFile, setTags)


def Start():
    for sFile in os.listdir():
        if not sFile.endswith(".md"):
            continue
        Code2MD(sFile)


if __name__ == "__main__":
    Start()
