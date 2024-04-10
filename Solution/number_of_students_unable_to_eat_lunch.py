from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        square_student = students.count(1)
        circle_student = students.count(0)

        for sandwich in sandwiches:
            if sandwich == 0 and circle_student == 0:
                break
            if sandwich == 1 and square_student == 0:
                break
            if sandwich == 0:
                circle_student -= 1
            else:
                square_student -= 1

        return circle_student + square_student
    
def test1():
    solution = Solution()
    students = [1,1,0,0]
    sandwiches = [0,1,0,1]

    assert solution.countStudents(students, sandwiches) == 0

def test2():
    solution = Solution()
    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]

    assert solution.countStudents(students, sandwiches) == 3