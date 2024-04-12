from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()
        for i, s in enumerate(senate):
            if s == "R":
                r_queue.append(i)
            if s == "D":
                d_queue.append(i)
        
        while r_queue and d_queue:
            r = r_queue.popleft()
            d = d_queue.popleft()
            if r < d:
                r_queue.append(r + len(senate))
            else:
                d_queue.append(r + len(senate))
        
        if r_queue:
            return "Radiant"
        else:
            return "Dire"

def test1():
    solution = Solution()
    senate = "RD"

    solution.predictPartyVictory(senate) == "Radiant"


def test2():
    solution = Solution()
    senate = "RDD"

    solution.predictPartyVictory(senate) == "Dire"