from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] * nums[left])
                left += 1
            else:
                res.append(nums[right] * nums[right])
                right -= 1

        return res[::-1]
    
def test1():
    solution = Solution()
    nums = [-4,-1,0,3,10]

    assert solution.sortedSquares(nums) == [0,1,9,16,100]

def test2():
    solution = Solution()
    nums = [-7,-3,2,3,11]

    assert solution.sortedSquares(nums) == [4,9,9,49,121]