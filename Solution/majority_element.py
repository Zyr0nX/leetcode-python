import math
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        res = nums[0]
        
        for num in nums[1:]:
            if num == res:
                count += 1
            else:
                if count == 0:
                    count = 1
                    res = num
                else:
                    count -= 1
        
        return res