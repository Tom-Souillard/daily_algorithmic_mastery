class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        """
        Counts the number of sub-islands in the second grid that are entirely contained
        within islands in the first grid.

        Args:
            grid1 (list[list[int]]): The first grid representing the reference islands.
            grid2 (list[list[int]]): The second grid in which we check for sub-islands.

        Returns:
            int: The number of sub-islands in grid2 that are fully contained within islands in grid1.
        """

        def dfs(x: int, y: int) -> bool:
            if x < 0 or y < 0 or x >= len(grid2) or y >= len(grid2[0]) or grid2[x][y] == 0:
                return True
            grid2[x][y] = 0
            res = True
            if grid1[x][y] == 0:
                res = False
            res &= dfs(x + 1, y)
            res &= dfs(x - 1, y)
            res &= dfs(x, y + 1)
            res &= dfs(x, y - 1)
            return res

        sous_iles = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and dfs(i, j):
                    sous_iles += 1
        return sous_iles


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.countSubIslands(
        [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
        [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]) == 3
    assert solution.countSubIslands(
        [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
        [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]) == 2
    print("All tests passed.")
