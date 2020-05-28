#!/bin/bash

cat words.txt | tr ' ' '\n' | tr -s '\n' | sort | uniq -c | sort -rn | awk '{print $2 " " $1}'

# tr ' ' '\n' # 将空格替换成换行
# tr -s '\n'  # 剔除连续的换行
# sort        # 排序
# uniq -c     # 每一行连续出现的次数
#     sort | uniq -c  # 通常一起使用，打印每个不同行出现的次数
# sort -rn    # -r 从大到小排序 -n按数字进行排序
# awk '{print $2 " " $1}' # 按空格拆分，输出"$2 $1"
