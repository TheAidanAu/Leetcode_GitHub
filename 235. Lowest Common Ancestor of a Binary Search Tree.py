# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # iternate down the tree, compare p, q values to curr node,
        # if both nodes > cur, look right, update the cur node
        # last case is either the split (1 left 1 right) or p/q is the cur node
        # then curr is lca
        # (if the curr reaches p or q, an ancestor is not further down)
        cur = root

        while cur:
            if p.val > cur and q.val > cur:
                cur = cur.right
            elif p.val < cur and q.val < cur:
                cur = cur.left
            else:
                return cur

# time: O(h) you visit 1 node per level
# usually O(log n) on average, O(N) if it's inbalanced
# space: O(1)