class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        Calculate the number of paths to move the ball out of the grid boundary.

        Args:
            m (int): The number of rows in the grid.
            n (int): The number of columns in the grid.
            maxMove (int): The maximum number of moves allowed.
            startRow (int): The starting row position of the ball.
            startColumn (int): The starting column position of the ball.

        Returns:
            int: The number of paths to move the ball out of the grid boundary modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(maxMove + 1)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        dp[0][startRow][startColumn] = 1
        result = 0

        for move in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            dp[move][i][j] = (dp[move][i][j] + dp[move - 1][ni][nj]) % MOD
                        else:
                            result = (result + dp[move - 1][i][j]) % MOD

        return result
