from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        for num in nums2:
            if not stack or stack[-1] < num:
                stack.append(num)
        
        stack.pop()
        res = [-1] * len(nums1)
        for index, num in enumerate(nums1):
            if num in stack:
                res[index] = 

        for num in stack:
            