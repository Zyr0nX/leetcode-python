from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        max_count = 0
        res = 0
        left = 0
        for right, num in enumerate(nums):
            if num == max_element:
                max_count += 1
            
            while max_count >= k:
                if nums[left] == max_element:
                    max_count -= 1
                left += 1
                res += len(nums) - right

        return res

def test1():
    solution = Solution()
    nums = [1,3,2,3,3]
    k = 2

    assert solution.countSubarrays(nums, k) == 6

def test2():
    solution = Solution()
    nums = [1,4,2,1]
    k = 3

    assert solution.countSubarrays(nums, k) == 0