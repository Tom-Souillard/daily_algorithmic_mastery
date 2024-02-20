class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Computes the square root of a non-negative integer x and returns the integer part of the square root.

        Args:
        x: A non-negative integer.

        Returns:
        The integer part of the square root of x.
        """
        return int(x ** 0.5)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(4))  # Output: 2
    print(solution.mySqrt(8))  # Output: 2
    print(solution.mySqrt(1))  # Output: 1
    print(solution.mySqrt(0))  # Output: 0
    print(solution.mySqrt(16))  # Output: 4