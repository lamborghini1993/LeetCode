# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2019-05-20 19:27:14
@UpdateDate: 2019-05-21 14:21:01

问题描述：

卡牌游戏问题

小a和小b玩一个游戏，有n张卡牌，每张上面有两个正整数x，y。取一张牌时，个人积分增加x，团队积分增加y。求小a，小b各取若干张牌，使得他们的个人积分相等，且团队积分最大。

用例描述：

输入：
4  # n=4 组数据
3 1  # x, y
2 2
1 4
1 4
输出：10  # 团队积分最大为10


分析：
本题乍一看很像一道经典的“取与不取”的01背包问题（x当作重量 y当作价值）但是仍然存在很多问题需要注意

1、如何解决二人同时取的问题？

首先我们来分析一下 由于数据较大避免MLE 所以最多二维dp

但是本题中同时存在三个变量：二人的取法 以及此时取到第几张

由于最后要求二人数目一样

也就是要求二人数目差为0（划重点！！！）

所以我们将二人的取法根据二人数目差压缩为一个变量

由此可得：dp[i][j]表示取到第i张牌二人差为j时团队积分的最大值（1<=i<=n  -50000<=j<=50000)

dp[0][0]=0

2、如何解决y为负数的情况？

这里我们要用到一个技巧：状态偏移

所以我们可以用k+60000表示当j=k+10000的情况（多加一点避免出现其他状况）

由此可得：dp[i][j]表示取到第i张牌二人差为j-60000时团队积分的最大值（1<=i<=n  60000<=j<=120000)

dp[0][60000]=0

3、状态如何进行转移？

对于本题来讲 对于第i张牌存在3种状态：a取、b取、不取

但是这里要注意一点 并不是所有的dp[i][j]都是有效状态（不是所有到第i张牌的取法都能够找出差为j的方法）

如何处理这种状态？

首先我们将dp数组整体置为-1

由于不存在的状态一定不可能被其他方法取到（即dp[i][j]=-1)

而正常的dp[i][j]可以由max(dp[i-w[k][j]+c[k],dp[i][j-w[k]+c[k]）转移到

于是我们可以将两种状态统一起来

首先我们先将dp[i][j]由max(dp[i-w[k][j],dp[i][j-w[k])转移

不难推出如果dp[i][j]不为无效状态则dp[i][j]！=-1

如果dp[i][j]！=-1则dp[i][j]+=c[k]

同样的

dp[i][j]在保证第i张牌不取时可以由dp[i-1][j]转移

为了确保我们取到了最大的情况 可以对dp[i][j]和dp[i-1][j]的大小进行比较

如果dp[i-1][j]>dp[i][j] 就让dp[i][j]返回不取的情况（dp[i][j]=dp[i-1][j])

综上所述，我们得到的转移方程：

dp[i][j]=max(dp[i-1][j-x[i]],dp[i-1][j+x[i]])
   if(dp[i][j]!=-1)dp[i][j]+=y[i]
   if(dp[i][j]<dp[i-1][j])dp[i][j]=dp[i-1][j]
'''


def getMaxGain1(n, x, y):

    mx = max(x)  # 获取最大值，作为差的边界

    dp = [[0] * (mx+1) for _ in range(n+1)]  # 初始化dp

    for i in range(2, n+1):
        for j in range(mx+1):
            tmp1, tmp2 = 0, 0
            if j - x[i-1] >= 0:  # 这张卡牌给小a
                tmp1 = dp[i-1][j-x[i-1]] + y[i-1]

            if j + x[i - 1] <= mx:  # 这张卡牌给小b
                tmp2 = dp[i-1][j+x[i-1]] + y[i-1]

            dp[i][j] = max(dp[i - 1][j], tmp1, tmp2)  # 三种状态的最高得分

            if i == 1 and j == 0:  # 只有一张卡牌时
                dp[i][j] = 0
    return dp[n][0]


def getMaxGain2(n, x, y):
    mx = max(x)  # 获取最大值，作为差的边界
    dp = [[0] * (mx+1) for _ in range(n+1)]  # 初始化dp
    # dp[1][x[0]] = y[0]  # 第1张牌，a-b积分为x[0]的时候最大和为y[0],下标从1开始
    dp[1][x[0]] = y[0]

    for i in range(2, n+1):
        for j in range(mx+1):

            tmp1 = tmp2 = 0

            if j - x[i-1] >= 0 and dp[i-1][j-x[i-1]]:  # 这张卡牌给小b,相差积分为 j-x[i-1]
                tmp1 = dp[i-1][j-x[i-1]] + y[i-1]

            if j + x[i-1] <= mx and dp[i-1][j+x[i-1]]:  # 这张卡牌给小a,相差积分为 j + x[i-1]
                tmp2 = dp[i-1][j+x[i-1]] + y[i-1]
            dp[i][j] = max(tmp1, tmp2)
            if not dp[i][j]:
                dp[i][j] = y[i-1]
            dp[i][j] = max(dp[i - 1][j], dp[i][j])  # 三种状态的最高得分

    return dp[n][0]


def getMaxGain4(n, x, y):
    mx = max(x)  # 获取最大值，作为差的边界
    dp = [[0] * (mx+1) for _ in range(n+1)]  # 初始化dp
    dp[0][x[0]] = y[0]  # 第0张牌，a-b积分为x[0]的时候最大和为y[0],下标从0开始

    for i in range(1, n):
        for j in range(mx+1):

            tmp = 0

            if j - x[i] >= 0:  # 这张卡牌给小b,相差积分为 j-x[i-1]
                tmp = dp[i-1][j-x[i]]

            if j + x[i] <= mx:  # 这张卡牌给小a,相差积分为 j + x[i-1]
                tmp = dp[i-1][j+x[i]]

            if tmp:
                dp[i][j] = tmp + y[i]

            dp[i][j] = max(dp[i - 1][j], dp[i][j])  # 三种状态的最高得分

    return dp[n-1][0]


def getMaxGain(n, x, y):
    """正确答案"""
    mx = sum(x)  # 获取最大值，作为差的边界
    dp = [[-1] * (10010) for _ in range(n+1)]  # 初始化dp
    # dp[i][j] 表示两人相差积分为j时的值
    dp[0][0] = 0
    for i in range(1, n+1):
        for j in range(mx):
            #       第i张牌给a          第i张牌给b
            tmp = max(dp[i-1][j-x[i]], dp[i-1][j+x[i]])

            if tmp != -1:
                dp[i][j] = tmp + y[i]

            dp[i][j] = max(dp[i - 1][j], dp[i][j])  # 三种状态的最高得分

    return dp[n][0]


def Test():
    def fun(data):
        n = len(data)
        x = []
        y = []
        for i in data:
            x.append(i[0])
            y.append(i[1])
        sum_x = sum(x)
        buf = [-float('inf')] * (2 * sum_x + 1)
        buf[sum_x] = 0
        num = len(buf)
        for i in range(n):
            b = buf.copy()
            for j in range(num):
                if j + x[i] < num:
                    buf[j] = max(b[j], b[j + x[i]] + y[i])
                if j - x[i] >= 0:
                    buf[j] = max(buf[j], b[j - x[i]] + y[i])
        return buf[sum_x]

    a = [[3, 1], [2, 2], [1, 4], [1, 4]]
    print(fun(a))


if __name__ == '__main__':
    n = 4
    x = [0, 3, 2, 1, 1]
    y = [0, 1, 2, 4, 4]
    print(getMaxGain(n, x, y))
    Test()
