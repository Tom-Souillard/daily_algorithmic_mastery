class Solution:
    def minDays(self, grille: list[list[int]]) -> int:
        """
        Determines the minimum number of days required to disconnect a connected island in a grid.

        Args:
            grille (list[list[int]]): A 2D binary grid where 1 represents land and 0 represents water.

        Returns:
            int: The minimum number of days required to disconnect the grid.
        """

        def nombre_iles(grille: list[list[int]]) -> int:
            """
            Counts the number of islands in the grid.

            Args:
                grille (list[list[int]]): A 2D binary grid.

            Returns:
                int: The number of islands in the grid.
            """

            def dfs(i: int, j: int):
                """
                Depth-First Search to mark all connected land cells as water.

                Args:
                    i (int): The row index of the current cell.
                    j (int): The column index of the current cell.
                """
                if i < 0 or i >= len(grille) or j < 0 or j >= len(grille[0]) or grille[i][j] == 0:
                    return
                grille[i][j] = 0
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

            compteur = 0
            for i in range(len(grille)):
                for j in range(len(grille[0])):
                    if grille[i][j] == 1:
                        dfs(i, j)
                        compteur += 1
            return compteur

        if nombre_iles([row[:] for row in grille]) != 1:
            return 0

        for i in range(len(grille)):
            for j in range(len(grille[0])):
                if grille[i][j] == 1:
                    grille[i][j] = 0
                    if nombre_iles([row[:] for row in grille]) != 1:
                        return 1
                    grille[i][j] = 1
        return 2


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minDays([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) == 2
    assert solution.minDays([[1, 1]]) == 2
    assert solution.minDays([[1, 0, 1, 0]]) == 0
    assert solution.minDays([[1]]) == 1
    print("All tests passed.")
