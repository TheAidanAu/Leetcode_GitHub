# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        # using sameTree Leetcode solution,
        # traverse s to check if any subtree in s equals t
        # An empty tree is a subtree of the bigger tree, BUT not the other way

        # then recursively check if the current node and the subtree are the same
        # or if either the left/right subtree and the current node are the same

        if not t:
            return True
        if not s:
            return False
        if self.sameTree(s, t):
            return True
        return (self.isSubtree(s.left, t) or
                self.isSubtree(s.right, t))

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
                    self.sameTree(s.right, t.right))
        return False

        # Time: O(S*T) for every node in S, we have to check all the nodes in T
        # Space: O(max(hs, ht))  primarily determined by the recursive calls made during the traversal of the trees
