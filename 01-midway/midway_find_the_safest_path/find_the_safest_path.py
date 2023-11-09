from heapq import heappush, heappop
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        Returns the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

        Args:
            grid (List[List[int]]): A 2D matrix of size n x n, where each cell is either 0 (empty) or 1 (thief).

        Returns:
            int: The maximum safeness factor of all paths from (0, 0) to (n - 1, n - 1).
        """
        n = len(grid)
        distances = [[float('inf')] * n for _ in range(n)]
        queue = []

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    distances[i][j] = 0
                    heappush(queue, (0, i, j))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            d, x, y = heappop(queue)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and distances[nx][ny] > d + 1:
                    distances[nx][ny] = d + 1
                    heappush(queue, (d + 1, nx, ny))

        start, end = (0, 0), (n - 1, n - 1)
        left, right = 0, distances[start[0]][start[1]]
        result = 0

        def is_valid_safeness(s):
            if distances[start[0]][start[1]] < s:
                return False
            visited = [[False] * n for _ in range(n)]
            stack = [start]
            while stack:
                x, y = stack.pop()
                if (x, y) == end:
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and distances[nx][ny] >= s:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
            return False

        while left <= right:
            mid = (left + right) // 2
            if is_valid_safeness(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result

if __name__ == "__main__":
    solution = Solution()
    grid1 = [[1,0,0],[0,0,0],[0,0,1]]
    assert solution.maximumSafenessFactor(grid1) == 0
    grid2 = [[0,0,1],[0,0,0],[0,0,0]]
    assert solution.maximumSafenessFactor(grid2) == 2
    grid3 = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
    assert solution.maximumSafenessFactor(grid3) == 2
    grid4 = [[0,1,0],[0,0,0],[0,1,0]]
    assert solution.maximumSafenessFactor(grid4) == 1
    grid5 = [[0,0,0],[1,1,1],[0,0,0]]
    assert solution.maximumSafenessFactor(grid5) == 0
