from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        res = []

        while queue:
            count = 0
            for _ in range(len(queue)):
                curr = queue.popleft()
                count += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(count) 
        if k > len(res):
            return -1
        else:       
            return sorted(res)[-k]
                
def test1():
    solution = Solution()
    root = TreeNode(5, TreeNode(8, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(1)), TreeNode(9, TreeNode(3), TreeNode(7)))
    k = 2

    assert solution.kthLargestLevelSum(root, k) == 13

def test2():
    solution = Solution()
    root = TreeNode(5, TreeNode(8, TreeNode(2), TreeNode(1)), TreeNode(9, TreeNode(3), TreeNode(7)))
    k = 4

    assert solution.kthLargestLevelSum(root, k) == -1

def test3():
    solution = Solution()
    root = TreeNode(411310, TreeNode(211244), TreeNode(111674))
    k = 2

    assert solution.kthLargestLevelSum(root, k) == 322918