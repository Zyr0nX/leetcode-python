from typing import List

class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:   
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for interval in intervals[1:]:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
    
def test1():
    solution = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    
    assert solution.mergeIntervals(intervals) == [[1,6],[8,10],[15,18]]

def test2():
    solution = Solution()
    intervals = [[1,4],[4,5]]
    
    assert solution.mergeIntervals(intervals) == [[1,5]]