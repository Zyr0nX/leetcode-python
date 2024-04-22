from collections import defaultdict
from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        
        if len(map) < 3:
            return 0
        n = len(nums)
        res = n * (n - 1) * (n - 2) // 6
        for v in map.values():
            if v < 2:
                continue

            same3 = v * (v - 1) * (v - 2) // 6
            same2 = (n - v) * v * (v - 1) // 2
            res -= same3 + same2
        
        return res
    
def test1():
    solution = Solution()
    nums = [1,3,1,2,4]

    assert solution.unequalTriplets(nums) == 7