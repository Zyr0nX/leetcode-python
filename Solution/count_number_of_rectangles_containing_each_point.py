from collections import defaultdict
from typing import List

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        def bs(arr, a):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == a:
                    return mid
                elif arr[mid] < a:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        map = defaultdict(list)
        res = []
        for l, h in rectangles:
            map[h].append(l)

        for v in map.values():
            v.sort()

        max_height = max(map.keys())

        for l, h in points:
            count = 0
            for i in range(h, max_height + 1):
                if map[i]:
                    count += len(map[i]) - bs(map[i], l)
            res.append(count)
            
        return res
    
def test1():
    solution = Solution()
    rectangles = [[4,7],[4,9],[8,5],[6,2],[6,4]]
    points = [[4,2],[5,6]]

    assert solution.countRectangles(rectangles, points) == [5, 0]

def test2():
    solution = Solution()
    rectangles = [[49,26],[7,80],[79,10],[57,23],[23,20],[24,82],[47,62],[55,93],[84,62],[67,22]]
    points = [[65,31],[54,59],[57,46],[63,49],[87,93],[81,4],[23,50],[58,33],[100,39],[79,58],[89,25],[12,37],[83,68],[19,16],[22,44],[5,87],[33,82],[69,62],[67,29],[92,25],[51,98],[48,60],[62,87],[71,59],[99,81],[91,91],[26,83],[40,87],[28,42],[94,53],[80,24],[10,94],[16,1],[45,7],[50,39],[53,37],[76,50],[7,69],[1,81],[95,40],[48,73],[47,16],[38,5],[41,17],[24,37],[35,10],[25,92],[9,78],[66,97],[34,52],[28,45],[33,28],[55,48],[25,17],[14,24],[70,63],[6,47],[13,32],[64,36],[57,1],[37,62],[41,61],[56,77],[41,18],[69,43],[69,68],[24,11],[51,35],[5,86],[44,67],[98,21],[81,53],[78,69]]

    assert solution.countRectangles(rectangles, points) == [1,2,1,1,0,1,4,1,0,1,0,4,0,8,4,1,1,1,1,0,0,2,0,1,0,0,1,1,3,0,1,0,9,7,2,2,1,3,2,0,1,6,7,6,4,7,1,2,0,3,3,3,2,6,5,0,5,4,1,4,3,3,0,6,1,0,7,2,1,1,0,1,0]