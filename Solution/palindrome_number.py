class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
def test1():
    solution = Solution()
    x = 121

    assert solution.isPalindrome(x) == True