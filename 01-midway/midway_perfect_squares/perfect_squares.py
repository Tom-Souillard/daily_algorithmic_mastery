class Solution:
    def numSquares(self, n: int) -> int:
        """
        Calculate the minimum number of perfect square numbers which sums to n.

        This method utilizes dynamic programming to build up a solution for the
        minimum number of perfect squares needed for all numbers up to n. Each
        position in the dp array represents the minimum number of perfect squares
        that sum to that index value.

        Args:
        n: An integer representing the target sum.

        Returns:
        An integer representing the least number of perfect square numbers that sum to n.
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]
