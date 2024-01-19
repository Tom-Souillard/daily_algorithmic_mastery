class Solution:
    def minFallingPathSum(self, matrice: List[List[int]]) -> int:
        """
        Calculate the minimum sum of any falling path through a square matrix.

        This function uses dynamic programming to compute the minimum falling path sum
        in a given n x n matrix. It iteratively updates each cell with the minimum sum
        obtained by either moving straight down, diagonally left, or diagonally right
        from the row above.

        Args:
        matrice (List[List[int]]): A square matrix of integers.

        Returns:
        int: The minimum sum of any falling path through the matrix.
        """
        n = len(matrice)
        for i in range(1, n):
            for j in range(n):
                gauche = matrice[i - 1][j - 1] if j > 0 else float('inf')
                milieu = matrice[i - 1][j]
                droite = matrice[i - 1][j + 1] if j < n - 1 else float('inf')
                matrice[i][j] += min(gauche, milieu, droite)

        return min(matrice[-1])


# Example usage
solution = Solution()
print(solution.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))  # Output: 13
print(solution.minFallingPathSum([[-19, 57], [-40, -5]]))  # Output: -59
