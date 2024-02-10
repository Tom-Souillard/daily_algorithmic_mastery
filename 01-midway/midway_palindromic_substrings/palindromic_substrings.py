class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Counts the number of palindromic substrings in the given string.

        This function utilizes the expand around center technique to efficiently
        find palindromic substrings. It iterates through each character and
        each pair of characters in the string, expanding around them to count
        palindromes.

        Args:
            s: A string for which to count palindromic substrings.

        Returns:
            The total number of palindromic substrings in the input string.
        """

        def compter_palindrome(centre_gauche: int, centre_droit: int) -> int:
            compteur = 0
            while centre_gauche >= 0 and centre_droit < len(s) and s[centre_gauche] == s[centre_droit]:
                compteur += 1
                centre_gauche -= 1
                centre_droit += 1
            return compteur

        total_palindromes = 0
        for i in range(len(s)):
            # Palindromes de longueur impaire
            total_palindromes += compter_palindrome(i, i)
            # Palindromes de longueur paire
            total_palindromes += compter_palindrome(i, i + 1)

        return total_palindromes
