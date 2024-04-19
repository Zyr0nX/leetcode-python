class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num = ""
        for i in range(2, len(num)):
            if num[i - 2] == num[i - 1] == num[i]:
                max_num = max(max_num, num[i])
        
        return "".join([max_num] * 3)
            
def test1():
    solution = Solution()
    num = "6777133339"

    assert solution.largestGoodInteger(num) == "777"