from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_map = defaultdict(set)
        for a, b in prerequisites:
            prerequisites_map[a].add(b)
        
        queue = deque()

        for course in range(numCourses):
            if course not in prerequisites_map:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            for pre in prerequisites_map:
                if course in prerequisites_map[pre]:
                    prerequisites_map[pre].remove(course)
                    if not prerequisites_map[pre]:
                        queue.append(pre)
                        prerequisites_map.pop(pre)
    
        return not prerequisites_map
    
def test1():
    solution = Solution()
    numCourses = 2
    prerequisites = [[1,0]]

    assert solution.canFinish(numCourses, prerequisites) == True