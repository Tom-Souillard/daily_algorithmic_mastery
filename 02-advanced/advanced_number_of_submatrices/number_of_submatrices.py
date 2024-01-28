from typing import List
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        Calculate the number of non-empty submatrices that sum to a given target value.

        Args:
        matrix (List[List[int]]): The input matrix of integers.
        target (int): The target sum for the submatrices.

        Returns:
        int: The number of submatrices that sum to the target value.
        """
        nb_lignes = len(matrix)
        nb_colonnes = len(matrix[0])
        res = 0

        # Calculating prefix sum of each row
        for ligne in matrix:
            for i in range(1, nb_colonnes):
                ligne[i] += ligne[i - 1]

        # Iterating over pairs of columns
        for i in range(nb_colonnes):
            for j in range(i, nb_colonnes):
                compte = defaultdict(int)
                compte[0] = 1
                cumulatif = 0
                for k in range(nb_lignes):
                    cumulatif += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    res += compte[cumulatif - target]
                    compte[cumulatif] += 1

        return res
