# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # count the length and make the linked list circular
        # (when counting length, you can't let the pointer go to None because you have to make it circular)
        # find the index of the new head
        # you don't have to rotate k times, but length -k mod length times
        # use 2 pointers cur and prev, advance both pointers
        # disconnect the prev pointer for pointing at None and return the cur as the new head

        # this handles the edge case of empty linked list or linked list with 1 node
        # if you pass this edge case, you have at least 1 node so N can be initialized at 1
        if not head or not head.next:
            return head

        cur = head
        N = 1
        while cur.next:
            N += 1
            cur = cur.next

        cur.next = head

        M = N - (k % N)  # Index of the new head after rotation

        # Second pass: Move the pointer to the new head and adjust the links
        # 2:14 Neetcode
        i = 0
        cur = head
        for i in range(M):
            prev = cur
            cur = cur.next

        # Disconnect the list at the node just before the new head (prev.next = None)
        # to break the circular structure and form the new head.
        # Update the head pointer accordingly.
        prev.next = None
        head = cur

        return head

# Time: O(2N) = O(N)
# Time: O(1)