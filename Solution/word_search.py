from collections import Counter
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        if len(word) > rows*cols:
            return False
        
        count = Counter(sum(board, []))
        
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
            
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        path = set()

        def dfs(r: int, c: int, i: int):
            if len(word) == i:
                return True

            if 0 > r or r >= rows or 0 > c or c >= cols or word[i] != board[r][c] or (r, c) in path:
                return False
            
            path.add((r, c))
            res = dfs(r + 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r, c))

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
                
        return False