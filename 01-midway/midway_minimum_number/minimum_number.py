class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        Calculate the minimum number of steps to make string t an anagram of string s.

        Args:
        s (str): The first string.
        t (str): The second string, to be transformed into an anagram of s.

        Returns:
        int: The minimum number of steps to make t an anagram of s.

        """

        # Frequency counters for characters in s and t
        frequence_s = {}
        frequence_t = {}

        # Count character frequencies in s
        for caractere in s:
            frequence_s[caractere] = frequence_s.get(caractere, 0) + 1

        # Count character frequencies in t
        for caractere in t:
            frequence_t[caractere] = frequence_t.get(caractere, 0) + 1

        # Calculate the number of changes needed
        nb_etapes = 0
        for caractere in frequence_s:
            nb_etapes += max(0, frequence_s[caractere] - frequence_t.get(caractere, 0))

        return nb_etapes
