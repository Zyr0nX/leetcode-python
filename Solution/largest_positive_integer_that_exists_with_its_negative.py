from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        set_num = set()
        res = -1
        for num in nums:
            if num not in set_num:
                set_num.add(-num)
            else:
                res = max(res, abs(num))
        
        return res