from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        Return the maximum amount of gold that can be collected from a gold mine grid.

        Args:
            grid (List[List[int]]): 2D list representing the gold mine grid where each cell
                                    contains an integer representing the amount of gold.

        Returns:
            int: The maximum amount of gold that can be collected.
        """
        def dfs(grille, x, y, or_actuel):
            nonlocal max_or
            or_actuel += grille[x][y]
            max_or = max(max_or, or_actuel)
            temp = grille[x][y]
            grille[x][y] = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grille) and 0 <= ny < len(grille[0]) and grille[nx][ny] > 0:
                    dfs(grille, nx, ny, or_actuel)
            grille[x][y] = temp

        max_or = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    dfs(grid, i, j, 0)
        return max_or

# Tests cases
sol = Solution()
print(sol.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))  # Output: 24
print(sol.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))  # Output: 28
print(sol.getMaximumGold([[1,2,3],[0,0,4],[5,6,0]]))  # Output: 17
print(sol.getMaximumGold([[0,0,0],[0,0,0],[0,0,0]]))  # Output: 0
print(sol.getMaximumGold([[10,33,13,15],[22,21,4,1],[5,0,2,3]]))  # Output: 99
