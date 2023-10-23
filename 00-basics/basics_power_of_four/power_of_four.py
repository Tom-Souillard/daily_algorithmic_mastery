class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Determine if a given integer is a power of four.

        Args:
            n (int): The integer to check.

        Returns:
            bool: True if n is a power of four, False otherwise.

        Explanation:
            - First, we check if n is greater than 0.
            - Then, we use bitwise AND operation n & (n - 1) to check if n is a power of 2.
            - Finally, we use bitwise AND operation n & 0xAAAAAAAA to check if n is a power of 4.
              The number 0xAAAAAAAA is a hexadecimal constant where all the odd bits are set to 1.
              If n is a power of 4, it should not have 1 bits at these positions.
        """
        return n > 0 and n & (n - 1) == 0 and n & 0xAAAAAAAA == 0
