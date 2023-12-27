from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        Calculate the minimum difficulty of scheduling jobs over `d` days.

        Args:
        jobDifficulty (List[int]): Array where the i-th element represents the difficulty of the i-th job.
        d (int): The number of days to schedule the jobs.

        Returns:
        int: The minimum difficulty of the job schedule if possible, otherwise -1.

        """
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[float('inf')] * n + [0] for _ in range(d + 1)]

        for i in range(1, d + 1):
            for j in range(i - 1, n):
                max_diff = 0
                for k in range(j, i - 2, -1):
                    max_diff = max(max_diff, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], dp[i - 1][k - 1] + max_diff)

        return dp[d][n - 1]


# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.minDifficulty([6, 5, 4, 3, 2, 1], 2) == 7
    assert sol.minDifficulty([9, 9, 9], 4) == -1
    assert sol.minDifficulty([1, 1, 1], 3) == 3
    assert sol.minDifficulty([1, 1, 1, 1], 2) == 2

