class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        minLeft = 0
        maxLeft = 0
        for i in range(len(s)):
            if s[i] == "(":
                if locked[i] == "1":
                    minLeft += 1
                else:
                    minLeft -= 1
                maxLeft += 1
            elif s[i] == ")":
                if locked[i] == "1":
                    maxLeft -= 1
                else:
                    maxLeft += 1
                minLeft -= 1
                
            if maxLeft < 0:
                return False
            
            minLeft = max(minLeft, 0)

        return minLeft == 0
    
def test1():
    solution = Solution()
    s = "))()))"
    locked = "010100"

    assert solution.canBeValid(s, locked) == True

def test2():
    solution = Solution()
    s = ")"
    locked = "0"

    assert solution.canBeValid(s, locked) == False

def test3():
    solution = Solution()
    s = "))))(())((()))))((()((((((())())((()))((((())()()))(()"
    locked = "101100101111110000000101000101001010110001110000000101"

    assert solution.canBeValid(s, locked) == False

def test4():
    solution = Solution()
    s = "))()))"
    locked = "010100"

    assert solution.canBeValid(s, locked) == True

def test5():
    solution = Solution()
    s = "()"
    locked = "11"

    assert solution.canBeValid(s, locked) == True