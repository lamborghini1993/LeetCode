# 题目地址
- 英文：https://leetcode.com/problems/3sum-closest/
- 中文：https://leetcode-cn.com/problems/3sum-closest/

# 题意：
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

# 解题思路：
- 碰到这种问题解决方法：
    1. 排序
    2. 遍历一个数据i，将三数求和变为两数求和
    3. j = i + 1, k = len - 1 从两头开始遍历
- 每次遍历和target比较大小，
    1. < target时，j++，并且比较当前相差最小值+记录
    2. > target时，k--，并且记录当前相差最小值+记录
    3. = target时，直接返回target
<!--c++0-->
