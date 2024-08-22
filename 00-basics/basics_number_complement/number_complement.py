class Solution:
    def findComplement(self, num: int) -> int:
        """
        Finds the complement of the given integer by flipping all bits in its binary representation.

        Args:
            num (int): The integer to find the complement of.

        Returns:
            int: The complement of the input integer.
        """
        masque = (1 << num.bit_length()) - 1
        return num ^ masque


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.findComplement(5) == 2
    assert solution.findComplement(1) == 0
    assert solution.findComplement(7) == 0
    assert solution.findComplement(10) == 5
    print("All tests passed.")
