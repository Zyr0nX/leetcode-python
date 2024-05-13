from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = []

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                fractions.append([arr[i], arr[j]])
        
        fractions.sort(key=lambda x: x[0] / x[1])

        return fractions[k - 1]
    

def test1():
    solution = Solution()
    arr = [1,2,3,5]
    k = 3

    assert solution.kthSmallestPrimeFraction(arr, k) == [2,5]