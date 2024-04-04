class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        res = 0
        for c in s:
            if c == "(":
                depth += 1
                res = max(res, depth)
            elif c == ")":
                depth -= 1

        return res
    
def test1():
    solution = Solution()
    s = "(1+(2*3)+((8)/4))+1"
    
    assert solution.maxDepth(s) == 3

def test2():
    solution = Solution()
    s = "(1)+((2))+(((3)))"
    
    assert solution.maxDepth(s) == 3