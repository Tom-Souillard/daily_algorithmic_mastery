class Solution:
    def checkRecord(self, n: int) -> int:
        """
        Return the number of valid attendance records of length n modulo 10^9 + 7.

        Args:
        n (int): The length of the attendance record.

        Returns:
        int: The number of valid attendance records.
        """
        MOD = 10 ** 9 + 7

        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1

        for _ in range(n):
            prev = [row[:] for row in dp]

            dp[0][0] = (prev[0][0] + prev[0][1] + prev[0][2]) % MOD
            dp[0][1] = prev[0][0]
            dp[0][2] = prev[0][1]

            dp[1][0] = (prev[0][0] + prev[0][1] + prev[0][2] + prev[1][0] + prev[1][1] + prev[1][2]) % MOD
            dp[1][1] = prev[1][0]
            dp[1][2] = prev[1][1]

        return (dp[0][0] + dp[0][1] + dp[0][2] + dp[1][0] + dp[1][1] + dp[1][2]) % MOD


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkRecord(2))  # Output: 8
    print(solution.checkRecord(1))  # Output: 3
    print(solution.checkRecord(10101))  # Output: 183236316
