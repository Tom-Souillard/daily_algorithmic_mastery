from typing import List

class Solution:
    def maxArea(self, hauteur: List[int]) -> int:
        """
        Given an array of integers representing the heights of n lines drawn on an x-axis,
        this function finds two lines that form a container capable of holding the maximum amount
        of water. It returns the maximum area of water that can be contained.

        Args:
        hauteur: A list of integers representing the heights of lines.

        Returns:
        The maximum area of water a container can store.
        """
        gauche, droite = 0, len(hauteur) - 1
        aire_maximale = 0
        while gauche < droite:
            largeur = droite - gauche
            hauteur_minimale = min(hauteur[gauche], hauteur[droite])
            aire_maximale = max(aire_maximale, largeur * hauteur_minimale)
            if hauteur[gauche] < hauteur[droite]:
                gauche += 1
            else:
                droite -= 1
        return aire_maximale

# Test case
if __name__ == "__main__":
    solution = Solution()
    assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49, "Le cas test 1 a échoué."
    assert solution.maxArea([1,1]) == 1, "Le cas test 2 a échoué."
    assert solution.maxArea([4,3,2,1,4]) == 16, "Le cas test supplémentaire a échoué."
    print("Tous les tests sont passés avec succès.")
