from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_sort = sorted(score, reverse=True)
        map = {}
        for i, s in enumerate(score_sort):
            map[s] = i
        
        res = []
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for s in score:
            if map[s] > 2:
                res.append(map[s] + 1)
            else:
                res.append(medals[map[s]])
        
        return res