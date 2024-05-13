# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __eq__(self, other):
        return self.val == other.val and self.next == other.next
    
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        curr = head
        dummy = ListNode()
        while curr:
            while stack and curr.val > stack[-1]:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next
        
        curr = dummy
        for node_val in stack:
            curr.next = ListNode(node_val)
            curr = curr.next
        
        return dummy.next
        
def test1():
    solution = Solution()
    head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))

    assert solution.removeNodes(head) == ListNode(13, ListNode(8))