from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = len(nums) - 2
        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1

        if left >= 0:

            right = left + 1
            while right < len(nums) - 1 and nums[left] < nums[right + 1]:
                right += 1

            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

        i = left + 1
        j = len(nums) - 1
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1

        return nums
    
def test1():
    solution = Solution()
    nums = [1,2,3]

    assert solution.nextPermutation(nums) == [1,3,2]

def test2():
    solution = Solution()
    nums = [3,2,1]

    assert solution.nextPermutation(nums) == [1,2,3]

def test3():
    solution = Solution()
    nums = [5,1,1]

    assert solution.nextPermutation(nums) == [1,1,5]