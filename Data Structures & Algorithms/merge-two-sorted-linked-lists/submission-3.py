# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        temp = res
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:

            if(curr1.val <= curr2.val):
                temp.next = curr1
                temp = temp.next
                curr1 = curr1.next
            elif(curr2.val < curr1.val):
                temp.next = curr2
                temp = temp.next
                curr2 = curr2.next
            
        while(curr1):
            temp.next = curr1
            temp = temp.next
            curr1 = curr1.next
        while(curr2):
            temp.next = curr2
            temp = temp.next
            curr2 = curr2.next

        return res.next