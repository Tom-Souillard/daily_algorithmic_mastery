from typing import List


class Solution:
    def matrixScore(self, grille: List[List[int]]) -> int:
        """
        Given a binary matrix, calculates the maximum possible score by flipping any number of rows and/or columns.
        The score is determined by interpreting each row as a binary number.

        Args:
        grille (List[List[int]]): The binary matrix.

        Returns:
        int: The highest possible score after flips.
        """
        m, n = len(grille), len(grille[0])
        resultat = 0

        for j in range(n):
            colonne_max = 0
            for i in range(m):
                colonne_max += grille[i][j] ^ grille[i][0]
            resultat += max(colonne_max, m - colonne_max) * (1 << (n - j - 1))

        return resultat


# Test cases
if __name__ == "__main__":
    sol = Solution()
    grille1 = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    print(sol.matrixScore(grille1))  # Output: 39
    grille2 = [[0]]
    print(sol.matrixScore(grille2))  # Output: 1
    grille3 = [[1, 0, 1, 1], [0, 1, 0, 0], [1, 1, 0, 1]]
    print(sol.matrixScore(grille3))  # Expected output: 31
