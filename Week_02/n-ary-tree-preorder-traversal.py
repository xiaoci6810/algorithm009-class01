"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
"""
给定一个 N 叉树，返回其节点值的前序遍历。
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if root is None:
            return 
        res.append(root.val)
        for item in root.children:
            res += self.preorder(item)
        return res