# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        prev = slow.next = None # break the chain b/w the 2 halved

        # reverse the second half
        while second_head:
            tmp = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = tmp



        # now we merge them
        first , second = head , prev # prev should be the new head of the second half now
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next  = second
            second.next = tmp1

            first = tmp1
            second = tmp2
