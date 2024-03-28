from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        for num in nums1:
            map[num] = True
        
        res = []
        for num in nums2:
            if num in map:
                res.append(num)
                map.pop(num)
        
        return res
    
def test1():
    solution = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2, 2]
    assert solution.intersection(nums1, nums2) == [2]

def test2():
    solution = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    assert solution.intersection(nums1, nums2) == [9,4]