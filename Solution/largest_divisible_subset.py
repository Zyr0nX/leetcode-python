from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[]] * len(nums)

        for i in reversed(range(len(nums))):
            for j in range(i, len(nums)):
                if nums[j] % nums[i] == 0:
                    dp[i] = max(dp[i], [nums[i]] + dp[j], key=len)
        
        return max(dp, key=len)
    
def test1():
    solution = Solution()
    nums = [1,2,3]

    assert solution.largestDivisibleSubset(nums) == [1,2]