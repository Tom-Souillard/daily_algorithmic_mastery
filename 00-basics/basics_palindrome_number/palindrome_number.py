class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determines whether a given integer is a palindrome.

        Args:
        - x (int): The integer to be checked.

        Returns:
        - bool: True if x is a palindrome, False otherwise.
        """
        return str(x) == str(x)[::-1]