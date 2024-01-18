class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculate the number of distinct ways to climb to the top of a staircase
        with `n` steps, where each step can either be 1 or 2 steps.

        Args:
        n (int): The total number of steps in the staircase.

        Returns:
        int: The number of distinct ways to climb to the top.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n <= 2:
            return n

        premiere_etape, deuxieme_etape = 1, 2

        for i in range(3, n + 1):
            total_etape = premiere_etape + deuxieme_etape
            premiere_etape = deuxieme_etape
            deuxieme_etape = total_etape

        return deuxieme_etape
