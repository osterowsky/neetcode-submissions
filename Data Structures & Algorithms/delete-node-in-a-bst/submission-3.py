# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent, node = None, root

        while node:
            if key < node.val:
                parent = node
                node = node.left
            elif key > node.val:
                parent = node
                node = node.right
            else:
                # Deletion
                if not node.right and not node.left:
                    # Case 1: key is leaf, we remove pointer to it
                    if not parent:
                        return None
                    if node.val < parent.val:
                        parent.left = None
                    else:
                        parent.right = None
                elif not node.right:
                    # Case 2: key has no successor, the parent pointer points to key left child
                    if not parent:
                        return node.left
                    if node.val < parent.val:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                else:
                    # Case 3: key has successor
                    left_children = node.left
                    leftmost = node.right
                    while leftmost.left:
                        leftmost = leftmost.left
                    
                    if not parent:  # Deleting root
                        leftmost.left = left_children
                        return node.right  # Return the right subtree as new root
                    elif node.val < parent.val:
                        parent.left = node.right
                    else:
                        parent.right = node.right
                    
                    leftmost.left = left_children
                break

        return root