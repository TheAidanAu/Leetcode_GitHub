# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper dfs with left and right bound,
        # recursive check if each subtree is a valid BST with updated bounds
        # (Empty tree is a valid BST)
        # Use Python float("inf"), "-inf", as parameters;

        def dfs(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            # since we're going left, left bound stays the same
            return (dfs(node.left, left, node.val) and
                    dfs(node.right, node.val, right))

        return dfs(root, float("-inf"), float("inf"))

# Time: O(2N) =O(N) go through each node in the tree and compare with 2 bounds
# Space: O(N) for imbalanced tree, O(log N) for balanced BST
# Recursive calls and call stacks take up space