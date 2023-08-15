'''
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

示例 1：
输入：head = [1,2,2,1]
输出：true

示例 2：
输入：head = [1,2]
输出：false
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        node_list = []
        cur = head
        while cur:
            node_list.append(cur.val)
            cur = cur.next
        first, last = 0, len(node_list) - 1
        while first < last:
            if node_list[first] == node_list[last]:
                first += 1
                last -= 1
            else:
                return False
        return True
