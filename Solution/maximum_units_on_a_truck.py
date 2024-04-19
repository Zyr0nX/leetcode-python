from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
            boxTypes.sort(key=lambda x: x[1], reverse=True)
            res = 0
            for boxType in boxTypes:
                [numberOfBoxes, numberOfUnitsPerBox] = boxType
                if numberOfBoxes <= truckSize:
                    res += numberOfBoxes * numberOfUnitsPerBox
                    truckSize -= numberOfBoxes
                else:
                    res += truckSize * numberOfUnitsPerBox
                    break
            
            return res
    
def test1():
    solution = Solution()
    boxTypes = [[1,3],[2,2],[3,1]]
    truckSize = 4

    assert solution.maximumUnits(boxTypes, truckSize) == 8

def test2():
    solution = Solution()
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10

    assert solution.maximumUnits(boxTypes, truckSize) == 91
