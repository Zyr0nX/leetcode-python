from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            res.append([nums[i], nums[i + 1], nums[i + 2]])
        return res
    
def test1():
    solution = Solution()
    nums = [1,3,4,8,7,9,3,5,1]
    k = 2
    assert solution.divideArray(nums, k) == [[1,1,3],[3,4,5],[7,8,9]]

def test2():
    solution = Solution()
    nums = [1,3,3,2,7,3]
    k = 3
    assert solution.divideArray(nums, k) == []

def test3():
    solution = Solution()
    nums = [17,15,20,16,15,10,20,19,17]
    k = 2
    assert solution.divideArray(nums, k) == []