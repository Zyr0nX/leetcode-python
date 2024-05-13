# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        curr = prev
        carry = 0
        while curr:
            val = curr.val * 2 + carry
            curr.val = val % 10
            carry = val // 10
            curr = curr.next
        
        curr = prev
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        if carry != 0:
            prev = ListNode(carry, prev)
        
        return prev

def test1():
    solution = Solution()
    head = ListNode(1, ListNode(8, ListNode(9)))

    assert solution.doubleIt(head) == ListNode(3, ListNode(7, ListNode(8)))
    
def test2():
    solution = Solution()
    head = ListNode(9, ListNode(9, ListNode(9)))

    assert solution.doubleIt(head) == ListNode(1, ListNode(9, ListNode(9, ListNode(8))))
    
def test3():
    solution = Solution()
    head = ListNode(3)

    assert solution.doubleIt(head) == ListNode(6)
    