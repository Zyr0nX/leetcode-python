# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node: Optional[TreeNode], is_left: bool):
            nonlocal res
            
            if not node:
                return

            if is_left and not node.left and not node.right:
                res += node.val
            
            if not node.left and not node.right:
                return

            dfs(node.left, True)
            dfs(node.right, False)
        
        dfs(root, False)
        return res
    
def test1():
    solution = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

    assert solution.sumOfLeftLeaves(root) == 24

def test2():
    solution = Solution()
    root = TreeNode(1, TreeNode(2))

    assert solution.sumOfLeftLeaves(root) == 24