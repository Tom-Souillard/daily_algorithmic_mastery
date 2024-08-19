class Solution:
    def minSteps(self, n: int) -> int:
        """
        Determines the minimum number of operations required to get exactly n 'A' characters on the screen.

        Args:
            n (int): The target number of 'A' characters.

        Returns:
            int: The minimum number of operations needed.
        """
        opérations = 0
        facteur = 2

        while n > 1:
            while n % facteur == 0:
                opérations += facteur
                n //= facteur
            facteur += 1

        return opérations


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.minSteps(3) == 3
    assert solution.minSteps(1) == 0
    assert solution.minSteps(4) == 4
    assert solution.minSteps(6) == 5
    print("All tests passed.")
