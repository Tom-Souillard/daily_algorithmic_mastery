from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """
        This function calculates the largest area of a submatrix of 1s in the given binary matrix,
        allowing rearrangement of columns. It uses an efficient approach to minimize time and space complexity.

        Args:
        matrix (List[List[int]]): A binary matrix of size m x n.

        Returns:
        int: The area of the largest submatrix of 1s after rearranging columns.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]

        aireMax = 0
        for i in range(m):
            matrix[i].sort(reverse=True)
            for j in range(n):
                aireMax = max(aireMax, matrix[i][j] * (j + 1))

        return aireMax
