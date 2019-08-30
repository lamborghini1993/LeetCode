# Bytedance AI Camp 2018 -编程题2-(北京时间)05月26日 09时30分-05月26日 12时00分
# 解题思路  二分查找（Binary Search）
# 将数组nums拆分成m个子数组，每个子数组的和的范围在 [sum(nums) / m，sum(nums)]内
# 又因为数组nums中只包含非负整数，因此可以通过二分法在上下界内搜索最优解。
# 时间复杂度O(n * log m)，其中n是数组nums的长度，m为数组nums的和（准确的说应该是sum(nums)-sum(nums)/m）
# @Time   :2018/5/27
# @Author :LiuYinxing


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        size = len(nums)
        high = sum(nums)  # 确定上界
        low = high // m  # 确定下界 （下取整）
        while low <= high:
            mid = (low + high) // 2  # （下取整）
            n = m
            cnt = 0
            valid = True
            for x in range(size):
                if nums[x] > mid:  # 如果发现数列里面有一个大于目标解的，说明真正的解在右区间，即继续搜索右区间
                    valid = False
                    break
                if cnt + nums[x] > mid:  # 进行一次分割， 并初始化 n, cnt
                    n -= 1
                    cnt = 0
                cnt += nums[x]  # 统计每次分割的小区间的和，
                if n == 0:  # n == 0 说明划分的段数超过了 m，说明真正的解在右区间，即继续搜索右区间
                    valid = False
                    break
            if valid:  # 确定下一个要搜索的区间范围
                high = mid - 1  # valid == True 说明最优解还可以再小，即在左区间里面
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    solu = Solution()
    nums, m = [1, 4, 2, 3, 5], 3
    nums, m = [7, 2, 5, 10, 8], 2
    print(solu.splitArray(nums, m))
