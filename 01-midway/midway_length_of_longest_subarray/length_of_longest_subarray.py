class Solution:
    def maxSubarrayLength(self, nums, k):
        """
        Finds the length of the longest good subarray within the given array.

        A good subarray is defined as a subarray where the frequency of each
        element is less than or equal to k.

        Args:
        nums: List[int], the input array of integers.
        k: int, the maximum allowed frequency for each element in a subarray.

        Returns:
        int, the length of the longest good subarray.
        """
        frequence = {}
        debut, longueur_max = 0, 0

        for fin in range(len(nums)):
            frequence[nums[fin]] = frequence.get(nums[fin], 0) + 1

            while frequence[nums[fin]] > k:
                frequence[nums[debut]] -= 1
                debut += 1

            longueur_max = max(longueur_max, fin - debut + 1)

        return longueur_max
