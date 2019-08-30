def findPath(maps, n, m):

    if n < 2 or n > 1000 or m < 2 or m > 1000:
        return None

    for i in range(n):  # 把16进制的数字转换成10进制
        for j in range(m):
            maps[i][j] = int(maps[i][j], 16)

    path = [[1] * m for _ in range(n)]  # 标记路径是否已经走过
    st, path[0][0] = [[0, 0, -1]], 0  # 初始化栈,并标记0 0 位置已经走过
    findp, min0 = [], float('inf')  # 记录路径和最小后缀零的个数

    while st:
        i, j, di = st[-1][0], st[-1][1], st[-1][2]  # 获取栈顶原始
        i1, j1, find = -1, -1, 0  # 下一个可能扩展的结点
        while di < 2 and find == 0:
            di += 1
            if di == 0:  # 向右
                i1, j1 = i, j + 1
            elif di == 1:  # 向下
                i1, j1 = i + 1, j
            if -1 < i1 < n and -1 < j1 < m and path[i1][j1] == 1:
                find = 1  # 找到

        if find == 1:  # 找到进栈
            st[-1][2] = di  # 当前栈顶的一个方向 进入下一个可走的方格
            st.append([i1, j1, -1])  # 入栈
            path[i1][j1] = 0  # 此位置已经走过

            if st[-1][0] == n - 1 and st[-1][1] == m - 1:  # 找到右下角
                product, count0, tmppath = 1, 0, ''  # 记录本次的乘积，后缀0的个数，和路径（字符串）
                for v in st:
                    product *= maps[v[0]][v[1]]  # 获取乘积
                    if v[2] == 0:
                        tmppath += '>'
                    elif v[2] == 1:
                        tmppath += 'V'

                product = hex(product)
                for i in range(len(product) - 1, 0, -1):  # 从倒数第一个字符开始计算
                    if product[i] == '0':
                        count0 += 1  # 统计后缀0的个数
                    else:
                        break  # 遇到不是0的字符串结束

                if count0 < min0:
                    min0, findp = count0, [tmppath]  # 找到后缀0更少的，更新min0, 清空findp并添加新的值
                elif count0 == min0:
                    findp.append(tmppath)  # 如果找到后缀0个数一样的，追加到findp里面

                path[st[-1][0]][st[-1][1]] = 1  # 出栈
                st.pop()
        else:
            path[st[-1][0]][st[-1][1]] = 1  # 出栈
            st.pop()
    print(min0)
    print(sorted(findp)[0])  # 对路径排序，输出第一个


if __name__ == '__main__':
    n, m = 3, 3
    maps = [['1', '4', '4'],
            ['2', '2', '4'],
            ['4', '2', '1']]
    n = 1000
    m = 1000
    maps = []
    for x in range(n):
        lst = []
        for y in range(m):
            lst.append('4')
        maps.append(lst)
    findPath(maps, n, m)
