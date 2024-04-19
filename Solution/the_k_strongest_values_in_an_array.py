from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr) - 1) // 2]

        left = 0
        right = len(arr) - 1
        res = []
        while left <= right and k > 0:
            if abs(arr[left] - median) > abs(arr[right] - median):
                res.append(arr[left])
                left += 1
            else:
                res.append(arr[right])
                right -= 1
            k -= 1

        return res
    
def test1():
    solution = Solution()
    arr = [513]
    k = 1

    assert solution.getStrongest(arr, k) == [513]