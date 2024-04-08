from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if mid > 0 and nums[mid - 1] >= nums[mid]:
                right = mid - 1
            elif mid < len(nums) - 1 and nums[mid + 1] >= nums[mid]:
                left = mid + 1
            else:
                return mid
        
        return 0
    
def test1():
    solution = Solution()
    nums = [1,2,3,1]

    assert solution.findPeakElement(nums) == 2

def test2():
    solution = Solution()
    nums = [1,2,1,3,5,6,4]

    assert solution.findPeakElement(nums) == 5

def test3():
    solution = Solution()
    nums = [1]

    assert solution.findPeakElement(nums) == 0