from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        face_up = 0
        face_down = len(tokens) - 1
        score = 0
        max_score = 0
        tokens.sort()
        while face_up <= face_down:
            if power >= tokens[face_up]:
                power -= tokens[face_up]
                face_up += 1
                score += 1
                max_score = max(max_score, score)
            elif score >= 1:
                power += tokens[face_down]
                face_down -= 1
                score -= 1
            else:
                break
        
        return max_score
    
def test1():
    solution = Solution()
    tokens = [100]
    power = 50

    assert solution.bagOfTokensScore(tokens, power) == 0

def test2():
    solution = Solution()
    tokens = [200,100]
    power = 150

    assert solution.bagOfTokensScore(tokens, power) == 1

def test3():
    solution = Solution()
    tokens = [100,200,300,400]
    power = 200

    assert solution.bagOfTokensScore(tokens, power) == 2