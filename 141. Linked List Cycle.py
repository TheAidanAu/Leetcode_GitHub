# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # because of Floyd's Tortoise and Hare
        # use a slow pointer and a fast pointer
        # if there's a cycle, they'll catch up and meet

        # initally, both pointers are set at the head
        slow, fast = head, head

        # check if fast and the next pointer reaches None
        # if fast reaches None before meeting slow, then it's not a cycle
        while fast and fast.next:
            # slow pointer moves 1 spot, fast moves 2 spots
            slow = slow.next
            fast = fast.next.next

            # if they catch up, then it's a cycle
            if slow == fast:
                return True

        # if fast reaches None, then it's not a cycle
        return False

#Time: O(N)
#Space: O(1)