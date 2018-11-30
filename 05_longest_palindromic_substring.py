# -*- coding: utf-8 -*-
"""
---------------------------- 
 @Time    : 2018/11/30 10:01
 @Author  : Mr.Guo
 @Site    : https://github.com/stevenguo1995
 @File    : 05_longest_palindromic_substring.py
 @Software: PyCharm
----------------------------

题目：
----
给定一个字符串 s，找到 s 中最长的回文子串。
你可以假设 s 的最大长度为 1000。
----------------------------
示例：
----
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
----------------------------
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp_str = ''
        res_str = ''
        for index, item in enumerate(s):
            temp_str += item
