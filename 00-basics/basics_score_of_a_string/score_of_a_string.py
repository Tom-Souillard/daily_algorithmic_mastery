class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        Calculate the score of a string defined as the sum of the absolute
        difference between the ASCII values of adjacent characters.

        Args:
            s (str): The input string.

        Returns:
            int: The score of the string.
        """
        return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.scoreOfString("hello") == 13
    assert solution.scoreOfString("zaz") == 50
    assert solution.scoreOfString("abcd") == 3
    assert solution.scoreOfString("a") == 0
    assert solution.scoreOfString("") == 0
    print("All tests passed.")
