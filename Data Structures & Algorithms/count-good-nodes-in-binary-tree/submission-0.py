# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        max_value = [] # stack for the current max_value
    
        def dfs(node: TreeNode):
            nonlocal count
            nonlocal max_value

            if not node:
                return
            
            if len(max_value) == 0 or node.val >= max_value[-1]:
                count += 1
            
            to_insert = max(node.val, max_value[-1]) if len(max_value) != 0 else node.val
            max_value.append(to_insert)

            dfs(node.left)
            dfs(node.right)
            max_value.pop()

        dfs(root)
        return count