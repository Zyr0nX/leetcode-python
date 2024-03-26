from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            nums[abs(num) - 1] = -nums[abs(num) - 1]
        return res
    
def test1():
    solution = Solution()
    nums = [4,3,2,7,8,2,3,1]
    
    assert solution.findDuplicates(nums) == [2,3]

def test2():
    solution = Solution()
    