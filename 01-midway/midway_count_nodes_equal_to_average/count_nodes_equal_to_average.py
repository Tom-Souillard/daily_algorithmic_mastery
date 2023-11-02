# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        """
        Counts the number of nodes in a binary tree where the value of the node is equal to the average of values in its subtree.

        Args:
        root: TreeNode - The root of the binary tree

        Returns:
        int - The number of nodes meeting the condition
        """

        def dfs(noeud):
            if not noeud:
                return 0, 0, 0

            somme_gauche, nombre_gauche, compteur_gauche = dfs(noeud.left)
            somme_droite, nombre_droite, compteur_droite = dfs(noeud.right)

            somme_totale = somme_gauche + somme_droite + noeud.val
            nombre_total = nombre_gauche + nombre_droite + 1

            compteur_moyenne = compteur_gauche + compteur_droite
            if noeud.val == somme_totale // nombre_total:
                compteur_moyenne += 1

            return somme_totale, nombre_total, compteur_moyenne

        _, _, compteur_moyenne = dfs(root)
        return compteur_moyenne
