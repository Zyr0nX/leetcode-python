from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        res = 0
        for i in range(len(grid)):
            sum = 0
            for j in range(len(grid[i])):
                sum += grid[i][j]
                if i > 0:
                    sum += grid[i - 1][j]
                    grid[i][j] += grid[i - 1][j]
                if sum <= k:
                    res += 1
                else:
                    break
        return res
    
def test1():
    solution = Solution()
    grid = [[7,6,3],[6,6,1]]
    k = 18

    assert solution.countSubmatrices(grid, k) == 4

def test2():
    solution = Solution()
    grid = [[7,2,9],[1,5,0],[2,6,6]]
    k = 20

    assert solution.countSubmatrices(grid, k) == 6