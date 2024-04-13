from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for index, height in enumerate(heights):
            min_index = index
            while (stack and height <= stack[-1][1]):
                i, h = stack.pop()
                min_index = i
                res = max(res, h * (index - i))
            stack.append((min_index, height))

        while stack:
            i, h = stack.pop()
            res = max(res, h * (len(heights) - i))

        return res
    
def test1():
    solution = Solution()
    heights = [2,1,5,6,2,3]

    assert solution.largestRectangleArea(heights) == 10

def test2():
    solution = Solution()
    heights = [2,1,2]

    assert solution.largestRectangleArea(heights) == 3