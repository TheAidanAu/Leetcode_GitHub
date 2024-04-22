# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre-order's first element  is always a root,
        # in-order: elements left of root are left subtree,
        # right of root are right subtree, recursively build subtrees using the same function
        # (in-order: l subtree first, root, r subtree)
        if not preorder and not inorder:
            return
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])  #3

        # e.g. preorder = [3,    9,      20,15,7],
        # #     inorder = [9,    3,      15,20,7]

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
#Time: O(N^2) for each node, you look for the index
# Space: O(logN) for balanced trees, O(N) for imbalanced trees, recursive calls & call stacks