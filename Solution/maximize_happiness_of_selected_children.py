import heapq
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = []
        for h in happiness:
            if not heap or heap[0] < h or len(heap) < k:
                heapq.heappush(heap, -h)
        
        res = 0
        count = 0
        while heap:
            res += max(0, -heapq.heappop(heap) - count)
            count += 1
            if count >= k:
                break
        
        return res
    
def test1():
    solution = Solution()
    happiness = [1,2,3]
    k = 2

    assert solution.maximumHappinessSum(happiness, k) == 4

def test2():
    solution = Solution()
    happiness = [2,3,4,5]
    k = 1

    assert solution.maximumHappinessSum(happiness, k) == 5

def test3():
    solution = Solution()
    happiness = [7,50,3]
    k = 3

    assert solution.maximumHappinessSum(happiness, k) == 57