from collections import deque
import math

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [0] * len(ring)

        for key_index in range(len(key)):
            next_dp = [math.inf] * len(ring)
            for ring_index in range(len(ring)):
                for curr_index, curr in enumerate(ring):
                    if curr == key[key_index]:
                        min_dist = min(abs(ring_index - curr_index), len(ring) - abs(ring_index - curr_index))
                        next_dp[ring_index] = min(next_dp[ring_index], min_dist + 1 + dp[curr_index])
            
            dp = next_dp
        return min(dp)

    
def test1():
    solution = Solution()
    ring = "godding"
    key = "gd"

    assert solution.findRotateSteps(ring, key) == 4

def test2():
    solution = Solution()
    ring = "abccbaxbe"
    key = "abx"

    assert solution.findRotateSteps(ring, key) == 6