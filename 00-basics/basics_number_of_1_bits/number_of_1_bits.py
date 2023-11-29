class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Compute the Hamming weight (number of '1' bits) of a 32-bit integer.

        Args:
            n (int): A 32-bit integer.

        Returns:
            int: The Hamming weight of the integer.
        """
        compteur = 0
        while n:
            compteur += n & 1
            n >>= 1
        return compteur
