'''
给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历

示例 1：
输入：root = [1,null,2,3]
输出：[3,2,1]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recursion(node, return_list):
            if not node:
                return
            recursion(node.left, return_list)
            recursion(node.right, return_list)
            return_list.append(node.val)
        return_list = []
        recursion(root, return_list)
        return return_list
