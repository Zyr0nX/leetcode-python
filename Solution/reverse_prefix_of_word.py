class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = 0
        right = 0
        list_word = list(word)
        while list_word[right] != ch:
            right += 1
            if right == len(word):
                return word
        
        while left < right:
            list_word[left], list_word[right] = list_word[right], list_word[left]
            left += 1
            right -= 1
        
        return "".join(list_word)
    
def test1():
    solution = Solution()
    word = "abcdefd"
    ch = "d"

    assert solution.reversePrefix(word, ch) == "dcbaefd"