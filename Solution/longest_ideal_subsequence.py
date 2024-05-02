class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for c in s:
            curr = ord(c) - ord("a")
            dp[curr] = max(dp[max(0, curr - k):min(26, curr + k + 1)]) + 1
        return max(dp)
    
def test1():
    solution = Solution()
    s = "acfgbd"
    k = 2

    assert solution.longestIdealString(s, k) == 5

def test2():
    solution = Solution()
    s = "eduktdb"
    k = 15

    assert solution.longestIdealString(s, k) == 4

def test3():
    solution = Solution()
    s = "znrkjnk"
    k = 8

    assert solution.longestIdealString(s, k) == 4

def test4():
    solution = Solution()
    s = "azaza"
    k = 25

    assert solution.longestIdealString(s, k) == 5