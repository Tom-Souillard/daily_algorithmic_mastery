from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Given a set of distinct positive integers, finds the largest subset where every pair of elements is mutually divisible.

        Args:
        nums: List[int] - A list of distinct positive integers.

        Returns:
        List[int] - The largest subset of nums where for every pair (i, j), either nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0.
        """
        # Tri des nombres pour garantir que les diviseurs précèdent toujours leurs multiples.
        nums.sort()
        n = len(nums)
        # dp[i] stocke la taille du plus grand sous-ensemble divisible se terminant avec nums[i].
        dp = [1] * n
        # parent[i] stocke l'indice du prédécesseur de nums[i] dans le sous-ensemble optimal.
        parent = [-1] * n
        max_size = 0
        max_index = 0

        # Remplissage des tableaux dp et parent.
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i

        # Reconstruction du plus grand sous-ensemble divisible.
        resultat = []
        while max_index != -1:
            resultat.append(nums[max_index])
            max_index = parent[max_index]

        return resultat[::-1]  # Inversion pour l'ordre croissant.
