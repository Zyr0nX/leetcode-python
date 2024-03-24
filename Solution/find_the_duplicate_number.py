from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
    
def test1():
    solution = Solution()
    nums = [1,3,4,2,2]
    
    assert solution.findDuplicate(nums) == 2

def test2():
    solution = Solution()
    nums = [3,1,3,4,2]
    
    assert solution.findDuplicate(nums) == 3

def test3():
    solution = Solution()
    nums = [3,3,3,3,3]
    
    assert solution.findDuplicate(nums) == 3