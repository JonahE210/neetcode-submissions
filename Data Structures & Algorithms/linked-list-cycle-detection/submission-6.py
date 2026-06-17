# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        dummyNode = ListNode()
        dummyNode.next = head
        if dummyNode.next is None:
            return False
        if(head.next is None):
            return False

        while fast:
            try:
                fast = fast.next.next
                slow = slow.next
            except Exception as e:
                return False
            if(fast == slow):
                return True


        return False