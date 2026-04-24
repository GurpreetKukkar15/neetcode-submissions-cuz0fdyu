# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we start with prev, and cur
        prev = None # dummy node
        cur = head
        while cur: # curr pointing to null means we reached the end of the list
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev # prev should point to the head in the new list
