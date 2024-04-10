from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != col(colsum):
            return []
        
        up_arr = []
        low_arr = []
        for col in colsum:
            if col == 2:
                upper -= 1
                up_arr.append(1)
                lower -= 1
                low_arr.append(1)
            if col == 1:
                if upper >= lower:
                    upper -= 1
                    up_arr.append(1)
                    low_arr.append(0)
                else:
                    lower -= 1
                    low_arr.append(1)
                    up_arr.append(0)
            if col == 0:
                up_arr.append(0)
                low_arr.append(0)
            
            if upper < 0 or lower < 0:
                return []

        return [up_arr, low_arr]
    
def test1():
    solution = Solution()
    upper = 5
    lower = 5
    colsum = [2,1,2,0,1,0,1,2,0,1]

    assert solution.reconstructMatrix(upper, lower, colsum) == [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]