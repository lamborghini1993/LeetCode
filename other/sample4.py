# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2019-05-20 17:42:17
@UpdateDate: 2019-05-20 17:47:19
两个同样大小的数组，a,b。统计MAX(a[l,k]) < MIN(b[l,k])的总数，即是在某一段相同始末位置的子数组中，a的该子数组的最大值如果小于b的对应的子数组的最小值则计数1。
思路：对于[l , k]区间来说，随着k变大 max( a[l,k+1] )>=max( a[l,k] ),
min(b[l,k+1])<=min(b[l,k])。这两条单调的性质意味着找到最大的k，使得：
max(a[l,k]) < max(b[l,k])，计数器加（k - l + 1）. 利用二分法，复杂度为O(nlog(n)).
'''


def fun(a, b):
    n = len(a)
    num = 0
    for i in range(n):
        left = i
        right = n-1
        while left <= right:
            # mid = left + (right - left)//2
            mid = (right + left) // 2
            if max(a[i:mid+1]) >= min(b[i:mid+1]):
                right = mid - 1
            else:
                left = mid + 1
        if max(a[i:mid+1]) < min(b[i:mid+1]):
            num += mid - i + 1
        else:
            num += mid - i
    return num


a = [1, 1, 2, 1, 1, 1]
b = [1, 2, 3, 4, 5, 6]

a = [4, 5, 6, 10, 9]
b = [7, 8, 9, 9, 10]
print(fun(a, b))
