from typing import List

class Solution:
    def insertInterval(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = 0
        right = len(intervals) - 1

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] > newInterval[0]:
                right = mid - 1
            else:
                left = mid + 1
        
        intervals.insert(left, newInterval)
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
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    
    assert solution.insertInterval(intervals, newInterval) == [[1,5],[6,9]]

def test2():
    solution = Solution()
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    
    assert solution.insertInterval(intervals, newInterval) == [[1,2],[3,10],[12,16]]