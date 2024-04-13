import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.floor(math.sqrt(n))
    
def test1():
    solution = Solution()
    n = 3

    assert solution.bulbSwitch(n) == 1

def test2():
    solution = Solution()
    n = 0

    assert solution.bulbSwitch(n) == 0