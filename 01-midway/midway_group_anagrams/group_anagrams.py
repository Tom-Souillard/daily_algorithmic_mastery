from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together from the given list of strings.

        Args:
            strs: A list of strings to be grouped.

        Returns:
            A list of lists, where each sublist contains anagrams of each other.

        The function utilizes a dictionary to map sorted string tuples to their anagrams, ensuring
        efficient grouping with O(NKlogK) time complexity, where N is the number of strings and K is
        the maximum length of a string in strs. The space complexity is O(NK), needed for the output
        and the dictionary.
        """
        dictionnaire = {}
        for mot in strs:
            cle = tuple(sorted(mot))
            if cle not in dictionnaire:
                dictionnaire[cle] = [mot]
            else:
                dictionnaire[cle].append(mot)
        return list(dictionnaire.values())
