# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
给定一个二叉树，返回它的 前序 遍历。
"""


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if root is None:
                return 
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res