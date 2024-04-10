# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root: Optional[TreeNode]):
            if not root:
                return None
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
    
def test1():
    solution = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))

    assert solution.inorderTraversal(root) == [1, 3, 2]