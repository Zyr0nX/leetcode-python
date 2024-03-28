from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        map = {}
        maxLen = 0
        for right, num in enumerate(nums):
            if not num in map:
                map[num] = 1
            else:
                map[num] += 1

            while left <= right and map[num] > k:
                map[nums[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen
    
def test1():
    solution = Solution()
    nums = [1,2,3,1,2,3,1,2]
    k = 2
    assert solution.maxSubarrayLength(nums, k) == 6

def test2():
    solution = Solution()
    nums = [1,2,1,2,1,2,1,2]
    k = 1
    assert solution.maxSubarrayLength(nums, k) == 2

def test3():
    solution = Solution()
    nums = [5,5,5,5,5,5,5]
    k = 4
    assert solution.maxSubarrayLength(nums, k) == 4

def test4():
    solution = Solution()
    nums = [1,4,4,3]
    k = 1
    assert solution.maxSubarrayLength(nums, k) == 2
