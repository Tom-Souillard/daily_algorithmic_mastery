class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the maximum difference between the values of any ancestor node and its descendant nodes.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            int: The maximum absolute difference between the values of any ancestor node and its descendant nodes.
        """

        def dfs(node, min_val, max_val):
            if not node:
                return max_val - min_val

            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            gauche = dfs(node.left, min_val, max_val)
            droite = dfs(node.right, min_val, max_val)

            return max(gauche, droite)

        return dfs(root, root.val, root.val)

# Example usage
# root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))
# sol = Solution()
# print(sol.maxAncestorDiff(root))  # Output: 7
