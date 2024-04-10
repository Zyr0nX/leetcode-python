class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft = 0
        maxLeft = 0
        for c in s:
            if c == "(":
                minLeft += 1
                maxLeft += 1
            elif c == ")":
                minLeft -= 1
                maxLeft -= 1
            else:
                minLeft -= 1
                maxLeft += 1
            if maxLeft < 0:
                return False
            minLeft = max(minLeft, 0)

        return minLeft == 0

def test1():
    solution = Solution()
    s = "()"

    assert solution.checkValidString(s) == True

def test2():
    solution = Solution()
    s = "(*)"

    assert solution.checkValidString(s) == True

def test3():
    solution = Solution()
    s = "(*))"

    assert solution.checkValidString(s) == True

def test4():
    solution = Solution()
    s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"

    assert solution.checkValidString(s) == True