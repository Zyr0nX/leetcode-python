from typing import List
import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        heap = []
        
        for num in nums:
            heapq.heappush(heap, -num)
        res = 0
        remove = 0
        while total - remove > total / 2:
            num = heapq.heappop(heap)
            res += 1
            remove -= num / 2
            heapq.heappush(heap, num / 2)
        
        return res
    
def test1():
    solution = Solution()
    nums = [5,19,8,1]

    assert solution.halveArray(nums) == 3

def test2():
    solution = Solution()
    nums = [1]

    assert solution.halveArray(nums) == 1
