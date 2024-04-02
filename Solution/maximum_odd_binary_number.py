class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ones = s.count('1')
        return '1' * (ones - 1) + '0' * (n - ones) + '1'
    
def test1():
    solution = Solution()
    s = "010"

    assert solution.maximumOddBinaryNumber(s) == "001"

def test2():
    solution = Solution()
    s = "0101"

    assert solution.maximumOddBinaryNumber(s) == "1001"