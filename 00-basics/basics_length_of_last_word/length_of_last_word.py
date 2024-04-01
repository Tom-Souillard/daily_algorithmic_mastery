class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Finds the length of the last word in a given string.

        Args:
        s (str): The input string containing words separated by spaces.

        Returns:
        int: The length of the last word in the input string.
        """
        index = len(s) - 1
        while index >= 0 and s[index] == " ":
            index -= 1
        longueur = 0
        while index >= 0 and s[index] != " ":
            longueur += 1
            index -= 1
        return longueur
