class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        """
        Determines the minimum number of days required to make a given number of bouquets using adjacent flowers.

        Args:
            bloomDay (List[int]): List of days when each flower blooms.
            m (int): Number of bouquets needed.
            k (int): Number of adjacent flowers required for each bouquet.

        Returns:
            int: Minimum number of days required to make the bouquets, or -1 if it's not possible.
        """

        def peutFaireBouquets(jour: int) -> bool:
            bouquets = 0
            fleursAdjacentes = 0
            for jourFleur in bloomDay:
                if jourFleur <= jour:
                    fleursAdjacentes += 1
                    if fleursAdjacentes == k:
                        bouquets += 1
                        fleursAdjacentes = 0
                else:
                    fleursAdjacentes = 0
            return bouquets >= m

        if len(bloomDay) < m * k:
            return -1

        debut, fin = min(bloomDay), max(bloomDay)
        while debut < fin:
            milieu = (debut + fin) // 2
            if peutFaireBouquets(milieu):
                fin = milieu
            else:
                debut = milieu + 1
        return debut if peutFaireBouquets(debut) else -1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minDays([1, 10, 3, 10, 2], 3, 1) == 3
    assert solution.minDays([1, 10, 3, 10, 2], 3, 2) == -1
    assert solution.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3) == 12
    assert solution.minDays([1000000000, 1000000000], 1, 1) == 1000000000
    print("All tests passed.")
