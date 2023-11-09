class Solution:
    def countHomogenous(self, s: str) -> int:
        """
        Calculate the number of homogenous substrings within a given string s.

        Each homogenous substring contains the same character. The function
        counts all such possible substrings and returns the count modulo 10^9 + 7.

        Args:
        s (str): The input string to analyze.

        Returns:
        int: The count of homogenous substrings modulo 10^9 + 7.

        Example:
        >>> countHomogenous("abbcccaa")
        13
        """
        modulo = 10 ** 9 + 7
        total_substr = 1
        current_count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_count += 1
            else:
                current_count = 1
            total_substr = (total_substr + current_count) % modulo

        return total_substr