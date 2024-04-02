class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        for i in range(len(s)):
            if s[i] not in map_s:
                map_s[s[i]] = t[i]
            if t[i] not in map_t:
                map_t[t[i]] = s[i]
            
            if map_s[s[i]] != t[i] or map_t[t[i]] != s[i]:
                return False
        
        return True
    
def test1():
    solution = Solution()
    s = "badc"
    t = "baba"
    assert solution.isIsomorphic(s, t) == False