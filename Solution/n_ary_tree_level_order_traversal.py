from collections import deque
from typing import List

#Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        res = [[root.val]]
        temp = deque()
        
        while queue:
            node = queue.popleft()
            
            for child in node.children:
                temp.append(child)
            
            if not queue:
                if temp:
                    res.append([x.val for x in temp])
                queue = temp
                temp = deque()

        return res