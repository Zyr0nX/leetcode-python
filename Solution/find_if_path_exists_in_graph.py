from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        edges_map = defaultdict(list)
        for edge in edges:
            edges_map[edge[0]].append(edge[1])
            edges_map[edge[1]].append(edge[0])
        self.visited = []
        def dfs(node: int):
            if node == destination:
                return True
            self.visited.append(node)
            for node_neighbor in edges_map[node]:
                if node_neighbor not in self.visited:
                    return dfs(node_neighbor)
            
            return False
        
        return dfs(source)
    
def test1():
    solution = Solution()
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2

    assert solution.validPath(n, edges, source, destination) == True