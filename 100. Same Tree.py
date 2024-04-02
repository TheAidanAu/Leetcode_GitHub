# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive dfs on both trees at the same time;

        # if both don't exist
        # if both exist  and both values are the same, it recursively calls the same function for the left and right subtrees
        # The result of this recursive call will be True if both left and right subtrees of p and q are identical, otherwise False.
        # if one tree exist but the other doesn't, it's false
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right))
        return False

        # Time: O(p+q)
        # Space: O(height of the tree)
