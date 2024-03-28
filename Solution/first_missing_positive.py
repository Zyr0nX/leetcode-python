from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # hasOne = False
        # for i, num in enumerate(nums):
        #     if num == 1:
        #         hasOne = True
        #     if num <= 0:
        #         nums[i] = 1
        # if not hasOne:
        #     return 1
        
        # for i, num in enumerate(nums):
        #     if abs(num) - 1 < len(nums) and nums[abs(num) - 1] > 0:
        #         nums[abs(num) - 1] = -nums[abs(num) - 1]

        # for i, num in enumerate(nums):
        #     if num > 0:
        #         return i + 1
            
        # return len(nums) + 1
        i = 0
        while i < len(nums):
            correctIndex = nums[i] - 1
            if 0 <= correctIndex < len(nums) and nums[i] != nums[correctIndex]:
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
            else:
                i += 1

        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
            
        return len(nums) + 1

def test1():
    solution = Solution()
    nums = [1,2,0]
    
    assert solution.firstMissingPositive(nums) == 3

def test2():
    solution = Solution()
    nums = [3,4,-1,1]
    
    assert solution.firstMissingPositive(nums) == 2

def test3():
    solution = Solution()
    nums = [7,8,9,11,12]
    
    assert solution.firstMissingPositive(nums) == 1


def test4():
    solution = Solution()
    nums = [1]
    
    assert solution.firstMissingPositive(nums) == 2