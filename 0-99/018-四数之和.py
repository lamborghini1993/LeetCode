from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """双层循环遍历 + 头尾指针取值 + 剪枝"""
        result = []
        N = len(nums)
        visit = {}
        nums.sort()

        def find_two_sum(two_sum, l, r):
            sub_result = []
            while l < r:
                if nums[l] + nums[r] == two_sum:
                    sub_result.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < two_sum:
                    l += 1
                else:
                    r -= 1
            return sub_result

        for i in range(N - 3):
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                continue
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue

            for j in range(i + 1, N - 2):
                left_result = target - nums[i] - nums[j]

                if nums[j + 1] + nums[j + 2] > left_result:
                    continue
                if nums[-1] + nums[-2] < left_result:
                    continue

                sub_result = find_two_sum(left_result, j + 1, N - 1)
                for item in sub_result:
                    tinfo = (nums[i], nums[j], item[0], item[1])
                    if tinfo not in visit:
                        visit[tinfo] = True
                        result.append(tinfo)
        return result

    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     """双层循环遍历 + 头尾指针取值 AC"""
    #     result = []
    #     N = len(nums)
    #     visit = {}
    #     nums.sort()

    #     def find_two_sum(two_sum, l, r):
    #         sub_result = []
    #         while l < r:
    #             if nums[l] + nums[r] == two_sum:
    #                 sub_result.append([nums[l], nums[r]])
    #                 l += 1
    #             elif nums[l] + nums[r] < two_sum:
    #                 l += 1
    #             else:
    #                 r -= 1
    #         return sub_result

    #     for i in range(N - 3):
    #         for j in range(i + 1, N - 2):
    #             left_result = target - nums[i] - nums[j]
    #             sub_result = find_two_sum(left_result, j + 1, N - 1)
    #             for item in sub_result:
    #                 tinfo = (nums[i], nums[j], item[0], item[1])
    #                 if tinfo not in visit:
    #                     visit[tinfo] = True
    #                     result.append(tinfo)
    #     return result

    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     """头尾指针，移动计算  ERROR-应该用双层循环遍历"""
    #     result = []
    #     N = len(nums)
    #     visit = {}
    #     nums.sort()

    #     def find_two_sum(two_sum, l, r):
    #         sub_result = []
    #         while l < r:
    #             if nums[l] + nums[r] == two_sum:
    #                 sub_result.append([nums[l], nums[r]])
    #                 l += 1
    #             elif nums[l] + nums[r] < two_sum:
    #                 l += 1
    #             else:
    #                 r -= 1
    #         return sub_result

    #     l1, r1 = 0, N - 1
    #     cnt = 0
    #     while l1 < r1:
    #         left_result = target - nums[l1] - nums[r1]
    #         sub_result = find_two_sum(left_result, l1 + 1, r1 - 1)
    #         for item in sub_result:
    #             tinfo = (nums[l1], item[0], item[1], nums[r1])
    #             if tinfo not in visit:
    #                 visit[tinfo] = True
    #                 result.append(tinfo)
    #                 # result.append([nums[l1], item[0], item[1], nums[r1]])
    #         cnt += 1
    #         if cnt % 2:
    #             l1 += 1
    #         else:
    #             r1 -= 1
    #     return result

    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     """超时"""
    #     result = []
    #     N = len(nums)
    #     visit = {}
    #     nums.sort()
    #     for i in range(N - 3):
    #         for j in range(i + 1, N - 2):
    #             for k in range(j + 1, N - 1):
    #                 for l in range(k + 1, N):
    #                     tinfo = (nums[i], nums[j], nums[k], nums[l])
    #                     if nums[i] + nums[j] + nums[k] + nums[l] == target and tinfo not in visit:
    #                         result.append([nums[i], nums[j], nums[k], nums[l]])
    #                         visit[tinfo] = True
    #     return result


obj = Solution()
print(obj.fourSum(nums=[-3, -1, 0, 2, 4, 5], target=0))
print(obj.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
print(obj.fourSum(nums=[2, 2, 2, 2, 2], target=8))
print(obj.fourSum(nums=[0, 0, 0, 0], target=1))
print(obj.fourSum(nums=[1, 1, 1, 1, 1, 1, 1], target=4))
