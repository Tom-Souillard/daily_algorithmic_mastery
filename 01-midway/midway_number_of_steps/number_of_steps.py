class Solution:
    def numSteps(self, s: str) -> int:
        """
        Given the binary representation of an integer as a string, return the number of steps
        to reduce it to 1 under the following rules:
        If the current number is even, you have to divide it by 2.
        If the current number is odd, you have to add 1 to it.

        Args:
        s (str): The binary representation of the integer.

        Returns:
        int: The number of steps to reduce the integer to 1.
        """
        steps = 0
        while s != '1':
            if s[-1] == '0':
                s = s[:-1]
            else:
                s = bin(int(s, 2) + 1)[2:]
            steps += 1
        return steps

# Test cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.numSteps("1101") == 6
    assert sol.numSteps("10") == 1
    assert sol.numSteps("1") == 0
