# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case for a leaf note
        # During each recursive call, the function swaps the left and right child of the current node.
        # This effectively swaps the subtree rooted at the current node.
        # we'll keep doing this recursively until all nodes are visited,
        # and their left and right child are swapped.
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# time: O(N)
# Space: O(N)
