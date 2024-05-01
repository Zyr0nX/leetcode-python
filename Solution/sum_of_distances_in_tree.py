from collections import defaultdict
from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        edges_map = defaultdict(list)
        subtree = [1] * n
        res = [0] * n
        for u, v in edges:
            edges_map[u].append(v)
            edges_map[v].append(u)
        def get_distance(node: int, parent: int):
            for neighbor in edges_map[node]:
                if neighbor != parent:
                    get_distance(neighbor, node)
                    subtree[node] += subtree[neighbor]
                    res[node] += res[neighbor] + subtree[neighbor]

        def reroot(root, pre):
            for i in edges_map[root]:
                if i != pre:
                    res[i] = res[root] - subtree[i] + n - subtree[i]
                    reroot(i, root)

        get_distance(0, -1)
        reroot(0, -1)
        return res
    
def test1():
    solution = Solution()
    n = 6
    edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]

    assert solution.sumOfDistancesInTree(n, edges) == [8,12,6,10,10,10]