from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        
        return res
    
def test1():
    solution = Solution()
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    assert solution.numIslands(grid) == 1
