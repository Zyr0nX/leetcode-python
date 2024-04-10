class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        set_char = set()
        res = 0
        for right, c in enumerate(s):
            while s[right] in set_char:
                set_char.remove(s[left])
                left += 1
            else:
                set_char.add(c)
            res = max(res, right - left + 1)
        
        return res

def test1():
    solution = Solution()
    s = "abcabcbb"

    assert solution.lengthOfLongestSubstring(s) == 3

def test2():
    solution = Solution()
    s = "pwwkew"

    assert solution.lengthOfLongestSubstring(s) == 3