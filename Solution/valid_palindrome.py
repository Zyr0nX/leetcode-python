class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if not (ord("a") <= ord(s[left].lower()) <= ord("z") or ord("0") <= ord(s[left]) <= ord("9")):
                left += 1
            elif not (ord("a") <= ord(s[right].lower()) <= ord("z") or ord("0") <= ord(s[right]) <= ord("9")):
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        
        return True
    
def test1():
    solution = Solution()
    s = "A man, a plan, a canal: Panama"

    assert solution.isPalindrome(s) == True

def test2():
    solution = Solution()
    s = " "

    assert solution.isPalindrome(s) == True

def test3():
    solution = Solution()
    s = "0P"

    assert solution.isPalindrome(s) == False