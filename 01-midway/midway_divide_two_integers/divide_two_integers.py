class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Divides two integers without using multiplication, division, and mod operator.

        Args:
        dividend (int): The number to be divided.
        divisor (int): The number by which to divide.

        Returns:
        int: The quotient after dividing dividend by divisor, truncated towards zero.
        """
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        signe = (dividend < 0) == (divisor < 0)
        dividende, diviseur = abs(dividend), abs(divisor)
        quotient = 0
        while dividende >= diviseur:
            puissance = 0
            while dividende >= diviseur << (puissance + 1):
                puissance += 1
            quotient += 1 << puissance
            dividende -= diviseur << puissance
        resultat = quotient if signe else -quotient
        return min(max(INT_MIN, resultat), INT_MAX)

# Test case
if __name__ == "__main__":
    solution = Solution()
    assert solution.divide(10, 3) == 3, "Le cas 10 divisé par 3 a échoué"
    assert solution.divide(7, -3) == -2, "Le cas 7 divisé par -3 a échoué"
    assert solution.divide(-2147483648, -1) == 2147483647, "Le cas limite a échoué"