from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        max_candy = max(candies)
        left = 1
        right = max_candy
        
        while left < right:
            mid = (left + right + 1) // 2
            if k > sum(candy // mid for candy in candies):
                right = mid - 1
            else:
                left = mid

        return left
    
def test1():
    solution = Solution()
    candies = [5,8,6]
    k = 3

    assert solution.maximumCandies(candies, k) == 5

def test2():
    solution = Solution()
    candies = [5,6,4,10,10,1,1,2,2,2]
    k = 9

    assert solution.maximumCandies(candies, k) == 3