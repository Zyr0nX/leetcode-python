class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(set(pattern)) != len(set(words)): return False
        map = {}
        for i in range(len(pattern)):
            if pattern[i] in map:
                if map[pattern[i]] != words[i]:
                    return False
            else:
                map[pattern[i]] = words[i]

        return True
    
def test1():
    solution = Solution()
    pattern = "abba"
    s = "dog cat cat dog"

    assert solution.wordPattern(pattern, s) == True

def test2():
    solution = Solution()
    pattern = "abba"
    s = "dog dog dog dog"

    assert solution.wordPattern(pattern, s) == False