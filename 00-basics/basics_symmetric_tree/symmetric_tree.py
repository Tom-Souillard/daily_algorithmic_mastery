from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Determine if a binary tree is symmetric around its center.

        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        bool: True if the tree is symmetric, False otherwise.
        """
        def estMiroir(gauche, droite):
            if not gauche and not droite:
                return True
            if not gauche or not droite:
                return False
            return (gauche.val == droite.val) and estMiroir(gauche.right, droite.left) and estMiroir(gauche.left, droite.right)

        return estMiroir(root, root)

# Test Cases
if __name__ == "__main__":
    # Construction des noeuds de l'arbre pour le premier exemple
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(3)
    n5 = TreeNode(4)
    n6 = TreeNode(4)
    n7 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    solution = Solution()
    print(solution.isSymmetric(n1))  # Doit retourner True

    # Construction des noeuds de l'arbre pour le deuxième exemple
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n5 = TreeNode(3)
    n7 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    n2.right = n5
    n3.right = n7

    print(solution.isSymmetric(n1))  # Doit retourner False
