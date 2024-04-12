from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            for i in range(len(res)):
                res.append(res[i] + [num])

        return res

def test1():
    solution = Solution()
    nums = [1,2,3]

    assert solution.subsets(nums) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]