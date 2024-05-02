from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = matrix[0]
        for i in range(1, len(matrix)):
            temp = [0] * len(matrix[i])
            for j in range(len(matrix[i])):
                min_dp = 0
                if j > 0 and j < len(matrix[i]) - 1:
                    min_dp = min(dp[j - 1], dp[j], dp[j + 1])
                elif j == 0 and j != len(matrix[i]) - 1:
                    min_dp = min(dp[j], dp[j + 1])
                elif j == len(matrix[i]) - 1 and j != 0:
                    min_dp = min(dp[j - 1], dp[j])
                else:
                    min_dp = dp[j]

                temp[j] = matrix[i][j] + min_dp
            dp = temp
        
        return min(dp)
    
def test1():
    solution = Solution()
    matrix = [[2,1,3],[6,5,4],[7,8,9]]

    assert solution.minFallingPathSum(matrix) == 13

def test2():
    solution = Solution()
    matrix = [[7], [7]]

    assert solution.minFallingPathSum(matrix) == 14