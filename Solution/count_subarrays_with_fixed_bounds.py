from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        p_min = -1
        p_max = -1
        p_bad = -1
        res = 0
        for index, num in enumerate(nums):
            if not minK <= num <= maxK:
                p_bad = index

            if num == minK:
                p_min = index
            if num == maxK:
                p_max = index
            res += max(0, min(p_min, p_max) - p_bad)
        
        return res

def test1():
    solution = Solution()
    nums = [1,3,5,2,7,5]
    minK = 1
    maxK = 5

    assert solution.countSubarrays(nums, minK, maxK) == 2
