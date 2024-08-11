class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        """
        Determines the number of regions in a grid represented by slashes and backslashes.

        Args:
            grid: List of strings representing the grid.

        Returns:
            An integer representing the number of distinct regions.
        """
        n = len(grid)
        parent = list(range(4 * n * n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            parent[find(x)] = find(y)

        for i in range(n):
            for j in range(n):
                base = 4 * (i * n + j)
                if grid[i][j] == '/':
                    union(base + 0, base + 3)
                    union(base + 1, base + 2)
                elif grid[i][j] == '\\':
                    union(base + 0, base + 1)
                    union(base + 2, base + 3)
                else:
                    union(base + 0, base + 1)
                    union(base + 1, base + 2)
                    union(base + 2, base + 3)

                if i > 0:
                    union(base + 0, base - 4 * n + 2)
                if j > 0:
                    union(base + 3, base - 4 + 1)

        return sum(parent[i] == i for i in range(4 * n * n))

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.regionsBySlashes([" /","/ "]) == 2
    assert solution.regionsBySlashes([" /","  "]) == 1
    assert solution.regionsBySlashes(["/\\","\\/"]) == 5
    assert solution.regionsBySlashes(["\\/","/\\"]) == 4
    assert solution.regionsBySlashes(["  ","  "]) == 1
    print("All tests passed.")
