class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        """
        合并然后在找中位数
        """
        lstResult = []
        i = j = 0
        while i < len(nums1) or j < len(nums2):
            if j >= len(nums2):
                lstResult.append(nums1[i])
                i += 1
                continue
            if i >= len(nums1):
                lstResult.append(nums2[j])
                j += 1
                continue
            if nums1[i] < nums2[j]:
                lstResult.append(nums1[i])
                i += 1
            else:
                lstResult.append(nums2[j])
                j += 1
        iLen = len(lstResult)
        if iLen % 2:
            return lstResult[iLen // 2]
        return (lstResult[iLen // 2 - 1] + lstResult[iLen // 2]) / 2


func = Solution().findMedianSortedArrays
print(func([1, 3], [2]))
print(func([1, 2], [3, 4]))
