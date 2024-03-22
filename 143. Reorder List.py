# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # split the linked list into 2 halves with f & s pointers,
        # reverse the second half
        # then merge it in the first half
        # (have 2 pointers pointing at the head of the 2 lists)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None

        # reverse the second half of the linked list
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # merge 2 half linked lists until the shorter linked list finishes
        # have 2 pointers pointing at the head of the 2 lists
        first, second = head, prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1

            # after shifting, the loop repeats 1st.next = 2nd
            first = temp1
            second = temp2

# Time: O(N) linear time even though iternatng the input linked list twice
# Space: O(1) not using extra space as we are reordering the list in-place.




