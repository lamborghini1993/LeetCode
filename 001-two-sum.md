---
title: Git submodule使用和一键配置
date: 2018-12-05 19:42:15
categories:
- LeetCode
tags:
- LeetCode
- python3
---

# 题目地址
- 英文：https://leetcode.com/problems/two-sum/
- 中文：https://leetcode-cn.com/problems/two-sum/

# 题意：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

# 解题思路一：
1. 双重循环遍历，判断nums[i] + nums[j] = target（超时）
    - 很显然这种方式太暴力，时间复杂度为O(N*N)
2. 竟然给定了target，我们就可以根据一个值求出另一个值，然后在判断这个值是否在nums数组中，即可。（勉强飘过）
3. 遍历一次用字典存储起来，然后获取另一个值