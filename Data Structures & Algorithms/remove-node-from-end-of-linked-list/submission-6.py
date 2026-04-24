# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        # i can have 2 pointer, one which is (n - 1) ahead
        ptr1 = dummy 
        ptr2 = head

        # move ptr2 ahead by (n-1)
        for _ in range(n):
            ptr2 = ptr2.next
        
        # now move both of them to the end
        while ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        ptr1.next = ptr1.next.next

        return dummy.next

        
