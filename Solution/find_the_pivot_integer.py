import math


class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot = math.sqrt(n * (n + 1) / 2)
        if pivot.is_integer():
            return int(pivot)
        return -1
    
def test1():
    solution = Solution()
    n = 8
    
    assert solution.pivotInteger(n) == 6

def test2():
    solution = Solution()
    n = 1
    
    assert solution.pivotInteger(n) == 1

def test3():
    solution = Solution()
    n = 4
    
    assert solution.pivotInteger(n) == -1