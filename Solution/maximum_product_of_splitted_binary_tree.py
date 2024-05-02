# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        total = 0
        def postorder(node: Optional[TreeNode]):
            if not node:
                return 0
            left = postorder(node.left)
            right = postorder(node.right)
            self.res = max(self.res, left * (total - left), right * (total - right))
            return left + right + node.val
        total = postorder(root)
        postorder(root)
        return self.res % (10**9 + 7)
    
def test1():
    solution = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))

    assert solution.maxProduct(root) == 110