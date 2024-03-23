from typing import List

class Solution:
    def minimumNumberOfArrowsToBurstBalloons(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[0])
        end = points[0][1]
        arrow = 1
        for point in points[1:]:
            if point[0] > end:
                arrow += 1
                end = point[1]
            else:
                end = min(end, point[1])
        
        return arrow
    
def test1():
    solution = Solution()
    points = [[10,16],[2,8],[1,6],[7,12]]
    
    assert solution.minimumNumberOfArrowsToBurstBalloons(points) == 2

def test2():
    solution = Solution()
    points = [[1,2],[3,4],[5,6],[7,8]]
    
    assert solution.minimumNumberOfArrowsToBurstBalloons(points) == 4