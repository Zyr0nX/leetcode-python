from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def palindromeLinkedList(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        while prev:
            if prev.val != head.val:
                return False
            
            prev = prev.next
            head = head.next

        return True
    
def test1():
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    
    assert solution.palindromeLinkedList(head) == True

def test2():
    solution = Solution()
    head = ListNode(1, ListNode(2))
    
    assert solution.palindromeLinkedList(head) == False