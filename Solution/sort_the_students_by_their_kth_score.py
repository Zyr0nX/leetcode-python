from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda s: s[k], reverse=True)
        return score

def test1():
    solution = Solution()
    score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
    k = 2

    assert solution.sortTheStudents(score, k) == [[7,5,11,2],[10,6,9,1],[4,8,3,15]]