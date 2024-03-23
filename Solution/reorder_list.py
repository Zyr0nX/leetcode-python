from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return head
        
        prev_slow = None
        slow = head
        fast = head
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        if prev_slow:
            prev_slow.next = None

        left = head
        next_right = slow
        right = None
        while next_right:
            next_next_right = next_right.next
            next_right.next = right
            right = next_right
            next_right = next_next_right
        slow.next = None
        
        while right:
            next_left = left.next
            left.next = right
            left = right
            right = next_left
        
def test1():
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    
    solution.reorderList(head) 
    assert head == ListNode(1, ListNode(4, ListNode(2, ListNode(3))))

def test2():
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    
    solution.reorderList(head) 
    assert head == ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3)))))

def test3():
    solution = Solution()
    head = ListNode(1)
    
    solution.reorderList(head) 
    assert head == ListNode(1)