from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        pixel = 0
        line = 1
        for c in s:
            width = widths[ord(c) - ord("a")]
            pixel += width
            if pixel > 100:
                pixel = width
                line += 1

        return [line, pixel]
    
def test1():
    solution = Solution()
    widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    s = "abcdefghijklmnopqrstuvwxyz"

    assert solution.numberOfLines(widths, s) == [3,60]