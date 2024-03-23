from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = { 0: -1 }
        sum = 0
        max_count = 0
        for index, num in enumerate(nums):
            if num == 0:
                sum -= 1
            else:
                sum += 1
            
            if sum in map:
                max_count = max(max_count, index - map[sum])
            else:
                map[sum] = index
        
        return max_count
    
def test1():
    solution = Solution()
    nums = [0,1]
    
    assert solution.findMaxLength(nums) == 2

def test2():
    solution = Solution()
    nums = [0,1,0]
    
    assert solution.findMaxLength(nums) == 2
            
            
            