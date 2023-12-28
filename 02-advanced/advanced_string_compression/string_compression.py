class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        Calculate the minimum length of the run-length encoded version of a string s,
        after deleting at most k characters.

        Args:
        s (str): The input string.
        k (int): The maximum number of characters that can be deleted.

        Returns:
        int: The minimum length of the compressed string.
        """
        n = len(s)
        if n <= k:
            return 0

        # Function to calculate length of encoding for a run
        def encoded_length(count):
            if count == 0:
                return 0
            elif count == 1:
                return 1
            else:
                return 1 + len(str(count))

        # Initialize DP table
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(k + 1):
                # Case 1: Delete the current character
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

                # Case 2: Keep the current character
                count, deletions = 0, 0
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        count += 1
                    else:
                        deletions += 1
                    if deletions <= j:
                        dp[i][j] = min(dp[i][j], dp[l - 1][j - deletions] + encoded_length(count))

        return dp[n][k]

# Example usage
sol = Solution()
print(sol.getLengthOfOptimalCompression("aaabcccd", 2))  # Expected Output: 4
print(sol.getLengthOfOptimalCompression("aaaaaaaaaaa", 0))  # Expected Output: 3
