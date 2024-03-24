from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        start = 0
        sum = 0
        prefix = 0
        count = 0
        for end, num in enumerate(nums):
            sum += num
            while start < end and (nums[start] == 0 or sum > goal):
                if nums[start] == 1:
                    prefix = 0
                else:
                    prefix += 1
                sum -= nums[start]
                start += 1

            if sum == goal:
                count += 1 + prefix

        return count
    
def test1():
    solution = Solution()
    nums = [1,0,1,0,1]
    goal = 2
    
    assert solution.numSubarraysWithSum(nums, goal) == 4

def test2():
    solution = Solution()
    nums = [0,0,0,0,0]
    goal = 0
    
    assert solution.numSubarraysWithSum(nums, goal) == 15