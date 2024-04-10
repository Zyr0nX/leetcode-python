class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        p = 0
        while p < len(s):
            p += maxJump
            back = 0
            if s[p] != "0":
                p -= 1
                back += 1
                if back > maxJump - minJump:
                    return False
            
            return True