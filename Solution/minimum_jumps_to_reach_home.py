from collections import deque
from typing import List

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        queue = deque([(0, 0, True)])
        visited = set(forbidden)
        upper_bound = max(x, max(forbidden)) + a + b
        while queue:
            position, jump, is_forward = queue.popleft()
            if position in visited:
                continue
            visited.add(position)
            if position == x:
                return jump
            
            if position + a <= upper_bound:
                queue.append((position + a, jump + 1, True))
            if position - b >= 0 and is_forward:
                queue.append((position - b, jump + 1, False))
            
        return -1
    
def test1():
    solution = Solution()
    forbidden = [8,3,16,6,12,20]
    a = 15
    b = 13
    x = 11

    assert solution.minimumJumps(forbidden, a, b, x) == -1

def test2():
    solution = Solution()
    forbidden = [1,6,2,14,5,17,4]
    a = 16
    b = 9
    x = 7

    assert solution.minimumJumps(forbidden, a, b, x) == 2

def test3():
    solution = Solution()
    forbidden = [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98]
    a = 29
    b = 98
    x = 80

    assert solution.minimumJumps(forbidden, a, b, x) == 121