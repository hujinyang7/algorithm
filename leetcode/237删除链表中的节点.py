'''
请编写一个函数，用于 删除单链表中某个特定节点 。在设计函数时需要注意，你无法访问链表的头节点 head ，只能直接访问 要被删除的节点
题目数据保证需要删除的节点 不是末尾节点
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #将想要删除的节点的值替换为它后面节点中的值，然后删除它之后的节点。
        node.val = node.next.val
        node.next = node.next.next
