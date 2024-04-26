from typing import List


class Solution:
    def minFallingPathSum(self, grille: List[List[int]]) -> int:
        """
        Calculates the minimum sum of a falling path through a matrix with non-zero shifts.

        Args:
        grille: A list of lists of integers representing the matrix.

        Returns:
        An integer representing the minimum sum of a falling path.
        """
        n = len(grille)
        if n == 1: return grille[0][0]

        precedent = grille[0]

        for i in range(1, n):
            actuel = grille[i][:]
            for j in range(n):
                actuel[j] += min(precedent[:j] + precedent[j + 1:])
            precedent = actuel

        return min(precedent)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    test_grid1 = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    test_grid2 = [[-19, 57], [-40, -5]]
    print("Output for test_grid1:", solution.minFallingPathSum(test_grid1))  # Expected output: 13
    print("Output for test_grid2:", solution.minFallingPathSum(test_grid2))  # Expected output: -59
