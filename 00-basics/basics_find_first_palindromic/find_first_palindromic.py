from typing import List

class Solution:
    def firstPalindrome(self, mots: List[str]) -> str:
        """
        Finds the first palindromic string in a list of strings.

        Args:
        mots: A list of strings to search through.

        Returns:
        The first string that is palindromic. Returns an empty string if no palindromic string is found.

        Time Complexity: O(n*k), where n is the number of strings in the list and k is the length of the longest string.
        Space Complexity: O(1), as no extra space is needed proportional to the input size.
        """
        for mot in mots:
            if mot == mot[::-1]:
                return mot
        return ""
