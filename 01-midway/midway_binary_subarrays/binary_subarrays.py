from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums, goal):
        """
        Finds the number of non-empty subarrays with a sum equal to the goal.

        Args:
        nums: List[int], a binary array.
        goal: int, the target sum for subarrays.

        Returns:
        int, the number of non-empty subarrays with a sum equal to the goal.

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n), for storing the prefix sum counts.
        """
        compte_somme = 0  # Stores the number of subarrays meeting the goal
        somme_courante = 0  # Current sum of elements in the sliding window
        pre_sommes = defaultdict(int)  # Counts of seen prefix sums
        pre_sommes[0] = 1  # Initialize for subarray starting from index 0

        for num in nums:
            somme_courante += num
            compte_somme += pre_sommes[somme_courante - goal]
            pre_sommes[somme_courante] += 1

        return compte_somme