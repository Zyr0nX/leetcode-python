# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __eq__(self, other):
        return self.val == other.val and self.next == other.next
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head

def test1():
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2

    assert solution.removeNthFromEnd(head, n) == ListNode(1, ListNode(2, ListNode(3, ListNode(5))))

def test2():
    solution = Solution()
    head = ListNode(1)
    n = 1

    assert solution.removeNthFromEnd(head, n) == None

def test3():
    solution = Solution()
    head = ListNode(1, ListNode(2))
    n = 2

    assert solution.removeNthFromEnd(head, n) == ListNode(2)