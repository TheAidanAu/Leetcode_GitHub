# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use a dict with defaultdict as a list
        # write a helper function that stores node values at each level into the dict
        # append each node and recursively call the function to the left & right child and increase the level
        # Call this helper function with the root node and level 0
        # The resulting values of the d is the expected output
        # (It traverses the binary tree by going deeper into the left subtree first before moving to the right subtree.
        # the left child of the current node is explored first, followed by the right child.)

        d = defaultdict(list)

        def dfs(node, level):
            if not node:
                return
            d[level].append(node.val)
            # It traverses the binary tree by going deeper into the left subtree first before moving to the right subtree.
            # the left child of the current node is explored first, followed by the right child.
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return d.values()

# time: O(N) visit every node
# space: O(N) because of the dict
