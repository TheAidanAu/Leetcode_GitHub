# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Traverse both linked lists simultaneously add the digits in each linked list digit by digit,
        # considering any carryover, which is initialized as 0.
        # remember to advance the pointer at every iteration
        # 1 edge case: 7+8 = 15, if there's still carry remaining
        dummy = cur = ListNode()
        carryover = 0

        while l1 or l2 or carryover:
            d = carryover

            if l1 and l2:
                d += (l1.val + l2.val)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                d += l1.val
                l1 = l1.next
            elif l2:
                d += l2.val
                l2 = l2.next

            carryover = d // 10
            # Create a new node with the value d % 10 and
            # append it to the result linked list pointed by cur.
            cur.next = ListNode(d % 10)
            # Move cur to the newly added node.
            cur = cur.next

        return dummy.next

# Time: O(max(N, M)), where N and M are the lengths of the input linked lists.
# Space: length of the longer input list O(max(N, M)).