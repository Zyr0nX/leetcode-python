from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = 0
        even = 1
        curr = 0
        res = 0
        for a in arr:
            curr += a
            if curr % 2 == 0:
                even += 1
                res += odd
            else:
                odd += 1
                res += even

        return res % (10 ** 9 + 7)
    
def test1():
    solution = Solution()
    arr = [1,3,5]

    assert solution.numOfSubarrays(arr) == 4