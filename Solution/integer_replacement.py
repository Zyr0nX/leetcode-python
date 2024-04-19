import math


class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
            res += 1
        return res
    
def test1():
    solution = Solution()
    n = 8

    assert solution.integerReplacement(n) == 3

def test2():
    solution = Solution()
    n = 7

    assert solution.integerReplacement(n) == 4

def test3():
    solution = Solution()
    n = 65535

    assert solution.integerReplacement(n) == 17

def test4():
    solution = Solution()
    n = 3

    assert solution.integerReplacement(n) == 2

def test5():
    solution = Solution()
    n = 100

    assert solution.integerReplacement(n) == 8