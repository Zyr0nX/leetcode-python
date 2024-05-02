from typing import List

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        diff = []
        for i in range(len(nums2) - 1):
            diff.append(nums2[i + 1] - nums2[i])
        
        for i in range(len(nums1) - 3):
            for index_d, d in diff:
                if nums1[i + d] + d != nums1[i + d + 1]:
                    break