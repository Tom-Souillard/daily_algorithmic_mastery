class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Finds the first non-repeating character in a string and returns its index.

        Args:
            s: A string to search through.

        Returns:
            The index of the first non-repeating character in the string. Returns -1 if no such character exists.
        """
        compte = {}  # Dictionnaire pour compter les occurrences de chaque caractère
        for caractere in s:
            if caractere in compte:
                compte[caractere] += 1
            else:
                compte[caractere] = 1

        for index in range(len(s)):
            if compte[s[index]] == 1:
                return index
        return -1
