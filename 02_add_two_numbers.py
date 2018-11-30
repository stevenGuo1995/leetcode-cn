# -*- coding: utf-8 -*-
"""
---------------------------- 
 @Time    : 2018/11/23 14:32
 @Author  : Mr.Guo
 @Site    : https://github.com/stevenguo1995
 @File    : 02_add_two_numbers.py
 @Software: PyCharm
---------------------------- 

题目
----
给出两个非空的链表用来表示两个非负的整数。

其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
---------------------------
示例
----
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
----------------------------
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class AddTwoNumbers:
    def __init__(self, l1, l2):
        self.result = self.add_two_numbers(l1, l2)

    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str_l1 = ''
        str_l2 = ''
        while l1 or l2:
            if l1:
                str_l1 += str(l1.val)
                l1 = l1.next

            if l2:
                str_l2 += str(l2.val)
                l2 = l2.next
        result = str(int(str_l1[::-1]) + int(str_l2[::-1]))

        head = cur = ListNode(0)
        for i in result:
            cur.next = ListNode(i)
            cur = cur.next
        return head.next


# if __name__ == '__main__':
#     pass
