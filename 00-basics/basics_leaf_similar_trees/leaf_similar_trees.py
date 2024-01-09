# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Determine if two binary trees are leaf-similar.

        Leaf-similar trees have the same sequence of leaf values when traversed from left to right.

        Args:
        root1 (Optional[TreeNode]): The root of the first binary tree.
        root2 (Optional[TreeNode]): The root of the second binary tree.

        Returns:
        bool: True if the trees are leaf-similar, False otherwise.
        """

        def obtenirFeuilles(racine):
            if not racine:
                return []
            if not racine.left and not racine.right:
                return [racine.val]
            return obtenirFeuilles(racine.left) + obtenirFeuilles(racine.right)

        return obtenirFeuilles(root1) == obtenirFeuilles(root2)
