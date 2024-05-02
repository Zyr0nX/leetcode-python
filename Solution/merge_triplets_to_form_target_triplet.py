from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]
        for triplet in triplet:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                res = [max(res[0], triplet[0]), max(res[1], triplet[1]), max(res[2], triplet[2])]
        
        return res == target