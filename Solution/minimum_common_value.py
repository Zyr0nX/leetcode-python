from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = 0
        p2 = 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1

        return -1
    
def test1():
    solution = Solution()
    nums1 = [1,2,3]
    nums2 = [2,4]
    assert solution.getCommon(nums1, nums2) == 2

def test2():
    solution = Solution()
    nums1 = [1,2,3,6]
    nums2 = [2,3,4,5]
    assert solution.getCommon(nums1, nums2) == 2