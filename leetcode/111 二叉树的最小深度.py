'''
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：2

示例 2：
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
         # 空树，高度为 0
        if not root:
            return 0
        # 初始化队列和层次
        queue = [root]
        depth = 1
        while queue:
            # 弹出当前层的所有节点，并将所有子节点入队列
            for i in range(len(queue)):
                current_node = queue.pop(0)
                if not current_node.left and not current_node.right:
                    return depth
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            depth += 1
        return depth
