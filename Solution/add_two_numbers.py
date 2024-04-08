from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remain = 0
        head = ListNode(0)
        node = head
        while l1 or l2:
            val1 = 0
            if l1:
                val1 = l1.val
            val2 = 0
            if l2:
                val2 = l2.val
            val = val1 + val2 + remain
            remain = 0
            if val > 9:
                remain = 1
                val %= 10
            
            node.next = ListNode(val)
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if remain == 1:
            node.next = ListNode(1)

        return head.next

def test1():
    solution = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    solution.addTwoNumbers(l1, l2) == ListNode(7, ListNode(0, ListNode(8)))

def test1():
    solution = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    solution.addTwoNumbers(l1, l2) == ListNode(7, ListNode(0, ListNode(8)))