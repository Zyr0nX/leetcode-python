from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(left: int, right: int) -> None:
            while left < right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1
        k = k % len(nums)
        
        left = 0
        right = len(nums) - k - 1

        swap(left, right)
        
        left = len(nums) - k
        right = len(nums) - 1

        swap(left, right)

        left = 0
        right = len(nums) - 1

        swap(left, right)

def test1():
    solution = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3

    solution.rotate(nums, k)
    assert nums == [5,6,7,1,2,3,4]

def test2():
    solution = Solution()
    nums = [-1,-100,3,99]
    k = 2

    solution.rotate(nums, k)
    assert nums == [3,99,-1,-100]