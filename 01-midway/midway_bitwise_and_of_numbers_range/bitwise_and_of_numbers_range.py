class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Calculate the bitwise AND of all numbers in the given range [left, right].

        Args:
            left: An integer, start of the range.
            right: An integer, end of the range.

        Returns:
            The bitwise AND of all numbers in the range [left, right].
        """
        deplacement = 0
        while left != right:
            left >>= 1
            right >>= 1
            deplacement += 1
        return left << deplacement
