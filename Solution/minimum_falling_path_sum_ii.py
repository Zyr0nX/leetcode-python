from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dp = grid[0]
        
        for i in range(1, len(grid)):
            temp_dp = [0] * len(grid[i])
            for j in range(len(grid[i])):
                min_dp = min(dp[:j] + dp[j+1:])
                temp_dp[j] = grid[i][j] + min_dp
            dp = temp_dp

        return min(dp)
    
def test1():
    solution = Solution()
    grid = [[1,2,3],[4,5,6],[7,8,9]]

    assert solution.minFallingPathSum(grid) == 13