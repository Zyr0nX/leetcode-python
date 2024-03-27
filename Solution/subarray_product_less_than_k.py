from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        product = 1
        total = 0
        for right, num in enumerate(nums):
            product *= num
            while product >= k and left <= right:
                product /= nums[left]
                left += 1
        
            total += right - left + 1
        return total
    
def test1():
    solution = Solution()
    nums = [10,5,2,6]
    k = 100
    
    assert solution.numSubarrayProductLessThanK(nums, k) == 8

def test2():
    solution = Solution()
    nums = [1,2,3]
    k = 0
    
    assert solution.numSubarrayProductLessThanK(nums, k) == 0