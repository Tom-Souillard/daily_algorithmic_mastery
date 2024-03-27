from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Calculate the number of contiguous subarrays where the product of all the elements
        in the subarray is strictly less than k.

        Args:
        nums: A list of integers representing the array of numbers.
        k: An integer representing the threshold product value.

        Returns:
        The total number of contiguous subarrays where the product of all elements is
        strictly less than k.

        """
        if k <= 1:
            return 0

        produit = 1
        resultat = gauche = 0

        for droite in range(len(nums)):
            produit *= nums[droite]
            while produit >= k:
                produit /= nums[gauche]
                gauche += 1
            resultat += droite - gauche + 1

        return resultat
