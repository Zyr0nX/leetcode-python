class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        # breakpoint = target // 2
        # if n < breakpoint:
        #     return n * (n + 1) // 2
        # res = breakpoint * (breakpoint + 1) // 2 + (target + target + n - breakpoint - 1) * (n - breakpoint) // 2
        # return res % (10 ** 9 + 7)
    
        breakpoint = target // 2
        if n < breakpoint:
            return n * (n + 1) // 2
        res = breakpoint * (breakpoint + 1) // 2 + (target * 2 + n - breakpoint - 1) * (n - breakpoint) // 2
        return res % (10 ** 9 + 7)
    
def test1():
    solution = Solution()
    n = 2
    target = 3

    assert solution.minimumPossibleSum(n, target) == 4

def test2():
    solution = Solution()
    n = 13
    target = 50

    assert solution.minimumPossibleSum(n, target) == 91