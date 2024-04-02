class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1])

def test1():
    solution = Solution()
    s = "Hello World"
    assert solution.lengthOfLastWord(s) == 5