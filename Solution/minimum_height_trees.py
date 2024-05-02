from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        node_map = defaultdict(set)
        for a, b in edges:
            node_map[a].add(b)
            node_map[b].add(a)

        leaves = deque()

        for node in node_map:
            if len(node_map[node]) == 1:
                leaves.append(node)

        while n > 2:
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for neighbor in node_map[node]:
                    node_map[neighbor].remove(node)
                    if len(node_map[neighbor]) == 1:
                        leaves.append(neighbor)
        
        return list(leaves)
        
    
def test1():
    solution = Solution()
    n = 4
    edges = [[1,0],[1,2],[1,3]]

    assert solution.findMinHeightTrees(n, edges) == [1]