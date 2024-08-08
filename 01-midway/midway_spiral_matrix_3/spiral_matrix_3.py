class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        """
        Generates a list of coordinates representing positions in a grid visited
        in a clockwise spiral order starting from a given starting point.

        Args:
            rows (int): Number of rows in the grid.
            cols (int): Number of columns in the grid.
            rStart (int): Starting row index.
            cStart (int): Starting column index.

        Returns:
            list[list[int]]: A list of coordinates visited in the spiral order.
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        resultat = []
        etape = 1
        x, y = rStart, cStart

        while len(resultat) < rows * cols:
            for dx, dy in directions:
                for _ in range(etape):
                    if 0 <= x < rows and 0 <= y < cols:
                        resultat.append([x, y])
                    x += dx
                    y += dy
                if dx == 1 or dx == -1:
                    etape += 1

        return resultat


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.spiralMatrixIII(1, 4, 0, 0) == [[0, 0], [0, 1], [0, 2], [0, 3]]
    assert solution.spiralMatrixIII(5, 6, 1, 4) == [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4],
                                                    [0, 5],
                                                    [3, 5], [3, 4], [3, 3], [3, 2], [2, 2], [1, 2], [0, 2], [4, 5],
                                                    [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1],
                                                    [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]
    print("All tests passed.")
