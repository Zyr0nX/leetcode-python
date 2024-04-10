from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        m = tickets[k]
        res = 0
        for index, ticket in enumerate(tickets):
            if ticket > m:
                res += m
            else:
                res += ticket

            if index > k and ticket >= m:
                res -= 1

        return res
    
def test1():
    solution = Solution()
    tickets = [2,3,2]
    k = 2

    assert solution.timeRequiredToBuy(tickets, k) == 6

def test2():
    solution = Solution()
    tickets = [15,66,3,47,71,27,54,43,97,34,94,33,54,26,15,52,20,71,88,42,50,6,66,88,36,99,27,82,7,72]
    k = 18

    assert solution.timeRequiredToBuy(tickets, k) == 1457