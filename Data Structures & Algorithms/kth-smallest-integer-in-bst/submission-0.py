# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_tree = []
        def inorder(root: Optional[TreeNode]):
            nonlocal sorted_tree

            if not root:
                return
            inorder(root.left)
            sorted_tree.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        return sorted_tree[k - 1]
