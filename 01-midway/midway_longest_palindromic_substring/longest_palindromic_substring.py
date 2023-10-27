class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Returns the longest palindromic substring in a given string `s`.

        Args:
        s (str): The input string.

        Returns:
        str: The longest palindromic substring in `s`.
        """

        def expande_autour_du_centre(gauche: int, droite: int) -> str:
            """
            Helper function to expand around the center.
            """
            while gauche >= 0 and droite < len(s) and s[gauche] == s[droite]:
                gauche -= 1
                droite += 1
            return s[gauche + 1:droite]

        plus_long_palindrome = ""

        for i in range(len(s)):
            palindrome1 = expande_autour_du_centre(i, i)
            palindrome2 = expande_autour_du_centre(i, i + 1)

            if len(palindrome1) > len(palindrome2):
                palindrome = palindrome1
            else:
                palindrome = palindrome2

            if len(palindrome) > len(plus_long_palindrome):
                plus_long_palindrome = palindrome

        return plus_long_palindrome
