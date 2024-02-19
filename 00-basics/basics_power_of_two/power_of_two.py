class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Determines if the given integer is a power of two.

        This function checks if a given integer 'n' is a power of two, utilizing
        the property that powers of two in binary form have exactly one bit set to 1
        and all other bits set to 0. This is optimized for both time and space complexity.

        Args:
            n: An integer to check.

        Returns:
            A boolean value indicating whether 'n' is a power of two.
        """
        return n > 0 and (n & (n - 1)) == 0
