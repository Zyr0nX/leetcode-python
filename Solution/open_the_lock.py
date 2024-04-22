from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        if "0000" in deadends_set:
            return -1
        
        queue = deque([("0000", 0)])
        visited = set("0000")
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            for i in range(4):
                for delta in [1, -1]:
                    new_node = list(node)
                    new_node[i] = str((int(new_node[i]) + delta) % 10)
                    new_node_str = "".join(new_node)
                    if (new_node_str not in visited and new_node_str not in deadends_set):
                        visited.add(new_node_str)
                        queue.append((new_node_str, depth + 1))

        return -1
    
def test1():
    solution = Solution()
    deadends = ["0000"]
    target = "0202"

    assert solution.openLock(deadends, target) == -1