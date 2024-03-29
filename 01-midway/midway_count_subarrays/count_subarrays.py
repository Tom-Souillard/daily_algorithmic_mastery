class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        Counts the number of subarrays where the maximum element appears at least k times.

        Args:
        nums: A list of integers representing the array.
        k: An integer indicating the minimum number of times the maximum element must appear in a subarray.

        Returns:
        The number of subarrays where the maximum element appears at least k times.
        """
        valeur_max = max(nums)
        resultat = debut = compte_max_dans_fenetre = 0

        for fin in range(len(nums)):
            if nums[fin] == valeur_max:
                compte_max_dans_fenetre += 1
            while compte_max_dans_fenetre == k:
                if nums[debut] == valeur_max:
                    compte_max_dans_fenetre -= 1
                debut += 1
            resultat += debut
        return resultat
