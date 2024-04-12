from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        res = 0

        while left < right:
            if max_left <= max_right:
                left += 1
                max_left = max(max_left, height[left])
                res += max(max_left - height[left], 0)
            else:
                right -= 1
                max_right = max(max_right, height[right])
                res += max(max_right - height[right], 0)

        return res
    
def test1():
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]

    assert solution.trap(height) == 6