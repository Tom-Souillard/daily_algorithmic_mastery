class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        Converts a binary tree to a string in preorder traversal manner.

        Args:
        root (Optional[TreeNode]): Root of the binary tree.

        Returns:
        str: The string representation of the binary tree.

        The function uses depth-first search (DFS) to traverse the tree.
        It omits unnecessary empty parenthesis pairs, preserving the
        one-to-one mapping relationship between the string and the tree.
        """
        if not root:
            return ""

        gauche = self.tree2str(root.left)
        droite = self.tree2str(root.right)

        if not gauche and not droite:
            return str(root.val)
        if not droite:
            return f"{root.val}({gauche})"
        return f"{root.val}({gauche})({droite})"


# Example usage
if __name__ == "__main__":
    # Construct the tree for Example 1
    node4 = TreeNode(4)
    node2 = TreeNode(2, left=node4)
    node3 = TreeNode(3)
    root = TreeNode(1, left=node2, right=node3)

    # Solution instance
    sol = Solution()

    # Get the string representation
    print(sol.tree2str(root))  # Output should be "1(2(4))(3)"
