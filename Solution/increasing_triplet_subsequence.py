import math
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = math.inf
        min2 = math.inf
        for i in range(len(nums)):
            if nums[i] <= min1:
                min1 = nums[i]
            elif nums[i] <= min2:
                min2 = nums[i]
            else:
                return True
        return False


def test1():
    solution = Solution()
    nums = [2,4,-2,-3]

    assert solution.increasingTriplet(nums) == False

def test2():
    solution = Solution()
    nums = [5,1,6]

    assert solution.increasingTriplet(nums) == False