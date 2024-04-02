# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive dfs to find max-depth of subtrees;
        # if no root, -> 0 depth
        # if a root with no child, 1 depth
        # a tree may not be balanced, you have to find the max depth of left & right subtrees
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# time: O(N)
 # Space: O(h), or O(N) if not a balanced tree (think of a 1-branch tree)

