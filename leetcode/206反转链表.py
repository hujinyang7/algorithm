'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution():
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur != None:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
