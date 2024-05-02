class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return 0
        res = ""
        while n != 0:
            negBit = n % 2
            res = str(negBit) + res
            n = -(n // 2)
        
        return res
    
def test1():
    solution = Solution()
    n = 2

    assert solution.baseNeg2(n) == "110"