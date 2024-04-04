from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        for i in range(1,10):
            temp = i
            for j in range(i + 1, 10):
                temp = 10 * temp + j
                if temp in range(low, high + 1):
                    res.append(temp)
                    
        return sorted(res)

    
def test1():
    solution = Solution()
    low = 100
    high = 300
    
    assert solution.sequentialDigits(low, high) == [123,234]

def test2():
    solution = Solution()
    low = 1000
    high = 13000
    
    assert solution.sequentialDigits(low, high) == [1234,2345,3456,4567,5678,6789,12345]