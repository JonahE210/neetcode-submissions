# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        mid = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        #reverse the order of second half
        second = slow.next
        prev = slow.next = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
