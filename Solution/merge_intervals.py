from typing import List

class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:   
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.pop(i + 1)
            else:
                i += 1
        return intervals
    
def test1():
    solution = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    
    assert solution.mergeIntervals(intervals) == [[1,6],[8,10],[15,18]]

def test2():
    solution = Solution()
    intervals = [[1,4],[4,5]]
    
    assert solution.mergeIntervals(intervals) == [[1,5]]