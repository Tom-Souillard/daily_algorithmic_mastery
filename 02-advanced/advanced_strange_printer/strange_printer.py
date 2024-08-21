class Solution:
    def strangePrinter(self, s: str) -> int:
        """
        Calculates the minimum number of turns needed by the printer to print the string.

        Args:
            s (str): The input string.

        Returns:
            int: The minimum number of turns needed.
        """
        if not s:
            return 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for longueur in range(1, n + 1):
            for i in range(n - longueur + 1):
                j = i + longueur - 1
                dp[i][j] = dp[i + 1][j] + 1 if i + 1 <= j else 1
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        dp[i][j] = min(dp[i][j], dp[i][k - 1] + (dp[k + 1][j] if k + 1 <= j else 0))

        return dp[0][n - 1]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.strangePrinter("aaabbb") == 2
    assert solution.strangePrinter("aba") == 2
    assert solution.strangePrinter("aaa") == 1
    print("All tests passed.")
