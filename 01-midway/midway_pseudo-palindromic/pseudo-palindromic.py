class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        """
        Count the number of pseudo-palindromic paths in a binary tree. A path is
        pseudo-palindromic if at least one permutation of the node values in the path
        is a palindrome.

        Args:
        root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        int: The number of pseudo-palindromic paths from the root to leaf nodes.
        """

        def dfs(node, path_count):
            if not node:
                return 0

            # Flip the bit corresponding to the current node's value.
            path_count ^= 1 << node.val

            # If it's a leaf node, check if the path count has at most one bit set.
            if not node.left and not node.right:
                # Check if path_count is a power of 2 or 0 (which means at most one bit is set).
                return int(path_count & (path_count - 1) == 0)

            # Continue DFS on left and right children.
            return dfs(node.left, path_count) + dfs(node.right, path_count)

        return dfs(root, 0)
