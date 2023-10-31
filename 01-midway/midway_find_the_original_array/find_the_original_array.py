from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        """
        Given a list of integers representing prefix XORs, reconstructs and
        returns the original list.

        Args:
            pref (List[int]): List of integers where the i-th element represents
                the XOR of the first i+1 elements of the original list.

        Returns:
            List[int]: The original list of integers from which the prefix XORs
                were generated.
        """
        for i in range(len(pref) - 1, 0, -1):
            pref[i] = pref[i] ^ pref[i - 1]

        return pref
