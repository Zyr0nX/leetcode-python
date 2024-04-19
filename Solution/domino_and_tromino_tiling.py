class Solution:
    def numTilings(self, n: int) -> int:
        dp_d = [1, 2] + [0] * (n - 2)
        dp_t = [0, 0, 1] * (n - 2)
        for i in range(2, n):
            dp_d[i] = (dp_d[i-1] + dp_d[i-2] + dp_t[i-1] * 2) % 1000000007
            dp_t[i] = (dp_d[i - 2] + dp_t[i-1]) % 1000000007
        
        return dp_d[n-1]
    
def test1():
    solution = Solution()
    n = 3

    assert solution.numTilings(n) == 5