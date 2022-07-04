'''
给你一个二叉树的根节点 root ， 检查它是否轴对称

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    双指针，p和q分别指向root的左右子树。
    深度优先搜索，p和q不同时就返回False，包括Nullptr和值不相等的情况。
    '''
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        p = root.left
        q = root.right
        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return dfs(p.left, q.right) and dfs(p.right, q.left)
        return dfs(p, q)
