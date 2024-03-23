from typing import List

class Solution:
    def insertIntervals(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = 0
        right = len(intervals) - 1

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] > newInterval[0]:
                right = mid - 1
            else:
                left = mid + 1
        
        intervals.insert(left, newInterval)
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
    
def test1():
    solution = Solution()
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    
    assert solution.insertIntervals(intervals, newInterval) == [[1,5],[6,9]]

def test2():
    solution = Solution()
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    
    assert solution.insertIntervals(intervals, newInterval) == [[1,2],[3,10],[12,16]]