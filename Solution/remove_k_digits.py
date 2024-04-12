class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"

        stack = []
        for c in num:
            while stack and stack[-1] > c and k > 0:
                stack.pop()
                k -= 1
            if stack or c != "0":
                stack.append(c)

        while k > 0 and stack:
            stack.pop()
            k -= 1
        
        if not stack:
            return "0"
        return "".join(stack)

def test1():
    solution = Solution()
    num = "1432219"
    k = 3

    assert solution.removeKdigits(num, k) == "1219"

def test2():
    solution = Solution()
    num = "10200"
    k = 1

    assert solution.removeKdigits(num, k) == "200"

def test3():
    solution = Solution()
    num = "10"
    k = 2

    assert solution.removeKdigits(num, k) == "0"