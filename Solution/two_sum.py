from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            if num in map:
                return [map[num], i]
            map[target - num] = i

        return []
    
def test1():
    solution = Solution()
    nums = [2,7,11,15]
    target = 9

    assert solution.twoSum(nums, target) == [0, 1]