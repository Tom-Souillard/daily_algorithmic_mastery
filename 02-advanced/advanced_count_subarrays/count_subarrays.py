class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        Counts the number of subarrays within a given array where the minimum
        value equals minK and the maximum value equals maxK.

        Args:
        nums: A list of integers representing the array.
        minK: An integer representing the minimum value of the subarray.
        maxK: An integer representing the maximum value of the subarray.

        Returns:
        The total number of fixed-bound subarrays.

        """
        total, dernier_min, dernier_max, dernier_hors_limites = 0, -1, -1, -1
        for i, val in enumerate(nums):
            if val < minK or val > maxK:
                dernier_hors_limites = i
            if val == minK:
                dernier_min = i
            if val == maxK:
                dernier_max = i
            total += max(0, min(dernier_min, dernier_max) - dernier_hors_limites)
        return total
