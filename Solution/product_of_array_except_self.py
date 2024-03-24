from typing import List


class Solution:
    def productOfArrayExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]

        temp = 1 #prefix
        for num in nums[:-1]:
            temp *= num
            output.append(temp)

        temp = 1 #postfix

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= temp
            temp *= nums[i]
        
        return output
    
def test1():
    solution = Solution()
    nums = [1,2,3,4]
    
    assert solution.productOfArrayExceptSelf(nums) == [24,12,8,6]

def test2():
    solution = Solution()
    nums = [-1,1,0,-3,3]
    
    assert solution.productOfArrayExceptSelf(nums) == [0,0,9,0,0]