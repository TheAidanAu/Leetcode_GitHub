# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # In-order traversal (l, root, r) of a BST is actually sorted
        # Initialize a counter to be 1 and a kSmallest
        # Recursive DFS, going to the left and deepest as possible
        # At each step, compare the counter with k,
        # when the counter reaches k, update the kSmallest
        self.counter = 1
        self.kSmallest = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.counter == k:
                self.kSmallest = node.val
            self.counter += 1
            inorder(node.right)

        inorder(root)

        return self.kSmallest

# Time: O(N+k)= O(N) visit every node in the tree, find the kth smallest
# Space: O(N) depth of the recursive calls can be as large as N for an imbalanced tree
