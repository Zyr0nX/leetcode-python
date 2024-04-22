from typing import Counter, List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        square_nums = []
        counter_nums = Counter(nums) 
        res = 0
        for num in nums:
            square_nums.append(num * num)
        
        for num in square_nums:
            if num in counter_nums and counter_nums[num] >= 2:
                res += 1

        return res
    
def test1():
    solution = Solution()
    nums = [1, 1]

    assert solution.maximumLength(nums) == 1