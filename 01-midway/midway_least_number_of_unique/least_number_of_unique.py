from typing import List
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """
        Finds the least number of unique integers in the array after removing k elements.

        Args:
            arr: A list of integers.
            k: An integer representing the number of elements to remove.

        Returns:
            The least number of unique integers after removing k elements.

        The function first counts the frequency of each integer in the array using a Counter.
        Then, it sorts these frequencies in ascending order. It iterates over these sorted frequencies,
        subtracting the count from k for each unique integer until k is less than or equal to zero.
        Finally, it returns the count of remaining unique integers.
        """
        compteur = Counter(arr)
        frequences = sorted(compteur.values())

        nb_uniques = len(frequences)
        for frequence in frequences:
            if k >= frequence:
                k -= frequence
                nb_uniques -= 1
            else:
                break

        return nb_uniques
