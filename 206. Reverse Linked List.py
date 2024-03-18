# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using 2 pointers, prev and curr
        # initialize the prev pointer as null and the curr pointer as head
        # Iterate through the linked list, save the next pointer first
        # then point the current pointer to the prev pointer
        prev, curr = None, head

        while curr:
            # every line follows the line before, look at the right and left
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        # return the head of the new linked list


# Time: O(N)
# Space: O(1)

