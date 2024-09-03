from typing import List


class Solution:
    def chalkReplacer(self, craies: List[int], k: int) -> int:
        """
        Determines which student will need to replace the chalk.

        Args:
            craies (List[int]): A list of integers where each integer represents the amount of chalk each student uses.
            k (int): The total number of chalk pieces available initially.

        Returns:
            int: The index of the student who will need to replace the chalk.
        """
        total_craies = sum(craies)
        k %= total_craies

        for i, c in enumerate(craies):
            if k < c:
                return i
            k -= c

        return -1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.chalkReplacer([5, 1, 5], 22) == 0
    assert solution.chalkReplacer([3, 4, 1, 2], 25) == 1
    assert solution.chalkReplacer([1, 2, 3], 6) == 0
    print("All tests passed.")
