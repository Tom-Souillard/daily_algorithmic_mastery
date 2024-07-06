class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """
        Determines the index of the person holding the pillow after a given time.

        Args:
            n (int): The number of people in the line.
            time (int): The time in seconds after which to determine the pillow holder.

        Returns:
            int: The index of the person holding the pillow.
        """
        direction = 1 if (time // (n - 1)) % 2 == 0 else -1
        position = time % (n - 1) if direction == 1 else n - (time % (n - 1)) - 1
        return position + 1

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.passThePillow(4, 5) == 2
    assert solution.passThePillow(3, 2) == 3
    assert solution.passThePillow(2, 1) == 2
    print("All tests passed.")