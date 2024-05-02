from typing import Counter, List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count_nums = Counter(nums)
        res = 0
        if k == 0:
            for num in count_nums:
                if count_nums[num] > 1:
                    res += 1
        else:
            for num in count_nums:
                if num + k in count_nums:
                    res += 1
        return res
    
def test1():
    solution = Solution()
    nums = [1,3,1,5,4]
    k = 0

    assert solution.findPairs(nums, k) == 1