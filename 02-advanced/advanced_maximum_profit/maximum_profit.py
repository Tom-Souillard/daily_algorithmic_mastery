from typing import List
from bisect import bisect_right


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        Calculate the maximum profit that can be achieved by scheduling non-overlapping jobs.

        This function takes three lists, each representing the start time, end time, and profit of jobs.
        It returns the maximum profit that can be obtained without scheduling overlapping jobs.

        Args:
        startTime (List[int]): A list of integers where startTime[i] is the start time of the ith job.
        endTime (List[int]): A list of integers where endTime[i] is the end time of the ith job.
        profit (List[int]): A list of integers where profit[i] is the profit of the ith job.

        Returns:
        int: The maximum profit that can be achieved.
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        fin_temps = [jobs[i][1] for i in range(n)]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            inclure_profit = jobs[i - 1][2]
            dernier_non_conflict = bisect_right(fin_temps, jobs[i - 1][0], 0, i - 1)
            inclure_profit += dp[dernier_non_conflict]
            dp[i] = max(inclure_profit, dp[i - 1])

        return dp[n]


# Example usage
sol = Solution()
print(sol.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))  # Output: 120
