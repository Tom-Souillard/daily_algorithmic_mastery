from typing import List


class Solution:
    def numIslands(self, grille: List[List[str]]) -> int:
        """
        Given a 2D grid representing a map of '1's (land) and '0's (water), this function returns the number of islands.
        An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.

        Args:
        grille: List[List[str]] - A 2D list of strings representing the grid map of '1's and '0's.

        Returns:
        int - The number of islands in the grid.
        """
        if not grille:
            return 0

        nb_lignes = len(grille)
        nb_colonnes = len(grille[0])
        nb_iles = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= nb_lignes or j >= nb_colonnes or grille[i][j] == '0':
                return
            grille[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(nb_lignes):
            for j in range(nb_colonnes):
                if grille[i][j] == '1':
                    nb_iles += 1
                    dfs(i, j)

        return nb_iles


# Test cases
if __name__ == "__main__":
    solution = Solution()
    grille1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grille2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    grille3 = [
        ["1", "0", "0", "1", "0"],
        ["1", "0", "1", "0", "1"],
        ["0", "0", "1", "0", "0"],
        ["1", "1", "0", "1", "1"]
    ]
    assert solution.numIslands(grille1) == 1
    assert solution.numIslands(grille2) == 3
    assert solution.numIslands(grille3) == 6
    print("All tests passed.")
