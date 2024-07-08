class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        Determine the winner of a circular game.

        Args:
            n (int): The number of friends in the game.
            k (int): The step count to determine the next friend to leave.

        Returns:
            int: The position of the friend who wins the game.
        """
        amis = list(range(1, n + 1))
        index = 0
        while len(amis) > 1:
            index = (index + k - 1) % len(amis)
            amis.pop(index)
        return amis[0]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.findTheWinner(5, 2) == 3
    assert solution.findTheWinner(6, 5) == 1
    assert solution.findTheWinner(7, 3) == 4
    assert solution.findTheWinner(8, 2) == 1
    print("All tests passed.")
