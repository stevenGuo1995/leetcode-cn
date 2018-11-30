# -*- coding: utf-8 -*-
"""
---------------------------- 
 @Time    : 2018/11/26 9:36
 @Author  : Mr.Guo
 @Site    : https://github.com/stevenguo1995
 @File    : 03_longest_substring_without_repeating.py
 @Software: PyCharm
----------------------------

题目：
----
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
----------------------------
示例1：
----
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
----------------------------
示例2：
----
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意！你的答案必须是‘子串’的长度，"pwke" 是一个子序列，不是子串。
---------------------------
"""


class Solution:
    def __init__(self, s):
        self.res = self.length_of_longest_substring(s)

    def length_of_longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        str_dict = {}
        con = 0
        for index, item in enumerate(s):
            if item in str_dict:
                con = max(str_dict[item], con)
            count = max(count, index - con + 1)
            str_dict[item] = index + 1

        return count


if __name__ == '__main__':
    print(Solution('biidygcc').res)
