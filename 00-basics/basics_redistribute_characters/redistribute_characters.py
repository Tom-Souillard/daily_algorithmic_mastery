from collections import Counter
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        """
        Determines if it's possible to redistribute characters among the words such that
        all words become equal.

        Args:
        words: A list of strings.

        Returns:
        A boolean indicating whether it's possible to make all strings in words equal.

        Example:
        >>> makeEqual(["abc", "aabc", "bc"])
        True
        >>> makeEqual(["ab", "a"])
        False
        """
        total_length = len(words)
        compte_total = Counter("".join(words))

        for _, compte in compte_total.items():
            if compte % total_length != 0:
                return False

        return True
