class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the diameter of a binary tree.

        The diameter is the length of the longest path between any two nodes in the tree.
        This path may or may not pass through the root.

        Args:
            root: The root node of the binary tree.

        Returns:
            The length of the diameter of the tree.
        """
        diametre = 0

        def hauteur(node):
            nonlocal diametre
            if not node:
                return -1
            gauche = hauteur(node.left)
            droite = hauteur(node.right)
            diametre = max(diametre, 2 + gauche + droite)
            return 1 + max(gauche, droite)

        hauteur(root)
        return diametre
