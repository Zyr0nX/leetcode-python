#Definition for a Node.
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def order(root: 'Node'):
            if not root:
                return None
            if root.children:
                for child in root.children:
                    order(child)
            res.append(root.val)
        order(root)
        return res
    
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)
        
        return res[::-1]
    
def test1():
    solution = Solution()
    root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])

    assert solution.postorder(root) == [5,6,3,2,4,1]