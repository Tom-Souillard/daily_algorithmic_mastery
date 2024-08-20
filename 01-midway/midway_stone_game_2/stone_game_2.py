from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        Determine the maximum number of stones Alice can collect in the game, given that both players play optimally.

        Args:
            piles (List[int]): A list of integers representing the number of stones in each pile.

        Returns:
            int: The maximum number of stones Alice can collect.
        """
        n = len(piles)
        # Suffix sums to store the sum of stones from the current index to the end
        suffix_sums = [0] * n
        suffix_sums[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]

        # DP table where dp[i][m] represents the maximum stones the current player can get starting from index i with M = m
        dp = [[0] * (n + 1) for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                for x in range(1, 2 * m + 1):
                    if i + x <= n:
                        dp[i][m] = max(dp[i][m], suffix_sums[i] - (dp[i + x][max(m, x)] if i + x < n else 0))

        return dp[0][1]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.stoneGameII([2,7,9,4,4]) == 10
    assert solution.stoneGameII([1,2,3,4,5,100]) == 104
    assert solution.stoneGameII([3,9,1,2]) == 12
    assert solution.stoneGameII([4,5,6,7,8,9,10]) == 27
    print("All tests passed.")
