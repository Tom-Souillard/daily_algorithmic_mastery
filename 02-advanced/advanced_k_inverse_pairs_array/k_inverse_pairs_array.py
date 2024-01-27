class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        """
        Calculate the number of arrays of length n with exactly k inverse pairs.

        Args:
        n (int): The length of the array.
        k (int): The exact number of inverse pairs in the array.

        Returns:
        int: The number of different arrays of length n with exactly k inverse pairs.
        """
        modulo = 10**9 + 7
        if k == 0:
            return 1

        dp = [[0] * (k + 1) for _ in range(2)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            cumulatif = 0
            for j in range(k + 1):
                cumulatif += dp[(i - 1) % 2][j]
                if j >= i:
                    cumulatif -= dp[(i - 1) % 2][j - i]
                dp[i % 2][j] = cumulatif % modulo

        return dp[n % 2][k]
