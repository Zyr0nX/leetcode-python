from typing import List

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        min_nums1 = min(nums1)
        min_nums2 = min(nums2)
        return min_nums1 - min_nums2