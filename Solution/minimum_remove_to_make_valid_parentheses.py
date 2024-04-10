class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        temp = []
        for c in s:
            if c == '(':
                count += 1
                temp.append(c)
            elif c == ')' and count > 0:
                count -= 1
                temp.append(c)
            elif c != ")":
                temp.append(c)

        res = []
        for c in reversed(temp):
            if c == '(' and count > 0:
                count -= 1
            else:
                res.append(c)
        return "".join(reversed(res))
    
def test1():
    solution = Solution()
    s = "lee(t(c)o)de)"

    assert solution.minRemoveToMakeValid(s) == "lee(t(c)o)de"