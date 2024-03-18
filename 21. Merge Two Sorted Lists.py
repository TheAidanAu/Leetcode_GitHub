# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # create a new linked list, starting with a dummy node
        # set the tail to be the dummy node
        # the goal is to update the tail all the way to the end
        # When done, the head would be dummy's next

        dummy = ListNode()
        tail = dummy

        # case: both linked lists are NOT empty
        # case: one of them is NOT empty

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

            # case: one of them is NOT empty
        # then you point the tail to the remaining non-empty list

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

        # Time: O(N+n) size of the 2 linked lists
        # Space: O(N+N) size of the 2 linked lists 