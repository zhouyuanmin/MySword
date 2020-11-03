"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

来源：力扣
链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]

限制：
0 <= 链表长度 <= 10000
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_print(self, head: ListNode) -> List[int]:
    nodes: List = []
    while head:
        nodes.insert(0, head.val)
        head = head.next
    return nodes
