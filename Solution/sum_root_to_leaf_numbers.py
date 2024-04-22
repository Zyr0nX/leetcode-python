# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], curr: int) -> int:
            if not node:
                return 0
            
            curr = curr * 10 + node.val

            if not node.left and not node.right:
                return curr
            
            return dfs(node.left, curr) + dfs(node.right, curr)
        
        return dfs(root, 0)