class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        fibonacci = [0, 1, 1]
        for _ in range(n - 2):
            t_3 = sum(fibonacci)
            fibonacci[0] = fibonacci[1]
            fibonacci[1] = fibonacci[2]
            fibonacci[2] = t_3
        
        return fibonacci[2]

def test1():
    solution = Solution()
    n = 4

    assert solution.tribonacci(n) == 4