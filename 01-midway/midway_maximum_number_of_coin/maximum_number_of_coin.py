class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        """
        Finds the maximum number of coins that can be obtained.

        This function sorts the piles of coins in descending order. Then, it iteratively selects the second largest pile (the first pile being selected by Alice and the third by Bob) in each step, ensuring the maximum coins for the user. The process continues until all piles are exhausted.

        Args:
        piles: A list of integers representing the number of coins in each pile.

        Returns:
        int: The maximum number of coins that the user can collect.
        """
        piles.sort(reverse=True)
        nombreDePiles = len(piles) // 3
        somme = 0
        for i in range(nombreDePiles):
            somme += piles[2*i + 1]
        return somme
