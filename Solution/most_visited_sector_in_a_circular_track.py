from typing import List

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        res = []
        first = rounds[0]
        last = rounds[-1]
        if last >= first:
            return list(range(first, last + 1))
        else:
            res = []
            for i in range(n):
                if i + 1 <= last or i + 1 >= first:
                    res.append(i+1)
            return sorted(res)

def test1():
    solution = Solution()
    n = 4
    rounds = [1,3,1,2]

    assert solution.mostVisited(n, rounds) == [1, 2]

def test2():
    solution = Solution()
    n = 2
    rounds = [1,3,5,7]

    assert solution.mostVisited(n, rounds) == [1,2,3,4,5,6,7]