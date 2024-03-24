# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use a dummy node to handle some edge cases
        # insert a dummy node right before the head
        # initalize the l pointer right at the dummy, advance both pointers

        dummy = ListNode()
        dummy.next = head

        l, r = dummy, head
        for i in range(n):
            r = r.next

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next

        return dummy.next
# Time: O(N)
# Space: O(1) making changes to nodes in place and returning the head only

