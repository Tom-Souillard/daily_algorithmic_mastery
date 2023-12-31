class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        Finds the length of the longest substring between two equal characters in a given string.

        Args:
        s: A string in which the longest substring is to be found.

        Returns:
        The length of the longest substring found. If no such substring exists, returns -1.

        The function iterates through the string, utilizing a dictionary to store the first occurrence of each character. It updates the maximum length found for substrings between two equal characters.
        """
        premiere_occurrence = {}  # Stores the first occurrence of each character
        max_longueur = -1  # Maximum length found, initialized to -1

        for index, caractere in enumerate(s):
            if caractere in premiere_occurrence:
                # Update max length if the current character has been seen before
                max_longueur = max(max_longueur, index - premiere_occurrence[caractere] - 1)
            else:
                # Store the first occurrence of the character
                premiere_occurrence[caractere] = index

        return max_longueur
