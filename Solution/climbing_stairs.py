class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        fib = [0, 1]
        for _ in range(n):
            next = sum(fib)
            fib[0] = fib[1]
            fib[1] = next
        
        return fib[1]
    
def test4():
    solution = Solution()
    n = 0

    assert solution.climbStairs(n) == 0
    
def test1():
    solution = Solution()
    n = 2

    assert solution.climbStairs(n) == 2

def test2():
    solution = Solution()
    n = 3

    assert solution.climbStairs(n) == 3

def test3():
    solution = Solution()
    n = 4

    assert solution.climbStairs(n) == 5