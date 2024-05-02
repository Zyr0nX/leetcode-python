from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        res = 0
        set_nums = set(nums)
        for index, num in enumerate(nums):
            if index == 0 or num - nums[index - 1] == 1:
                res += num
            else:
                break

        while res in set_nums:
            res += 1

        return res
    
def test1():
    solution = Solution()
    nums = [1,2,3,2,5]

    assert solution.missingInteger(nums) == 6

def test2():
    solution = Solution()
    nums = [29,30,31,32,33,34,35,36,37]

    assert solution.missingInteger(nums) == 297

def test3():
    solution = Solution()
    nums = [38,43,44]

    assert solution.missingInteger(nums) == 39