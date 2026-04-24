# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = fast = head        
        while fast: # so if fast points to null we know that no loop exists
            slow = slow.next
            fast = fast.next
            if fast == None:
                break
            fast = fast.next
            
            if slow is fast:
                return True
                break
        return False