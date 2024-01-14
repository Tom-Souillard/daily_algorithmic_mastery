class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Determine if two strings are close. Two strings are considered close if one can be
        transformed into the other using a series of character swaps and transformations.

        Args:
        word1 (str): The first string to be compared.
        word2 (str): The second string to be compared.

        Returns:
        bool: True if the strings are close, False otherwise.
        """
        if len(word1) != len(word2):
            return False

        frequence1 = {}
        frequence2 = {}

        for char in word1:
            frequence1[char] = frequence1.get(char, 0) + 1

        for char in word2:
            frequence2[char] = frequence2.get(char, 0) + 1

        return sorted(frequence1.values()) == sorted(frequence2.values()) and set(word1) == set(word2)
