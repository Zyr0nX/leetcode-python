class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            c = s[left]

            while left <= right and s[left] == c:
                left += 1
            
            while left <= right and s[right] == c:
                right -= 1

        return right - left + 1
            
    
def test1():
    solution = Solution()
    s = "ca"
    assert solution.minimumLength(s) == 2

def test2():
    solution = Solution()
    s = "cabaabac"
    assert solution.minimumLength(s) == 0

def test3():
    solution = Solution()
    s = "aabccabba"
    assert solution.minimumLength(s) == 3