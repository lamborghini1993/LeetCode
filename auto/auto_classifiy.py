# -*- coding:utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2020-05-28 20:24:35
@Description: 自动分类
"""

import os
import sys
import argparse
import shutil


# def is_leetcode_file(filename):
#     for sp in ("-", "."):
#         num: str = filename.split(sp, 2)[0]
#         if num.isdigit():
#             return True
#     return False


class AutoClassifiy(object):
    def __init__(self, args) -> None:
        self.args = args
        self.files = set()

    def run(self):
        for filename in os.listdir("."):
            if os.path.isdir(filename):
                continue
            if not filename.endswith(".py"):
                continue

            realname = filename[:-3]

            num, name = None, None
            for sp in ("-", "."):
                lst = realname.split(sp, 2)
                if len(lst) != 2:
                    continue
                snum, endname = lst
                if snum.isdigit():
                    num = int(snum)
                    name = endname
                    break
            if not num:
                continue

            dirnum: int = num // 100 * 100
            dirname = f"{dirnum}-{dirnum+99}"
            destname = f"{num:>03}-{name}.py"
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            desf_full_file = os.path.join(dirname, destname)
            shutil.move(filename, desf_full_file)
            if self.args.commit:
                os.system(f"git add {desf_full_file}")
        
        if self.args.commit:
            os.system("git commit -m 'leetcode -auto'")
            os.system("git push")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="自动分类leetcode题目")
    parser.add_argument("-c", "--commit", type=int, default=0)
    args = parser.parse_args()
    AutoClassifiy(args).run()
