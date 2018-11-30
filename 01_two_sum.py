# -*- coding: utf-8 -*-
"""
---------------------------- 
 @Time    : 2018/11/23 14:16
 @Author  : Mr.Guo
 @Site    : https://github.com/stevenguo1995
 @File    : 01_two_sum.py
 @Software: PyCharm
---------------------------- 

题目
----
01 两数之和
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
----------------------------
示例
----
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
----------------------------
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 方法一 遍历两次数组
        # l = len(nums)
        # for i in range(l - 1):
        #     for j in range(i + 1,l):
        #         if nums[i] + nums[j] == target:
        #             return i, j

        # 方法二 遍历一次数组
        for i in range(len(nums)):
            if target - nums[i] in nums[i + 1:]:
                print(nums[i + 1:])
                return i, nums[i + 1:].index(target - nums[i]) + i + 1

        # 方法三 字典
        # d = {}
        # for i, num in enumerate(nums):
        #     print(i,num)
        #     if target - num in d:
        #         return [d[target - num], i]
        #     d[num] = i


if __name__ == "__main__":
    n = [3, 2, 4, 11, 15]
    t = 6
    s = Solution()
    print(s.twoSum(n, t))
