from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        """
        Determines the number of 3x3 magic square subgrids within a given grid.

        A magic square is defined as a 3x3 grid containing distinct integers
        from 1 to 9 where the sum of numbers in each row, column, and both diagonals
        are equal.

        Args:
            grid (List[List[int]]): A 2D list of integers representing the grid.

        Returns:
            int: The number of 3x3 magic square subgrids in the grid.
        """

        def est_magique(sous_grille: List[List[int]]) -> bool:
            nums = [sous_grille[i][j] for i in range(3) for j in range(3)]
            if sorted(nums) != list(range(1, 10)):
                return False
            somme = sum(sous_grille[0])
            return (
                    sum(sous_grille[1]) == somme and
                    sum(sous_grille[2]) == somme and
                    sum(sous_grille[i][0] for i in range(3)) == somme and
                    sum(sous_grille[i][1] for i in range(3)) == somme and
                    sum(sous_grille[i][2] for i in range(3)) == somme and
                    sous_grille[0][0] + sous_grille[1][1] + sous_grille[2][2] == somme and
                    sous_grille[0][2] + sous_grille[1][1] + sous_grille[2][0] == somme
            )

        x, y = len(grid), len(grid[0])
        compte = 0

        for i in range(x - 2):
            for j in range(y - 2):
                if est_magique([row[j:j + 3] for row in grid[i:i + 3]]):
                    compte += 1

        return compte


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]) == 1
    assert solution.numMagicSquaresInside([[8]]) == 0
    assert solution.numMagicSquaresInside([[10, 3, 5], [3, 8, 1], [6, 7, 2]]) == 0
    assert solution.numMagicSquaresInside([[5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 0
    print("All tests passed.")
