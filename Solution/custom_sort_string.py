class Solution:
    def customSortString(self, order: str, s: str) -> str:
        map = {}
        for char in s:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1
        
        res = ""
        for char in order:
            if char in map:
                res += char * map[char]
                del map[char]

        for char in map:
            res += char * map[char]

        return res
    
def test1():
    solution = Solution()
    order = "cba"
    s = "abcd"
    assert solution.customSortString(order, s) == "cbad"

def test2():
    solution = Solution()
    order = "bcafg"
    s = "abcd"
    assert solution.customSortString(order, s) == "bcad"