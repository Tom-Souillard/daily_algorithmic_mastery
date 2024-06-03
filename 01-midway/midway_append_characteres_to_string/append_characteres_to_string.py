class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        Returns the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

        Args:
            s (str): The original string.
            t (str): The target subsequence string.

        Returns:
            int: The minimum number of characters to append.
        """
        index_s, index_t = 0, 0
        while index_s < len(s) and index_t < len(t):
            if s[index_s] == t[index_t]:
                index_t += 1
            index_s += 1
        return len(t) - index_t


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.appendCharacters("coaching", "coding") == 4
    assert solution.appendCharacters("abcde", "a") == 0
    assert solution.appendCharacters("z", "abcde") == 5
    print("All tests passed.")