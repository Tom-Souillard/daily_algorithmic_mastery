from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        """
        Calculates the maximum sum of happiness values that can be achieved by selecting k children.
        Each selection causes a decrement in the happiness values of all remaining children, if their happiness is positive.

        Args:
        happiness (List[int]): List of initial happiness values of each child.
        k (int): Number of children to select.

        Returns:
        int: Maximum sum of happiness values of selected children.
        """
        n = len(happiness)
        happiness.sort()

        total_bonheur = 0
        decrementation = 0

        for i in range(n - 1, n - k - 1, -1):
            valeur_maj = happiness[i] - decrementation

            if valeur_maj > 0:
                total_bonheur += valeur_maj

            decrementation += 1

        return total_bonheur


# Test
if __name__ == "__main__":
    sol = Solution()
    assert sol.maximumHappinessSum([1, 2, 3], 2) == 4
    assert sol.maximumHappinessSum([1, 1, 1, 1], 2) == 1
    assert sol.maximumHappinessSum([2, 3, 4, 5], 1) == 5

