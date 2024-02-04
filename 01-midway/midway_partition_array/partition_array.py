from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        Calculates the largest sum possible by partitioning the array into subarrays of length at most k, where each subarray's elements are replaced by the maximum value in that subarray.

        Args:
        arr: List[int] - The input array of integers.
        k: int - The maximum allowed length of each partitioned subarray.

        Returns:
        int - The largest sum achievable after partitioning and modifying the array as described.

        This function utilizes dynamic programming to keep track of the maximum sum achievable up to each index i of the array, considering partitions of length up to k.
        """

        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            max_val = 0
            for j in range(1, min(k, i) + 1):
                max_val = max(max_val, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + max_val * j)

        return dp[n]
