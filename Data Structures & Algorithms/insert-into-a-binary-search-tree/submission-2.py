# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val = val)
        if not root:
            return node
        
        prev = None
        curr = root
        while curr and (curr.left or curr.right):
            prev = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        if not curr:
            curr = prev
        if val < curr.val:
            curr.left = node
        else:
            curr.right = node

        return root