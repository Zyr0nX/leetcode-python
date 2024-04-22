# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val, root)
            return newRoot
        
        def add(node: Optional[TreeNode], currDepth: int) -> Optional[TreeNode]:
            if not node:
                return
            
            if currDepth == depth - 1:
                node = TreeNode(node.val, TreeNode(val, node.left), TreeNode(val, None, node.right))

            node.left = add(node.left, currDepth + 1)
            node.right = add(node.right, currDepth + 1)
            
            return node
        
        root = add(root, 1)
        return root