class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        Finds the number of contiguous subarrays containing exactly k distinct integers.

        Args:
        nums: List[int] - The input array of integers.
        k: int - The target number of distinct integers.

        Returns:
        int - The number of subarrays meeting the criteria.
        """

        def sous_arrays_avec_au_plus_k_distincts(k: int) -> int:
            compte = collections.Counter()
            debut, total = 0, 0
            for fin, val in enumerate(nums):
                if compte[val] == 0:
                    k -= 1
                compte[val] += 1
                while k < 0:
                    compte[nums[debut]] -= 1
                    if compte[nums[debut]] == 0:
                        k += 1
                    debut += 1
                total += fin - debut + 1
            return total

        return sous_arrays_avec_au_plus_k_distincts(k) - sous_arrays_avec_au_plus_k_distincts(k - 1)
