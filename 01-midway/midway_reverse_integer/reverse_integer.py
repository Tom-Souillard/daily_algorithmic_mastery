class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse the digits of the given integer.

        Args:
            x (int): The integer to be reversed.

        Returns:
            int: The reversed integer. If the reversed integer goes outside
                 the 32-bit signed integer range, return 0.
        """
        inverse = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        return 0 if inverse < -2 ** 31 or inverse > 2 ** 31 - 1 else inverse


# Test cases
sol = Solution()
print(sol.reverse(123))  # Expected output: 321
print(sol.reverse(-123))  # Expected output: -321
print(sol.reverse(120))  # Expected output: 21
