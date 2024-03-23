# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next

class Solution:
    def mergeInBetweenLinkedLists(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = ListNode()
        end = list1
        for i in range(b + 1):
            if i == a - 1:
                start = end
            end = end.next
        
        start.next = list2

        while list2.next:
            list2 = list2.next
        
        list2.next = end

        return list1
    
def test1():
    solution = Solution()
    list1 = ListNode(10, ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5))))))
    a = 3
    b = 4
    list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
    
    assert solution.mergeInBetweenLinkedLists(list1, a, b, list2) == ListNode(10, ListNode(1, ListNode(13, ListNode(1000000, ListNode(1000001, ListNode(1000002, ListNode(5)))))))

def test2():
    solution = Solution()
    list1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    a = 2
    b = 5
    list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002, ListNode(1000003, ListNode(1000004)))))
    
    assert solution.mergeInBetweenLinkedLists(list1, a, b, list2) == ListNode(0, ListNode(1, ListNode(1000000, ListNode(1000001, ListNode(1000002, ListNode(1000003, ListNode(1000004, ListNode(6))))))))