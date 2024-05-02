from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        self.maxi = 0
        self.maxj = 0
        def dfs(i: int, j: int):
            if i < 0 or i >= len(land) or j < 0 or j >= len(land[i]) or land[i][j] == 0:
                return
            self.maxi = max(self.maxi, i)
            self.maxj = max(self.maxj, j)
            land[i][j] = 0
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        res = []
        for i in range(len(land)):
            for j in range(len(land[i])):
                if land[i][j] == 1:
                    self.maxi = i
                    self.maxj = j
                    dfs(i, j)
                    res.append([i, j, self.maxi, self.maxj])
        
        return res