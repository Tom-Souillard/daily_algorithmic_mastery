from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Determines if the number of occurrences of each value in the array is unique.

        Args:
        arr: List[int] - A list of integers.

        Returns:
        bool - True if each value in the array has a unique number of occurrences, False otherwise.
        """
        occurrences = Counter(arr)
        return len(occurrences.values()) == len(set(occurrences.values()))
