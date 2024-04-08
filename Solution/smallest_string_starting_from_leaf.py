# Definition for a binary tree node.
from typing import Optional
from string import ascii_lowercase

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        stack = []
        ans = ""
        def dfs(node: Optional[TreeNode], word,):
            if not node:
                stack.pop()
            stack.append(chr(node.val + 97))
            if not node.left and not node.right:
                if ans != "":
                    ans = min(ans, "".join(stack))
                else:
                    ans = "".join(stack)
            dfs(node.left)
            dfs(node.right)
                
        dfs(root)

        return ans
    
def test1():
    solution = Solution()
    root = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))

    assert solution.smallestFromLeaf(root) == "dba"