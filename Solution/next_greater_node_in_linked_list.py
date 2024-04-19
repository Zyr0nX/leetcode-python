# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        count = 0
        stack = []
        res = []
        while curr:
            res.append(0)
            while stack and curr.val > stack[-1][1]:
                i, v = stack.pop()
                res[i] = curr.val
            stack.append((count, curr.val))
            count += 1
            curr = curr.next
        
        return res
    
def test1():
    solution = Solution()
    head = ListNode(2, ListNode(1, ListNode(5)))

    assert solution.nextLargerNodes(head) == [5,5,0]

def test2():
    solution = Solution()
    head = ListNode(2, ListNode(7, ListNode(4, ListNode(3, ListNode(5)))))

    assert solution.nextLargerNodes(head) == [7,0,5,5,0]

def test3():
    solution = Solution()
    head = ListNode(1, ListNode(7, ListNode(5, ListNode(1, ListNode(9, ListNode(2, ListNode(5, ListNode(1))))))))

    assert solution.nextLargerNodes(head) == [7,9,9,9,0,5,0,0]