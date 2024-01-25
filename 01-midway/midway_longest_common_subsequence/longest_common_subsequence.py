class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Calculate the length of the longest common subsequence between two strings.

        Args:
        text1 (str): The first string.
        text2 (str): The second string.

        Returns:
        int: The length of the longest common subsequence.
        """
        longueur1, longueur2 = len(text1), len(text2)
        matrice = [[0] * (longueur2 + 1) for _ in range(longueur1 + 1)]

        for i in range(1, longueur1 + 1):
            for j in range(1, longueur2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    matrice[i][j] = matrice[i - 1][j - 1] + 1
                else:
                    matrice[i][j] = max(matrice[i - 1][j], matrice[i][j - 1])

        return matrice[longueur1][longueur2]
