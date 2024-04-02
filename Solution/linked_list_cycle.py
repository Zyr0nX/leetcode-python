# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
    
def test1():
    solution = Solution()
    head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
    head.next.next.next.next = head.next
    assert solution.hasCycle(head)

def test2():
    solution = Solution()
    head = ListNode(1, ListNode(2))
    # head.next.next = head
    assert not solution.hasCycle(head)

def test3():
    solution = Solution()
    head = ListNode(1)
    assert not solution.hasCycle(head)