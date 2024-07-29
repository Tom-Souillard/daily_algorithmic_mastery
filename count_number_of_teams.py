from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """
        Count the number of valid teams of 3 soldiers based on given rating rules.

        Args:
            rating (List[int]): List of integers representing the ratings of the soldiers.

        Returns:
            int: The number of valid teams of 3 soldiers.
        """
        n = len(rating)
        count = 0

        for j in range(1, n - 1):
            left_less = left_greater = right_less = right_greater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                if rating[i] > rating[j]:
                    left_greater += 1

            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_less += 1
                if rating[k] > rating[j]:
                    right_greater += 1

            count += left_less * right_greater + left_greater * right_less

        return count


# Test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.numTeams([2, 5, 3, 4, 1]) == 3
    assert solution.numTeams([2, 1, 3]) == 0
    assert solution.numTeams([1, 2, 3, 4]) == 4
    print("All tests passed.")
