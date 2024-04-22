from collections import defaultdict
from typing import List

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if all(x == suits[0] for x in suits):
            return "Flush"
        map_rank = defaultdict()
        for rank in ranks:
            map_rank[rank] += 1

        for rank in map_rank.values():
            if rank == 3:
                return "Three of a Kind"
        
        for rank in map_rank.values():
            if rank == 2:
                return "Pair"
        
        return "High Card"