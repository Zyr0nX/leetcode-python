from collections import defaultdict, deque
from typing import List

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted_set = set(restricted)
        if 0 in restricted_set:
            return 0
        
        map_edges = defaultdict(list)
        for a, b in edges:
            map_edges[a].append(b)
            map_edges[b].append(a)
        
        queue = deque([0])
        visited = set([0])
        res = 0
        while queue:
            node = queue.popleft()
            res += 1
            for next_node in map_edges[node]:
                if next_node not in restricted_set and next_node not in visited:
                    queue.append(next_node)
                    visited.add(next_node)
        
        return res