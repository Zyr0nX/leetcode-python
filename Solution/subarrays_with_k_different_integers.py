from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        map = {}
        res = 0
        curr_count = 0

        while right < len(nums):
            map[nums[right]] = map.get(nums[right], 0) + 1

            if len(map) > k:
                if map[nums[left]] > 1:
                    map[nums[left]] -= 1
                else:
                    map.pop(nums[left])
                left += 1
                curr_count = 0
            
            if len(map) == k:
                while map.get(nums[left]) > 1:
                    if map[nums[left]] > 1:
                        map[nums[left]] -= 1
                    else:
                        map.pop(nums[left])
                    curr_count += 1
                    left += 1
                res += curr_count + 1

            right += 1
        
        return res
    
def test1():
    solution = Solution()
    nums = [1,2,1,2,3]
    k = 2

    assert solution.subarraysWithKDistinct(nums, k) == 7