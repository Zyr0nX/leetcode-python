from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
def test1():
    solution = Solution()
    nums = [10,9,2,5,3,7,101,18]
    
    assert solution.lengthOfLIS(nums) == 4