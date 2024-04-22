# Definition for a binary tree node.
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        queue = deque([root])
        res = [root.val]
        temp = deque()

        while queue:
            node = queue.popleft()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            
            if not queue:
                if temp:
                    res.append(sum([x.val for x in temp]) / len(temp))
                queue = temp
                temp = deque()

        return res