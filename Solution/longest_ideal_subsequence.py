class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * len(s)
        for c in s:
            