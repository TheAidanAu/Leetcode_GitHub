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

        # then check if the current node and the subtree are the same
        # or recursively check if either the left/right subtree and the current node are the same
        # When making a recursive call to isSubtree from within the same class
        # (self.isSubtree), you must use self to reference the method correctly.
        def sameTree(s, t):
            if not s and not t:
                return True
            if s and t and s.val == t.val:
                return (sameTree(s.left, t.left) and
                        sameTree(s.right, t.right))
            return False

        if not t:
            return True
        if not s:
            return False
        if sameTree(s, t):
            return True

        return (self.isSubtree(s.left, t) or
                self.isSubtree(s.right, t))

# Time: O(S*T) for every node in S, we have to check all the nodes in T
# Space: O(max(hs, ht)) because of the recursive calls made when we traverse the trees   
