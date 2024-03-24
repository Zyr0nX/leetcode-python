# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        map = {0: front}
        sum = 0
        prev = front
        curr = head
        while curr.next:
            sum += curr.val

            if map.get(sum):
                map[sum].next = curr.next
            else:
                map[sum] = prev
            
            curr = curr.next
        return front.next
    
def test1():
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(-3, ListNode(3, ListNode(1)))))
    assert solution.removeZeroSumSublists(head) == ListNode(3, ListNode(1)) or solution.removeZeroSumSublists(head) == ListNode(1, ListNode(2, ListNode(1)))

def test2():
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(4)))))
    assert solution.removeZeroSumSublists(head) == ListNode(1, ListNode(2, ListNode(4)))

def test3():
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(-2)))))
    assert solution.removeZeroSumSublists(head) == ListNode(1)