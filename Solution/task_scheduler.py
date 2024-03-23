from typing import List

class Solution:
    def taskScheduler(self, tasks: List[str], n: int) -> int:
        taskMap = {}
        max_count = 0
        for task in tasks:
            if taskMap.get(task):
                taskMap[task] += 1
            else:
                taskMap[task] = 1
            max_count = max(max_count, taskMap[task])

        time = (max_count - 1) * (n + 1)
        for freq in taskMap.values():
            if freq == max_count:
                time += 1

        return max(len(tasks), time)

def test1():
    solution = Solution()
    tasks = ["A","A","A","B","B","B"]
    n = 2
    
    assert solution.taskScheduler(tasks, n) == 8

def test2():
    solution = Solution()
    tasks = ["A","C","A","B","D","B"]
    n = 1
    
    assert solution.taskScheduler(tasks, n) == 6

def test3():
    solution = Solution()
    tasks = ["A","A","A", "B","B","B"]
    n = 3
    
    assert solution.taskScheduler(tasks, n) == 10