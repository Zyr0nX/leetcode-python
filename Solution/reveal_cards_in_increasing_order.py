from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque(range(len(deck)))
        res = [0] * len(deck)
        for card in deck:
            res[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())

        return res


def test1():
    solution = Solution()
    deck = [17,13,11,2,3,5,7]

    assert solution.deckRevealedIncreasing(deck) == [2,13,3,11,5,17,7]