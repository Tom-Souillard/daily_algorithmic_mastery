from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        Calculates the maximum number of cherries two robots can collect starting from the top row to the bottom row.
        Robots can move to three adjacent cells in the row below (left, down, right). If both robots choose the same cell,
        cherries are collected only once. The function returns the maximum total cherries collected by both robots.
        """
        rows, cols = len(grid), len(grid[0])
        # Memoization cache, where key is (row, col1, col2) and value is the max cherries picked up to this point
        memo = {}

        def dp(row, col1, col2):
            # Base cases
            if col1 < 0 or col1 >= cols or col2 < 0 or col2 >= cols:
                return 0  # Out of bounds
            if row == rows:
                return 0  # Reached the bottom
            if (row, col1, col2) in memo:
                return memo[(row, col1, col2)]

            # Calculate cherries picked by both robots at current cells
            result = grid[row][col1]
            if col1 != col2:
                result += grid[row][col2]

            # Max cherries picked from next row
            maxCherries = 0
            for nextCol1 in [col1 - 1, col1, col1 + 1]:
                for nextCol2 in [col2 - 1, col2, col2 + 1]:
                    maxCherries = max(maxCherries, dp(row + 1, nextCol1, nextCol2))

            result += maxCherries
            memo[(row, col1, col2)] = result
            return result

        return dp(0, 0, cols - 1)
