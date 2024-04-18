from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * len(matrix[0])
        res = 0
        for row in matrix:
            for i in range(len(heights)):
                if row[i] == "0":
                    heights[i] = 0
                else:
                    heights[i] += 1

            stack = []
            for index, height in enumerate(heights):
                min_index = index
                while stack and stack[-1][1] >= height:
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
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

    assert solution.maximalRectangle(matrix) == 6