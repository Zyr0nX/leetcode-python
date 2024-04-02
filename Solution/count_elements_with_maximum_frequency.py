from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
                
        res = 0
        for num in map:
            if map[num] == max(map.values()):
                res += map[num]

        return res
    
def test1():
    solution = Solution()
    nums = [1,2,2,3,1,4]
    assert solution.maxFrequencyElements(nums) == 4

def test2():
    solution = Solution()
    nums = [1,2,3,4,5]
    assert solution.maxFrequencyElements(nums) == 5
