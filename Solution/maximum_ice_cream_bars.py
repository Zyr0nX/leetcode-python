from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        count_arr = [0] * (max_cost + 1)

        for cost in costs:
            count_arr[cost] += 1
        
        res = 0
        for cost, count in enumerate(count_arr):
            if coins >= count * cost:
                coins -= count * cost
                res += count
            else:
                res += coins // cost    
                break
        
        return res
    
def test1():
    solution = Solution()
    costs = [1,3,2,4,1]
    coins = 7

    assert solution.maxIceCream(costs, coins) == 4