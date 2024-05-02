from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        xor ^= k
        res = 0
        while xor:
            xor = xor & (xor - 1)
            res += 1

        return res

def test1():
    solution = Solution()
    nums = [2,1,3,4]
    k = 1

    assert solution.minOperations(nums, k) == 2