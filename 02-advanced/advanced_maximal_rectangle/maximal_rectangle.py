from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Finds the largest rectangle containing only 1's in a binary matrix and returns its area.

        Args:
        matrix: A list of lists containing '0' and '1' as string elements.

        Returns:
        An integer representing the area of the largest rectangle containing only 1's.
        """
        if not matrix or not matrix[0]:
            return 0
        lignes = len(matrix)
        colonnes = len(matrix[0])
        hauteur = [0] * colonnes
        maxAire = 0

        for i in range(lignes):
            for j in range(colonnes):
                hauteur[j] = hauteur[j] + 1 if matrix[i][j] == '1' else 0

            pile = []
            for k in range(colonnes + 1):
                while pile and (k == colonnes or hauteur[k] < hauteur[pile[-1]]):
                    h = hauteur[pile.pop()]
                    largeur = k if not pile else k - pile[-1] - 1
                    maxAire = max(maxAire, h * largeur)
                pile.append(k)

        return maxAire


# Partie test
if __name__ == "__main__":
    solution = Solution()
    assert solution.maximalRectangle([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]) == 6
    assert solution.maximalRectangle([["0"]]) == 0
    assert solution.maximalRectangle([["1"]]) == 1
    assert solution.maximalRectangle([
        ["1", "1", "0", "1"],
        ["1", "1", "0", "1"],
        ["1", "1", "1", "1"]
    ]) == 6
