from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        """
        Trouve la chaîne lexicographiquement la plus petite qui commence à une feuille et se termine à la racine dans un arbre binaire.

        Args:
        root (Optional[TreeNode]): La racine de l'arbre binaire.

        Returns:
        str: La chaîne lexicographiquement la plus petite formée de la feuille à la racine.
        """
        if not root:
            return ""

        def parcours(node, chaine):
            if not node:
                return chr(255) * 26  # Retourne une chaîne qui est plus grande que toutes les autres possibles
            chaine = chr(node.val + 97) + chaine
            if not node.left and not node.right:
                return chaine
            left_result = parcours(node.left, chaine)
            right_result = parcours(node.right, chaine)
            return min(left_result, right_result)

        return parcours(root, "")


# Test cases
if __name__ == "__main__":
    # Helper function to construct binary trees
    def newNode(val, left=None, right=None):
        return TreeNode(val, left, right)


    root1 = newNode(0, newNode(1, newNode(3), newNode(4)), newNode(2, newNode(3), newNode(4)))
    assert Solution().smallestFromLeaf(root1) == "dba"

    root2 = newNode(25, newNode(1, newNode(1), newNode(3)), newNode(3, newNode(0), newNode(2)))
    assert Solution().smallestFromLeaf(root2) == "adz"

    root3 = newNode(2, newNode(2, None, newNode(1, newNode(0))), newNode(1, newNode(0)))
    assert Solution().smallestFromLeaf(root3) == "abc"
