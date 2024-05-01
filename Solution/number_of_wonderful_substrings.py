from collections import defaultdict


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask = 0
        freq = defaultdict(int)
        res = 0
        for c in word:
            k = ord(c) - ord("a")
            mask ^= (1 << k) # flip bit k
            if mask & (mask - 1) == 0:
                res += 1

            res += freq[mask]
            freq[mask] += 1

            for odd_c in range(10):
                res += freq[mask ^ (1 << odd_c)]
        
        return res

def test1():
    solution = Solution()
    word = "aba"

    assert solution.wonderfulSubstrings(word) == 4