# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2019-05-20 15:21:21
@UpdateDate: 2019-05-20 16:36:17
题目

给定一个 n*m 的矩阵 A ，矩阵中每一个元素为一个十六进制数。寻找一条从左上角都右下角的路径，每次只能向右或者向下移动，使得路径上所有数字之积在 16 进制下的后缀 0 最少。
输入描述：

    第一行：n, m (2 <= n,m <= 1000)
    接下来 n 行，每行 m 个 16 进制整数 0<= a_ij
    <=10^9

输出描述：

    第一行：最少后缀 0 的个数(十进制)
    第二行：路径方案，从左上角开始，">" 代表向右移动，"V" 代表向下移动。 如果有多种方案，输出字典序最小的方案(">" 的字典序小于 "V")。

示例：

输入

    3 3
    3 2 8
    c 8 8
    2 a f

输出

    1
    >>VV

说明
从左上角到右下角的所有路径中， 0x3 * 0x2 * 0x8 * 0x8 * 0xf = 0x1680 后缀 0 最少为 1， 且路径 “>>VV” 的字典序最小。
'''


import copy

lstSample = [
    [3, 2, 8],
    [12, 8, 8],
    [2, 10, 15]
]
lstSample = [
    [1, 4, 4],
    [2, 2, 4],
    [4, 2, 1]
]
N = len(lstSample)
M = len(lstSample[0])


class Record:
    def __init__(self, x):
        self.cnt = 0    # 0个数
        self.num = x    # 最后一位数
        self.pre = ">"
        self.Mod()

    def Mod(self):
        while self.num:
            if self.num % 16 == 0:
                self.cnt += 1
            else:
                self.num %= 16
                break
            self.num //= 16

    def Multip(self, obj, pre=">"):
        self.num *= obj.num
        self.cnt += obj.cnt
        self.pre = pre
        self.Mod()


dp = []
for x in range(N):
    lst = []
    for y in range(M):
        lst.append(Record(lstSample[x][y]))
    dp.append(lst)

result = 0
for x in range(1, M):
    obj1 = dp[0][x-1]
    obj2 = dp[0][x]
    obj2.Multip(obj1)

for y in range(1, N):
    obj1 = dp[y-1][0]
    obj2 = dp[y][0]
    obj2.Multip(obj1, "V")

for x in range(1, N):
    for y in range(1, M):
        obj1 = dp[x-1][y]
        obj2 = dp[x][y-1]
        obj_1 = dp[x][y]
        obj_2 = copy.deepcopy(obj_1)
        obj_1.Multip(obj1, "V")
        obj_2.Multip(obj2, ">")
        if obj_1.cnt <= obj_2.cnt:
            dp[x][y] = obj_1
        else:
            dp[x][y] = obj_2

print(dp[N-1][M-1].cnt)
s = ""
x = N-1
y = M-1
while x or y:
    c = dp[x][y].pre
    if c == ">":
        y -= 1
    else:
        x -= 1
    s = c+s
print(s)
