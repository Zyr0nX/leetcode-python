class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        num = 0
        for i in range(k):
            num = (num * 10 + 1) % k
            if num == 0:
                return i + 1
        
        return -1
    
def test1():
    solution = Solution()
    k = 6
    
    assert solution.smallestRepunitDivByK(6) == -1