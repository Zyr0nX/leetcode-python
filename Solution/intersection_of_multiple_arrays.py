from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        nums.sort(key=len)
        res = []
        for num in nums[0]:
            found = True
            for listNums in nums[1:]:
                if num not in listNums:
                    found = False
                    break
            if found:
                res.append(num)

        return sorted(res)
    
def test1():
    solution = Solution()
    nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]

    assert solution.intersection(nums) == [3, 4]