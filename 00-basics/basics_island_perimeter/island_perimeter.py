from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Calculates the perimeter of an island in a grid. The island is formed by cells with value 1 and surrounded by water (0s).

        Args:
        grid (List[List[int]]): A 2D list representing the map, with 1s as land and 0s as water.

        Returns:
        int: The perimeter of the island.
        """
        hauteur = len(grid)
        largeur = len(grid[0])
        perimetre = 0
        for i in range(hauteur):
            for j in range(largeur):
                if grid[i][j] == 1:
                    perimetre += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimetre -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimetre -= 2
        return perimetre

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16
    assert solution.islandPerimeter([[1]]) == 4
    assert solution.islandPerimeter([[1,0]]) == 4
    assert solution.islandPerimeter([[1,1],[0,1]]) == 8
