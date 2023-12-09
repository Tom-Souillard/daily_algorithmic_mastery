# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root

        while current or stack:
            # Reach the left most Node of the current Node
            while current:
                stack.append(current)
                current = current.left

            # Current must be None at this point
            current = stack.pop()
            result.append(current.val)

            # We have visited the node and its left subtree. Now, it's right subtree's turn
            current = current.right

        return result
