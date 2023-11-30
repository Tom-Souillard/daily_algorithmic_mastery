class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        Calculate the minimum number of one-bit operations to transform a number to zero.

        Args:
        n (int): The number to be transformed.

        Returns:
        int: Minimum number of operations.

        This function iteratively reduces the number to a form of Gray code, then
        converts it to zero using the minimum number of operations.
        """
        resultat = 0
        while n:
            resultat ^= n
            n >>= 1
        return resultat

