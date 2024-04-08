from collections import Counter
from typing import List

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        max = 0
        second_max = 0
        for meal in deliciousness:
            if meal > max:
                second_max = max
                max = meal
            elif meal > second_max:
                second_max = meal

        max_sum = max + second_max
        pow_2_max = 1
        while max_sum >= pow_2_max:
            pow_2_max *= 2
        pow_2_max //= 2

        counter = Counter(deliciousness)
        res = 0
        while pow_2_max >= 1:
            for meal in deliciousness:
                if pow_2_max - meal in counter:
                    if pow_2_max - meal == meal:
                        res += counter[pow_2_max - meal] - 1
                    else:
                        res += counter[pow_2_max - meal]
            
            pow_2_max //= 2

        return res // 2 % (10 ** 9 + 7)
    
def test1():
    solution = Solution()
    deliciousness = [1,3,5,7,9]

    assert solution.countPairs(deliciousness) == 4

def test2():
    solution = Solution()
    deliciousness = [1,1,1,3,3,3,7]

    assert solution.countPairs(deliciousness) == 15

def test3():
    solution = Solution()
    deliciousness = [149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234]

    assert solution.countPairs(deliciousness) == 12