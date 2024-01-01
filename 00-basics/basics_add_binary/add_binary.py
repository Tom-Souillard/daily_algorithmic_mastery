class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Adds two binary strings and returns their sum as a binary string.

        Args:
        a: A string representing a binary number.
        b: A string representing a binary number.

        Returns:
        A string representing the sum of the two binary numbers.
        """
        return bin(int(a, 2) + int(b, 2))[2:]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.addBinary("11", "1"))  # Output: "100"
    print(solution.addBinary("1010", "1011"))  # Output: "10101"
    print(solution.addBinary("111", "110"))  # Output: "1101"