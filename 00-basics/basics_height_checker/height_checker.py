class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        """
        Returns the number of indices where the heights differ from the expected order.

        Args:
            heights (List[int]): List of student heights in current order.

        Returns:
            int: Number of indices where heights differ from expected order.
        """
        attendu = sorted(heights)
        return sum(1 for i in range(len(heights)) if heights[i] != attendu[i])

# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.heightChecker([1, 1, 4, 2, 1, 3]) == 3
    assert solution.heightChecker([5, 1, 2, 3, 4]) == 5
    assert solution.heightChecker([1, 2, 3, 4, 5]) == 0
    print("All tests passed.")
