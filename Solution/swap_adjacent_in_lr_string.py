class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) == len(end) == 1:
            return start == end
        
        p_start = 0
        p_end = 0

        while p_start < len(start) or p_end < len(end):
            while p_start < len(start) and start[p_start] == "X" :
                p_start += 1
            while p_end < len(end) and end[p_end] == "X":
                p_end += 1
            
            if p_start == len(start) and p_end == len(end):
                return True
            if p_start == len(start) or p_end == len(end):
                return False
            
            if start[p_start] != end[p_end]:
                return False
            if start[p_start] == end[p_end] == "L" and p_start < p_end:
                return False
            if start[p_start] == end[p_end] == "R" and p_end < p_start:
                return False
            p_start += 1
            p_end += 1
                
        return True
    
def test1():
    solution = Solution()
    start = "RXXLRXRXL"
    end = "XRLXXRRLX"

    assert solution.canTransform(start, end) == True

def test2():
    solution = Solution()
    start = "X"
    end = "L"

    assert solution.canTransform(start, end) == False

def test3():
    solution = Solution()
    start = "XLLR"
    end = "LXLX"

    assert solution.canTransform(start, end) == False
