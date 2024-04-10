from typing import List

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        sum_idx = 0
        sum_flip = 0
        res = 0
        for index, flip in enumerate(flips):
            sum_idx += index + 1
            sum_flip += flip
            if sum_idx == sum_flip:
                res += 1

        return res
    
def test1():
    solution = Solution()
    flips = [3,2,4,1,5]

    assert solution.numTimesAllBlue(flips) == 2