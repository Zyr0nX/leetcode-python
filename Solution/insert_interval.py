from typing import List

class Solution:
    def insertInterval(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = 0
        right = len(intervals) - 1

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < newInterval[0]:
                left = mid + 1
            else:
                right = mid - 1

        if left > 0 and intervals[left - 1][1] >= newInterval[0]:
            left -= 1
        
        start = left

        right = len(intervals) - 1

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][1] <= newInterval[1]:
                left = mid + 1
            else:
                right = mid - 1

        if right + 1 < len(intervals) and intervals[right + 1][0] <= newInterval[1]:
            right += 1
        
        end = right
        insert = start
        if start < len(intervals) and intervals[start][0] < newInterval[0]:
            insert += 1
            
        intervals.insert(insert, newInterval)
        while start <= end:
            if intervals[start][1] >= intervals[start + 1][0]:
                intervals[start][1] = max(intervals[start][1], intervals[start + 1][1])
                intervals.pop(start + 1)
                end -= 1
            else:
                start += 1
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

def test3():
    solution = Solution()
    intervals = [[1,5]]
    newInterval = [2,3]
    
    assert solution.insertInterval(intervals, newInterval) == [[1,5]]