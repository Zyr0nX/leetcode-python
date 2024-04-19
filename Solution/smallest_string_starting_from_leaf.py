# Definition for a binary tree node.
from typing import List, Optional
from string import ascii_lowercase

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node: Optional[TreeNode], word: str) -> str:
            if not node:
                return
            
            word = chr(node.val + ord("a")) + word
            if node.left and node.right:
                return min(dfs(node.left, word), dfs(node.right, word))
            if node.left:
                return dfs(node.left, word)
            if node.right:
                return dfs(node.right, word)
            
            return word
        
        return dfs(root, "")
    
def test1():
    solution = Solution()
    root = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))

    assert solution.smallestFromLeaf(root) == "dba"