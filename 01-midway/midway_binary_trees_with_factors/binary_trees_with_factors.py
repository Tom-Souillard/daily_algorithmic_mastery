from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """
        Calcule le nombre d'arbres binaires possibles à partir d'un tableau donné.

        Args:
            arr (List[int]): Un tableau d'entiers uniques, chaque entier étant strictement supérieur à 1.

        Returns:
            int: Le nombre d'arbres binaires possibles, modulo 10^9 + 7.
        """

        MODULO = 10 ** 9 + 7
        arr.sort()

        dp = {}

        for x in arr:
            dp[x] = 1

            for y in arr:
                if y >= x:
                    break
                if x % y == 0 and x // y in dp:
                    dp[x] += dp[y] * dp[x // y]

        resultat = sum(dp.values()) % MODULO

        return resultat
